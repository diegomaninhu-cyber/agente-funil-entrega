const express = require('express');
const compression = require('compression');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;
const SALES_FILE = path.join(__dirname, 'vendas.json');
const ANALYTICS_FILE = process.env.ANALYTICS_FILE || path.join(__dirname, 'analytics.json');
const analyticsClients = new Set();

// Parse JSON bodies (for webhook)
app.use(compression({
  filter: (req, res) => {
    if (req.path === '/api/analytics/stream') {
      return false;
    }

    return compression.filter(req, res);
  }
}));
app.use(express.json());

// ─── WEBHOOK InfinitePay ─────────────────────────────────────────────────────
// URL para colocar no checkout: https://agente-funil-entrega-production.up.railway.app/webhook
app.post('/webhook', (req, res) => {
  try {
    const payload = req.body;
    const timestamp = new Date().toISOString();

    // Monta o registro da venda
    const venda = {
      timestamp,
      invoice_slug: payload.invoice_slug || null,
      amount: payload.amount || null,
      paid_amount: payload.paid_amount || null,
      installments: payload.installments || null,
      capture_method: payload.capture_method || null,
      transaction_nsu: payload.transaction_nsu || null,
      order_nsu: payload.order_nsu || null,
      receipt_url: payload.receipt_url || null,
      customer: payload.customer || null,
      items: payload.items || null,
      raw: payload
    };

    // Lê o arquivo de vendas atual (ou cria vazio)
    let vendas = [];
    if (fs.existsSync(SALES_FILE)) {
      try {
        vendas = JSON.parse(fs.readFileSync(SALES_FILE, 'utf8'));
      } catch (e) {
        vendas = [];
      }
    }

    // Adiciona a nova venda e salva
    vendas.push(venda);
    fs.writeFileSync(SALES_FILE, JSON.stringify(vendas, null, 2), 'utf8');

    console.log(`✅ [VENDA] ${timestamp} | R$ ${(venda.paid_amount / 100).toFixed(2)} | ${venda.capture_method}`);

    // Responde 200 OK em menos de 1 segundo (obrigatório pela InfinitePay)
    res.status(200).json({ status: 'ok', received: timestamp });
  } catch (err) {
    console.error('❌ Erro no webhook:', err);
    res.status(400).json({ status: 'error', message: err.message });
  }
});

// ─── PAINEL DE VENDAS (protegido por query param) ────────────────────────────
app.get('/vendas', (req, res) => {
  const token = req.query.token;
  if (token !== (process.env.ADMIN_TOKEN || 'diego2026')) {
    return res.status(401).json({ error: 'Não autorizado' });
  }

  if (!fs.existsSync(SALES_FILE)) {
    return res.json({ total: 0, vendas: [] });
  }

  try {
    const vendas = JSON.parse(fs.readFileSync(SALES_FILE, 'utf8'));
    const total_arrecadado = vendas.reduce((acc, v) => acc + (v.paid_amount || 0), 0);
    res.json({
      total_vendas: vendas.length,
      total_arrecadado_reais: (total_arrecadado / 100).toFixed(2),
      vendas: vendas.map(v => ({
        data: v.timestamp,
        valor: `R$ ${((v.paid_amount || 0) / 100).toFixed(2)}`,
        metodo: v.capture_method,
        recibo: v.receipt_url,
        cliente: v.customer
      }))
    });
  } catch (e) {
    res.status(500).json({ error: 'Erro ao ler vendas' });
  }
});

// ─── ANALYTICS ───────────────────────────────────────────────────────────────

function readAnalyticsEvents() {
  if (!fs.existsSync(ANALYTICS_FILE)) {
    return [];
  }

  try {
    return JSON.parse(fs.readFileSync(ANALYTICS_FILE, 'utf8'));
  } catch (e) {
    return [];
  }
}

function writeAnalyticsEvents(events) {
  fs.writeFileSync(ANALYTICS_FILE, JSON.stringify(events, null, 2), 'utf8');
}

function notifyAnalyticsClients(eventPayload) {
  const data = `data: ${JSON.stringify(eventPayload)}\n\n`;
  analyticsClients.forEach((client) => {
    try {
      client.write(data);
    } catch (e) {
      analyticsClients.delete(client);
    }
  });
}

// Função para enviar para o Facebook CAPI
function sendToFacebookCAPI(eventPayload, req, anonIp) {
  const FB_PIXEL_ID = '607914143271127';
  const FB_CAPI_TOKEN = process.env.FB_CAPI_TOKEN;
  
  if (!FB_CAPI_TOKEN) {
    // Silently skip if no token is configured
    return;
  }

  const fbEventName = eventPayload.custom_event_name || (eventPayload.event === 'page_view' ? 'PageView' : 'InitiateCheckout');
  const actionSource = 'website';
  const eventTime = Math.floor(Date.now() / 1000);

  const userData = {
    client_ip_address: req.headers['x-forwarded-for'] || req.socket.remoteAddress || anonIp,
    client_user_agent: req.headers['user-agent'] || eventPayload.metadata?.user_agent || '',
  };

  if (eventPayload.fbp) userData.fbp = eventPayload.fbp;
  if (eventPayload.fbc) userData.fbc = eventPayload.fbc;

  const data = [{
    event_name: fbEventName,
    event_time: eventTime,
    action_source: actionSource,
    event_id: eventPayload.event_id || `evt_${eventTime}`,
    event_source_url: eventPayload.event_source_url || eventPayload.page || '',
    user_data: userData,
    custom_data: {
      content_name: eventPayload.metadata?.button_text || eventPayload.event
    }
  }];

  const payload = { data: data };

  // Extracao do test_event_code
  try {
    const urlStr = eventPayload.event_source_url || eventPayload.page || '';
    const match = urlStr.match(/[?&]test_event_code=([^&#]*)/);
    if (match && match[1]) {
      payload.test_event_code = match[1];
    }
  } catch (e) {}

  const postData = JSON.stringify(payload);

  const https = require('https');
  const options = {
    hostname: 'graph.facebook.com',
    path: `/v19.0/${FB_PIXEL_ID}/events?access_token=${FB_CAPI_TOKEN}`,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(postData)
    }
  };

  const request = https.request(options, (res) => {
    res.on('data', () => {}); // Consume data to free memory
  });

  request.on('error', (e) => {
    console.error('❌ Erro no CAPI:', e.message);
  });

  request.write(postData);
  request.end();
}

// 1. Receber eventos do Frontend
app.post('/api/track', (req, res) => {
  try {
    const events = readAnalyticsEvents();
    
    // IP anonimizado
    const rawIp = req.headers['x-forwarded-for'] || req.socket.remoteAddress || '';
    const anonIp = rawIp.replace(/\.\d+$/, '.0').replace(/:[0-9a-fA-F]+$/, ':0000');

    const eventPayload = {
      ...req.body,
      ip: anonIp,
      server_timestamp: new Date().toISOString()
    };

    events.push(eventPayload);
    writeAnalyticsEvents(events);
    notifyAnalyticsClients(eventPayload);

    // Envia para o Facebook CAPI assincronamente
    sendToFacebookCAPI(eventPayload, req, anonIp);

    res.status(200).json({ status: 'ok' });
  } catch (err) {
    console.error('❌ Erro no track:', err);
    res.status(500).json({ status: 'error' });
  }
});

app.get('/api/analytics/stream', (req, res) => {
  const token = req.query.token;
  if (token !== (process.env.ADMIN_TOKEN || 'diego2026')) {
    return res.status(401).end();
  }

  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  res.flushHeaders?.();
  res.write(': connected\n\n');
  analyticsClients.add(res);

  const heartbeat = setInterval(() => {
    res.write(': heartbeat\n\n');
  }, 15000);

  req.on('close', () => {
    clearInterval(heartbeat);
    analyticsClients.delete(res);
  });
});

// 2. Painel HTML protegido
app.get('/analytics', (req, res) => {
  const token = req.query.token;
  if (token !== (process.env.ADMIN_TOKEN || 'diego2026')) {
    return res.status(401).send('<h1>Não autorizado</h1>');
  }
  res.sendFile(path.join(__dirname, 'analytics-dashboard.html'));
});

// 3. API JSON para o Painel
app.get('/api/analytics', (req, res) => {
  const token = req.query.token;
  if (token !== (process.env.ADMIN_TOKEN || 'diego2026')) {
    return res.status(401).json({ error: 'Não autorizado' });
  }

  try {
    const events = readAnalyticsEvents();
    res.json({ events });
  } catch (e) {
    res.status(500).json({ error: 'Erro ao ler analytics' });
  }
});

// ─── SERVE PÁGINAS DE OFERTA E ENTREGA ──────────────────────────────────────
app.use(express.static(path.join(__dirname), {
  etag: true,
  maxAge: '7d',
  setHeaders: (res, filePath) => {
    if (/\.(html)$/i.test(filePath)) {
      res.setHeader('Cache-Control', 'no-cache');
      return;
    }

    if (/\.(webp|png|jpg|jpeg|mp4|css|js|woff2?)$/i.test(filePath)) {
      res.setHeader('Cache-Control', 'public, max-age=2592000');
    }
  }
}));

app.get('/oferta', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta.html'));
});

app.get('/oferta2', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta2.html'));
});

app.get('/oferta3', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta3.html'));
});

app.get('/oferta4', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta4.html'));
});

app.get('/oferta5', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta5.html'));
});

app.get('/oferta6', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta6.html'));
});

app.get('/oferta7', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta7.html'));
});

app.get('/oferta8', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta8.html'));
});

app.get('/oferta9', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta9.html'));
});

app.get('/oferta10', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta10.html'));
});

app.get('/oferta11', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta11.html'));
});

app.get('/oferta12', (req, res) => {
  res.sendFile(path.join(__dirname, 'oferta12.html'));
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`✅ Servidor rodando na porta ${PORT}`);
  console.log(`🔗 Webhook URL: https://agente-funil-entrega-production.up.railway.app/webhook`);
  console.log(`📊 Painel de vendas: https://agente-funil-entrega-production.up.railway.app/vendas?token=diego2026`);
  console.log(`📊 Painel de analytics: https://agente-funil-entrega-production.up.railway.app/analytics?token=diego2026`);
});
