import streamlit as st

# Səhifə parametrləri və GitHub elementlərinin gizlədilməsi
st.set_page_config(page_title="Bizim Büdcə", layout="wide", page_icon="🏦")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #f8f9fa; }
    div.stButton > button { width: 100%; border-radius: 10px; height: 3em; background-color: #007bff; color: white; }
    .metric-container { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🏦 Ailə Maliyyə Paneli (22 May Maaş Dövrü)")

# Əsas Gəlir
MAAS = 3000

# Tablar: Planlama və İzləmə
tab1, tab2 = st.tabs(["📅 Maaş Bölgüsü (Plan)", "💸 Xərcləri İzlə (Real)"])

with tab1:
    st.header("📊 May Ayı Üçün Plan")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🏠 Məcburi")
        kredit_label = st.text_input("Etiket 1", "Kredit")
        kredit_val = st.number_input(f"{kredit_label}", value=650)
        
        komunal_label = st.text_input("Etiket 2", "Komunal (Öz + Xalidə x.)")
        komunal_val = st.number_input(f"{komunal_label}", value=150)
        st.caption("ℹ️ Xalidə xanım 50 AZN komunal üçün geri verir.")

        borc_label = st.text_input("Etiket 3", "Xalidə x. Borc/Zapas")
        borc_val = st.number_input(f"{borc_label}", value=150)

    with col2:
        st.subheader("👨‍👩‍👧‍👦 Ailə")
        yoldas_label = st.text_input("Etiket 4", "Şaxnuz (Maaş/Baxım)")
        yoldas_val = st.number_input(f"{yoldas_label}", value=700)

        usaq_label = st.text_input("Etiket 5", "Uşaq (Similac/Pampers)")
        # 3 Similac (135) + 3 Pampers (75) = 210
        usaq_val = st.number_input(f"{usaq_label}", value=210)
        
        toyuq_label = st.text_input("Etiket 6", "Toyuqların dəni (Anamgil)")
        toyuq_val = st.number_input(f"{toyuq_label}", value=40)

    with col3:
        st.subheader("🚗 Gündəlik")
        bazarlig_label = st.text_input("Etiket 7", "Böyük Bazarlıq")
        bazarlig_val = st.number_input(f"{bazarlig_label}", value=400)

        benzin_label = st.text_input("Etiket 8", "Benzin")
        benzin_val = st.number_input(f"{benzin_label}", value=50)

        restoran_label = st.text_input("Etiket 9", "Restoran/Mcd")
        restoran_val = st.number_input(f"{restoran_label}", value=150)

    st.divider()
    
    col_extra1, col_extra2 = st.columns(2)
    with col_extra1:
        hekim_check = st.checkbox("Bu ay Həkim/Əməliyyat xərci var?", value=True)
        hekim_val = st.number_input("Həkim məbləği", value=400) if hekim_check else 0
    
    with col_extra2:
        istirahet_val = st.select_slider("Rayon İstirahəti Planı", options=[0, 150, 300, 450], value=300)

    # Planın Hesablanması
    toplam_plan = kredit_val + komunal_val + borc_val + yoldas_val + usaq_val + toyuq_val + bazarlig_val + benzin_val + restoran_val + hekim_val + istirahet_val
    qalan_plan = MAAS - toplam_plan + 50 # 50 AZN qaynana köməyi daxil

    st.subheader(f"💰 Plan Sonu Qalan Zapas: {qalan_plan} AZN")
    if qalan_plan < 0:
        st.error(f"⚠️ Plan kəsirdədir! {abs(qalan_plan)} AZN çatışmır. İstirahət və ya Restoranı azaldın.")
    else:
        st.success("✅ Bu planla ayı rahat bağlamaq olar.")

with tab2:
    st.header("🛒 Xərclədikcə Bura Yazın")
    st.info("Maaşı alandan sonra xərclədiyiniz hər manatı bura əlavə edin, toplamdan çıxılsın.")
    
    col_real1, col_real2 = st.columns(2)
    
    with col_real1:
        xerc_edilib = st.number_input("Bu günə qədər cəmi nə qədər xərcləmisiniz?", value=0.0, step=10.0)
        st.caption("Məsələn: Bazarlıq (400) + Benzin (20) = 420 yazın.")
        
    with col_real2:
        elave_gelir = st.number_input("Gözlənilməz əlavə gəlir?", value=0.0)

    # Real vəziyyət hesabı
    real_balans = MAAS - xerc_edilib + elave_gelir
    
    st.divider()
    st.metric(label="Cibinizdə Qalan Pul", value=f"{real_balans} AZN", delta=f"-{xerc_edilib} Xərc")

    if real_balans < 500:
        st.warning("⚠️ Diqqət: Pulunuz 500 AZN-dən aşağı düşdü. Xalidə xaladan borc almalı ola bilərsiniz!")
    
    # Günlük limit hesabı (Maaşın bitməsinə qalan günə görə - May 22-dən İyun 22-yə)
    st.write("### 📅 Günlük Limit Analizi")
    days_left = st.slider("Ayın bitməsinə neçə gün qalıb?", 1, 30, 15)
    daily_limit = real_balans / days_left
    st.write(f"Gündəlik maksimum **{daily_limit:.2f} AZN** xərcləyə bilərsiniz.")
