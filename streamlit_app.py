"""
Serves the GameHub static landing page inside Streamlit (for local run or Streamlit Community Cloud).
Source of truth: gamehub_landing_page_2/code.html
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).resolve().parent
HTML_PATH = BASE / "gamehub_landing_page_2" / "code.html"

st.set_page_config(
    page_title="GameHub | The Neon Frontier of Web3 Gaming",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)

if not HTML_PATH.is_file():
    st.error(f"Missing landing HTML: `{HTML_PATH}`")
    st.stop()

html = HTML_PATH.read_text(encoding="utf-8")
# Full document in iframe; tall viewport so hero + footer scroll inside the embed.
components.html(html, width=None, height=5600, scrolling=True)
