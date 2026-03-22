"""
GameHub landing only — deploy this app on Streamlit Cloud for URL #1.
HTML: gamehub_landing_page_2/code.html
"""
from streamlit_landing_common import BASE, run_landing

run_landing(
    html_path=BASE / "gamehub_landing_page_2" / "code.html",
    iframe_height=5600,
    page_title="GameHub | The Neon Frontier of Web3 Gaming",
)
