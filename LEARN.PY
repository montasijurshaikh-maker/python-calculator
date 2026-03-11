<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Python Projects</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    min-height: 100vh;
    background: #080c08;
    font-family: 'Courier New', monospace;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 28px 16px;
    background-image: radial-gradient(ellipse at 20% 20%, #0a1f0a 0%, transparent 60%),
                      radial-gradient(ellipse at 80% 80%, #0a1a0a 0%, transparent 60%);
  }

  .header { text-align: center; margin-bottom: 28px; }
  .label { font-size: 11px; color: #00ff41; letter-spacing: 6px; margin-bottom: 10px; text-transform: uppercase; }
  .title { font-size: clamp(22px, 5vw, 40px); color: #fff; font-weight: 900; letter-spacing: -1px; }
  .subtitle { color: #3a5a3a; font-size: 13px; margin-top: 8px; }

  .tabs {
    display: flex; gap: 10px; flex-wrap: wrap;
    justify-content: center; margin-bottom: 22px;
  }

  .tab {
    background: #0e130e;
    border: 1.5px solid #1c2c1c;
    color: #3a5a3a;
    padding: 9px 18px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 13px;
    font-family: monospace;
    transition: all 0.2s;
    font-weight: 600;
  }
  .tab:hover { border-color: #00aa00; color: #00cc00; transform: translateY(-2px); }
  .tab.active { border-color: #00ff41; color: #00ff41; background: #0a1f0a; }

  .terminal {
    width: 100%; max-width: 780px;
    background: #0a0d0a;
    border: 1px solid #1a2e1a;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 0 80px #00ff0015, 0 30px 80px #00000099;
  }

  .term-bar {
    background: #0f120f;
    padding: 13px 18px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px solid #1a2a1a;
  }
  .dot { width: 13px; height: 13px; border-radius: 50%; }
  .dot-r { background: #ff5f57; }
  .dot-y { background: #febc2e; }
  .dot-g { background: #28c840; }
  .term-title { color: #2a4a2a; font-size: 12px; flex: 1; text-align: center; letter-spacing: 1px; }

  .code-area {
    padding: 22px;
    min-height: 260px;
    position: relative;
  }

  pre {
    color: #00cc00;
    font-size: clamp(11px, 2vw, 13.5px);
    line-height: 1.75;
    white-space: pre-wrap;
    word-break: break-word;
  }

  .cursor {
    display: inline-block;
    width: 8px; height: 14px;
    background: #00ff41;
    vertical-align: middle;
    animation: blink 0.7s infinite;
    margin-left: 2px;
  }

  .run-area { padding: 0 22px 20px; display: flex; align-items: center; gap: 14px; }

  .run-btn {
    background: #00bb00;
    color: #000;
    border: none;
    padding: 12px 32px;
    border-radius: 9px;
    cursor: pointer;
    font-size: 15px;
    font-weight: 900;
    font-family: monospace;
    transition: all 0.2s;
    letter-spacing: 1px;
  }
  .run-btn:hover:not(:disabled) { background: #00dd00; transform: scale(1.05); }
  .run-btn:active:not(:disabled) { transform: scale(0.97); }
  .run-btn:disabled { background: #1a2a1a; color: #2a4a2a; cursor: not-allowed; }

  .spinner {
    width: 22px; height: 22px;
    border: 3px solid #1a3a1a;
    border-top-color: #00ff41;
    border-radius: 50%;
    animation: spin 0.7s linear infinite;
    display: none;
  }

  .output-box {
    margin: 0 22px 22px;
    background: #050a05;
    border: 1px solid #1a3a1a;
    border-radius: 12px;
    padding: 18px;
    display: none;
    animation: fadeUp 0.4s ease;
  }
  .out-label { color: #2a4a2a; font-size: 10px; letter-spacing: 3px; margin-bottom: 12px; }

  /* Palette */
  .palette { display: flex; gap: 10px; flex-wrap: wrap; }
  .swatch { text-align: center; }
  .swatch-box { width: 56px; height: 56px; border-radius: 10px; border: 2px solid #1a2a1a; }
  .swatch-hex { color: #445544; font-size: 10px; margin-top: 4px; }

  /* Password */
  .pwd-chars { display: flex; gap: 3px; flex-wrap: wrap; margin-top: 10px; }
  .pwd-c { padding: 3px 5px; border-radius: 4px; font-size: 13px; font-weight: bold; color: #fff; }
  .c-upper { background: #2244aa; }
  .c-lower { background: #228855; }
  .c-digit { background: #aa5522; }
  .c-sym   { background: #993355; }
  .legend { display: flex; gap: 10px; margin-top: 10px; flex-wrap: wrap; font-size: 11px; }

  /* Stats */
  .stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 8px; }
  .stat-card { background: #0a150a; border: 1px solid #1a3a1a; border-radius: 9px; padding: 10px; }
  .stat-label { color: #445544; font-size: 10px; letter-spacing: 1px; }
  .stat-val { color: #00ee00; font-size: 22px; font-weight: bold; margin-top: 2px; }

  /* Dice */
  .dice-wrap { text-align: center; }
  .dice-row { display: flex; gap: 24px; justify-content: center; margin-bottom: 12px; }
  .die { font-size: 72px; filter: drop-shadow(0 0 18px #00ff4155); }
  .dice-total { color: #ffff80; font-size: 24px; font-weight: bold; }
  .dice-msg { color: #80ff80; font-size: 20px; margin-top: 8px; }

  /* Number Game */
  .num-game { text-align: center; }
  .secret-area { margin: 12px 0; }
  .num-input-row { display: flex; gap: 10px; justify-content: center; margin-top: 12px; }
  .num-input { background: #0a150a; border: 1px solid #1a3a1a; color: #00ff41; padding: 10px 16px; border-radius: 8px; font-size: 18px; font-family: monospace; width: 100px; text-align: center; outline: none; }
  .guess-btn { background: #006600; color: #00ff41; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-family: monospace; font-size: 14px; font-weight: bold; }
  .guess-btn:hover { background: #008800; }
  .hint-txt { font-size: 20px; margin-top: 12px; min-height: 30px; }
  .tries-txt { color: #445544; font-size: 12px; margin-top: 6px; }

  .tags { margin-top: 20px; display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }
  .tag { background: #0e130e; border: 1px solid #1a2a1a; color: #3a5a3a; padding: 6px 14px; border-radius: 20px; font-size: 11px; }

  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
  @keyframes spin { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
  @keyframes fadeUp { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
</style>
</head>
<body>

<div class="header">
  <div class="label">🐍 Python Projects</div>
  <h1 class="title">Reel-Worthy Projects</h1>
  <p class="subtitle">Click করো → Run করো → Reel বানাও!</p>
</div>

<div class="tabs">
  <button class="tab active" onclick="selectProject(0)">🎨 Color Palette</button>
  <button class="tab" onclick="selectProject(1)">🔐 Password Gen</button>
  <button class="tab" onclick="selectProject(2)">📊 Number Stats</button>
  <button class="tab" onclick="selectProject(3)">🎲 Dice Game</button>
  <button class="tab" onclick="selectProject(4)">🔢 Guessing Game</button>
</div>

<div class="terminal">
  <div class="term-bar">
    <div class="dot dot-r"></div>
    <div class="dot dot-y"></div>
    <div class="dot dot-g"></div>
    <span class="term-title" id="termTitle">project.py</span>
  </div>
  <div class="code-area">
    <pre id="codeDisplay"><span style="color:#2a4a2a">$ </span></pre>
  </div>
  <div class="run-area">
    <button class="run-btn" id="runBtn" onclick="runCode()">▶ Run Code</button>
    <div class="spinner" id="spinner"></div>
  </div>
  <div class="output-box" id="outputBox">
    <div class="out-label">OUTPUT ▼</div>
    <div id="outputContent"></div>
  </div>
</div>

<div class="tags">
  <span class="tag">🟢 Beginner Friendly</span>
  <span class="tag">⚡ Fast to Build</span>
  <span class="tag">📱 Reel-Ready</span>
  <span class="tag">🆓 100% Free</span>
</div>

<script>
const projects = [
  {
    title: "color_palette.py",
    code: `import random

def generate_palette(n=5):
    palette = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        palette.append(hex_color)
    return palette

colors = generate_palette()
print("Your Palette:", colors)`,
    run: function() {
      const colors = Array.from({length:5}, () => {
        const r = Math.floor(Math.random()*256);
        const g = Math.floor(Math.random()*256);
        const b = Math.floor(Math.random()*256);
        return `#${r.toString(16).padStart(2,'0')}${g.toString(16).padStart(2,'0')}${b.toString(16).padStart(2,'0')}`;
      });
      let html = '<div class="palette">';
      colors.forEach(c => {
        html += `<div class="swatch"><div class="swatch-box" style="background:${c};box-shadow:0 0 14px ${c}66"></div><div class="swatch-hex">${c}</div></div>`;
      });
      html += '</div>';
      return html;
    }
  },
  {
    title: "password_gen.py",
    code: `import random, string

def generate_password(length=16):
    chars = (string.ascii_letters + 
             string.digits + 
             "!@#$%^&*")
    password = ''.join(
        random.choice(chars) 
        for _ in range(length)
    )
    strength = "💪 Strong!"
    return password, strength

pwd, level = generate_password(16)
print(f"Password: {pwd}")
print(f"Strength: {level}")`,
    run: function() {
      const upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
      const lower = 'abcdefghijklmnopqrstuvwxyz';
      const digits = '0123456789';
      const syms = '!@#$%^&*';
      const all = upper+lower+digits+syms;
      const pwd = Array.from({length:16}, () => all[Math.floor(Math.random()*all.length)]);
      let chars = '';
      pwd.forEach(c => {
        let cls = upper.includes(c)?'c-upper':lower.includes(c)?'c-lower':digits.includes(c)?'c-digit':'c-sym';
        chars += `<span class="pwd-c ${cls}">${c}</span>`;
      });
      return `<p style="color:#a0ffa0;font-family:monospace">Password: <b style="color:#ffff80">${pwd.join('')}</b></p>
<p style="color:#80ff80;margin-top:6px">Strength: 💪 Strong!</p>
<div class="pwd-chars">${chars}</div>
<div class="legend">
  <span style="color:#4488ee">■ Uppercase</span>
  <span style="color:#44cc88">■ Lowercase</span>
  <span style="color:#ee8844">■ Digit</span>
  <span style="color:#cc4488">■ Symbol</span>
</div>`;
    }
  },
  {
    title: "number_stats.py",
    code: `def analyze(numbers):
    total  = sum(numbers)
    mean   = total / len(numbers)
    srtd   = sorted(numbers)
    median = srtd[len(srtd)//2]
    
    return {
        "Mean"  : round(mean, 1),
        "Median": median,
        "Max"   : max(numbers),
        "Min"   : min(numbers),
        "Sum"   : total
    }

data = [23,45,12,67,34,89,56,71]
stats = analyze(data)
for k,v in stats.items():
    print(f"{k:8}: {v}")`,
    run: function() {
      const nums = Array.from({length:8}, () => Math.floor(Math.random()*99)+1);
      const sorted = [...nums].sort((a,b)=>a-b);
      const sum = nums.reduce((a,b)=>a+b,0);
      const stats = [
        ["Mean 📈", (sum/nums.length).toFixed(1)],
        ["Median 📊", sorted[Math.floor(sorted.length/2)]],
        ["Max ⬆️", Math.max(...nums)],
        ["Min ⬇️", Math.min(...nums)],
        ["Sum ➕", sum],
        ["Count 🔢", nums.length]
      ];
      let cards = stats.map(([k,v]) => `<div class="stat-card"><div class="stat-label">${k}</div><div class="stat-val">${v}</div></div>`).join('');
      return `<p style="color:#445544;font-family:monospace;font-size:12px;margin-bottom:10px">Data: [${nums.join(', ')}]</p><div class="stats-grid">${cards}</div>`;
    }
  },
  {
    title: "dice_game.py",
    code: `import random

def roll_dice(sides=6, count=2):
    rolls = [random.randint(1, sides)
             for _ in range(count)]
    total = sum(rolls)
    
    if total == 12:
        result = "🎉 JACKPOT!"
    elif total >= 9:
        result = "😄 Great Roll!"
    elif total >= 6:
        result = "👍 Not Bad!"
    else:
        result = "🎲 Try Again!"
    
    return rolls, total, result

dice, total, msg = roll_dice(6, 2)
print(f"Rolled: {dice}")
print(f"Total : {total}")
print(f"Result: {msg}")`,
    run: function() {
      const faces = ['','⚀','⚁','⚂','⚃','⚄','⚅'];
      const d1 = Math.floor(Math.random()*6)+1;
      const d2 = Math.floor(Math.random()*6)+1;
      const total = d1+d2;
      const msg = total===12?"🎉 JACKPOT!":total>=9?"😄 Great Roll!":total>=6?"👍 Not Bad!":"🎲 Try Again!";
      return `<div class="dice-wrap">
        <div class="dice-row"><span class="die">${faces[d1]}</span><span class="die">${faces[d2]}</span></div>
        <div class="dice-total">Total: ${total}</div>
        <div class="dice-msg">${msg}</div>
      </div>`;
    }
  },
  {
    title: "guessing_game.py",
    code: `import random

secret = random.randint(1, 100)
tries  = 0

print("1 থেকে 100 এর মধ্যে একটি সংখ্যা আছে!")

while True:
    guess = int(input("তোমার অনুমান: "))
    tries += 1
    
    if guess < secret:
        print("⬆️  আরো বড়!")
    elif guess > secret:
        print("⬇️  আরো ছোট!")
    else:
        print(f"🎉 সঠিক! {tries} চেষ্টায়!")
        break`,
    run: function() {
      window._secret = Math.floor(Math.random()*100)+1;
      window._tries = 0;
      return `<div class="num-game">
        <p style="color:#a0ffa0;font-size:14px">🎮 ১ থেকে ১০০ এর মধ্যে একটি সংখ্যা আছে!</p>
        <div class="num-input-row">
          <input class="num-input" id="guessInput" type="number" min="1" max="100" placeholder="??">
          <button class="guess-btn" onclick="makeGuess()">অনুমান করো!</button>
        </div>
        <div class="hint-txt" id="hintTxt" style="color:#ffff80"></div>
        <div class="tries-txt" id="triesTxt">চেষ্টা: 0</div>
      </div>`;
    }
  }
];

function makeGuess() {
  const input = document.getElementById('guessInput');
  const hint = document.getElementById('hintTxt');
  const triesEl = document.getElementById('triesTxt');
  const val = parseInt(input.value);
  if (!val || val < 1 || val > 100) { hint.textContent = '⚠️ ১ থেকে ১০০ এর মধ্যে দাও!'; return; }
  window._tries++;
  triesEl.textContent = `চেষ্টা: ${window._tries}`;
  if (val < window._secret) hint.innerHTML = `<span style="color:#ff8844">⬆️ আরো বড় সংখ্যা!</span>`;
  else if (val > window._secret) hint.innerHTML = `<span style="color:#4488ff">⬇️ আরো ছোট সংখ্যা!</span>`;
  else {
    hint.innerHTML = `<span style="color:#00ff41">🎉 সঠিক! ${window._tries} চেষ্টায় জিতেছ!</span>`;
    input.disabled = true;
    document.querySelector('.guess-btn').disabled = true;
  }
  input.value = '';
  input.focus();
}

let current = 0;
let typingInterval = null;

function selectProject(i) {
  current = i;
  document.querySelectorAll('.tab').forEach((t,j) => t.classList.toggle('active', i===j));
  document.getElementById('termTitle').textContent = projects[i].title;
  document.getElementById('outputBox').style.display = 'none';
  document.getElementById('runBtn').disabled = true;
  document.getElementById('runBtn').textContent = '⌨️ Loading...';

  clearInterval(typingInterval);
  const pre = document.getElementById('codeDisplay');
  const code = projects[i].code;
  let idx = 0;
  pre.innerHTML = '<span style="color:#2a4a2a">$ </span>';

  typingInterval = setInterval(() => {
    if (idx < code.length) {
      const char = code[idx] === '<' ? '&lt;' : code[idx] === '>' ? '&gt;' : code[idx] === '&' ? '&amp;' : code[idx];
      pre.innerHTML = '<span style="color:#2a4a2a">$ </span>' +
        escapeHtml(code.slice(0, idx+1)) +
        '<span class="cursor"></span>';
      idx++;
    } else {
      clearInterval(typingInterval);
      pre.innerHTML = '<span style="color:#2a4a2a">$ </span>' + escapeHtml(code);
      document.getElementById('runBtn').disabled = false;
      document.getElementById('runBtn').textContent = '▶ Run Code';
    }
  }, 14);
}

function escapeHtml(str) {
  return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function runCode() {
  const btn = document.getElementById('runBtn');
  const spinner = document.getElementById('spinner');
  const box = document.getElementById('outputBox');
  btn.disabled = true;
  btn.textContent = '⏳ Running...';
  spinner.style.display = 'block';
  box.style.display = 'none';

  setTimeout(() => {
    const html = projects[current].run();
    document.getElementById('outputContent').innerHTML = html;
    box.style.display = 'block';
    spinner.style.display = 'none';
    btn.disabled = false;
    btn.textContent = '▶ Run Again';
  }, 1100);
}

// Init
selectProject(0);
</script>
</body>
</html>