import streamlit as st
import pandas as pd
import plotly.express as px

# Geniş və Müasir Konfiqurasiya
st.set_page_config(page_title="Maliyyə Pro", layout="wide", page_icon="💎")

# Finex Referanslı Premium CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f4f7fa;
    }
    
    #MainMenu, footer, header {visibility: hidden !important;}
    .stDeployButton {display:none !important;}

    /* Kart Dizaynı */
    .finance-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #eef2f6;
        margin-bottom: 20px;
    }

    /* Tabları Finex stilinə gətiririk */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        justify-content: center;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: white;
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 10px 30px;
        font-weight: 600;
        transition: 0.3s;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0061ff !important;
        color: white !important;
        border: none;
    }

    /* Metriklər */
    [data-testid="stMetric"] {
        background: #ffffff;
        border-radius: 15px;
        padding: 15px;
        border-left: 5px solid #0061ff;
    }
    
    /* Düymə */
    .stButton>button {
        background: linear-gradient(135deg, #0061ff 0%, #60efff 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 15px;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 4px 15px rgba(0,97,255,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# Məlumatın saxlanılması
if 'real_xercler' not in st.session_state:
    st.session_state.real_xercler = []

# Sabitlər
MAAS = 3000
QAYNANA_KOMEY = 50
BUTUN_GELIR = MAAS + QAYNANA_KOMEY

st.markdown("<h1 style='text-align: center; color: #1e293b;'>📊 Personal Finance Analytics</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b;'>2026 May Dövrü Üçün Ağıllı Büdcə İdarəetməsi</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💎 STRATEJİ PLAN", "💸 CANLI İZLƏMƏ", "📈 ANALİTİKA"])

with tab1:
    c1, c2 = st.columns([1, 1], gap="large")
    
    with c1:
        st.markdown("<div class='finance-card'>", unsafe_allow_html=True)
        st.subheader("📌 Əsas Öhdəliklər")
        v1 = st.number_input("💳 Kredit", value=650, step=50, format="%d")
        v2 = st.number_input("🔌 Kommunal", value=150, step=10, format="%d")
        v3 = st.number_input("👩‍💼 Şaxnuz (Maaş)", value=700, step=50, format="%d")
        v4 = st.number_input("🤝 Borc/Ehtiyat", value=150, step=50, format="%d")
        v5 = st.number_input("🛒 Böyük Bazarlıq", value=400, step=20, format="%d")
        v6 = st.number_input("👶 Arslan (Qida/Bezi)", value=210, step=10, format="%d")
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='finance-card'>", unsafe_allow_html=True)
        st.subheader("🔄 Dəyişən və İstirahət")
        v7 = st.slider("🎡 İstirahət (Rayon)", 0, 600, 300, step=50)
        v8 = st.number_input("🍔 Restoran/Əyləncə", value=100, step=10, format="%d")
        v9 = st.number_input("⛽ Benzin", value=50, step=10, format="%d")
        v10 = st.number_input("📦 Temu/Online", value=50, step=10, format="%d")
        v11 = st.number_input("🥩 Ət təminatı", value=110, step=10, format="%d")
        
        hekim_check = st.toggle("🏥 Tibbi Xərc (Aktiv/Deaktiv)", value=True)
        v_hekim = st.number_input("Məbləğ", value=400, format="%d") if hekim_check else 0
        st.markdown("</div>", unsafe_allow_html=True)

    # Hesablama Paneli
    toplam_xerc = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v_hekim
    qalan_mebleg = BUTUN_GELIR - toplam_xerc

    col_res1, col_res2, col_res3 = st.columns(3)
    col_res1.metric("Ümumi Büdcə", f"{BUTUN_GELIR} AZN")
    col_res2.metric("Planlanan Xərc", f"{toplam_xerc} AZN", delta=f"-{toplam_xerc}", delta_color="inverse")
    col_res3.metric("Net Qalıq", f"{qalan_mebleg} AZN")

with tab2:
    st.markdown("<div class='finance-card'>", unsafe_allow_html=True)
    st.subheader("📝 Yeni Xərc Qeydi")
    
    cats = ["Kredit", "Komunal", "Şaxnuz", "Borc", "Bazarlıq", "Arslan", "Restoran", "İstirahət", "Həkim", "Benzin", "Temu", "Ət", "Digər"]
    
    x_col1, x_col2, x_col3 = st.columns([2, 1, 1])
    secilen_cat = x_col1.selectbox("Kateqoriya", cats, label_visibility="collapsed")
    secilen_mebleg = x_col2.number_input("Məbləğ", value=0, step=1, format="%d", label_visibility="collapsed")
    if x_col3.button("➕ SİYAHIYA ƏLAVƏ ET"):
        if secilen_mebleg > 0:
            st.session_state.real_xercler.append({"Kateqoriya": secilen_cat, "Məbləğ": int(secilen_mebleg)})
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.real_xercler:
        df = pd.DataFrame(st.session_state.real_xercler)
        real_toplam = df["Məbləğ"].sum()
        
        st.write("### ⏱️ Canlı Balans")
        proqress = min(real_toplam / BUTUN_GELIR, 1.0)
        st.progress(proqress)
        
        m_col1, m_col2 = st.columns(2)
        m_col1.metric("İstifadə Edilib", f"{real_toplam} AZN")
        m_col2.metric("Cibdə Qalan", f"{BUTUN_GELIR - real_toplam} AZN")
        
        st.dataframe(df, use_container_width=True)
        if st.button("🗑️ AYI SIFIRLA"):
            st.session_state.real_xercler = []
            st.rerun()

with tab3:
    if st.session_state.real_xercler:
        st.markdown("<div class='finance-card'>", unsafe_allow_html=True)
        st.subheader("📊 Xərc Strukturu")
        fig = px.pie(df, values='Məbləğ', names='Kateqoriya', hole=.4, 
                     color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Gündəlik Limit Hesablayıcı
        st.markdown("<div class='finance-card'>", unsafe_allow_html=True)
        st.subheader("📅 Gündəlik Limit Analizi")
        gun = st.slider("Ayın bitməsinə neçə gün qalıb?", 1, 31, 15)
        limit = (BUTUN_GELIR - real_toplam) / gun
        st.info(f"Növbəti maaşa qədər günlük limitiniz: **{limit:.2f} AZN**")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Analiz üçün hələ ki məlumat yoxdur. Xərcləri qeyd etdikdən sonra bura baxın.")
