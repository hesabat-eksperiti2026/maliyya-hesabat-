import streamlit as st
import pandas as pd

# Geniş ekran rejimi (bütün səhifəni əhatə edir)
st.set_page_config(page_title="Büdcə Paneli", layout="wide", page_icon="💰")

# CSS - Tam genişlik və sıfır xəta dizaynı
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #ffffff; }
    [data-testid="stMetricValue"] { font-size: 1.8rem !important; }
    .stNumberInput div div input { font-weight: bold; font-size: 1.1rem; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    hr { margin: 10px 0px; }
    </style>
    """, unsafe_allow_html=True)

if 'real_xercler' not in st.session_state:
    st.session_state.real_xercler = []

MAAS = 3000
QAYNANA_KOMEY = 50

st.title("💰 Ailə Büdcə Paneli (2026)")

tab1, tab2 = st.tabs(["📊 MAAŞ PLANI", "💸 XƏRCLƏRİ QEYD ET"])

with tab1:
    col1, col2 = st.columns(2)
    
    def input_row(label, val_default, key_id):
        c_label, c_val = st.columns([3, 2])
        c_label.markdown(f"<div style='padding-top:10px;'><b>{label}</b></div>", unsafe_allow_html=True)
        # format="%d" yalnız tam rəqəmləri göstərir
        val = c_val.number_input("", value=int(val_default), step=1, format="%d", key=f"v_{key_id}", label_visibility="collapsed")
        return val

    with col1:
        st.subheader("📌 Sabit xərclər")
        v1 = input_row("Kredit", 650, 1)
        v2 = input_row("Komunal", 150, 2)
        v3 = input_row("Şaxnuz maaş", 700, 3)
        v4 = input_row("Borc (Qaynana)", 150, 4)
        v5 = input_row("Böyük bazarlıq", 400, 5)
        v6 = input_row("Gündəlik bazarlıq", 100, 6)
        v7 = input_row("Arslan bazarlıq (Similac/Pam)", 210, 7)
        v8 = input_row("Ehtiyat pul (Zapas)", 150, 8)

    with col2:
        st.subheader("🔄 Dəyişən xərclər")
        v9 = input_row("Restoran/Mcd", 100, 9)
        v10 = input_row("Toyuq yem", 40, 10)
        v11 = input_row("Ət (1 aydan bir)", 110, 11)
        v12 = input_row("Benzin", 50, 12)
        v13 = input_row("Temu", 50, 13)
        v14 = input_row("Baxım (Fərdi)", 50, 14)
        v15 = input_row("Usta/Təmir", 30, 15)
        
        st.write("---")
        # Həkim seçimi (Aktiv/Deaktiv)
        hekim_check = st.checkbox("🏥 Həkim/Əməliyyat xərci var?", value=True)
        if hekim_check:
            v_hekim = st.number_input("Həkim məbləği", value=400, step=1, format="%d")
        else:
            v_hekim = 0
            
        st.write("---")
        istirahet = st.select_slider("**🎡 İstirahət (Rayon)**", options=[0, 150, 300, 450], value=300)

    # Hesablama
    total_plan = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v_hekim+istirahet
    final_zapas = MAAS - total_plan + QAYNANA_KOMEY

    st.markdown("---")
    res_col1, res_col2, res_col3 = st.columns([1, 1, 2])
    res_col1.metric("Ümumi Plan", f"{total_plan} AZN")
    res_col2.metric("Qalan Pul", f"{final_zapas} AZN")

    # MƏSLƏHƏTÇİ HİSSƏSİ
    with res_col3:
        st.markdown("### 💡 Büdcə Analizi")
        if final_zapas < 0:
            st.error(f"⚠️ KƏSİR VAR: {abs(final_zapas)} AZN çatışmır!")
            st.write("👉 **Məsləhət:** İstirahət büdcəsini 150-yə endirin və ya Temu/Restoran xərcini azaldın.")
        elif final_zapas < 100:
            st.warning("⚠️ Büdcə çox sıxdır. Beklənilməz bir xərc olsa, borc almalı olacaqsınız.")
            st.write("👉 **Məsləhət:** 'Ehtiyat pul'u artırmaq üçün dəyişən xərclərdən birini azaldın.")
        else:
            st.success(f"✅ Plan düzgündür. Ay sonuna {final_zapas} AZN zapasınız qalır.")
            st.write("👉 **Məsləhət:** Bu pulu Xalidə xanımdakı borcun üstünə qoya bilərsiniz.")

with tab2:
    st.subheader("💸 Xərcləri İzlə")
    
    cats = ["Kredit", "Komunal", "Şaxnuz maaş", "Borc", "Böyük bazarlıq", "Gündəlik bazarlıq", 
            "Arslan bazarlıq", "Ehtiyat pul", "Restoran", "İstirahət", "Həkim", "Toyuq yem", 
            "Ət", "Benzin", "Temu", "Baxım", "Usta", "Digər"]
    
    c1, c2, c3 = st.columns([2, 1, 1])
    sel_cat = c1.selectbox("Kateqoriya", cats)
    # Burada da format="%d" istifadə olundu
    sel_val = c2.number_input("Xərclənən", value=0, step=1, format="%d")
    add_btn = c3.button("➕ Əlavə et", use_container_width=True)

    if add_btn and sel_val > 0:
        st.session_state.real_xercler.append({"Kateqoriya": sel_cat, "Məbləğ": int(sel_val)})
        st.rerun()

    st.markdown("---")
    
    if st.session_state.real_xercler:
        df = pd.DataFrame(st.session_state.real_xercler)
        total_spent = df["Məbləğ"].sum()
        
        m1, m2 = st.columns(2)
        m1.metric("Cəmi Xərclənib", f"{total_spent} AZN")
        m2.metric("Maaşdan Qalan", f"{MAAS - total_spent} AZN")
        
        # Cədvəldə tam rəqəmləri göstərmək üçün stil
        st.table(df)
        
        if st.button("Siyahını Təmizlə (Yeni ay üçün)"):
            st.session_state.real_xercler = []
            st.rerun()
    else:
        st.info("Hələ xərc qeyd edilməyib. Xərclədikcə bura yazın.")
