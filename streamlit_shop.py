"""
GameHub merch / shop landing only — deploy on Streamlit Cloud for a third public URL.
HTML: shop/code.html
"""
from streamlit_landing_common import BASE, run_landing

run_landing(
    html_path=BASE / "shop" / "code.html",
    iframe_height=6000,
    page_title="GameHub Official Merch Store | Web3 Integrated Gaming Gear",
)
