import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bizim Büdcə", layout="wide", page_icon="🏦")

# CSS - Dizaynı gözəlləşdiririk
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #f0f2f6; }
    .stNumberInput, .stTextInput { border: 2px solid #007bff; border-radius: 8px; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #ffffff; 
        border-radius: 10px 10px 0 0; 
        padding: 10px 20px;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.05);
    }
    .main-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #007bff;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏦 Ailə Büdcə İdarəetmə Paneli")

# Məlumatları yaddaşda saxlamaq üçün (Sayt yenilənənə qədər)
if 'real_xercler' not in st.session_state:
    st.session_state.real_xercler = []

MAAS = 3000
QAYNANA_KOMEY = 50

tab1, tab2 = st.tabs(["📅 MAAŞ PLANI", "💸 XƏRCLƏRİ QEYD ET"])

with tab1:
    st.info("Bu ay üçün nəzərdə tutulan xərcləri bura qeyd edin.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.subheader("📌 Sabit Ödənişlər")
        kr_name = st.text_input("Xərc adı 1", "Kredit")
        kr_val = st.number_input(f"{kr_name} Məbləği", value=650)
        
        km_name = st.text_input("Xərc adı 2", "Komunallar")
        km_val = st.number_input(f"{km_name} Məbləği", value=150)
        
        br_name = st.text_input("Xərc adı 3", "Xalidə x. Borc/Zapas")
        br_val = st.number_input(f"{br_name} Məbləği", value=150)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.subheader("🚗 Gündəlik")
        bz_name = st.text_input("Xərc adı 4", "Böyük Bazarlıq")
        bz_val = st.number_input(f"{bz_name} Məbləği", value=400)
        
        bn_name = st.text_input("Xərc adı 5", "Benzin")
        bn_val = st.number_input(f"{bn_name} Məbləği", value=50)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.subheader("👨‍👩‍👧 Ailə və Baxım")
        sh_name = st.text_input("Xərc adı 6", "Şaxnuz (Maaş)")
        sh_val = st.number_input(f"{sh_name} Məbləği", value=700)
        
        us_name = st.text_input("Xərc adı 7", "Uşaq (Qida/Bezi)")
        us_val = st.number_input(f"{us_name} Məbləği", value=210)
        
        ty_name = st.text_input("Xərc adı 8", "Toyuqların dəni")
        ty_val = st.number_input(f"{ty_name} Məbləği", value=40)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.subheader("🎡 Əlavə")
        hekim = st.number_input("Həkim/Əməliyyat", value=400)
        istirahet = st.slider("İstirahət Büdcəsi", 0, 500, 300)
        restoran = st.number_input("Restoran/Mcd", value=150)
        st.markdown('</div>', unsafe_allow_html=True)

    # Cəmi Hesablama
    total_plan = kr_val + km_val + br_val + bz_val + bn_val + sh_val + us_val + ty_val + hekim + istirahet + restoran
    final_zapas = MAAS - total_plan + QAYNANA_KOMEY

    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("Ümumi Planlanan Xərc", f"{total_plan} AZN")
    c2.metric("Sonda Qalan Zapas", f"{final_zapas} AZN")

with tab2:
    st.subheader("💸 Real Xərcləri İzlə")
    
    # Kateqoriya seçimi
    kateqoriya = st.selectbox("Xərc Kateqoriyası Seç", 
                             [kr_name, km_name, br_name, bz_name, bn_name, sh_name, us_name, ty_name, "Həkim", "Restoran", "İstirahət", "Digər"])
    
    məbləğ = st.number_input("Xərclənən Məbləğ (AZN)", min_value=0.0, step=1.0)
    
    if st.button("Xərci Siyahıya Əlavə Et"):
        st.session_state.real_xercler.append({"Kateqoriya": kateqoriya, "Məbləğ": məbləğ})
        st.toast(f"{kateqoriya} üçün {məbləğ} AZN əlavə edildi!")

    st.divider()
    
    if st.session_state.real_xercler:
        df = pd.DataFrame(st.session_state.real_xercler)
        total_real = df["Məbləğ"].sum()
        
        col_res1, col_res2 = st.columns(2)
        col_res1.metric("Cəmi Xərclənib", f"{total_real} AZN")
        col_res2.metric("Maaşdan Qalan", f"{MAAS - total_real} AZN")
        
        st.write("### 📝 Xərc Tarixçəsi")
        st.table(df)
        
        if st.button("Siyahını Təmizlə"):
            st.session_state.real_xercler = []
            st.rerun()
    else:
        st.info("Hələ ki heç bir xərc qeyd edilməyib.")
