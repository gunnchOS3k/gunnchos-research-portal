"""SurfaceKit V2 renderer.

Turns a repository's own files into a public page with a primary action.
Truth copy stays in About / Build status. No invented metrics.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

PRIMARY = {
    "STATIC_RESEARCH_SURFACE_WORKER": "Explore evidence",
    "STATIC_PRODUCT_SURFACE_WORKER": "Explore device",
    "META_DIRECTORY_WORKER": "Browse directory",
    "BACKEND_CONTROL_SURFACE_WORKER": "Run local demo",
    "HEAVY_ASSET_EXTERNAL_RUNTIME_SURFACE": "Review build status",
    "GAME_LANDING_WORKER": "Review build status",
    "LIVE_DEVELOPMENT_RUNTIME": "Play development build",
}

OULU_NOTE = (
    "Independent readiness lab. This page is not a University of Oulu affiliation "
    "and it is not a live Oulu testbed."
)


def _flat_yaml(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("#") or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("'\"")
    return data


def _readme_sections(text: str, limit: int = 6) -> list[dict[str, str]]:
    sections: list[dict[str, str]] = []
    current_title = "Overview"
    buf: list[str] = []

    def flush() -> None:
        body = " ".join(part.strip() for part in buf if part.strip())
        body = re.sub(r"\s+", " ", body)[:420]
        if body:
            sections.append({"id": _slug(current_title), "title": current_title, "body": body})

    for line in text.splitlines():
        if line.startswith("## "):
            flush()
            if len(sections) >= limit:
                break
            current_title = line[3:].strip()
            buf = []
        else:
            if line.startswith("|") or line.startswith("```"):
                continue
            buf.append(line)
    if len(sections) < limit:
        flush()
    return sections[:limit]


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "item"


def extract_explore(repo: Path, meta: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, str]] = []
    sources: list[str] = []
    for pattern in ("configs/scenarios/*.yaml", "configs/scenarios/*.yml", "config/scenarios/*.yaml"):
        for path in sorted(repo.glob(pattern)):
            if path.stat().st_size > 80_000:
                continue
            fields = _flat_yaml(path.read_text(encoding="utf-8", errors="replace"))
            if not fields:
                continue
            row = {"source": str(path.relative_to(repo))}
            for key in (
                "scenario_id",
                "site_id",
                "location_type",
                "terrestrial_status",
                "ntn_available",
                "fallback_policy",
                "ethical_framing",
                "outage_duration_minutes",
            ):
                if key in fields:
                    row[key] = fields[key]
            if len(row) > 1:
                rows.append(row)
                sources.append(row["source"])

    readme = repo / "README.md"
    sections = _readme_sections(readme.read_text(encoding="utf-8", errors="replace")) if readme.exists() else []
    if not rows:
        for section in sections:
            rows.append(
                {
                    "source": "README.md",
                    "scenario_id": section["title"],
                    "site_id": meta.get("family", ""),
                    "ethical_framing": section["body"],
                }
            )

    nodes = []
    if any("terrestrial_status" in row for row in rows):
        nodes = [
            {"id": "site", "label": "Community site"},
            {"id": "terrestrial", "label": "Terrestrial link"},
            {"id": "ntn", "label": "NTN fallback"},
        ]
        measured = True
        diagram_note = "Node labels follow fields in the repository scenario files. Values change with the selector. This is not a live network."
    else:
        for section in sections[:4]:
            nodes.append({"id": section["id"], "label": section["title"][:42]})
        measured = False
        diagram_note = "Reading aid built from repository headings. It is not a measured topology and it is not a live system."

    artifacts = []
    for folder in ("results", "figures", "paper", "docs"):
        root = repo / folder
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".json", ".csv", ".png", ".svg", ".pdf"}:
                continue
            if path.stat().st_size > 2_000_000:
                continue
            artifacts.append(str(path.relative_to(repo)))
            if len(artifacts) >= 12:
                break
        if len(artifacts) >= 12:
            break

    repro = repo / "REPRODUCIBILITY.md"
    methods = ""
    if repro.exists():
        methods = re.sub(r"\s+", " ", repro.read_text(encoding="utf-8", errors="replace"))[:700]
    elif (repo / "docs" / "REPRODUCIBILITY.md").exists():
        methods = re.sub(
            r"\s+",
            " ",
            (repo / "docs" / "REPRODUCIBILITY.md").read_text(encoding="utf-8", errors="replace"),
        )[:700]

    classification = str(meta.get("classification") or "")
    cards = []
    if classification == "META_DIRECTORY_WORKER":
        for row in rows:
            cards.append({"title": row.get("scenario_id") or "Entry", "body": row.get("ethical_framing") or row.get("source") or ""})
    return {
        "schema": "gunnchos.surfacekit.v2",
        "measured_topology": measured,
        "diagram_note": diagram_note,
        "nodes": nodes,
        "rows": rows[:24],
        "sources": sources[:24],
        "sections": sections,
        "artifacts": artifacts,
        "methods": methods,
        "cards": cards,
        "runtime_mode": "LOCAL/DEMO" if classification == "BACKEND_CONTROL_SURFACE_WORKER" else "PRECOMPUTED",
        "runtime_boot": False,
    }


def _esc(value: Any) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_page(meta: dict[str, Any], explore: dict[str, Any]) -> tuple[str, str, str]:
    classification = str(meta.get("classification") or "STATIC_RESEARCH_SURFACE_WORKER")
    primary = PRIMARY.get(classification, "Explore evidence")
    name = str(meta.get("productName") or meta.get("repo") or "gunnchOS surface")
    summary = str(meta.get("summary") or "")
    family = str(meta.get("family") or "")
    sha = str(meta.get("acceptedSha") or "")
    source = str(meta.get("sourceUrl") or "")
    limitations = meta.get("limitations") or []
    if not isinstance(limitations, list):
        limitations = [str(limitations)]
    repo = str(meta.get("repo") or "")
    independent = ""
    if repo.startswith("oulu-") or "oulu" in name.lower():
        independent = OULU_NOTE
    sections = explore.get("sections") or []
    overview = sections[:3]
    limit_items = "".join(f"<li>{_esc(item)}</li>" for item in limitations)
    overview_html = "".join(
        f"<article><h3>{_esc(item.get('title'))}</h3><p>{_esc(item.get('body'))}</p></article>"
        for item in overview
    ) or f"<article><h3>Overview</h3><p>{_esc(summary)}</p></article>"
    artifact_html = "".join(
        f"<li><code>{_esc(item)}</code></li>" for item in explore.get("artifacts") or []
    ) or "<li>No packaged download was attached on this page. Use the source repository.</li>"
    methods = explore.get("methods") or "Run the repository locally. This Worker does not execute the native toolchain."
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>{_esc(name)} · gunnchOS</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body data-surfacekit="v2" data-theme="dark">
  <a class="skip" href="#content">Skip to content</a>
  <header class="top">
    <p class="mark">gunnchOS</p>
    <nav class="tools" aria-label="Surface">
      <button type="button" id="theme-toggle">Light theme</button>
      <a id="portal-return" href="#return" aria-label="Return to gunnchOS">← gunnchOS</a>
    </nav>
  </header>
  <main id="content">
    <p class="kicker">{_esc(family)} · STAGING_WORKER</p>
    <h1>{_esc(name)}</h1>
    <p class="lead">{_esc(summary)}</p>
    {f'<p class="note">{_esc(independent)}</p>' if independent else ''}
    <p><a class="cta" id="primary-action" href="#explore">{_esc(primary)}</a></p>
    <section id="explore" aria-labelledby="explore-title">
      <h2 id="explore-title">{_esc(primary)}</h2>
      <p id="diagram-note"></p>
      <div class="layout">
        <div>
          <svg id="diagram" role="img" aria-labelledby="diagram-note" viewBox="0 0 640 160"></svg>
          <label for="row-select">Repository record</label>
          <select id="row-select"></select>
          <label for="row-filter">Filter records</label>
          <input id="row-filter" type="search" placeholder="Filter by text in the repository records">
        </div>
        <div id="detail" tabindex="0" aria-live="polite"></div>
      </div>
      <div id="directory"></div>
      <table id="evidence">
        <caption>Records copied from this repository</caption>
        <thead><tr id="evidence-head"></tr></thead>
        <tbody id="evidence-body"></tbody>
      </table>
    </section>
    <section id="overview" aria-labelledby="overview-title">
      <h2 id="overview-title">Overview</h2>
      <div class="cards">{overview_html}</div>
    </section>
    <section id="methods" aria-labelledby="methods-title">
      <h2 id="methods-title">Methods</h2>
      <p>{_esc(methods)}</p>
      <p>Native research runtimes stay on a local checkout. This page shows repository records only.</p>
    </section>
    <section id="artifacts" aria-labelledby="artifacts-title">
      <h2 id="artifacts-title">Artifacts</h2>
      <ul>{artifact_html}</ul>
    </section>
    <section id="source" aria-labelledby="source-title">
      <h2 id="source-title">Source</h2>
      <p><a href="{_esc(source)}">Source repository</a></p>
      <p>Pinned source <code>{_esc(sha)}</code></p>
    </section>
    <section id="limits" aria-labelledby="limits-title">
      <h2 id="limits-title">Limitations</h2>
      <ul>{limit_items}</ul>
    </section>
    <section id="about" aria-labelledby="about-title">
      <h2 id="about-title">About / Build status / Evidence</h2>
      <h2 id="what">What is this?</h2>
      <p>{_esc(summary)}</p>
      <p>The research code is not executing here. This is a research surface.</p>
      <h2 id="why">Why does it exist?</h2>
      <p>It gives this repository a public web surface inside the gunnchOS ecosystem without pretending the original runtime runs on Cloudflare Workers.</p>
      <h2 id="today">What can I actually do with it today?</h2>
      <p>Use the primary action to inspect repository records, then open the source for the local toolchain.</p>
      <h2 id="unfinished">What is not finished?</h2>
      <ul>{limit_items}</ul>
      <p class="badge">STAGING_WORKER</p>
      <p>Runtime mode on this page: {_esc(explore.get("runtime_mode"))}. No remote model call is made.</p>
    </section>
  </main>
  <script src="/app.js"></script>
</body>
</html>
"""
    css = """:root { color-scheme: dark; --bg:#10141a; --ink:#eef2f4; --muted:#b7c0c7; --line:#31404a; --accent:#7dcea0; --card:#182028; }
[data-theme="light"] { color-scheme: light; --bg:#f4f7f8; --ink:#142028; --muted:#3d4c55; --line:#c5d0d6; --card:#fff; }
* { box-sizing: border-box; }
body { margin:0; font:18px/1.5 Georgia, "Iowan Old Style", serif; background:var(--bg); color:var(--ink); }
a { color:var(--accent); }
.skip { position:absolute; left:-999px; }
.skip:focus { left:8px; top:8px; background:var(--card); padding:8px; }
.top, main { width:min(1080px, calc(100% - 32px)); margin:0 auto; }
.top { display:flex; justify-content:space-between; align-items:center; padding:16px 0; }
.mark { letter-spacing:.08em; text-transform:uppercase; font:600 13px/1 ui-sans-serif, system-ui, sans-serif; }
.tools { display:flex; gap:12px; align-items:center; }
button, .cta, select, input { font:16px/1.3 ui-sans-serif, system-ui, sans-serif; }
button, .cta { background:var(--accent); color:#102018; border:0; border-radius:999px; padding:10px 16px; text-decoration:none; display:inline-block; }
.kicker, .badge, .note { font:600 13px/1.4 ui-sans-serif, system-ui, sans-serif; color:var(--muted); }
h1 { font-size:clamp(2rem, 5vw, 3.4rem); line-height:1.05; margin:8px 0; }
.lead { font-size:1.2rem; max-width:42rem; }
.layout { display:grid; grid-template-columns:1.1fr .9fr; gap:16px; }
#diagram { width:100%; height:auto; background:var(--card); border:1px solid var(--line); border-radius:12px; }
#detail, article, table { background:var(--card); border:1px solid var(--line); border-radius:12px; }
#detail, article { padding:12px 14px; }
.cards { display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; }
table { width:100%; border-collapse:collapse; }
th, td { text-align:left; padding:8px; border-bottom:1px solid var(--line); font:14px/1.4 ui-sans-serif, system-ui, sans-serif; }
label { display:block; margin-top:10px; font:600 13px/1.3 ui-sans-serif, system-ui, sans-serif; }
select, input { width:100%; padding:8px; border-radius:8px; border:1px solid var(--line); background:var(--bg); color:var(--ink); }
a:focus-visible, button:focus-visible, select:focus-visible, input:focus-visible { outline:3px solid var(--accent); outline-offset:2px; }
.node { cursor:pointer; }
@media (max-width: 800px) {
  .layout, .cards { grid-template-columns:1fr; }
  .top { align-items:flex-start; gap:8px; }
}
"""
    js = r"""const link = document.getElementById("portal-return");
const themeButton = document.getElementById("theme-toggle");
const root = document.body;
function applyTheme(theme) {
  root.setAttribute("data-theme", theme);
  themeButton.textContent = theme === "dark" ? "Light theme" : "Dark theme";
}
themeButton.addEventListener("click", () => {
  applyTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark");
});
const saved = window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
applyTheme(saved);

function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }
function cell(tag, text) {
  const el = document.createElement(tag);
  el.textContent = text == null ? "" : String(text);
  return el;
}

Promise.all([
  fetch("/project-surface.json").then((res) => res.json()),
  fetch("/explore.json").then((res) => res.json())
]).then(([meta, explore]) => {
  if (meta && typeof meta.returnUrl === "string" && /^https:\/\//.test(meta.returnUrl)) {
    link.href = meta.returnUrl;
  }
  const note = document.getElementById("diagram-note");
  note.textContent = explore.diagram_note || "";
  const svg = document.getElementById("diagram");
  const nodes = Array.isArray(explore.nodes) ? explore.nodes : [];
  nodes.forEach((node, index) => {
    const x = 40 + index * 200;
    const group = document.createElementNS("http://www.w3.org/2000/svg", "g");
    group.setAttribute("class", "node");
    group.setAttribute("tabindex", "0");
    group.setAttribute("role", "button");
    group.setAttribute("aria-label", node.label || "node");
    const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    rect.setAttribute("x", String(x));
    rect.setAttribute("y", "48");
    rect.setAttribute("width", "160");
    rect.setAttribute("height", "64");
    rect.setAttribute("rx", "12");
    rect.setAttribute("fill", "#20343a");
    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", String(x + 80));
    text.setAttribute("y", "86");
    text.setAttribute("text-anchor", "middle");
    text.setAttribute("fill", "#eef2f4");
    text.setAttribute("font-size", "14");
    text.textContent = node.label || "";
    group.appendChild(rect);
    group.appendChild(text);
    group.addEventListener("click", () => { document.getElementById("row-filter").value = node.label || ""; draw(); });
    svg.appendChild(group);
  });
  const select = document.getElementById("row-select");
  const filter = document.getElementById("row-filter");
  const rows = Array.isArray(explore.rows) ? explore.rows : [];
  function visible() {
    const q = filter.value.trim().toLowerCase();
    return rows.filter((row) => !q || JSON.stringify(row).toLowerCase().includes(q));
  }
  function draw() {
    const list = visible();
    clear(select);
    list.forEach((row, index) => {
      const option = document.createElement("option");
      option.value = String(index);
      option.textContent = row.scenario_id || row.source || ("Record " + (index + 1));
      select.appendChild(option);
    });
    const keys = [];
    list.forEach((row) => Object.keys(row).forEach((key) => { if (!keys.includes(key) && key !== "ethical_framing") keys.push(key); }));
    const head = document.getElementById("evidence-head");
    const body = document.getElementById("evidence-body");
    clear(head); clear(body);
    keys.slice(0, 6).forEach((key) => head.appendChild(cell("th", key)));
    list.forEach((row) => {
      const tr = document.createElement("tr");
      keys.slice(0, 6).forEach((key) => tr.appendChild(cell("td", row[key] || "")));
      body.appendChild(tr);
    });
    const current = list[Number(select.value)] || list[0];
    const detail = document.getElementById("detail");
    clear(detail);
    if (!current) {
      detail.appendChild(cell("p", "No repository record matches that filter."));
      return;
    }
    detail.appendChild(cell("h3", current.scenario_id || "Record"));
    detail.appendChild(cell("p", current.ethical_framing || current.source || ""));
    detail.appendChild(cell("p", "Source file: " + (current.source || "repository")));
    const directory = document.getElementById("directory");
    clear(directory);
    (explore.cards || []).forEach((card) => {
      const article = document.createElement("article");
      article.appendChild(cell("h3", card.title || ""));
      article.appendChild(cell("p", card.body || ""));
      directory.appendChild(article);
    });
  }
  select.addEventListener("change", draw);
  filter.addEventListener("input", draw);
  draw();
}).catch(() => {});
"""
    return html, css, js


def write_surface(repo: Path) -> dict[str, Any]:
    public = repo / "web-surface" / "public"
    meta_path = public / "project-surface.json"
    if not meta_path.exists():
        raise FileNotFoundError(meta_path)
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    explore = extract_explore(repo, meta)
    html, css, js = render_page(meta, explore)
    forbidden = ("workers.dev", "gunnchos-finds", "FINDS", "play now", "official oulu")
    blob = (html + css + js).lower()
    for phrase in forbidden:
        if phrase in blob:
            raise RuntimeError(f"surface kit emitted forbidden phrase: {phrase}")
    (public / "index.html").write_text(html, encoding="utf-8")
    (public / "styles.css").write_text(css, encoding="utf-8")
    (public / "app.js").write_text(js, encoding="utf-8")
    (public / "explore.json").write_text(json.dumps(explore, indent=2) + "\n", encoding="utf-8")
    return {"repo": meta.get("repo"), "rows": len(explore["rows"]), "measured_topology": explore["measured_topology"]}
