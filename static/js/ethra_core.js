(function() {
  // ── Always show landing page first ──
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  const worldSection = document.getElementById('section-world');
  if (worldSection) worldSection.classList.add('active');

  // ── Arc tabs + the falling tome (round 9) ──
  // The shelf never hides. The chosen volume tips over and lies flat on its
  // board, the neighbours lean across it, and once it lands the silk ribbon
  // drops and the folio opens below the stacks.
  const arcNav = document.getElementById('arcNav');
  const storySection = document.getElementById('section-story');
  const shelfReturn = document.getElementById('shelfReturn');

  let fallenTab = null;
  function clearFall() {
    if (!arcNav) return;
    arcNav.querySelectorAll('.arc-tab').forEach(t => {
      t.classList.remove('fallen', 'lean-l', 'lean-r', 'active');
      t.style.transition = '';
      t.style.transform = '';
    });
  }
  /* FLIP: capture x, mutate the shelf, invert, let the 0.7s transition play */
  function flipTabs(mutate) {
    if (!arcNav) return;
    const tabs = Array.from(arcNav.querySelectorAll('.arc-tab'));
    const firstX = new Map(tabs.map(t => [t, t.getBoundingClientRect().left]));
    mutate();
    arcNav.getBoundingClientRect();
    tabs.forEach(t => {
      const dx = firstX.get(t) - t.getBoundingClientRect().left;
      if (Math.abs(dx) > 0.5) {
        t.style.transition = 'none';
        t.style.transform = 'translateX(' + dx + 'px)';
      }
    });
    arcNav.getBoundingClientRect();
    tabs.forEach(t => {
      if (t.style.transform) { t.style.transition = ''; t.style.transform = ''; }
    });
  }
  function canonicalSort() {
    Array.from(arcNav.querySelectorAll('.arc-tab'))
      .sort((a, b) => (+a.getAttribute('data-arc')) - (+b.getAttribute('data-arc')))
      .forEach(t => arcNav.appendChild(t));
  }
  function fallTome(tab) {
    if (!arcNav) return;
    arcNav.querySelectorAll('.arc-tab').forEach(t => {
      if (t !== tab) t.classList.add('lean-l');
    });
    tab.classList.remove('lean-l');
    tab.classList.add('fallen');
    fallenTab = tab;
  }
  /* R24: the silk is dispensed with. The book keeps its own red notch
     (pure CSS on the tab), and the chapter rail is sewn across the folio.
     The landing gate remains only to hold the folio veiled until the tome
     actually lies flat — one token, one watcher, no geometry anywhere. */
  let ribbonReleaseToken = 0;
  let ribbonReleaseHardTimer = null;
  function cancelRibbonRelease() {
    ribbonReleaseToken++;
    if (ribbonReleaseHardTimer) { clearTimeout(ribbonReleaseHardTimer); ribbonReleaseHardTimer = null; }
  }
  function whenTomeLanded(tab, cb) {
    const token = ribbonReleaseToken;
    let done = false;
    // "flat" is relative to THIS tome: lying down, its bounding box is no
    // taller than its own spine width (+2px slack). A fixed pixel threshold
    // fails both ways — arc 3 rests at 61px on desktop, and on mobile the
    // overshoot bounce can stay under a fixed bar.
    const flatEnough = () => tab.getBoundingClientRect().height <= tab.offsetWidth + 2;
    const finish = () => {
      if (done || token !== ribbonReleaseToken) return;
      done = true;
      tab.removeEventListener('transitionend', onEnd);
      if (ribbonReleaseHardTimer) { clearTimeout(ribbonReleaseHardTimer); ribbonReleaseHardTimer = null; }
      cb();
    };
    const onEnd = (e) => {
      // the fall is a transform transition; ignore the filter's event, and
      // trust only an end that leaves the tome lying flat
      if (e.target === tab && e.propertyName === 'transform' && flatEnough()) finish();
    };
    tab.addEventListener('transitionend', onEnd);
    // fallback 1: watch the box. The fall bezier OVERSHOOTS, so the box
    // swings THROUGH "flat" once mid-air; a single thin reading is not a
    // landing. Only SUSTAINED flatness (3 consecutive frames) releases.
    let flatStreak = 0;
    const poll = () => {
      if (done || token !== ribbonReleaseToken) return;
      if (flatEnough()) {
        if (++flatStreak >= 3) { finish(); return; }
      } else {
        flatStreak = 0;
      }
      requestAnimationFrame(poll);
    };
    requestAnimationFrame(poll);
    // fallback 2: never leave the silk knotted if both watchers miss
    ribbonReleaseHardTimer = setTimeout(finish, 1400);
  }
  function releaseFolioOnLanding(tab, panel) {
    whenTomeLanded(tab, () => {
      if (panel.classList.contains('active')) panel.classList.remove('dropping');
    });
  }
  function selectArc(arcNum, tab) {
    cancelRibbonRelease(); // a new opening supersedes any pending release
    const switching = fallenTab && fallenTab !== tab;
    arcNav.querySelectorAll('.arc-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    document.querySelectorAll('.arc-panel').forEach(p => p.classList.remove('active', 'dropping'));
    const panel = document.getElementById('arc-panel-' + arcNum);
    panel.classList.add('active', 'dropping');
    const veil = document.getElementById('chronicleVeil');
    if (veil) veil.classList.add('gone');
    // first opening of a volume: wake its first chapter
    if (!panel.querySelector('.chapter-tab.active')) {
      const firstTab = panel.querySelector('.chapter-tab');
      if (firstTab) firstTab.click();
    }
    localStorage.setItem('ethra-arc', arcNum);
    if (storySection) storySection.classList.add('reading');
    if (shelfReturn) shelfReturn.hidden = false;
    if (arcNav) arcNav.scrollIntoView({ behavior: 'smooth', block: 'start' });
    if (switching) {
      // replacement only: the old tome rises and slides home, the new one
      // slides to first place and tips left; the others never re-fall
      const old = fallenTab;
      fallenTab = tab;
      old.classList.remove('fallen');
      flipTabs(() => {
        canonicalSort();
        arcNav.prepend(tab);
      });
      setTimeout(() => {
        if (fallenTab === tab && !tab.classList.contains('fallen')) fallTome(tab);
      }, 350);
      setTimeout(() => {
        if (panel.classList.contains('active')) panel.classList.remove('dropping');
      }, 300);
    } else {
      // fresh fall: the tome takes first place and tips left at once.
      // Force a layout between the DOM move and the class so the fall
      // actually animates instead of snapping flat.
      arcNav.prepend(tab);
      void arcNav.offsetHeight;
      fallTome(tab);
      // the tome falls first; once flat, the folio rises
      releaseFolioOnLanding(tab, panel);
    }
  }
  function shelveAll() {
    if (!arcNav) return;
    cancelRibbonRelease(); // shelving supersedes any pending release
    fallenTab = null;
    flipTabs(() => {
      canonicalSort();
      arcNav.querySelectorAll('.arc-tab').forEach(t =>
        t.classList.remove('fallen', 'lean-l', 'lean-r', 'active'));
    });
    document.querySelectorAll('.chapter-subnav').forEach(r => { r.classList.remove('waiting', 'unfurl'); });
    if (shelfReturn) shelfReturn.hidden = true;
    if (storySection) storySection.classList.remove('reading');
    document.querySelectorAll('.arc-panel').forEach(p => p.classList.remove('active', 'dropping'));
    if (arcNav) arcNav.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  if (arcNav) {
    arcNav.querySelectorAll('.arc-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        if (tab.classList.contains('fallen')) { shelveAll(); return; }
        selectArc(tab.getAttribute('data-arc'), tab);
      });
    });
  }
  if (shelfReturn) shelfReturn.addEventListener('click', shelveAll);
  // give each ribbon number its chapter title for the hover reveal
  document.querySelectorAll('.chapter-tab').forEach(b => {
    if (!b.getAttribute('data-title')) b.setAttribute('data-title', b.textContent.trim());
  });

  // ── Chapter sub-tabs ──
  // Lazy chapter loading: each chapter div is rendered as empty by the server.
  // When the user clicks a chapter tab (or the first chapter of an arc is
  // auto-activated), we fetch /api/chapter/<id>, inject the HTML into the
  // div, mark it as loaded, and cache the response for instant re-click.
  const chapterCache = new Map();   // chapter_id -> html string
  const chapterInflight = new Map(); // chapter_id -> Promise<html>

  function fetchChapter(chapterId) {
    if (chapterCache.has(chapterId)) {
      return Promise.resolve(chapterCache.get(chapterId));
    }
    if (chapterInflight.has(chapterId)) {
      return chapterInflight.get(chapterId);
    }
    const p = fetch('/api/chapter/' + encodeURIComponent(chapterId), {
      credentials: 'same-origin',
      headers: { 'Accept': 'text/html' }
    }).then(r => {
      if (!r.ok) throw new Error('HTTP ' + r.status + ' loading ' + chapterId);
      return r.text();
    }).then(html => {
      chapterCache.set(chapterId, html);
      chapterInflight.delete(chapterId);
      return html;
    }).catch(err => {
      chapterInflight.delete(chapterId);
      throw err;
    });
    chapterInflight.set(chapterId, p);
    return p;
  }

  function renderChapterInto(chapterId, html) {
    const div = document.getElementById(chapterId);
    if (!div) return;
    const card = div.querySelector('.content-card');
    if (!card) return;
    // Preserve any chapter-illustration / image-placeholder AFTER the prose
    // by building a fresh prose container at the TOP of the card.
    let proseHost = card.querySelector('.chapter-prose');
    if (!proseHost) {
      proseHost = document.createElement('div');
      proseHost.className = 'chapter-prose';
      // Insert at the top so the illustration block remains below (or wherever
      // it currently sits). For consistency with current layout, prepend.
      card.insertBefore(proseHost, card.firstChild);
    }
    proseHost.innerHTML = html;
    // the "Loading…" scaffold has served its purpose — clear it so the
    // end-of-chapter illustration sits flush under the prose
    const scaffold = card.querySelector('.chapter-loading-placeholder');
    if (scaffold) scaffold.remove();
    div.setAttribute('data-loaded', 'true');
  }

  function activateChapter(chapterId) {
    const div = document.getElementById(chapterId);
    if (!div) return Promise.resolve();
    if (div.getAttribute('data-loaded') === 'true') return Promise.resolve();
    return fetchChapter(chapterId)
      .then(html => renderChapterInto(chapterId, html))
      .catch(err => {
        const card = div.querySelector('.content-card');
        if (card) {
          card.insertAdjacentHTML(
            'afterbegin',
            '<div class="chapter-load-error" style="padding:1rem;color:#a04040;">' +
              '<strong>Could not load chapter.</strong><br>' +
              (err && err.message ? err.message : 'Unknown error') +
              '</div>'
          );
        }
        console.error('Chapter load failed', chapterId, err);
      });
  }


  document.querySelectorAll('.chapter-subnav').forEach(subnav => {
    const parentPanel = subnav.parentElement;
    const chapterTabs = subnav.querySelectorAll('.chapter-tab');
    const chapterContents = parentPanel.querySelectorAll('.chapter-content');

    chapterTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.getAttribute('data-chapter');
        chapterTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        chapterContents.forEach(c => c.classList.remove('active'));
        document.getElementById(target).classList.add('active');
        try { localStorage.setItem('ethra-chapter', target); } catch(e) {}
        activateChapter(target);
      });
    });
  });

  // ── Prefetch first chapter of each arc after page load ──
  // Walks the rendered subnavs, grabs the first chapter of each arc, and
  // pre-loads it so cold-start behaves as if it were inlined (without the
  // 2 MB cost).
  document.querySelectorAll('.chapter-subnav').forEach(subnav => {
    const firstTab = subnav.querySelector('.chapter-tab');
    if (firstTab) {
      const firstId = firstTab.getAttribute('data-chapter');
      // schedule, don't block
      if ('requestIdleCallback' in window) {
        requestIdleCallback(() => activateChapter(firstId), { timeout: 1500 });
      } else {
        setTimeout(() => activateChapter(firstId), 50);
      }
    }
  });

  // Round-7 direction: the reading pane stays veiled until a volume is
  // chosen by hand — no auto-restore of the last arc/chapter on load.
  // (Deep links still click their arc/chapter tabs explicitly.)

  // ── Section switching (from hamburger menu) ──
  window.__firstSwitch = true;
  window.switchSection = function(sectionId) {
    const target = document.getElementById('section-' + sectionId);
    const current = document.querySelector('.section.active');
    const first = window.__firstSwitch; window.__firstSwitch = false;
    if (target && current && target !== current && !window.__secAnimating && !first) {
      // orrery-style zoom between categories
      window.__secAnimating = true;
      current.classList.add('sec-zoom-out');
      setTimeout(function () {
        current.classList.remove('active', 'sec-zoom-out');
        target.classList.add('active', 'sec-zoom-in');
        setTimeout(function () { target.classList.remove('sec-zoom-in'); window.__secAnimating = false; }, 560);
      }, 320);
    } else {
      document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
      if (target) target.classList.add('active');
    }
    // Toggle bestiary parchment mode
    const container = document.querySelector('.container');
    if (container) {
      if (sectionId === 'bestiary') {
        container.classList.add('bestiary-mode');
      } else {
        container.classList.remove('bestiary-mode');
      }
    }
    // Close menu
    const hb = document.getElementById('hamburgerBtn');
    const bm = document.getElementById('biomeMenu');
    if (hb) hb.classList.remove('active');
    if (bm) bm.classList.remove('active');
    try { localStorage.setItem('ethra-section', sectionId); } catch(e) {}
  };
  
  // ── Collapsible menu sections ──
  window.toggleSection = function(submenuId) {
    const sub = document.getElementById(submenuId);
    const arrow = document.getElementById('arrow-' + submenuId);
    if (sub) sub.classList.toggle('open');
    if (arrow) arrow.classList.toggle('open');
  };
  
  // ── Load biome creatures ──
  window.loadBiome = async function(biome) {
    switchSection('bestiary');
    const resp = await fetch(`/ethra/api/creatures/${biome}`);
    const creatures = await resp.json();
    const cc = document.querySelector('#section-bestiary .content-card');
    let html = '<div class="biome-header"><h2>Biomes of Ethra</h2><button class="back-button" onclick="loadBestiaryBook()">← Back</button></div>';
    html += '<div class="biome-title">' + formatBiomeName(biome) + '</div><div class="creature-grid">';
    creatures.forEach(c => {
      html += '<button class="creature-card" onclick="loadCreature(\'' + biome + '\',\'' + c + '\')"><div class="creature-name">' + formatCreatureName(c) + '</div></button>';
    });
    html += '</div>';
    cc.innerHTML = html;
  };
  
  // ── Load individual creature ──
  window.loadCreature = async function(biome, creature) {
    const resp = await fetch(`/ethra/api/creature/${biome}/${creature}`);
    const data = await resp.json();
    const cc = document.querySelector('#section-bestiary .content-card');
    cc.innerHTML = '<div class="biome-header"><h2>Biomes of Ethra</h2><button class="back-button" onclick="loadBiome(\'' + biome + '\')">← Back</button></div><div class="creature-detail"><div class="creature-name-title">' + formatCreatureName(creature) + '</div><div class="biome-badge">' + formatBiomeName(biome) + '</div><div class="creature-content">' + data.content + '</div></div>';
  };

  // ── Show landing page — THE GREAT ORRERY (three-stage zoom) ──
  window.showLandingPage = function() {
    const cc = document.querySelector('#section-world .content-card');
    cc.className = 'content-card landing-page orrery-card';
    cc.innerHTML =
      '<div class="orrery" id="orrery">' +
        '<div class="orrery-stage" id="orrery-stage-1">' +
          '<div class="orrery-space">' +
            '<div class="orrery-stars"></div>' +
            '<div class="orrery-center"><div class="binary-spin"><span class="sun sun-steadfast"></span><span class="sun sun-flicker"></span></div></div>' +
            '<div class="orbit orbit-ethra">' +
              '<button class="world-dot" id="orrery-ethra" aria-label="Ethra"><span class="world-sphere"></span><span class="world-label">ETHRA</span></button>' +
            '</div>' +
          '</div>' +
          '<p class="orrery-hint">Touch the world.</p>' +
        '</div>' +
        '<div class="orrery-stage" id="orrery-stage-2" hidden>' +
          '<div class="world-view">' +
            '<div class="world-diagram">' +
              '<div class="world-big" id="orrery-world" role="button" tabindex="0" aria-label="Descend to the map of Ethra" title="Descend to Ethra">' +
                  '<svg class="wb-svg" viewBox="0 0 150 150" aria-hidden="true">' +
                    '<defs>' +
                      '<clipPath id="wb-clip"><circle cx="75" cy="75" r="74"/></clipPath>' +
                      '<clipPath id="wb-landclip"><path d="M26 66 C28 50 44 38 62 34 C74 31 88 30 100 36 C110 41 122 48 126 58 C129 66 122 72 116 76 C112 79 114 86 108 90 C102 94 96 92 92 98 C88 104 90 110 80 112 C70 114 64 106 56 102 C48 98 40 98 34 90 C28 83 24 76 26 66 Z"/></clipPath>' +
                      '<radialGradient id="wb-ocean" cx="38%" cy="34%" r="80%">' +
                        '<stop offset="0%" stop-color="#3f96a8"/><stop offset="45%" stop-color="#2a7a8a"/><stop offset="100%" stop-color="#0e2f4c"/>' +
                      '</radialGradient>' +
                      '<linearGradient id="wb-land" x1="0" y1="0" x2="0" y2="1">' +
                        '<stop offset="0%" stop-color="#93b066"/><stop offset="55%" stop-color="#7a9a5a"/><stop offset="100%" stop-color="#b28c4e"/>' +
                      '</linearGradient>' +
                      '<radialGradient id="wb-shade" cx="32%" cy="30%" r="90%">' +
                        '<stop offset="0%" stop-color="rgba(255,244,214,.30)"/><stop offset="30%" stop-color="rgba(255,244,214,0)"/>' +
                        '<stop offset="70%" stop-color="rgba(4,10,20,0)"/><stop offset="100%" stop-color="rgba(4,10,20,.62)"/>' +
                      '</radialGradient>' +
                      '<filter id="wb-soft"><feGaussianBlur stdDeviation="1.4"/></filter>' +
                    '</defs>' +
                    '<circle cx="75" cy="75" r="74" fill="url(#wb-ocean)"/>' +
                    '<g clip-path="url(#wb-clip)">' +
                      '<g class="wb-surf">' +
                        '<g id="wb-cont">' +
                          '<path d="M26 66 C28 50 44 38 62 34 C74 31 88 30 100 36 C110 41 122 48 126 58 C129 66 122 72 116 76 C112 79 114 86 108 90 C102 94 96 92 92 98 C88 104 90 110 80 112 C70 114 64 106 56 102 C48 98 40 98 34 90 C28 83 24 76 26 66 Z" fill="none" stroke="rgba(127,208,218,.20)" stroke-width="6"/>' +
                          '<path d="M26 66 C28 50 44 38 62 34 C74 31 88 30 100 36 C110 41 122 48 126 58 C129 66 122 72 116 76 C112 79 114 86 108 90 C102 94 96 92 92 98 C88 104 90 110 80 112 C70 114 64 106 56 102 C48 98 40 98 34 90 C28 83 24 76 26 66 Z" fill="url(#wb-land)" stroke="rgba(232,217,174,.28)" stroke-width=".8"/>' +
                          '<g clip-path="url(#wb-landclip)">' +
                            '<ellipse cx="72" cy="32" rx="34" ry="9" fill="#eef4f2" opacity=".85"/>' +
                            '<ellipse cx="70" cy="101" rx="38" ry="14" fill="#c9a059" opacity=".8"/>' +
                            '<ellipse cx="50" cy="68" rx="12" ry="7" fill="#5f8346" opacity=".55"/>' +
                            '<ellipse cx="96" cy="58" rx="10" ry="6" fill="#5f8346" opacity=".45"/>' +
                          '</g>' +
                          '<path d="M38 62 C46 55 58 54 64 59 C58 64 46 67 40 66 Z" fill="#2a7a8a" opacity=".9"/>' +
                          '<circle cx="128" cy="82" r="4" fill="url(#wb-land)"/>' +
                          '<circle cx="134" cy="93" r="2.6" fill="url(#wb-land)"/>' +
                          '<circle cx="18" cy="100" r="3.4" fill="url(#wb-land)"/>' +
                          '<circle cx="14" cy="40" r="2.6" fill="#eef4f2" opacity=".7"/>' +
                        '</g>' +
                        '<use href="#wb-cont" x="150"/>' +
                      '</g>' +
                      '<g class="wb-clouds" fill="#ffffff" opacity=".5" filter="url(#wb-soft)">' +
                        '<g id="wb-cl">' +
                          '<ellipse cx="34" cy="52" rx="18" ry="4.5"/>' +
                          '<ellipse cx="76" cy="66" rx="26" ry="5.5"/>' +
                          '<ellipse cx="116" cy="48" rx="15" ry="4"/>' +
                          '<ellipse cx="98" cy="100" rx="20" ry="4.5"/>' +
                          '<ellipse cx="46" cy="118" rx="14" ry="3.5"/>' +
                          '<ellipse cx="12" cy="80" rx="10" ry="3"/>' +
                        '</g>' +
                        '<use href="#wb-cl" x="150"/>' +
                      '</g>' +
                    '</g>' +
                    '<circle cx="75" cy="75" r="74" fill="url(#wb-shade)"/>' +
                    '<circle cx="75" cy="75" r="73.2" fill="none" stroke="rgba(160,220,235,.35)" stroke-width="1.4"/>' +
                  '</svg>' +
              '</div>' +
              '<div class="orbit orbit-sun-a"><span class="sun sun-steadfast"></span></div>' +
              '<div class="orbit orbit-sun-b"><span class="sun sun-flicker"></span></div>' +
              '<div class="world-names"><span class="wn-gold">STEADFAST</span><span class="wn-red">FLICKER</span></div>' +
            '</div>' +
            '<aside class="world-lore" id="orrery-lore"><p><em>Reading the twin fires…</em></p></aside>' +
          '</div>' +
          '<p class="orrery-hint">Touch the world again to descend. &nbsp; <button class="orrery-back" id="orrery-back-1">← The Orrery</button></p>' +
        '</div>' +
      '</div>';
    const s1 = document.getElementById('orrery-stage-1');
    const s2 = document.getElementById('orrery-stage-2');
    function zoomTo(hideEl, showEl) {
      hideEl.classList.add('zoom-out');
      showEl.hidden = false;
      requestAnimationFrame(function(){ showEl.classList.add('zoom-in'); });
      setTimeout(function(){ hideEl.hidden = true; hideEl.classList.remove('zoom-out'); }, 650);
      setTimeout(function(){ showEl.classList.remove('zoom-in'); }, 700);
    }
    document.getElementById('orrery-ethra').addEventListener('click', function() {
      zoomTo(s1, s2);
      fetch('/ethra/api/world/cosmology').then(function(r){ return r.json(); }).then(function(d) {
        const el = document.getElementById('orrery-lore');
        if (el && d && d.content) el.innerHTML = '<h3>' + (d.title || 'Cosmology: The Twin Fires') + '</h3>' + d.content;
      }).catch(function(){});
    });
    document.getElementById('orrery-back-1').addEventListener('click', function(e) {
      e.stopPropagation();
      zoomTo(s2, s1);
    });
    function descendToMap(){ document.body.classList.add('descend'); setTimeout(function(){ var a = document.querySelector('#site-nav a[href*="/map/"]'); location.href = a ? a.getAttribute('href') : '/map/'; }, 620); }
    const wb = document.getElementById('orrery-world');
    wb.addEventListener('click', descendToMap);
    wb.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' ') descendToMap(); });
  };
  // Initial landing render — the Great Orrery
  showLandingPage();

  // ── Load world sub-section ──
  window.loadWorldSection = async function(section) {
    // Switch from whichever section is active (story, bestiary, etc.)
    // to the world section FIRST — without this, the user is visually
    // stuck on Tales of Ethra even though a world-section card has been
    // populated inside the (still empty, still hidden) #section-world.
    const cc0 = document.querySelector('#section-world .content-card');
    if (cc0 && cc0.querySelector('.orrery')) cc0.innerHTML = '';
    if (typeof window.switchSection === 'function') {
      window.switchSection('world');
    }
    const resp = await fetch(`/ethra/api/world/${section}`);
    const data = await resp.json();
    const cc = document.querySelector('#section-world .content-card');
    // Remove all theme classes
    cc.className = 'content-card';
    // Add the section's theme class
    cc.classList.add(section + '-theme');
    // Build content with back button
    const _tabs = [['cosmology','Cosmology'],['magic','Magic'],['geography','Geography'],['religion','Religion'],['history','History'],['culture','Culture']];
    cc.innerHTML = '<div class="world-header"><h2>The World of Ethra</h2><div class="world-tabs">' + _tabs.map(t => '<button class="world-tab' + (t[0]===section?' active':'') + '" onclick="loadWorldSection(\'' + t[0] + '\')">' + t[1] + '</button>').join('') + '</div></div><div class="world-content">' + data.content + '</div>';
  };

  // ── Deep links: /?world=cosmology opens that World of Ethra section on load.
  //    Used by the interactive map (the twin-suns banner links here). ──
  try {
    const _qs = new URLSearchParams(window.location.search);
    const _w = _qs.get('world');
    if (_w) {
      window.addEventListener('load', function () {
        setTimeout(function () { if (window.loadWorldSection) window.loadWorldSection(_w); }, 80);
      });
    }
    const _s = _qs.get('section');
    if (_s && ['story', 'bestiary', 'world'].indexOf(_s) >= 0) {
      window.addEventListener('load', function () {
        setTimeout(function () {
          if (_s === 'bestiary') { if (window.loadBestiaryBook) window.loadBestiaryBook(); }
          else if (window.switchSection) window.switchSection(_s);
        }, 80);
      });
    }
    const _b = _qs.get('biome');
    if (_b) {
      window.addEventListener('load', function () {
        setTimeout(function () { if (window.loadBestiaryBook) window.loadBestiaryBook(_b); }, 80);
      });
    }
  } catch (e) { /* deep link is best-effort */ }

  // ── Site bar: orrery-style zoom between categories (in-page when possible) ──
  document.querySelectorAll('#site-nav a').forEach(a => {
    a.addEventListener('click', (e) => {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault();
      const u = a.getAttribute('href');
      const q = u.indexOf('?');
      const qs = q >= 0 ? new URLSearchParams(u.slice(q + 1)) : null;
      const sec = qs && qs.get('section');
      const wor = qs && qs.get('world');
      if (u === '/') {
        if (window.showLandingPage) { window.switchSection('world'); window.showLandingPage(); try { history.pushState(null, '', '/'); } catch (err) {} }
        return;
      }
      if (sec === 'story') { window.switchSection('story'); try { history.pushState(null, '', u); } catch (err) {} return; }
      if (sec === 'bestiary') { if (window.loadBestiaryBook) window.loadBestiaryBook(); try { history.pushState(null, '', u); } catch (err) {} return; }
      if (wor && window.loadWorldSection) { window.loadWorldSection(wor); try { history.pushState(null, '', u); } catch (err) {} return; }
      // /map/ and anything else: true navigation with the fade
      document.body.classList.add('leaving');
      setTimeout(() => { location.href = u; }, 280);
    });
  });

  // ── Hamburger Menu (retired 2026-08-21 — the site bar is the single nav system) ──
  const hamburgerBtn = document.getElementById('hamburgerBtn');
  const biomeMenu = document.getElementById('biomeMenu');
  
  if (hamburgerBtn && biomeMenu) {
    hamburgerBtn.addEventListener('click', () => {
      hamburgerBtn.classList.toggle('active');
      biomeMenu.classList.toggle('active');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!hamburgerBtn.contains(e.target) && !biomeMenu.contains(e.target)) {
        hamburgerBtn.classList.remove('active');
        biomeMenu.classList.remove('active');
      }
    });
  }
  
  // ── Wrap creature portraits for hover banner ──
  function wrapCreaturePortraits() {
    document.querySelectorAll('.creature-portrait').forEach(img => {
      // Skip if already wrapped
      const parent = img.parentElement;
      if (parent && parent.classList.contains('portrait-wrapper')) return;
      // If parent is already an inline wrapper (creature-inline-img), upgrade it instead
      if (parent && parent.classList.contains('creature-inline-img')) {
        parent.classList.add('portrait-wrapper');
        // Add label if not already present
        if (!parent.querySelector('.portrait-label')) {
          const label = document.createElement('span');
          label.className = 'portrait-label';
          label.textContent = img.getAttribute('alt') || 'Creature';
          parent.appendChild(label);
        }
        return;
      }
      
      const wrapper = document.createElement('span');
      wrapper.className = 'portrait-wrapper';
      
      // Transfer inline styles from img to wrapper (float, margin, max-width, etc.)
      const inlineStyle = img.getAttribute('style') || '';
      const maxWidthMatch = inlineStyle.match(/max-width:\s*(\d+px)/);
      const maxWidth = maxWidthMatch ? maxWidthMatch[0] : 'max-width: 350px';
      // Only transfer display, float, margin to wrapper
      const wrapperStyle = inlineStyle
        .replace(/max-width:\s*\d+px;?\s*/gi, '')
        .replace(/border:\s*[^;]+;?\s*/gi, '');
      wrapper.setAttribute('style', wrapperStyle);
      // Keep max-width on image, fill wrapper
      img.setAttribute('style', maxWidth + '; width: 100%; height: auto; display: block;');
      
      // Create label banner
      const label = document.createElement('span');
      label.className = 'portrait-label';
      label.textContent = img.getAttribute('alt') || 'Creature';
      
      img.parentNode.insertBefore(wrapper, img);
      wrapper.appendChild(img);
      wrapper.appendChild(label);
    });
  }
  
  // Run on initial load
  wrapCreaturePortraits();

  // ── Patch loadBiome and loadCreature to re-wrap after content updates ──
  const origLoadBiome = window.loadBiome;
  window.loadBiome = async function(biome) {
    await origLoadBiome(biome);
    wrapCreaturePortraits();
  };
  const origLoadCreature = window.loadCreature;
  window.loadCreature = async function(biome, creature) {
    await origLoadCreature(biome, creature);
    wrapCreaturePortraits();
  };
})();

// ── Format helpers (global for onclick=) ──
function formatBiomeName(biome) {
  return biome.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}
function formatCreatureName(creature) {
  return creature.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}

// ════════════════ CREATURE PORTRAIT MODAL ════════════════
// Bestiary gallery loads thumbnails (~7 KB ea); click opens full-size image
// in a fixed overlay. Stored full-size paths come from server.py's
// _swap_bestiary_to_thumbnails() in data-* attributes.
(function() {
  // CSS injected only when needed (bestiary section visible)
  const CSS_ID = 'creature-modal-styles';
  function ensureModalCss() {
    if (document.getElementById(CSS_ID)) return;
    const style = document.createElement('style');
    style.id = CSS_ID;
    style.textContent = `
      #creature-modal {
        display: none;
        position: fixed; inset: 0;
        background: rgba(10, 22, 40, 0.92);
        z-index: 9999;
        align-items: center; justify-content: center;
        padding: 20px;
        cursor: zoom-out;
      }
      #creature-modal.open { display: flex; }
      #creature-modal img {
        max-width: 92vw; max-height: 92vh;
        box-shadow: 0 0 0 4px #b89a70, 0 0 0 9px #6b3a1a, 0 16px 48px rgba(0,0,0,0.6);
        border-radius: 4px;
        cursor: default;
      }
      #creature-modal-close {
        position: fixed; top: 18px; right: 22px;
        color: #f4e8d0; font-size: 32px; line-height: 1;
        background: rgba(107, 58, 26, 0.85);
        border: 2px solid #b89a70; border-radius: 50%;
        width: 44px; height: 44px;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer; font-weight: 700;
        user-select: none;
        z-index: 10000;
      }
      #creature-modal-close:hover { background: #8b4a2a; }
      #creature-modal-cap {
        position: fixed; bottom: 20px; left: 50%;
        transform: translateX(-50%);
        color: #d4c8a8; font-family: Georgia, serif;
        background: rgba(10, 22, 40, 0.78);
        padding: 8px 16px; border-radius: 4px;
        border: 1px solid #6b3a1a;
        max-width: 90vw; text-align: center;
      }
      .creature-zoomable { cursor: zoom-in; }
      .creature-zoomable img { cursor: zoom-in; }
    `;
    document.head.appendChild(style);
  }

  function buildModal() {
    if (document.getElementById('creature-modal')) return;
    ensureModalCss();
    const overlay = document.createElement('div');
    overlay.id = 'creature-modal';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.innerHTML = `
      <button id="creature-modal-close" aria-label="Close">&times;</button>
      <img id="creature-modal-img" alt="" />
      <div id="creature-modal-cap"></div>
    `;
    document.body.appendChild(overlay);
    overlay.addEventListener('click', closeModal);
    document.getElementById('creature-modal-close').addEventListener('click', function(e) {
      e.stopPropagation(); closeModal();
    });
    document.getElementById('creature-modal-img').addEventListener('click', function(e) {
      e.stopPropagation();
    });
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeModal();
    });
  }

  function openModal(pic, imgEl) {
    buildModal();
    const webp = pic.dataset.fullWebp || '';
    const jpg = pic.dataset.fullJpg || '';
    const modalImg = document.getElementById('creature-modal-img');
    const cap = document.getElementById('creature-modal-cap');
    modalImg.src = webp || jpg;
    // Hide modal briefly if browser doesn't support webp
    modalImg.onerror = function() {
      if (this.src === webp && jpg) this.src = jpg;
    };
    cap.textContent = imgEl.alt || '';
    document.getElementById('creature-modal').classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    const overlay = document.getElementById('creature-modal');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  // Event delegation — catches clicks on any creature-zoomable in the document.
  document.addEventListener('click', function(e) {
    const pic = e.target.closest('picture.creature-zoomable');
    if (!pic) return;
    const img = pic.querySelector('img');
    if (!img) return;
    e.preventDefault();
    openModal(pic, img);
  });
})();
