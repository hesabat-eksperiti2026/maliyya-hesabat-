import streamlit as st
import pandas as pd

# Səhifə parametrləri
st.set_page_config(page_title="Büdcə Paneli", layout="wide", page_icon="💰")

# Mobil üçün xüsusi CSS və GitHub/Streamlit elementlərinin tam gizlədilməsi
st.markdown("""
    <style>
    /* GitHub və Streamlit menyularını hər yerdə gizlət */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display:none !important;}
    
    /* Arxa fon rəngi */
    .stApp {
        background: #f8f9fa;
    }

    /* Tabların mobil və veb üçün dizaynı */
    .stTabs [data-baseweb="tab-list"] {
        gap: 5px !important;
        display: flex !important;
        justify-content: center !important;
        background-color: #2c3e50 !important;
        padding: 8px !important;
        border-radius: 50px !important;
        margin: 0 auto 20px auto !important;
        width: 95% !important; /* Mobil üçün daha geniş */
        max-width: 500px !important;
    }

    .stTabs [data-baseweb="tab"] {
        color: white !important;
        font-size: 14px !important; /* Mobildə sığması üçün kiçildildi */
        font-weight: bold !important;
        height: 40px !important;
        padding: 0px 15px !important;
        border-radius: 25px !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: #3498db !important;
    }

    /* Kart dizaynı */
    .main-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }

    /* Rəqəm girişləri və düymələr */
    .stNumberInput input {
        font-size: 16px !important; /* Zoom olmaması üçün */
    }

    div.stButton > button {
        background-color: #27ae60 !important;
        color: white !important;
        border-radius: 8px !important;
        width: 100% !important;
        margin-top: 10px !important;
    }

    /* Metrik rəqəmlərini mobildə kiçiltmək */
    [data-testid="stMetricValue"] {
        font-size: 1.4rem !important;
    }
    
    /* Mobil üçün sütun tənzimləməsi */
    @media (max-width: 640px) {
        .stColumns {
            display: block !important;
        }
        .stColumn {
            width: 100% !important;
            margin-bottom: 10px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

if 'real_xercler' not in st.session_state:
    st.session_state.real_xercler = []

MAAS = 3000
QAYNANA_KOMEY = 50

st.markdown("<h2 style='text-align: center; color: #2c3e50; padding-bottom: 10px;'>💎 Ailə Büdcəsi</h2>", unsafe_allow_html=True)

# TABLAR
tab1, tab2 = st.tabs(["📊 PLAN", "💸 XƏRC"])

with tab1:
    col1, col2 = st.columns(2)
    
    def input_row(icon, label, val_default, key_id):
        c_label, c_val = st.columns([3, 2])
        c_label.markdown(f"<div style='padding-top:8px; font-size: 15px;'>{icon} {label}</div>", unsafe_allow_html=True)
        val = c_val.number_input("", value=int(val_default), step=1, format="%d", key=f"v_{key_id}", label_visibility="collapsed")
        return val

    with col1:
        st.markdown("<div class='main-card'><b>📌 Sabit</b>", unsafe_allow_html=True)
        v1 = input_row("💳", "Kredit", 650, 1)
        v2 = input_row("🔌", "Komunal", 150, 2)
        v3 = input_row("👩‍💼", "Şaxnuz", 700, 3)
        v4 = input_row("🤝", "Borc", 150, 4)
        v5 = input_row("🛒", "Böyük Baz.", 400, 5)
        v6 = input_row("👶", "Arslan", 210, 6)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='main-card'><b>🔄 Dəyişən</b>", unsafe_allow_html=True)
        v7 = input_row("🍔", "Restoran", 100, 7)
        v8 = input_row("⛽", "Benzin", 50, 8)
        v9 = input_row("📦", "Temu", 50, 9)
        v10 = input_row("🐥", "Toyuq", 40, 10)
        v11 = input_row("🥩", "Ət", 110, 11)
        v12 = input_row("🛡️", "Zapas", 150, 12)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    hekim_check = st.checkbox("🏥 Həkim xərci var?", value=True)
    v_hekim = st.number_input("Həkim məbləği", value=400, step=1, format="%d") if hekim_check else 0
    istirahet = st.select_slider("🎡 İstirahət", options=[0, 150, 300, 450], value=300)
    st.markdown("</div>", unsafe_allow_html=True)

    # Hesablama
    total_plan = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v_hekim+istirahet
    final_zapas = MAAS - total_plan + QAYNANA_KOMEY

    st.markdown("<div class='main-card' style='background-color: #2c3e50; color: white;'>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.metric("Toplam Plan", f"{total_plan} AZN")
    c2.metric("Qalan Zapas", f"{final_zapas} AZN")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.subheader("💸 Xərci Qeyd Et")
    
    cats = ["💳 Kredit", "🔌 Komunal", "👩‍💼 Şaxnuz", "🤝 Borc", "🛒 Böyük Baz.", "👶 Arslan", "🍔 Restoran", "🎡 İstirahət", "🏥 Həkim", "⛽ Benzin", "📦 Temu", "🐥 Toyuq", "🥩 Ət", "❓ Digər"]
    
    sel_cat = st.selectbox("Kateqoriya", cats)
    sel_val = st.number_input("Məbləğ (AZN)", value=0, step=1, format="%d")
    add_btn = st.button("➕ ƏLAVƏ ET")

    if add_btn and sel_val > 0:
        st.session_state.real_xercler.append({"Kat": sel_cat, "Məbləğ": int(sel_val)})
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.real_xercler:
        df = pd.DataFrame(st.session_state.real_xercler)
        total_spent = df["Məbləğ"].sum()
        
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.metric("Cəmi Xərclənib", f"{total_spent} AZN")
        st.metric("Maaşdan Qalan", f"{MAAS - total_spent} AZN")
        st.write("---")
        st.dataframe(df, use_container_width=True)
        if st.button("🗑️ Sıfırla"):
            st.session_state.real_xercler = []
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
