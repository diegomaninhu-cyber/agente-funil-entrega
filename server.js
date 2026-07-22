const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;
const SALES_FILE = path.join(__dirname, 'vendas.json');
const ANALYTICS_FILE = process.env.ANALYTICS_FILE || path.join(__dirname, 'analytics.json');

// Parse JSON bodies (for webhook)
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

// 1. Receber eventos do Frontend
app.post('/api/track', (req, res) => {
  try {
    let events = [];
    if (fs.existsSync(ANALYTICS_FILE)) {
      try {
        events = JSON.parse(fs.readFileSync(ANALYTICS_FILE, 'utf8'));
      } catch (e) {
        events = [];
      }
    }
    
    // IP anonimizado
    const rawIp = req.headers['x-forwarded-for'] || req.socket.remoteAddress || '';
    const anonIp = rawIp.replace(/\.\d+$/, '.0').replace(/:[0-9a-fA-F]+$/, ':0000');

    const eventPayload = {
      ...req.body,
      ip: anonIp,
      server_timestamp: new Date().toISOString()
    };

    events.push(eventPayload);
    fs.writeFileSync(ANALYTICS_FILE, JSON.stringify(events, null, 2), 'utf8');

    res.status(200).json({ status: 'ok' });
  } catch (err) {
    console.error('❌ Erro no track:', err);
    res.status(500).json({ status: 'error' });
  }
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

  if (!fs.existsSync(ANALYTICS_FILE)) {
    return res.json({ events: [] });
  }

  try {
    const events = JSON.parse(fs.readFileSync(ANALYTICS_FILE, 'utf8'));
    res.json({ events });
  } catch (e) {
    res.status(500).json({ error: 'Erro ao ler analytics' });
  }
});

// ─── SERVE PÁGINAS DE OFERTA E ENTREGA ──────────────────────────────────────
app.use(express.static(path.join(__dirname)));

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
