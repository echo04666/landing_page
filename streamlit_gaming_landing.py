"""
Aetheria / gaming_landing only — deploy this app on Streamlit Cloud for URL #2.
HTML: gaming_landing/code.html
"""
from streamlit_landing_common import BASE, run_landing

run_landing(
    html_path=BASE / "gaming_landing" / "code.html",
    iframe_height=7000,
    page_title="Aetheria Studios | Community-Powered Web3 Gaming",
)
