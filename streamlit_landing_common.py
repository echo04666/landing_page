"""Shared helpers for single-page Streamlit HTML embeds."""
from __future__ import annotations

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).resolve().parent

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


def run_landing(*, html_path: Path, iframe_height: int, page_title: str) -> None:
    st.set_page_config(
        page_title=page_title,
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(HIDE_CHROME, unsafe_allow_html=True)

    if not html_path.is_file():
        st.error(f"Missing HTML: `{html_path}`")
        st.stop()

    html = html_path.read_text(encoding="utf-8")
    components.html(html, width=None, height=iframe_height, scrolling=True)
