<!doctype html>
<html lang="az">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Xərclərim - Pro Dashboard</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">

  <style>
    :root{
      --bg: #0c0f14;
      --stroke: rgba(255,255,255,.12);
      --text: rgba(255,255,255,.92);
      --muted: rgba(255,255,255,.65);
      --yellow: #ff9f1a;
      --yellow2:#ff7a00;
      --good:#2ee59d;
      --bad:#ff6b6b;
      --shadow: 0 18px 60px rgba(0,0,0,.45);
      --radius: 18px;
      --pillRadius: 14px;
    }

    *{ box-sizing:border-box; }
    body{
      margin:0;
      font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      color: var(--text);
      background:
        radial-gradient(900px 520px at 20% 10%, rgba(255,159,26,.16), transparent 60%),
        radial-gradient(900px 520px at 82% 18%, rgba(46,229,157,.10), transparent 60%),
        radial-gradient(900px 520px at 60% 92%, rgba(255,107,107,.10), transparent 55%),
        var(--bg);
      min-height:100vh;
      padding: 28px 16px 44px;
    }

    .wrap{ max-width: 1080px; margin: 0 auto; }

    /* Topbar & Pills */
    .topbar{ display:flex; align-items:center; justify-content:space-between; gap:12px; margin-bottom:12px; flex-wrap:wrap; }
    .title{ display:flex; flex-direction:column; gap:6px; min-width:240px; }
    .title h1{ margin:0; font-size:20px; letter-spacing:.2px; }
    .title p{ margin:0; color:var(--muted); font-size:13px; line-height:1.35; }

    .pill{
      display:flex; align-items:center; gap:10px; padding:10px 12px;
      border:1px solid var(--stroke); background:linear-gradient(180deg, rgba(255,255,255,.10), rgba(255,255,255,.06));
      border-radius:var(--pillRadius); box-shadow:0 10px 30px rgba(0,0,0,.18);
    }
    .pill input{ width:120px; font:inherit; color:var(--text); background:rgba(0,0,0,.25); border:1px solid rgba(255,255,255,.14); border-radius:12px; padding:8px 10px; text-align:right; font-weight:900; outline:none; }

    .calPill{
      display:flex; align-items:center; gap:10px; padding:10px 12px; border:1px solid rgba(255,255,255,.14);
      background:rgba(0,0,0,.18); border-radius:var(--pillRadius); min-width:320px; justify-content:space-between;
    }
    .calRight b{ color:var(--yellow); font-variant-numeric:tabular-nums; }

    /* Filters */
    .filtersBar{ display:flex; gap:10px; flex-wrap:wrap; margin-bottom:14px; }
    .filterPill{ display:flex; align-items:center; gap:10px; padding:8px 12px; border:1px solid rgba(255,255,255,.14); background:rgba(0,0,0,.18); border-radius:var(--pillRadius); }
    .searchInput, .select{ font:inherit; font-size:12px; color:#fff; background:#0a0f1d; border:1px solid rgba(255,255,255,.14); border-radius:12px; padding:8px; outline:none; }

    /* Grid & Cards */
    .grid{ display:grid; grid-template-columns: 1.35fr .65fr; gap:14px; }
    @media (max-width: 980px){ .grid{ grid-template-columns: 1fr; } }

    .card{ border:1px solid var(--stroke); background:linear-gradient(180deg, rgba(255,255,255,.10), rgba(255,255,255,.06)); border-radius:var(--radius); box-shadow:var(--shadow); overflow:hidden; }
    .cardHeader{ padding:14px 16px; display:flex; align-items:center; justify-content:space-between; background:rgba(255,255,255,.03); border-bottom:1px solid rgba(255,255,255,.10); }

    /* Table Styles */
    table{ width:100%; border-collapse:collapse; }
    thead th{ text-align:left; font-size:11px; color:#000; background:linear-gradient(180deg, var(--yellow), var(--yellow2)); padding:10px 14px; }
    tbody td{ padding:10px 14px; border-bottom:1px solid rgba(255,255,255,.06); font-size:13px; vertical-align:top; }
    
    /* Inputs in Table */
    .srcInput, .noteInput, .amtInput{ font:inherit; border:1px solid rgba(255,255,255,.12); border-radius:10px; padding:8px; outline:none; color:#fff; background:rgba(0,0,0,.15); }
    .srcInput{ font-weight:800; width:100%; }
    .noteInput{ font-size:11px; width:100%; margin-top:5px; }
    .amtInput{ font-weight:900; width:90px; text-align:right; }

    /* Rows */
    tr.paidRow{ opacity:0.5; }
    tr.paidRow .srcInput{ text-decoration:line-through; }

    /* Heat levels */
    .heat-low .amtInput{ border-color:var(--good); }
    .heat-high .amtInput{ border-color:var(--bad); }

    /* Footer KPIs */
    .footer{ padding:16px; background:rgba(0,0,0,.15); }
    .kpis{ display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:12px; }
    .kpi{ padding:12px; background:rgba(255,255,255,.05); border-radius:12px; border:1px solid var(--stroke); display:flex; justify-content:space-between; align-items:center; }
    .kpi .value{ font-weight:900; font-size:18px; }

    .bar{ height:8px; background:rgba(0,0,0,0.3); border-radius:10px; overflow:hidden; }
    .bar i{ display:block; height:100%; width:0%; background:var(--yellow); transition:width .3s; }

    /* Buttons */
    button{ cursor:pointer; font:inherit; border-radius:10px; border:1px solid rgba(255,255,255,0.15); background:rgba(255,255,255,0.08); color:#fff; padding:8px 12px; transition:0.2s; }
    button:hover{ background:rgba(255,255,255,0.15); }
    .btnPay.paid{ background:var(--good); color:#000; font-weight:800; }

    /* Right Panel Panels */
    .panel{ background:rgba(255,255,255,0.04); border:1px solid var(--stroke); border-radius:16px; padding:12px; margin-bottom:12px; }
    .panel h3{ margin:0 0 10px; font-size:12px; color:var(--muted); text-transform:uppercase; }
    .sumRow, .miniRow{ display:flex; justify-content:space-between; margin-bottom:6px; font-size:12px; padding:6px; background:rgba(0,0,0,0.1); border-radius:8px; }

    /* Modal */
    .modalOverlay{ position:fixed; inset:0; background:rgba(0,0,0,0.7); display:none; align-items:center; justify-content:center; z-index:100; }
    .modalOverlay.open{ display:flex; }
    .modal{ background:#161b22; width:min(500px, 95%); border-radius:18px; padding:20px; border:1px solid var(--stroke); }

    .subtle{ font-size:11px; color:var(--muted); margin-top:8px; line-height:1.4; }
  </style>
</head>

<body>
  <div class="wrap">
    <!-- TOPBAR -->
    <div class="topbar">
      <div class="title">
        <h1>Xərclərim</h1>
        <p>Gündəlik xərclərin idarəetmə paneli</p>
      </div>

      <div class="calPill">
        <div class="calDate"><b id="todayText">-- -- --</b></div>
        <div class="calRight"><span>İlin sonuna:</span> <b id="countdownText">0 gün</b></div>
      </div>

      <div class="pill">
        <label>Büdcə</label>
        <input id="budgetInput" type="text" value="0" />
      </div>
    </div>

    <!-- FILTERS -->
    <div class="filtersBar">
      <div class="filterPill">
        <label>Ay:</label>
        <select id="monthSelect" class="select"></select>
      </div>
      <div class="filterPill">
        <input id="searchInput" class="searchInput" type="text" placeholder="Axtarış..." />
      </div>
      <div class="filterPill">
        <select id="categoryFilter" class="select">
          <option value="">Bütün kateqoriyalar</option>
          <option value="Market">Market</option>
          <option value="Restoran">Restoran</option>
          <option value="Nəqliyyat">Nəqliyyat</option>
          <option value="Kommunal">Kommunal</option>
          <option value="İllik yığım">İllik yığım</option>
          <option value="Digər">Digər</option>
        </select>
      </div>
    </div>

    <div class="grid">
      <!-- MAIN TABLE CARD -->
      <div class="card">
        <div class="cardHeader">
          <strong>Xərclər Cədvəli</strong>
          <button id="btnAddRow" style="background:var(--yellow2); border:none; color:#000; font-weight:800;">+ Əlavə et</button>
        </div>

        <table>
          <thead>
            <tr>
              <th style="width:65%">MƏNBƏ / QEYD</th>
              <th style="width:35%; text-align:right;">MƏBLƏĞ & AKSİYA</th>
            </tr>
          </thead>
          <tbody id="rows"></tbody>
        </table>

        <div class="footer">
          <div class="kpis">
            <div class="kpi">
              <span class="label">TOTAL:</span>
              <span class="value" id="totalValue">0</span>
            </div>
            <div class="kpi">
              <span class="label">QALIQ:</span>
              <span class="value" id="balanceValue">0</span>
            </div>
          </div>
          <div class="progressBox">
            <div style="display:flex; justify-content:space-between; font-size:11px; margin-bottom:5px;">
              <span>Xərclənən faiz</span>
              <span id="spentPct">0%</span>
            </div>
            <div class="bar"><i id="barFill"></i></div>
          </div>
        </div>

        <div style="padding:15px; border-top:1px solid var(--stroke); display:flex; justify-content:space-between;">
           <strong>Edəcəklər Siyahısı</strong>
           <button id="btnTodoOpen">Siyahını aç</button>
        </div>
      </div>

      <!-- SIDE PANEL -->
      <div class="card" style="padding:15px;">
        <div class="panel">
          <h3>Overtime (Manual)</h3>
          <input id="overtimeManual" class="amtInput" style="width:100%" type="text" value="0" />
        </div>

        <div class="panel">
          <h3>İllik Ümumi Yığım</h3>
          <div class="miniRow">
            <span>Bütün aylar üzrə:</span>
            <b id="annualTotal" style="color:var(--good)">0 AZN</b>
          </div>
          <p class="subtle">"İllik yığım" kateqoriyalı xərclərin cəmidir.</p>
        </div>

        <div class="panel">
          <h3>Kateqoriya üzrə (Bu ay)</h3>
          <div id="categorySums"></div>
        </div>

        <div class="btns" style="display:grid; gap:8px;">
          <button id="btnBackupDownload">Ehtiyat nüsxə (Backup) yüklə</button>
          <button id="btnClearAll" style="color:var(--bad)">Bütün datanı təmizlə</button>
        </div>
      </div>
    </div>
  </div>

  <!-- TODO MODAL -->
  <div class="modalOverlay" id="todoOverlay">
    <div class="modal">
      <div style="display:flex; justify-content:space-between; margin-bottom:15px;">
        <strong>Edəcəklər</strong>
        <button id="btnTodoClose">X</button>
      </div>
      <div style="display:flex; gap:10px; margin-bottom:15px;">
        <input id="todoInput" class="srcInput" placeholder="Yeni tapşırıq..." />
        <button id="btnTodoAdd">Ekle</button>
      </div>
      <div id="todoList"></div>
    </div>
  </div>

  <script>
    // Config & Selectors
    const monthSelect = document.getElementById('monthSelect');
    const rowsBody = document.getElementById('rows');
    const budgetInput = document.getElementById('budgetInput');
    const overtimeInput = document.getElementById('overtimeManual');

    let currentMonthKey = "";
    let db = {}; // All months data

    // 1. Initialize Months
    function initMonths() {
      const months = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "İyun", "İyul", "Avqust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"];
      const year = 2026;
      months.forEach((m, idx) => {
        const opt = document.createElement('option');
        const key = `${m}_${year}`;
        opt.value = key;
        opt.textContent = `${m} ${year}`;
        monthSelect.appendChild(opt);
      });

      // Set current month
      const now = new Date();
      monthSelect.selectedIndex = now.getMonth();
      currentMonthKey = monthSelect.value;
    }

    // 2. Data Management
    function loadData() {
      const saved = localStorage.getItem('xerc_db_v2');
      db = saved ? JSON.parse(saved) : {};
      if (!db[currentMonthKey]) {
        db[currentMonthKey] = { budget: 0, overtime: 0, items: [] };
      }
      render();
    }

    function saveData() {
      localStorage.setItem('xerc_db_v2', JSON.stringify(db));
      updateSummary();
    }

    // 3. Rendering
    function render() {
      const monthData = db[currentMonthKey];
      budgetInput.value = monthData.budget || 0;
      overtimeInput.value = monthData.overtime || 0;
      
      const search = document.getElementById('searchInput').value.toLowerCase();
      const catFilter = document.getElementById('categoryFilter').value;

      rowsBody.innerHTML = "";
      monthData.items.forEach((item, index) => {
        if (search && !item.src.toLowerCase().includes(search)) return;
        if (catFilter && item.cat !== catFilter) return;

        const tr = document.createElement('tr');
        if (item.paid) tr.classList.add('paidRow');
        
        // Heat logic
        const val = parseFloat(item.amt) || 0;
        if (val > 500) tr.classList.add('heat-high');
        else if (val > 0 && val < 50) tr.classList.add('heat-low');

        tr.innerHTML = `
          <td>
            <input class="srcInput" value="${item.src}" onchange="updateItem(${index}, 'src', this.value)" placeholder="Mənbə...">
            <div style="display:flex; gap:5px; align-items:center; margin-top:5px;">
              <select class="select" style="padding:4px; font-size:10px;" onchange="updateItem(${index}, 'cat', this.value)">
                <option ${item.cat === 'Market' ? 'selected' : ''}>Market</option>
                <option ${item.cat === 'Restoran' ? 'selected' : ''}>Restoran</option>
                <option ${item.cat === 'Nəqliyyat' ? 'selected' : ''}>Nəqliyyat</option>
                <option ${item.cat === 'Kommunal' ? 'selected' : ''}>Kommunal</option>
                <option ${item.cat === 'İllik yığım' ? 'selected' : ''}>İllik yığım</option>
                <option ${item.cat === 'Digər' ? 'selected' : ''}>Digər</option>
              </select>
              <input class="noteInput" style="margin:0" value="${item.note || ''}" onchange="updateItem(${index}, 'note', this.value)" placeholder="Qeyd...">
            </div>
          </td>
          <td style="text-align:right">
            <input class="amtInput" type="number" value="${item.amt}" onchange="updateItem(${index}, 'amt', this.value)">
            <div style="margin-top:8px; display:flex; justify-content:flex-end; gap:5px;">
              <button class="btnPay ${item.paid ? 'paid' : ''}" onclick="togglePaid(${index})">${item.paid ? 'Ödənildi' : 'Ödə'}</button>
              <button onclick="deleteItem(${index})" style="color:var(--bad)">×</button>
            </div>
          </td>
        `;
        rowsBody.appendChild(tr);
      });
      updateSummary();
    }

    // 4. Actions
    window.updateItem = (idx, key, val) => {
      db[currentMonthKey].items[idx][key] = val;
      saveData();
      if(key === 'amt') render(); // re-render for heat
    };

    window.togglePaid = (idx) => {
      db[currentMonthKey].items[idx].paid = !db[currentMonthKey].items[idx].paid;
      saveData();
      render();
    };

    window.deleteItem = (idx) => {
      db[currentMonthKey].items.splice(idx, 1);
      saveData();
      render();
    };

    document.getElementById('btnAddRow').onclick = () => {
      db[currentMonthKey].items.push({ src: "", amt: 0, cat: "Market", paid: false, note: "" });
      saveData();
      render();
    };

    // 5. Calculations
    function updateSummary() {
      const data = db[currentMonthKey];
      const items = data.items;
      
      const total = items.reduce((sum, i) => sum + (parseFloat(i.amt) || 0), 0);
      const budget = parseFloat(budgetInput.value) || 0;
      const overtime = parseFloat(overtimeInput.value) || 0;
      const balance = (budget + overtime) - total;

      document.getElementById('totalValue').textContent = total.toFixed(2) + " AZN";
      document.getElementById('balanceValue').textContent = balance.toFixed(2) + " AZN";
      
      // Progress bar
      const pct = budget > 0 ? Math.min((total / budget) * 100, 100) : 0;
      document.getElementById('spentPct').textContent = Math.round(pct) + "%";
      document.getElementById('barFill').style.width = pct + "%";

      // Annual and Categories
      let annualSum = 0;
      let catMap = {};

      Object.values(db).forEach(m => {
        m.items.forEach(it => {
          if (it.cat === "İllik yığım") annualSum += (parseFloat(it.amt) || 0);
        });
      });

      data.items.forEach(it => {
        catMap[it.cat] = (catMap[it.cat] || 0) + (parseFloat(it.amt) || 0);
      });

      document.getElementById('annualTotal').textContent = annualSum.toFixed(2) + " AZN";
      
      const catDiv = document.getElementById('categorySums');
      catDiv.innerHTML = "";
      for (let [c, v] of Object.entries(catMap)) {
        catDiv.innerHTML += `<div class="sumRow"><span>${c}</span><b>${v.toFixed(2)}</b></div>`;
      }
    }

    // 6. UI Helpers (Countdown etc)
    function runClock() {
      const now = new Date();
      document.getElementById('todayText').textContent = now.toLocaleDateString('az-AZ', { day:'numeric', month:'long', year:'numeric' });
      
      const endYear = new Date(now.getFullYear(), 11, 31);
      const diff = Math.ceil((endYear - now) / (1000 * 60 * 60 * 24));
      document.getElementById('countdownText').textContent = diff + " gün";
    }

    // Listeners
    monthSelect.onchange = (e) => { 
      currentMonthKey = e.target.value; 
      loadData(); 
    };
    budgetInput.oninput = (e) => { 
      db[currentMonthKey].budget = e.target.value; 
      saveData(); 
    };
    overtimeInput.oninput = (e) => { 
      db[currentMonthKey].overtime = e.target.value; 
      saveData(); 
    };
    document.getElementById('searchInput').oninput = render;
    document.getElementById('categoryFilter').onchange = render;

    // Backup & Clear
    document.getElementById('btnBackupDownload').onclick = () => {
      const blob = new Blob([JSON.stringify(db, null, 2)], {type: 'application/json'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Xercler_Backup_${new Date().toISOString().slice(0,10)}.json`;
      a.click();
    };

    document.getElementById('btnClearAll').onclick = () => {
      if(confirm("Bütün məlumatlar silinsin?")) {
        db = {};
        saveData();
        loadData();
      }
    };

    // Todo Logic Simple
    const todoOverlay = document.getElementById('todoOverlay');
    document.getElementById('btnTodoOpen').onclick = () => todoOverlay.classList.add('open');
    document.getElementById('btnTodoClose').onclick = () => todoOverlay.classList.remove('open');

    // Init
    initMonths();
    loadData();
    runClock();
  </script>
</body>
</html>
