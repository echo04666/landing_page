# Publishing the GameHub landing page

**中文摘要：** 静态页已放在 **`publish/index.html`**。若要用 **Streamlit**：根目录 **`streamlit_app.py`** 可在侧边栏切换 **GameHub**（`gamehub_landing_page_2/code.html`）与 **Aetheria**（`gaming_landing/code.html`）；需将上述目录一并提交到 GitHub，再在 **Streamlit Community Cloud** 部署。详见下文各节。

The page is ready for static hosting as a single HTML file (Tailwind + fonts load from CDNs). A copy named **`index.html`** lives in the **`publish/`** folder so hosts that expect a default document work without extra configuration.

---

## What was added in this repo

| Path | Purpose |
|------|--------|
| `publish/index.html` | Same content as `code.html`; use this folder as the **site root** when uploading or deploying. |

---

## Permanent hosting (recommended)

Anyone with the link can open the site; choose one provider and keep the project connected to your account.

### 1. Netlify Drop (fastest, no CLI)

1. Zip the **`publish`** folder (the zip should contain `index.html` at the **top level**, not inside a nested `publish` folder—on macOS: open `publish`, select `index.html`, compress, or zip so extracting gives `index.html` directly).
2. Go to [Netlify Drop](https://app.netlify.com/drop) and drag the zip or the folder.
3. Netlify assigns a URL like `https://random-name.netlify.app`; you can rename the site under **Site settings → Domain management**.

### 2. GitHub Pages

1. Create a new repository on GitHub and push this project (or only the `publish` folder contents).
2. In the repo: **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**, branch `main`, folder **`/publish`** (or **`/ (root)`** if you pushed only the contents of `publish`).
4. The site will be at `https://<username>.github.io/<repo>/` (or the root domain if you used a `username.github.io` repo with files at root).

### 3. Cloudflare Pages

1. Sign in to [Cloudflare Dashboard](https://dash.cloudflare.com/) → **Workers & Pages** → **Create** → **Pages** → **Upload assets**.
2. Upload the **`publish`** folder (or a zip of it).
3. Assign a `*.pages.dev` hostname or your own domain.

### 4. Streamlit (two landing pages)

**`streamlit_app.py`** embeds whichever HTML you pick in the **sidebar**:

- **GameHub — Web3 funding** → `gamehub_landing_page_2/code.html`
- **Aetheria — gaming landing** → `gaming_landing/code.html`

Tailwind CDN + fonts still load over the network inside the iframe.

**Local:**

```bash
cd /path/to/stitch_gamehub_landing_page
python3 -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the URL Streamlit prints (usually `http://localhost:8501`). Others on your LAN can use **Network URL** if you start with `streamlit run streamlit_app.py --server.address 0.0.0.0`.

**Public (Streamlit Community Cloud):**

1. Put the project in a **GitHub** repository (include `streamlit_app.py`, `requirements.txt`, `gamehub_landing_page_2/code.html`, and **`gaming_landing/code.html`**).
2. Sign in at [Streamlit Community Cloud](https://streamlit.io/cloud), **New app**, pick the repo, main file **`streamlit_app.py`**, deploy.
3. You get a stable `https://*.streamlit.app` link for sharing.

### 5. Vercel / other CLIs (if you use Node.js)

From the machine where `npm`/`npx` is installed:

```bash
cd gamehub_landing_page_2/publish
npx vercel --prod
```

Follow the login prompt once; you get a permanent `*.vercel.app` URL.

---

## Quick temporary link (demo only)

To share with someone **for a short test** without signing up, you can expose your local `publish` folder with **Cloudflare Quick Tunnel** (URL changes each run; tunnel stops when you close the terminal).

Requirements: `python3`, and the `cloudflared` binary ([releases](https://github.com/cloudflare/cloudflared/releases)).

```bash
cd gamehub_landing_page_2/publish
python3 -m http.server 8765 &
cloudflared tunnel --url http://127.0.0.1:8765
```

Copy the `https://….trycloudflare.com` URL from the log. Stop with `Ctrl+C` on `cloudflared`, then `fg` and `Ctrl+C` on the server, or:

```bash
pkill -f "http.server 8765"
pkill -f "cloudflared tunnel"
```

**Do not rely on this for production**—no uptime guarantee and the link is not stable.

---

## Checklist after deploy

- Open the live URL on a phone or another network to confirm it loads.
- External assets (Tailwind CDN, Google Fonts, Material Symbols) need **internet access** for visitors; no change required for normal hosting.
