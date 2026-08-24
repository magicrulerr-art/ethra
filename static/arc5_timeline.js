/*
 * Arc 5 War-Dispatch Timeline — runtime (Option A: bare clock)
 * ----------------------------------------------------------------------------
 * Builds the bar with:
 *   - Hour train (5h..12h, gold flips to crimson at 12h)
 *   - Track line + progressed fill (gold→crimson)
 *   - 22 dots, one per chapter, positioned along the rail by minute
 *   - 5 med markers (slightly larger), at position medIdx
 *   - 1 vertical "now" line that moves with selection
 *   - Title bar with the active timestamp readout
 *
 * No medallion ring. No image wells. No <img> fallback. No hover labels.
 * ----------------------------------------------------------------------------
 */
(function() {
  const ARC5_NUM = 5;
  const MED_CHAPTERS_ABS = [1, 5, 11, 19, 22];
  const TIMESTAMP_RE = /^(\d{2}):(\d{2})/;

  function timeToMinutes(hh, mm) {
    const h = parseInt(hh, 10), m = parseInt(mm, 10);
    if (Number.isNaN(h) || Number.isNaN(m)) return null;
    return h * 60 + m;
  }
  function railPct(min, lo, hi) {
    if (hi <= lo) return 0;
    return Math.max(0, Math.min(100, ((min - lo) / (hi - lo)) * 100));
  }

  function buildTimelineForArc5() {
    const arcPanel = document.querySelector('#arc-panel-' + ARC5_NUM);
    if (!arcPanel) return null;

    const tabs = Array.from(arcPanel.querySelectorAll('.chapter-tab'));
    if (!tabs.length) return null;

    const entries = tabs.map(tab => {
      const id = tab.getAttribute('data-chapter');
      const title = (tab.textContent || '').trim();
      const m = title.match(TIMESTAMP_RE);
      const hh = m ? m[1] : null;
      const mm = m ? m[2] : null;
      return {
        id,
        title,
        hh, mm,
        min: timeToMinutes(hh, mm),
        absIdx: parseInt((id.match(/ch(\d+)/) || [])[1] || '0', 10),
      };
    });
    const timed = entries.filter(e => e.min != null).sort((a, b) => a.min - b.min);
    if (!timed.length) return null;

    const lo = timed[0].min;
    const hi = timed[timed.length - 1].min;
    timed.forEach(e => { e.pct = railPct(e.min, lo, hi); });

    const tickShell = document.createElement('div');
    tickShell.className = 'Arc5Timeline';
    tickShell.id = 'arc5Timeline';
    tickShell.setAttribute('role', 'slider');
    tickShell.setAttribute('aria-label', 'Arc 5 hour dispatch');
    tickShell.setAttribute('aria-valuemin', '1');
    tickShell.setAttribute('aria-valuemax', String(timed.length));
    tickShell.setAttribute('aria-valuenow', '1');

    /* Title bar */
    const label = document.createElement('div');
    label.className = 'timeline-label';
    const titleText = document.createElement('span');
    titleText.textContent = '✦ The War Under Twin Suns — Hour Dispatch ✦';
    const secondsBox = document.createElement('span');
    secondsBox.className = 'sepia-seconds';
    secondsBox.id = 'arc5_now_text';
    secondsBox.textContent = timed[0].hh + ':' + timed[0].mm;
    label.appendChild(titleText);
    label.appendChild(secondsBox);
    tickShell.appendChild(label);

    /* Rail row anchored to the bar */
    const railRow = document.createElement('div');
    railRow.className = 'rail-row';

    /* Track line */
    const track = document.createElement('div');
    track.className = 'rail-track';
    railRow.appendChild(track);

    /* Progressed fill */
    const fill = document.createElement('div');
    fill.className = 'rail-fill';
    railRow.appendChild(fill);

    /* 22 ticks + 5 med markers, each positioned absolutely on the rail */
    const nodes = [];
    let medIdx = 0;
    timed.forEach((e, idx) => {
      const isMed = MED_CHAPTERS_ABS.includes(e.absIdx);
      const node = document.createElement('div');
      node.className = isMed ? 'med' : 'tick';
      node.style.left = e.pct + '%';
      node.setAttribute('data-chapter', e.id);
      node.setAttribute('data-min', String(e.min));
      node.setAttribute('data-idx', String(idx));
      node.setAttribute('data-active', 'false');
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.setAttribute('aria-label',
        'Chapter ' + e.absIdx + ' — ' + e.hh + ':' + e.mm);
      if (isMed) {
        if (parseInt(e.hh, 10) >= 12) node.classList.add('flicker');
        /* Probe for a real illustration at arc5-med-<id>-v{N}.png — try v5
         * down to v1, since v2/v3/etc have been used for chapter-end images
         * but the timeline med slot keeps its own versioning. Pick first
         * on-disk match in priority order. */
        function tryProbe(version, onFound, onFail) {
          /* /ethra/ prefix like every other fetch: the local PrefixMiddleware
           * strips it, and the Pages mirror bakes the art at that path. A bare
           * /static/ probe 404s on Pages and leaves the hover bubble a black
           * disc (Ainz-reported, 2026-08-24). */
          const path = '/ethra/static/images/arc5-med-' + e.id + '-' + version + '.png';
          const sub = new Image();
          sub.onload = () => onFound(path, version);
          sub.onerror = () => onFail();
          sub.src = path;
        }
        function attachIllust(path) {
          node.setAttribute('data-illust', '1');
          node.style.setProperty('--med-illust', 'url(' + path + ')');
        }
        /* Try versions in priority order — v99-style overrides first, then
         * v1–v5 series. First hit wins. */
        let tried = 0;
        const order = ['v101', 'v100', 'v99', 'v98', 'v97', 'v96', 'v95', 'v9', 'v8', 'v7', 'v6', 'v5', 'v4', 'v3', 'v2', 'v1'];
        function attempt() {
          if (tried >= order.length) return;
          const v = order[tried++];
          tryProbe(v, attachIllust, attempt);
        }
        attempt();
      }
      node.addEventListener('click', () => selectChapter(e.id, e.pct));
      node.addEventListener('keydown', (ev) => {
        if (ev.key === 'Enter' || ev.key === ' ') {
          ev.preventDefault();
          selectChapter(e.id, e.pct);
        }
      });
      railRow.appendChild(node);
      nodes.push(node);
      if (isMed) medIdx++;
    });

    /* Vertical "now" indicator — sits at the active chapter's minute */
    const nowFlag = document.createElement('div');
    nowFlag.className = 'now-flag';
    nowFlag.style.left = timed[0].pct + '%';
    railRow.appendChild(nowFlag);

    tickShell.appendChild(railRow);

    /* Hour train below */
    const hourTrain = document.createElement('div');
    hourTrain.className = 'hour-train';
    const startH = parseInt(timed[0].hh, 10);
    const endH = parseInt(timed[timed.length - 1].hh, 10);
    for (let h = startH; h <= endH; h++) {
      const lbl = document.createElement('div');
      const hourText = String(h).padStart(2, '0');
      lbl.innerHTML = '<span class="h ' + (h >= 12 ? 'flicker' : '') + '">' + hourText + 'h</span>';
      hourTrain.appendChild(lbl);
    }
    tickShell.appendChild(hourTrain);

    /* ─── Slider row + chapter-title readout (primary navigation) ─── */
    const sliderRow = document.createElement('div');
    sliderRow.className = 'slider-row';

    const slider = document.createElement('input');
    slider.type = 'range';
    slider.className = 'arc5-slider';
    slider.min = '0';
    slider.max = String(timed.length - 1);
    slider.step = '1';
    slider.value = '0';
    slider.setAttribute('aria-label', 'Arc 5 chapter slider');
    sliderRow.appendChild(slider);

    const readout = document.createElement('div');
    readout.className = 'chapter-readout';
    const readoutTitle = document.createElement('span');
    readoutTitle.className = 'title';
    readoutTitle.id = 'arc5_readout_title';
    readoutTitle.textContent = timed[0].title || '';
    const readoutTs = document.createElement('span');
    readoutTs.className = 'ts';
    readoutTs.id = 'arc5_readout_ts';
    readoutTs.textContent = timed[0].hh + ':' + timed[0].mm;
    readout.appendChild(readoutTitle);
    readout.appendChild(readoutTs);

    tickShell.appendChild(sliderRow);
    tickShell.appendChild(readout);

    let suppressSlider = false;
    slider.addEventListener('input', () => {
      if (suppressSlider) return;
      const idx = parseInt(slider.value, 10) || 0;
      const entry = timed[idx];
      if (!entry) return;
      /* Don't navigate yet on `input` — only on `change`, to avoid firing
       * an AJAX load on every micro-pixel of mouse motion. */
      readoutTitle.textContent = entry.title || '';
      readoutTs.textContent = entry.hh + ':' + entry.mm;
      fill.style.width = entry.pct + '%';
      nowFlag.style.left = entry.pct + '%';
    });
    slider.addEventListener('change', () => {
      const idx = parseInt(slider.value, 10) || 0;
      const entry = timed[idx];
      if (!entry) return;
      selectChapter(entry.id, entry.pct);
    });

    /* Update slider value when a chapter-tab is clicked externally.
     * This keeps the slider in sync; otherwise clicking a tab in the
     * chapter-subnav leaves the slider stuck at a stale position. */
    function syncSliderToId(id) {
      const idx = timed.findIndex(e => e.id === id);
      if (idx >= 0) {
        suppressSlider = true;
        slider.value = String(idx);
        suppressSlider = false;
      }
    }
    /* Listen for tab clicks so the slider follows */
    arcPanel.addEventListener('click', (ev) => {
      const t = ev.target.closest('.chapter-tab');
      if (!t) return;
      syncSliderToId(t.getAttribute('data-chapter'));
    });

    const subnav = arcPanel.querySelector('.chapter-subnav');
    subnav.parentNode.insertBefore(tickShell, subnav);

    function selectChapter(id, pct) {
      /* Drive the existing chapter-tab click so the chapter-content active class &
       * lazy-load plumbing stay canonical. */
      const tab = arcPanel.querySelector('.chapter-tab[data-chapter="' + id + '"]');
      if (tab) tab.click();
      const content = document.getElementById(id);
      if (content && content.scrollIntoView) {
        setTimeout(() => content.scrollIntoView({ behavior: 'smooth', block: 'start' }), 60);
      }
      onSelect(pct, id);
    }

    function onSelect(pct, id) {
      /* Move fill + now-flag to chapter position */
      fill.style.width = (pct ?? 0) + '%';
      nowFlag.style.left = (pct ?? 0) + '%';

      /* Update active state + active timestamp readout */
      let activeIdx = 0;
      nodes.forEach((n, i) => {
        const isActive = n.getAttribute('data-chapter') === id;
        n.classList.toggle('active', isActive);
        if (isActive) activeIdx = i;
      });
      const e = timed.find(t => t.id === id);
      const secondsBox = document.getElementById('arc5_now_text');
      if (secondsBox && e) secondsBox.textContent = e.hh + ':' + e.mm;
      /* Update chapter-title readout + slider value */
      const rT = document.getElementById('arc5_readout_title');
      const rTs = document.getElementById('arc5_readout_ts');
      const sliderEl = tickShell.querySelector('input.arc5-slider');
      if (rT && e) rT.textContent = e.title || '';
      if (rTs && e) rTs.textContent = e.hh + ':' + e.mm;
      if (sliderEl && e) {
        const idx = timed.findIndex(x => x.id === e.id);
        if (idx >= 0) {
          suppressSlider = true;
          sliderEl.value = String(idx);
          suppressSlider = false;
        }
      }
    }

    /* Listen for in-panel chapter-tab clicks so the timeline reflects them */
    arcPanel.addEventListener('click', (ev) => {
      const t = ev.target.closest('.chapter-tab');
      if (!t) return;
      const id = t.getAttribute('data-chapter');
      const entry = timed.find(e => e.id === id);
      if (entry) onSelect(entry.pct, id);
    });

    /* Keyboard nav on the slider container itself */
    tickShell.addEventListener('keydown', (ev) => {
      const curId = arcPanel.querySelector('.chapter-tab.active')?.getAttribute('data-chapter');
      const curIdx = timed.findIndex(t => t.id === curId);
      if (ev.key === 'ArrowRight') {
        ev.preventDefault();
        const next = timed[(curIdx + 1) % timed.length];
        if (next) selectChapter(next.id, next.pct);
      } else if (ev.key === 'ArrowLeft') {
        ev.preventDefault();
        const prev = timed[(curIdx - 1 + timed.length) % timed.length];
        if (prev) selectChapter(prev.id, prev.pct);
      } else if (ev.key === 'Home') {
        ev.preventDefault();
        selectChapter(timed[0].id, timed[0].pct);
      } else if (ev.key === 'End') {
        ev.preventDefault();
        selectChapter(timed[timed.length - 1].id, timed[timed.length - 1].pct);
      }
    });

    /* Initial paint: position fill + now-flag at the active chapter-tab */
    const initial = arcPanel.querySelector('.chapter-tab.active');
    if (initial) {
      const entry = timed.find(e => e.id === initial.getAttribute('data-chapter'));
      if (entry) {
        fill.style.width = entry.pct + '%';
        nowFlag.style.left = entry.pct + '%';
        nodes.forEach(n => {
          n.classList.toggle('active', n.getAttribute('data-chapter') === entry.id);
        });
        const secondsBox = document.getElementById('arc5_now_text');
        if (secondsBox) secondsBox.textContent = entry.hh + ':' + entry.mm;
        /* Reflect in slider + readout */
        const iniIdx = timed.findIndex(e => e.id === entry.id);
        if (iniIdx >= 0) slider.value = String(iniIdx);
        const rT = document.getElementById('arc5_readout_title');
        const rTs = document.getElementById('arc5_readout_ts');
        if (rT) rT.textContent = entry.title || '';
        if (rTs) rTs.textContent = entry.hh + ':' + entry.mm;
      }
    }

    return tickShell;
  }

  function syncTimelineVisibility() {
    const tl = document.getElementById('arc5Timeline');
    if (!tl) {
      const arc5Panel = document.querySelector('#arc-panel-' + ARC5_NUM);
      if (arc5Panel && arc5Panel.classList.contains('active')) {
        const built = buildTimelineForArc5();
        if (built) {
          document.body.classList.add('arc5-timeline-on');
          built.classList.add('active');
        }
      } else {
        document.body.classList.remove('arc5-timeline-on');
      }
      return;
    }
    const arc5Panel = document.querySelector('#arc-panel-' + ARC5_NUM);
    const onArc5 = arc5Panel && arc5Panel.classList.contains('active');
    tl.classList.toggle('active', !!onArc5);
    document.body.classList.toggle('arc5-timeline-on', !!onArc5);
  }

  function hookArcTabs() {
    document.addEventListener('click', (ev) => {
      const t = ev.target.closest('.arc-tab');
      if (!t) return;
      setTimeout(syncTimelineVisibility, 60);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    hookArcTabs();
    setTimeout(syncTimelineVisibility, 80);
  });
})();
