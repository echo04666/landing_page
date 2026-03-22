"""
Serves static landing pages inside Streamlit (local or Streamlit Community Cloud).
Sources: gamehub_landing_page_2/code.html, gaming_landing/code.html
"""
from __future__ import annotations

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).resolve().parent

# label -> (html path, iframe height px)
LANDINGS: dict[str, tuple[Path, int]] = {
    "GameHub — Web3 funding": (BASE / "gamehub_landing_page_2" / "code.html", 5600),
    "Aetheria — gaming landing": (BASE / "gaming_landing" / "code.html", 7000),
}

HIDE_CHROME = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: 100% !important;
    }
</style>
"""

st.set_page_config(
    page_title="GameHub & Aetheria Landings",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(HIDE_CHROME, unsafe_allow_html=True)

st.sidebar.markdown("### Landing page")
choice = st.sidebar.radio(
    "Select page",
    list(LANDINGS.keys()),
    label_visibility="collapsed",
)

path, height = LANDINGS[choice]

if not path.is_file():
    st.error(f"Missing HTML: `{path}`")
    st.stop()

html = path.read_text(encoding="utf-8")
components.html(html, width=None, height=height, scrolling=True)
