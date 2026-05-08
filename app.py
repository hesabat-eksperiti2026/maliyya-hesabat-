import streamlit as st
import pandas as pd

st.set_page_config(page_title="Büdcə Paneli", layout="wide", page_icon="💰")

# Müasir və Rəngli CSS Dizaynı
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {
        background: linear-gradient(to right, #ece9e6, #ffffff);
    }
    .main-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stButton>button {
        border-radius: 20px;
        font-weight: bold;
        transition: 0.3s;
    }
    /* Əlavə et düyməsi - Yaşıl */
    div.stButton > button:first-child {
        background-color: #28a745;
        color: white;
        border: none;
    }
    /* Təmizlə düyməsi - Qırmızı */
    [data-testid="stBaseButton-secondary"] {
        background-color: #dc3545 !important;
        color: white !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #f1f3f5;
        padding: 10px;
        border-radius: 15px;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

if 'real_xercler' not in st.session_state:
    st.session_state.real_xercler = []

MAAS = 3000
QAYNANA_KOMEY = 50

st.markdown("<h1 style='text-align: center; color: #2c3e50;'>💎 Ailə Maliyyə Paneli</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📊 MAAŞ PLANI", "💸 XƏRCLƏRİ QEYD ET"])

with tab1:
    col1, col2 = st.columns(2)
    
    def input_row(label, val_default, key_id):
        c_label, c_val = st.columns([3, 2])
        c_label.markdown(f"<div style='padding-top:10px; color: #495057;'><b>{label}</b></div>", unsafe_allow_html=True)
        val = c_val.number_input("", value=int(val_default), step=1, format="%d", key=f"v_{key_id}", label_visibility="collapsed")
        return val

    with col1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("📌 Sabit Xərclər")
        v1 = input_row("Kredit", 650, 1)
        v2 = input_row("Komunal", 150, 2)
        v3 = input_row("Şaxnuz maaş", 700, 3)
        v4 = input_row("Borc (Qaynana)", 150, 4)
        v5 = input_row("Böyük bazarlıq", 400, 5)
        v6 = input_row("Gündəlik bazarlıq", 100, 6)
        v7 = input_row("Arslan bazarlıq", 210, 7)
        v8 = input_row("Ehtiyat pul (Zapas)", 150, 8)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("🔄 Dəyişən Xərclər")
        v9 = input_row("Restoran/Mcd", 100, 9)
        v10 = input_row("Toyuq yem", 40, 10)
        v11 = input_row("Ət (1 aydan bir)", 110, 11)
        v12 = input_row("Benzin", 50, 12)
        v13 = input_row("Temu", 50, 13)
        v14 = input_row("Baxım (Fərdi)", 50, 14)
        v15 = input_row("Usta/Təmir", 30, 15)
        
        st.markdown("---")
        hekim_check = st.checkbox("🏥 Həkim/Əməliyyat xərci var?", value=True)
        v_hekim = st.number_input("Həkim məbləği", value=400, step=1, format="%d") if hekim_check else 0
        
        istirahet = st.select_slider("**🎡 İstirahət (Rayon)**", options=[0, 150, 300, 450], value=300)
        st.markdown("</div>", unsafe_allow_html=True)

    # Hesablama
    total_plan = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v_hekim+istirahet
    final_zapas = MAAS - total_plan + QAYNANA_KOMEY

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    res_col1, res_col2, res_col3 = st.columns([1, 1, 2])
    res_col1.metric("Ümumi Plan", f"{total_plan} AZN")
    res_col2.metric("Qalan Pul", f"{final_zapas} AZN")

    with res_col3:
        st.markdown("### 💡 Büdcə Analizi")
        if final_zapas < 0:
            st.error(f"⚠️ Kəsiri bağlamaq üçün {abs(final_zapas)} AZN azaltmalısan!")
        else:
            st.success(f"✅ Plan əladır. {final_zapas} AZN artıq qalır.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.subheader("💸 Real Xərcləri İzlə")
    
    cats = ["Kredit", "Komunal", "Şaxnuz maaş", "Borc", "Böyük bazarlıq", "Gündəlik bazarlıq", 
            "Arslan bazarlıq", "Ehtiyat pul", "Restoran", "İstirahət", "Həkim", "Toyuq yem", 
            "Ət", "Benzin", "Temu", "Baxım", "Usta", "Digər"]
    
    # Xərc əlavə etmə paneli - Səliqəli düzülüş
    c1, c2, c3 = st.columns([3, 2, 1])
    sel_cat = c1.selectbox("Kateqoriya seçin", cats)
    sel_val = c2.number_input("Məbləği yazın", value=0, step=1, format="%d")
    add_btn = c3.button("➕ Əlavə Et", use_container_width=True)

    if add_btn and sel_val > 0:
        st.session_state.real_xercler.append({"Kateqoriya": sel_cat, "Məbləğ": int(sel_val)})
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.real_xercler:
        df = pd.DataFrame(st.session_state.real_xercler)
        total_spent = df["Məbləğ"].sum()
        
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        m1, m2 = st.columns(2)
        m1.metric("Cəmi Xərclənib", f"{total_spent} AZN")
        m2.metric("Maaşdan Qalan", f"{MAAS - total_spent} AZN", delta_color="normal")
        
        st.write("### 📝 Tarixçə")
        st.table(df)
        
        if st.button("🗑️ Siyahını Sıfırla"):
            st.session_state.real_xercler = []
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
