
  // ═════ LOAD BESTIARY MAP ═════
  window.loadBestiaryMap = async function() {
    switchSection('bestiary');
    const cc = document.querySelector('#section-bestiary .content-card');
    if (!cc) return;
    cc.innerHTML = '<div class="map-container"><img class="map-image" src="/ethra/static/images/map-supercontinent-v2.png" alt="Ethra Supercontinent Map" /><div class="dot-overlay" id="dot-overlay"></div></div>';
    const overlay = document.getElementById('dot-overlay');
    if (!overlay) return;
    
    try {
      const resp = await fetch('/ethra/api/map/coordinates');
      const data = await resp.json();
      
      // Render creature dots
      (data.creatures || []).forEach(c => {
        const dot = document.createElement('button');
        dot.className = 'creature-dot';
        dot.style.left = c.x_pct + '%';
        dot.style.top = c.y_pct + '%';
        dot.setAttribute('aria-label', c.name + ' in ' + (data.biomes.find(b=>b.slug===c.biome)?.name || c.biome));
        dot.dataset.creature = JSON.stringify(c);
        
        // Tooltip
        const tip = document.createElement('div');
        tip.className = 'dot-tooltip';
        tip.innerHTML = '<span class="creature-name">'+c.name+'</span><span class="creature-biome">'+(data.biomes.find(b=>b.slug===c.biome)?.name || c.biome)+'</span>';
        tip.style.left = (c.x_pct + 2) + '%';
        tip.style.top = (c.y_pct - 5) + '%';
        document.body.appendChild(tip);
        
        dot.addEventListener('mouseenter', () => {
          tip.classList.add('visible');
          if(c.image_full) {
            const thumb = document.createElement('img');
            thumb.className = 'creature-thumb';
            thumb.src = c.image_full;
            tip.appendChild(thumb);
          }
        });
        dot.addEventListener('mouseleave', () => {
          tip.classList.remove('visible');
          const thumb = tip.querySelector('.creature-thumb');
          if(thumb) thumb.remove();
        });
        dot.addEventListener('focus', () => tip.classList.add('visible'));
        dot.addEventListener('blur', () => tip.classList.remove('visible'));
        
        // Click → open full-page modal
        dot.addEventListener('click', () => {
          if(c.kind === 'race' || c.kind === 'creature') {
            openCreaturePage(c.biome, c.slug);
          }
        });
        
        overlay.appendChild(dot);
      });
      
      // Underground cave special case
      if(data.underground_cave) {
        const uc = data.underground_cave;
        const dot = document.createElement('button');
        dot.className = 'creature-dot underground-dot';
        dot.style.left = uc.x_pct + '%';
        dot.style.top = uc.y_pct + '%';
        dot.setAttribute('aria-label', uc.name);
        dot.dataset.cave = JSON.stringify(uc);
        
        const tip = document.createElement('div');
        tip.className = 'dot-tooltip';
        tip.innerHTML = '<span class="creature-name">'+uc.name+'</span><span class="creature-biome">'+uc.subtitle+'</span>';
        tip.style.left = (uc.x_pct + 2) + '%';
        tip.style.top = (uc.y_pct - 5) + '%';
        document.body.appendChild(tip);
        
        dot.addEventListener('mouseenter', () => tip.classList.add('visible'));
        dot.addEventListener('mouseleave', () => tip.classList.remove('visible'));
        dot.addEventListener('focus', () => tip.classList.add('visible'));
        dot.addEventListener('blur', () => tip.classList.remove('visible'));
        dot.addEventListener('click', () => openUndergroundCave(uc));
        
        overlay.appendChild(dot);
      }
      
      // City pins — P1 drop-in: each content/places/<slug>.md with
      // x_pct/y_pct frontmatter arrives in data.city_pins. Gold diamonds;
      // click opens the gazetteer entry. One file per city, zero code edits.
      (data.city_pins || []).forEach(p => {
        if (!p || p.x_pct === undefined || p.y_pct === undefined) return;
        const dot = document.createElement('button');
        dot.className = 'city-dot';
        dot.style.left = p.x_pct + '%';
        dot.style.top = p.y_pct + '%';
        dot.setAttribute('aria-label', p.name + ' — ' + (p.kind || 'place'));
        
        const tip = document.createElement('div');
        tip.className = 'dot-tooltip';
        tip.innerHTML = '<span class="creature-name">' + p.name + '</span><span class="creature-biome">' + (p.kind || 'place') + '</span>';
        tip.style.left = (p.x_pct + 2) + '%';
        tip.style.top = (p.y_pct - 5) + '%';
        document.body.appendChild(tip);
        
        dot.addEventListener('mouseenter', () => tip.classList.add('visible'));
        dot.addEventListener('mouseleave', () => tip.classList.remove('visible'));
        dot.addEventListener('focus', () => tip.classList.add('visible'));
        dot.addEventListener('blur', () => tip.classList.remove('visible'));
        dot.addEventListener('click', () => openPlaceGazetteer(p.id));
        
        overlay.appendChild(dot);
      });
      
    } catch(e) {
      cc.innerHTML = '<p style="color:#8a7a55;text-align:center;padding:2rem;"><em>Failed to load map coordinates.</em></p>';
      console.error(e);
    }
  };
  
  // ═════ PLACE GAZETTEER (P1 drop-in — content/places/<slug>.md) ═════
  window.openPlaceGazetteer = async function(slug) {
    let gz = document.getElementById('place-gazetteer');
    if (!gz) {
      gz = document.createElement('div');
      gz.id = 'place-gazetteer';
      gz.setAttribute('role', 'dialog');
      gz.setAttribute('aria-modal', 'true');
      gz.innerHTML = '<div id="place-gazetteer-card"><button id="place-gazetteer-close" aria-label="Close">&times;</button><div id="place-gazetteer-body"></div></div>';
      document.body.appendChild(gz);
      gz.addEventListener('click', function(e) { if (e.target === gz) closePlaceGazetteer(); });
      document.getElementById('place-gazetteer-close').addEventListener('click', closePlaceGazetteer);
      document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closePlaceGazetteer(); });
    }
    const body = document.getElementById('place-gazetteer-body');
    body.innerHTML = '<p style="color:#8a7a55;font-style:italic">Consulting the gazetteer…</p>';
    gz.classList.add('open');
    document.body.style.overflow = 'hidden';
    try {
      const r = await fetch('/ethra/api/place/' + encodeURIComponent(slug));
      if (!r.ok) throw new Error('HTTP ' + r.status);
      const p = await r.json();
      body.innerHTML =
        '<h2 style="color:#d4af37;margin:0 0 2px">' + (p.name || slug) + '</h2>' +
        '<div style="color:#8a7a55;font-size:12px;margin-bottom:14px;letter-spacing:1px">' + (p.region || '') + '</div>' +
        (p.image ? '<img src="' + p.image + '" alt="" style="width:100%;max-height:280px;object-fit:cover;border:1px solid #4a3e2c;border-radius:4px;margin-bottom:14px">' : '') +
        '<div>' + (p.content || '') + '</div>';
    } catch (e) {
      body.innerHTML = '<p style="color:#8a7a55"><em>The gazetteer holds no entry for this place.</em></p>';
    }
  };
  window.closePlaceGazetteer = function() {
    const gz = document.getElementById('place-gazetteer');
    if (gz) gz.classList.remove('open');
    document.body.style.overflow = '';
  };
  
  // ═════ LOAD BESTIARY BOOK (closed leather tome → opens; ink melts & reforms) ═════
  window.loadBestiaryBook = async function(focusBiome, focusSlug) {
    switchSection('bestiary');
    const cc = document.querySelector('#section-bestiary .content-card');
    if (!cc) return;
    const NAMES = {'rune-belt':'The Rune Belt','steadfast-desert':'The Steadfast Desert','umbral-ring':'The Umbral Ring','flickermarch':'The Flickermarch','tidepools':'The Tidepool Shallows','underground':'The Deep Below'};
    const ORDER = ['rune-belt','steadfast-desert','umbral-ring','flickermarch','tidepools','underground'];
    function fmt(s){return s.replace(/-/g,' ').replace(/\b\w/g,function(l){return l.toUpperCase();});}
    function frontis(){return '<h2 class="book-title" style="margin-top:2.2rem">The Bestiary of Ethra</h2><p class="book-sub">being a true account of the beasts, races &amp; wonders of the supercontinent</p><p style="text-align:center;color:#7a5f3a;font-style:italic;margin-top:2rem">Choose an entry from the index.</p>';}
    // the tome lies closed until touched
    cc.innerHTML = '<div class="book-wrap" id="book-wrap"><div class="book-closed" id="book-closed" role="button" tabindex="0" aria-label="Open the Bestiary"><div class="bc-emblem">✦</div><div class="bc-title">The Bestiary of Ethra</div><div class="bc-sub">being a true account of the beasts, races &amp; wonders of the supercontinent</div><div class="bc-clasp"></div><div class="bc-hint">touch the tome to open it</div></div></div>';
    let DATA = null;
    try { const r = await fetch('/ethra/api/biomes'); DATA = await r.json(); } catch (e) { DATA = null; }
    const closed = document.getElementById('book-closed');
    let opened = false;
    // margin flourishes: corner vine-work, as in the old bestiaries
    function fl(cls){return '<svg class="pg-fl ' + cls + '" viewBox="0 0 70 70" aria-hidden="true"><g fill="none" stroke="#8a2a1a" stroke-width="1.5"><path d="M6 66 C10 38 28 18 64 8"/><path d="M16 44 c-7 -2 -11 3 -11 9 c7 2 11 -3 11 -9"/><path d="M30 28 c-2 -7 3 -11 9 -11 c2 7 -3 11 -9 11"/><path d="M47 15 c-4 -5 -1 -10 4 -12 c4 5 1 10 -4 12"/></g><circle cx="64" cy="8" r="2.2" fill="#8a2a1a"/></svg>';}
    const FLOUR = fl('tl') + fl('tr') + fl('bl') + fl('br');
    function openBook(){
      if (opened) return; opened = true;
      const wrap = document.getElementById('book-wrap');
      wrap.classList.add('book-opening');
      const book = document.createElement('div');
      book.className = 'book';
      book.innerHTML = '<div class="book-page book-left"><h2 class="book-title">Index</h2><ul class="book-index" id="book-index"><li style="color:#7a5f3a;text-align:center"><em>Opening the book…</em></li></ul><span class="book-folio">i</span>' + FLOUR + '</div>' +
        '<div class="book-spine"></div>' +
        '<div class="book-page book-right"><button class="book-back">← Index</button><div id="book-dossier" class="book-dossier">' + frontis() + '</div><span class="book-folio">ii</span>' + FLOUR + '</div>';
      wrap.appendChild(book);
      book.querySelector('.book-back').addEventListener('click', bookBackToIndex);
      setTimeout(function(){ const c = document.getElementById('book-closed'); if (c) c.remove(); wrap.classList.remove('book-opening'); }, 1750);
      buildIndex();
    }
    if (closed) {
      closed.addEventListener('click', openBook);
      closed.addEventListener('keydown', function(e){ if (e.key === 'Enter' || e.key === ' ') openBook(); });
    }
    // wet-ink melt: turbulence displacement swallows the old text, then releases the new
    function inkSwap(el, html){
      const f = document.getElementById('ink-melt');
      const turb = f && f.querySelector('feTurbulence');
      const disp = f && f.querySelector('feDisplacementMap');
      if (!turb || !disp) { el.innerHTML = html; return; }
      el.style.filter = 'url(#ink-melt)';
      const t0 = performance.now();
      (function melt(now){
        const p = Math.min(1, (now - t0) / 430);
        disp.setAttribute('scale', (p * 95).toFixed(1));
        turb.setAttribute('baseFrequency', (0.012 + p * 0.05).toFixed(4));
        el.style.opacity = String(1 - p * 0.9);
        if (p < 1) { requestAnimationFrame(melt); } else {
          el.innerHTML = html;
          const t1 = performance.now();
          (function reform(now2){
            const q = Math.min(1, (now2 - t1) / 600);
            const e2 = 1 - Math.pow(1 - q, 3);
            disp.setAttribute('scale', (95 * (1 - e2)).toFixed(1));
            turb.setAttribute('baseFrequency', (0.062 - e2 * 0.05).toFixed(4));
            el.style.opacity = String(0.1 + 0.9 * e2);
            if (q < 1) { requestAnimationFrame(reform); } else { el.style.filter = ''; el.style.opacity = ''; }
          })(t1);
        }
      })(t0);
    }
    function setPage(html){ inkSwap(document.getElementById('book-dossier'), html); }
    function chapterPage(slug, idx, n){
      return '<h2 class="book-entry-title">' + (NAMES[slug]||fmt(slug)) + '</h2><p class="book-sub">chapter ' + idx + ' · ' + n + ' entries recorded</p><p style="text-align:center;color:#7a5f3a;font-style:italic;margin-top:1.6rem">Choose a creature from the index.</p>';
    }
    function bookShowEntry(){ var b = document.querySelector('.book'); if (b) b.classList.add('book-show-entry'); }
    function bookBackToIndex(){ var b = document.querySelector('.book'); if (b) { b.classList.remove('book-show-entry'); if (window.matchMedia('(max-width:900px)').matches) b.scrollIntoView({behavior:'smooth', block:'start'}); } }
    function bookDossierView(){ if (window.matchMedia('(max-width:900px)').matches) { var b = document.querySelector('.book'); if (b) b.scrollIntoView({behavior:'smooth', block:'start'}); } }
    function openCreature(slug, biome, name){
      fetch('/ethra/api/creature/' + biome + '/' + slug).then(function(r){return r.json();}).then(function(d){
        const body = (d.content||'').replace(/^\s*<h[12][^>]*>[\s\S]*?<\/h[12]>/, '');
        setPage('<h2 class="book-entry-title">' + name + '</h2><div class="biome-badge">' + fmt(biome) + '</div><div class="creature-content">' + body + '</div>');
        bookShowEntry();
        setTimeout(bookDossierView, 450);
      }).catch(function(){ setPage('<h2 class="book-entry-title">' + name + '</h2><p><em>The ink for this entry is still being ground.</em></p>'); });
    }
    function buildIndex(){
      const data = DATA || {};
      const slugs = ORDER.filter(function(s){return data[s];}).concat(Object.keys(data).filter(function(s){return ORDER.indexOf(s)<0;}));
      const idx = document.getElementById('book-index');
      if (!slugs.length) { idx.innerHTML = '<li style="color:#7a5f3a;text-align:center"><em>The book would not open.</em></li>'; return; }
      idx.innerHTML = '';
      // beings that live in both layers are recorded in the deep chapter too
      const CROSS = {'underground': [{'slug':'mycelial-deep','home':'flickermarch','name':'The Mycelial Deep'},{'slug':'kyre-tree','home':'steadfast-desert','name':'The Kyre Tree'},{'slug':'abyssal-heart','home':'tidepools','name':'Abyssal Heart'}]};
      slugs.forEach(function(slug, i) {
        const list = (data[slug] || []).slice();
        (CROSS[slug] || []).forEach(function(x){ if (list.indexOf(x.slug) < 0) list.push(x.slug); });
        const li = document.createElement('li');
        li.className = 'book-biome';
        const head = document.createElement('button');
        head.className = 'book-biome-head';
        head.innerHTML = '<span>' + (NAMES[slug]||fmt(slug)) + '</span><span class="bk-count">' + list.length + '</span>';
        const ul = document.createElement('ul');
        ul.className = 'book-creatures';
        list.forEach(function(c){
          const x = (CROSS[slug] || []).filter(function(z){ return z.slug === c; })[0];
          const homeBiome = x ? x.home : slug;
          const dispName = x ? x.name : fmt(c);
          const b = document.createElement('button');
          b.className = 'book-creature';
          b.textContent = dispName;
          b.addEventListener('click', function(){
            idx.querySelectorAll('.book-creature.sel').forEach(function(y){y.classList.remove('sel');});
            b.classList.add('sel');
            openCreature(c, homeBiome, dispName);
          });
          const li2 = document.createElement('li');
          li2.appendChild(b); ul.appendChild(li2);
        });
        head.addEventListener('click', function(){
          li.classList.toggle('open');
          setPage(chapterPage(slug, i + 1, list.length));
        });
        li.appendChild(head); li.appendChild(ul); idx.appendChild(li);
        if (slug === focusBiome) {
          li.classList.add('open');
          const at = list.indexOf(focusSlug);
          if (focusSlug && at >= 0) {
            const btn = ul.querySelectorAll('.book-creature')[at];
            if (btn) { btn.classList.add('sel'); openCreature(focusSlug, slug, fmt(focusSlug)); }
          } else {
            setPage(chapterPage(slug, i + 1, list.length));
          }
        }
      });
    }
    // deep links open the tome directly to the requested chapter
    if (focusBiome) openBook();
  };

  // ═════ OPEN CREATURE PAGE MODAL ═════
  window.openCreaturePage = async function(biome, slug) {
    const modalId = 'creature-page-modal';
    let modal = document.getElementById(modalId);
    if(!modal) {
      modal = document.createElement('div');
      modal.id = modalId;
      modal.className = 'creature-page-modal';
      modal.innerHTML = '<div class="modal-chrome"><div class="modal-scroll"><div class="modal-content"></div></div><button class="modal-close" onclick="closeCreaturePageModal()">✕</button></div>';
      document.body.appendChild(modal);
    }
    modal.style.display = 'block';
    const content = modal.querySelector('.modal-content');
    content.innerHTML = '<p style="color:#8a7a55;text-align:center;padding:2rem;"><em>Loading...</em></p>';
    try {
      const resp = await fetch('/ethra/api/creature/'+biome+'/'+slug);
      const data = await resp.json();
      content.innerHTML = data.content || '<p><em>Content not available.</em></p>';
    } catch(e) {
      content.innerHTML = '<p style="color:#8a7a55;text-align:center;"><em>Failed to load creature.</em></p>';
    }
  };
  
  window.closeCreaturePageModal = function() {
    const modal = document.getElementById('creature-page-modal');
    if(modal) modal.style.display = 'none';
  };
  
  window.openUndergroundCave = function(cave) {
    const modalId = 'creature-page-modal';
    let modal = document.getElementById(modalId);
    if(!modal) {
      modal = document.createElement('div');
      modal.id = modalId;
      modal.className = 'creature-page-modal';
      modal.innerHTML = '<div class="modal-chrome"><div class="modal-scroll"><div class="modal-content"></div></div><button class="modal-close" onclick="closeCreaturePageModal()">✕</button></div>';
      document.body.appendChild(modal);
    }
    modal.style.display = 'block';
    const content = modal.querySelector('.modal-content');
    content.innerHTML = '<h3 style="color:#c9a059;margin-bottom:1rem;">'+cave.name+'</h3><p style="color:#8a7a55;margin-bottom:1.5rem;">'+cave.subtitle+'</p><div class="constituent-list"></div>';
    const list = content.querySelector('.constituent-list');
    (cave.constituents || []).forEach(c => {
      const link = document.createElement('button');
      link.style.display = 'block';
      link.style.width = '100%';
      link.style.padding = '0.75rem 1rem';
      link.style.marginBottom = '0.5rem';
      link.style.background = '#fff8e8';
      link.style.border = '2px solid #3a2f1f';
      link.style.borderRadius = '4px';
      link.style.cursor = 'pointer';
      link.style.fontFamily = 'Georgia, serif';
      link.style.fontSize = '0.95rem';
      link.style.color = '#2a1f0f';
      link.style.textAlign = 'left';
      link.textContent = '→ ' + c.name;
      link.onclick = function() { openCreaturePage('underground', c.slug); };
      list.appendChild(link);
    });
  };
  
  // Wire Bestiary nav button to map
  (function(){
    const bestiaryBtn = document.querySelector('.nav-section-header-nested[onclick*="bestiary"]');
    if(bestiaryBtn) {
      bestiaryBtn.onclick = function() {
        toggleSection('bestiary-nested');
        loadBestiaryMap();
      };
    }
  })();

