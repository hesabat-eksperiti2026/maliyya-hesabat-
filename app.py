import streamlit as st
import pandas as pd

st.set_page_config(page_title="Büdcə Paneli", layout="wide", page_icon="💰")

# Müasir Dizayn və Böyüdülmüş Tablar
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {
        background: linear-gradient(to right, #f4f7f6, #ffffff);
    }
    /* Tabları böyütmək və ortaya almaq */
    .stTabs [data-baseweb="tab-list"] {
        gap: 30px;
        display: flex;
        justify-content: center;
        background-color: #2c3e50;
        padding: 15px;
        border-radius: 50px;
        margin: 0 auto 30px auto;
        width: 60%;
    }
    .stTabs [data-baseweb="tab"] {
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        height: 50px !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3498db !important;
        border-radius: 30px;
    }
    .main-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    /* Düymə üslubu */
    div.stButton > button {
        background-color: #27ae60 !important;
        color: white !important;
        border-radius: 10px !important;
        height: 45px !important;
        margin-top: 28px !important; /* Mətnlə eyni səviyyəyə gətirmək üçün */
    }
    .stMetric {
        border: 1px solid #eee;
        padding: 15px;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'real_xercler' not in st.session_state:
    st.session_state.real_xercler = []

MAAS = 3000
QAYNANA_KOMEY = 50

st.markdown("<h1 style='text-align: center; color: #2c3e50; font-size: 45px;'>💎 Ailə Maliyyə Paneli</h1>", unsafe_allow_html=True)

# TABLARIN YARADILMASI
tab1, tab2 = st.tabs(["📊 MAAŞ PLANI", "💸 XƏRCLƏRİ QEYD ET"])

with tab1:
    col1,
