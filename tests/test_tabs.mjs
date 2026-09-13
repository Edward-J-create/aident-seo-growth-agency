// Execute the distributed template's actual JS against a minimal DOM model.
// This is behavioral logic coverage, not a browser/layout/accessibility audit.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const html = fs.readFileSync(new URL('../assets/html-report-template.html', import.meta.url), 'utf8');
const scripts = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/gi)].map(m => m[1]);
const tabDefs = [...html.matchAll(/<button\b[^>]*role="tab"[^>]*>/g)].map(m => Object.fromEntries([...m[0].matchAll(/([\w-]+)="([^"]*)"/g)].map(a => [a[1], a[2]])));
const panelDefs = [...html.matchAll(/<section\b[^>]*role="tabpanel"[^>]*>/g)].map(m => ({ id: m[0].match(/\bid="([^"]+)"/)[1], hidden: /\bhidden\b/.test(m[0]) }));
assert.ok(tabDefs.length > 1);

function setup(hash = '') {
  const winEvents = {};
  const listEvents = {};
  const details = [{ open: false }, { open: true }];
  const document = { activeElement: null };
  const tabs = tabDefs.map(attrs => ({
    attrs: { ...attrs }, events: {}, tabIndex: 0,
    getAttribute(k) { return this.attrs[k]; },
    setAttribute(k, v) { this.attrs[k] = v; },
    addEventListener(k, fn) { this.events[k] = fn; },
    focus() { document.activeElement = this; },
  }));
  const panels = panelDefs.map(p => ({ ...p }));
  const location = { hash };
  document.querySelectorAll = query => {
    if (query === '[role="tab"]') return tabs;
    if (query === '[role="tabpanel"]') return panels;
    if (query === 'details') return details;
    throw Error(`Unexpected query: ${query}`);
  };
  document.querySelector = query => {
    assert.equal(query, '[role="tablist"]');
    return { addEventListener: (k, fn) => { listEvents[k] = fn; } };
  };
  const context = vm.createContext({
    document, location,
    history: { replaceState: (_s, _t, value) => { location.hash = value; } },
    window: { addEventListener: (k, fn) => { winEvents[k] = fn; } },
  });
  scripts.forEach(script => vm.runInContext(script, context));
  function selected(index) {
    assert.equal(tabs.filter(t => t.attrs['aria-selected'] === 'true').length, 1);
    assert.equal(tabs[index].attrs['aria-selected'], 'true');
    assert.equal(tabs.filter(t => t.tabIndex === 0).length, 1);
    assert.deepEqual(panels.filter(p => !p.hidden).map(p => p.id), [tabs[index].attrs['aria-controls']]);
  }
  function key(key) { listEvents.keydown({ key, preventDefault() {} }); }
  return { tabs, panels, location, selected, key, details, winEvents };
}

const app = setup();
app.selected(0);
app.tabs.forEach((tab, index) => { tab.events.click(); app.selected(index); assert.equal(app.location.hash, '#' + tab.attrs['aria-controls']); });
app.tabs[0].focus();
app.key('End'); app.selected(app.tabs.length - 1);
app.key('ArrowRight'); app.selected(0);
app.key('ArrowLeft'); app.selected(app.tabs.length - 1);
app.key('Home'); app.selected(0);
app.key('ArrowDown'); app.selected(1);
app.key('ArrowUp'); app.selected(0);
app.location.hash = '#' + app.panels.at(-1).id;
app.winEvents.hashchange(); app.selected(app.tabs.length - 1);
setup('#' + app.panels.at(-1).id).selected(app.tabs.length - 1);
setup('#unknown-panel').selected(0);
app.winEvents.beforeprint(); assert.ok(app.details.every(d => d.open));
app.winEvents.afterprint(); assert.deepEqual(app.details.map(d => d.open), [false, true]);
assert.match(html, /<noscript>[\s\S]*\.panel\[hidden\]\{display:block\}/);
console.log(`PASS: ${app.tabs.length} tabs; click, keyboard wrap, hash, print expansion and no-JS declaration. Not browser visual QA.`);
