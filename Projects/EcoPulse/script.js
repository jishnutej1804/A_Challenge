/* EcoPulse script.js */

  const navbar = document.getElementById('navbar');
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('navMenu');
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Navbar scroll state
  const onScroll = () => navbar.classList.toggle('is-scrolled', scrollY > 10);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Mobile menu
  const setMenu = open => { menu.classList.toggle('is-open', open); toggle.setAttribute('aria-expanded', open); document.body.classList.toggle('no-scroll', open); };
  toggle.addEventListener('click', () => setMenu(!menu.classList.contains('is-open')));
  menu.addEventListener('click', e => { if (e.target.closest('a')) setMenu(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

  // Reveal, counters and bar animation when scrolled into view
  const animateCount = el => {
    const end = +el.dataset.count, suffix = el.dataset.suffix || '';
    if (reduceMotion) return;
    const start = performance.now();
    const tick = now => {
      const t = Math.min((now - start) / 900, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - t, 3))) + suffix;
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  const io = new IntersectionObserver(entries => entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('is-visible');
    entry.target.querySelectorAll('[data-count]').forEach(animateCount);
    io.unobserve(entry.target);
  }), { threshold: 0.2 });
  document.querySelectorAll('.reveal, .impact-card, .stat-grid, .dashboard, .goal-card').forEach(el => io.observe(el));

/* =====================================================
   1. CONFIG: every environmental assumption lives here.
   These factors are DEMO PLACEHOLDERS, not sourced data.
   Replace them with cited values (and note the source) later.
   ===================================================== */
const FACTORS = {
  status: 'demo-placeholder',
  transport: { carKm: 0.17, transitKm: 0.06 },        // kg CO2e per km
  energy:    { kwh: 0.7, lpgKg: 3 },                  // per kWh / per kg
  food:      { meat: 170, average: 120, vegetarian: 80, vegan: 60 }, // per month by diet
  shopping:  { clothingItem: 10 },                    // per item
  waste:     { perKg: 0.5, recyclingCredit: 0.5 }     // recycling cuts waste impact by up to 50%
};
const CONFIG = { meterMax: 500, levels: [[150, 'Lower impact'], [300, 'Moderate impact'], [Infinity, 'Higher impact']], xpPerLevel: 100 };
const DEFAULT_INPUTS = { carKm: 150, transitKm: 40, kwh: 80, lpgKg: 4, diet: 'vegetarian', clothing: 1, wasteKg: 20, recycling: 30 };
const ACTIONS = [
  { id: 'cycle',   icon: '🚲', title: 'Replace one car trip', desc: 'Walk, cycle or take transit for one short trip.', difficulty: 'Easy', kg: 3, xp: 10 },
  { id: 'transit', icon: '🚌', title: 'Use public transport', desc: 'Leave the car at home for a full day.', difficulty: 'Medium', kg: 5, xp: 20 },
  { id: 'power',   icon: '💡', title: 'Cut standby power', desc: 'Switch off devices you are not using.', difficulty: 'Easy', kg: 1, xp: 10 },
  { id: 'meal',    icon: '🥗', title: 'Choose a lower-impact meal', desc: 'Pick a plant-based meal today.', difficulty: 'Easy', kg: 2, xp: 10 },
  { id: 'recycle', icon: '♻️', title: 'Recycle plastic', desc: 'Sort and recycle your plastic waste.', difficulty: 'Easy', kg: 1, xp: 10 },
  { id: 'buy',     icon: '🛍️', title: 'Skip an unnecessary purchase', desc: 'Wait before buying something you do not need.', difficulty: 'Medium', kg: 4, xp: 20 }
];

/* =====================================================
   2. CALCULATION ENGINE: pure functions, no DOM access
   ===================================================== */
function calculate(i, f = FACTORS) {
  const byCategory = {
    Transportation: i.carKm * f.transport.carKm + i.transitKm * f.transport.transitKm,
    Energy: i.kwh * f.energy.kwh + i.lpgKg * f.energy.lpgKg,
    Food: f.food[i.diet] ?? f.food.average,
    Shopping: i.clothing * f.shopping.clothingItem,
    Waste: i.wasteKg * f.waste.perKg * (1 - (i.recycling / 100) * f.waste.recyclingCredit)
  };
  const total = Object.values(byCategory).reduce((a, b) => a + b, 0);
  return { total: Math.round(total), byCategory };
}
const levelLabel = kg => CONFIG.levels.find(([max]) => kg < max)[1];

/* =====================================================
   3. STORAGE: swap this for an API call in the backend stage
   ===================================================== */
const KEY = 'ecopulse:v1';
const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch { return {}; } };
const save = data => { try { localStorage.setItem(KEY, JSON.stringify(data)); } catch { /* storage unavailable */ } };
let store = load();   // { inputs, actions: { id: [dates] } }

/* =====================================================
   4. UI: calculator, meter, breakdown
   ===================================================== */
const $ = id => document.getElementById(id);
const form = $('calcForm');

function readInputs() {
  const v = {};
  for (const el of form.elements) {
    if (!el.name) continue;
    v[el.name] = el.tagName === 'SELECT' ? el.value : Math.max(0, Number(el.value) || 0);
  }
  return v;
}
function fillForm(inputs) {
  for (const [k, val] of Object.entries(inputs)) if (form.elements[k]) form.elements[k].value = val;
  $('recyclingOut').textContent = inputs.recycling + '%';
}
function renderResult() {
  const inputs = store.inputs || DEFAULT_INPUTS;
  const { total, byCategory } = calculate(inputs);
  $('resultTotal').textContent = total;
  $('resultTag').textContent = store.inputs ? 'Your estimate' : 'Demo data';
  $('meterFill').style.width = Math.min(total / CONFIG.meterMax * 100, 100) + '%';
  $('meterLabel').textContent = levelLabel(total);
  $('breakdown').innerHTML = Object.entries(byCategory).map(([name, kg]) => {
    const pct = total ? Math.round(kg / total * 100) : 0;
    return `<li><span>${name}</span><b>${pct}%</b><div class="fill"><i style="--value:${pct}"></i></div></li>`;
  }).join('');
  renderSimulator();
}
form.addEventListener('input', e => { if (e.target.name === 'recycling') $('recyclingOut').textContent = e.target.value + '%'; });
form.addEventListener('submit', e => {
  e.preventDefault();
  store.inputs = readInputs();
  save(store); renderResult();
  $('formMsg').textContent = 'Saved. Your results are updated.';
});
$('resetBtn').addEventListener('click', () => {
  delete store.inputs; save(store); fillForm(DEFAULT_INPUTS); renderResult();
  $('formMsg').textContent = 'Back to demo values.';
});

/* =====================================================
   5. WHAT-IF SIMULATOR: reuses calculate() with changed inputs
   ===================================================== */
const sims = ['Car', 'Energy', 'Food'];
function renderSimulator() {
  const base = store.inputs || DEFAULT_INPUTS;
  const cut = n => Number($('sim' + n).value) / 100;
  sims.forEach(n => $('sim' + n + 'Out').textContent = $('sim' + n).value + '%');
  const before = calculate(base);
  const changed = { ...base, carKm: base.carKm * (1 - cut('Car')), kwh: base.kwh * (1 - cut('Energy')) };
  const after = calculate(changed);
  const afterTotal = Math.round(after.total - after.byCategory.Food * cut('Food'));
  const saving = before.total - afterTotal;
  const scale = Math.max(before.total, 1);
  $('baBefore').style.width = '100%';
  $('baAfter').style.width = Math.max(afterTotal / scale * 100, 0) + '%';
  $('baBeforeVal').textContent = before.total + ' kg';
  $('baAfterVal').textContent = afterTotal + ' kg';
  $('simSaving').textContent = saving > 0 ? `Projected reduction: ${saving} kg CO₂e per month (estimate)` : 'Move a slider to see a projected change.';
}
sims.forEach(n => $('sim' + n).addEventListener('input', renderSimulator));

/* =====================================================
   6. ECO ACTIONS, STREAK AND XP
   Rule: each action counts once per day, so clicking repeatedly earns nothing.
   ===================================================== */
const dayKey = d => d.toLocaleDateString('en-CA');           // local YYYY-MM-DD
const today = () => dayKey(new Date());
const daysBetween = (a, b) => Math.round((new Date(b + 'T00:00:00') - new Date(a + 'T00:00:00')) / 864e5);
function getStats() {
  const done = store.actions || {};
  const days = new Set(Object.values(done).flat());
  let xp = 0;
  ACTIONS.forEach(a => xp += (done[a.id] || []).length * a.xp);
  let cur = 0, d = new Date();
  if (!days.has(dayKey(d))) d.setDate(d.getDate() - 1);
  while (days.has(dayKey(d))) { cur++; d.setDate(d.getDate() - 1); }
  let best = 0, run = 0, prev = null;
  [...days].sort().forEach(day => { run = prev && daysBetween(prev, day) === 1 ? run + 1 : 1; best = Math.max(best, run); prev = day; });
  return { cur, best, xp };
}
function renderActions() {
  const done = store.actions || {};
  $('actionGrid').innerHTML = ACTIONS.map(a => {
    const isDone = (done[a.id] || []).includes(today());
    return `<article class="action-card"><h3>${a.icon} ${a.title}</h3><p>${a.desc}</p>
      <p class="action-meta"><span>${a.difficulty}</span><span>≈ ${a.kg} kg CO₂e (demo)</span><span>+${a.xp} XP</span></p>
      <button class="cta-button cta-small" data-action="${a.id}" ${isDone ? 'disabled' : ''}>${isDone ? 'Done today ✓' : 'Complete action'}</button></article>`;
  }).join('');
  const s = getStats();
  $('streakNow').innerHTML = `${s.cur} <small>days</small>`;
  $('streakBest').innerHTML = `${s.best} <small>days</small>`;
  $('levelNum').textContent = Math.floor(s.xp / CONFIG.xpPerLevel) + 1;
  $('xpFill').style.width = (s.xp % CONFIG.xpPerLevel) + '%';
  $('xpText').textContent = `${s.xp % CONFIG.xpPerLevel} / ${CONFIG.xpPerLevel} XP to next level`;
}
$('actionGrid').addEventListener('click', e => {
  const btn = e.target.closest('[data-action]');
  if (!btn) return;
  store.actions = store.actions || {};
  (store.actions[btn.dataset.action] = store.actions[btn.dataset.action] || []).push(today());
  save(store); renderActions();
});

/* Highlight the nav link of the section in view */
const links = [...document.querySelectorAll('.nav-menu li a')];
const spy = new IntersectionObserver(entries => entries.forEach(en => {
  if (en.isIntersecting) links.forEach(l => (l.hash === '#' + en.target.id) ? l.setAttribute('aria-current', 'true') : l.removeAttribute('aria-current'));
}), { rootMargin: '-45% 0px -50% 0px' });
links.forEach(l => { const s = document.querySelector(l.hash); if (s) spy.observe(s); });

/* Start */
fillForm(store.inputs || DEFAULT_INPUTS);
renderResult();
renderActions();


/* =====================================================
   7. THEME: saved choice, else system preference.
   The pre-paint script in <head> sets data-theme first (no flash).
   ===================================================== */
const root = document.documentElement;
const themeBtns = [...document.querySelectorAll('[data-theme-toggle]')];   // menu/desktop button + mobile header button
function applyTheme(theme, remember) {
  root.dataset.theme = theme;
  const next = theme === 'dark' ? 'light' : 'dark';
  themeBtns.forEach(b => {
    b.setAttribute('aria-pressed', theme === 'dark');
    b.setAttribute('aria-label', 'Switch to ' + next + ' mode');
    const label = b.querySelector('.theme-label'); if (label) label.textContent = 'Switch to ' + next + ' mode';
  });
  if (remember) { try { localStorage.setItem('ecopulse:theme', theme); } catch { /* ignore */ } }
}
applyTheme(root.dataset.theme || 'light', false);
themeBtns.forEach(b => b.addEventListener('click', () => {
  root.classList.add('theme-anim');                   // short, subtle colour transition
  applyTheme(root.dataset.theme === 'dark' ? 'light' : 'dark', true);
  setTimeout(() => root.classList.remove('theme-anim'), 400);
}));
matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
  let saved = null; try { saved = localStorage.getItem('ecopulse:theme'); } catch { /* ignore */ }
  if (!saved) applyTheme(e.matches ? 'dark' : 'light', false);
});

/* Close the mobile menu if the window grows to desktop width */
matchMedia('(min-width: 1024px)').addEventListener('change', e => { if (e.matches) setMenu(false); });