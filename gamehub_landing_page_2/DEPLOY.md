# Publishing the GameHub landing page

**中文摘要：** 若要用 **Streamlit** 且要 **两个不同公网链接**：在 Cloud 上建 **两个应用**，同一仓库、同一分支，主文件分别选 **`streamlit_app.py`**（GameHub）与 **`streamlit_gaming_landing.py`**（Aetheria / `gaming_landing`），会得到两个 **`*.streamlit.app`**。详见下文「Streamlit」一节。

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

### 4. Streamlit (two separate public URLs)

There are **two entry files** so you can run **two Streamlit Cloud apps** on the **same repo** and get **two different** `https://*.streamlit.app` links:

| Main file on Cloud | Page embedded |
|--------------------|---------------|
| **`streamlit_app.py`** | `gamehub_landing_page_2/code.html` (GameHub) |
| **`streamlit_gaming_landing.py`** | `gaming_landing/code.html` (Aetheria) |

Shared logic lives in **`streamlit_landing_common.py`** (do not pick this as the Cloud main file).

Tailwind CDN + fonts load over the network inside the iframe.

**Local:**

```bash
cd /path/to/stitch_gamehub_landing_page
pip install -r requirements.txt
streamlit run streamlit_app.py              # GameHub — http://localhost:8501
streamlit run streamlit_gaming_landing.py # Aetheria — use another port: --server.port 8502
```

**Public (Streamlit Community Cloud) — two apps:**

1. Repo must include `requirements.txt`, `streamlit_app.py`, `streamlit_gaming_landing.py`, `streamlit_landing_common.py`, `gamehub_landing_page_2/code.html`, and `gaming_landing/code.html`.
2. **First app:** **New app** → your repo → branch `main` → main file **`streamlit_app.py`** → choose subdomain A → **Deploy** → URL #1.
3. **Second app:** **New app** again → **same repo and branch** → main file **`streamlit_gaming_landing.py`** → choose subdomain B → **Deploy** → URL #2.

Existing deployments that pointed at `streamlit_app.py` keep working as the GameHub-only app.

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
