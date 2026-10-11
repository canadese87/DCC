/* Miglioramenti dell'interfaccia: tabelle ordinabili e filtrabili, riquadri "Da verificare". */
(function () {
  "use strict";

  var SORT_MIN_ROWS = 4;
  var FILTER_MIN_ROWS = 8;
  var WIDE_MIN_COLS = 5;
  var STORE_KEY = "dcc-nascondi-verifiche";

  var collator = new Intl.Collator("it", { numeric: true, sensitivity: "base" });

  function cellText(row, idx) {
    var c = row.cells[idx];
    return c ? c.textContent.trim() : "";
  }

  function numericValue(text) {
    var m = text.replace(/−/g, "-").match(/^([+-]?)\s*(\d+(?:[.,]\d+)?)/);
    if (!m) return null;
    var n = parseFloat(m[2].replace(",", "."));
    return m[1] === "-" ? -n : n;
  }

  function compare(a, b) {
    var na = numericValue(a), nb = numericValue(b);
    if (na !== null && nb !== null && na !== nb) return na - nb;
    if (na !== null && nb === null) return -1;
    if (na === null && nb !== null) return 1;
    return collator.compare(a, b);
  }

  function sortBy(table, idx, dir) {
    var body = table.tBodies[0];
    var rows = Array.prototype.slice.call(body.rows);
    rows.sort(function (r1, r2) {
      var r = compare(cellText(r1, idx), cellText(r2, idx));
      return dir === "ascending" ? r : -r;
    });
    rows.forEach(function (r) { body.appendChild(r); });
  }

  function makeSortable(table) {
    var head = table.tHead && table.tHead.rows[0];
    if (!head) return;
    Array.prototype.forEach.call(head.cells, function (th, idx) {
      th.classList.add("dcc-sortable");
      th.setAttribute("tabindex", "0");
      function activate() {
        var cur = th.getAttribute("aria-sort");
        var dir = cur === "ascending" ? "descending" : "ascending";
        Array.prototype.forEach.call(head.cells, function (o) { o.removeAttribute("aria-sort"); });
        th.setAttribute("aria-sort", dir);
        sortBy(table, idx, dir);
      }
      th.addEventListener("click", activate);
      th.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); activate(); }
      });
    });
  }

  function makeFilterable(table) {
    var wrap = table.closest(".md-typeset__scrollwrap") || table;
    var input = document.createElement("input");
    input.type = "search";
    input.className = "dcc-filter";
    input.placeholder = "Filtra le righe della tabella…";
    input.setAttribute("aria-label", "Filtra le righe della tabella");
    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      Array.prototype.forEach.call(table.tBodies[0].rows, function (row) {
        row.style.display = !q || row.textContent.toLowerCase().indexOf(q) !== -1 ? "" : "none";
      });
    });
    wrap.parentNode.insertBefore(input, wrap);
  }

  function enhanceTables(root) {
    var tables = root.querySelectorAll(".md-typeset table:not([class])");
    Array.prototype.forEach.call(tables, function (table) {
      if (table.dataset.dccDone || !table.tBodies.length || !table.tHead) return;
      table.dataset.dccDone = "1";
      var rows = table.tBodies[0].rows.length;
      var cols = table.tHead.rows[0].cells.length;
      if (cols >= WIDE_MIN_COLS) table.classList.add("dcc-wide");
      if (rows >= SORT_MIN_ROWS) makeSortable(table);
      if (rows >= FILTER_MIN_ROWS) makeFilterable(table);
    });
  }

  function storedHidden() {
    try { return localStorage.getItem(STORE_KEY) === "1"; } catch (e) { return false; }
  }

  function storeHidden(v) {
    try { localStorage.setItem(STORE_KEY, v ? "1" : "0"); } catch (e) { /* storage non disponibile */ }
  }

  function markVerifiche(root) {
    var found = 0;
    var titles = root.querySelectorAll(".md-typeset .admonition-title, .md-typeset details > summary");
    Array.prototype.forEach.call(titles, function (t) {
      if (t.textContent.trim().toLowerCase() === "da verificare") {
        t.parentElement.classList.add("verifica");
        found++;
      }
    });
    return found;
  }

  function setupToggle(count) {
    var old = document.querySelector(".dcc-toggle");
    if (old) old.remove();
    document.body.classList.toggle("nascondi-verifiche", storedHidden());
    if (!count) return;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "dcc-toggle";
    function label() {
      var hidden = document.body.classList.contains("nascondi-verifiche");
      btn.textContent = (hidden ? "Mostra" : "Nascondi") + " “Da verificare” (" + count + ")";
    }
    btn.addEventListener("click", function () {
      storeHidden(document.body.classList.toggle("nascondi-verifiche"));
      label();
    });
    label();
    document.body.appendChild(btn);
  }

  function run() {
    enhanceTables(document);
    setupToggle(markVerifiche(document));
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(run);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
