import streamlit as st
import pandas as pd

st.set_page_config(page_title="Büdcə Paneli", layout="centered", page_icon="💰")

# CSS - Daha kompakt və təmiz görünüş
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp { background-color: #ffffff; }
    .compact-box {
        border: 1px solid #e6e9ef;
        padding: 15px;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin-bottom: 10px;
    }
    .stNumberInput div div input { font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

if 'real_xercler' not in st.session_state:
    st.session_state.real_xercler = []

MAAS = 3000
QAYNANA_KOMEY = 50

st.title("💰 Ailə Büdcə Paneli")

tab1, tab2 = st.tabs(["📊 MAAŞ PLANI", "💸 XƏRCLƏRİ QEYD ET"])

with tab1:
    col1, col2 = st.columns(2)
    
    def input_row(label_default, val_default, key_id):
        with st.container():
            c_label, c_val = st.columns([2, 1])
            name = c_label.text_input("Ad", label_default, key=f"n_{key_id}", label_visibility="collapsed")
            # format="%.0f" sıfırları (.00) yox edir
            val = c_val.number_input("Məbləğ", value=val_default, step=1, format="%d", key=f"v_{key_id}", label_visibility="collapsed")
            return val

    with col1:
        st.markdown("**📌 Sabit və Gündəlik**")
        v1 = input_row("Kredit", 650, 1)
        v2 = input_row("Komunallar", 150, 2)
        v3 = input_row("Xalidə x. Borc", 150, 3)
        v4 = input_row("Böyük Bazarlıq", 400, 4)
        v5 = input_row("Benzin", 50, 5)

    with col2:
        st.markdown("**👨‍👩‍👧 Ailə və Digər**")
        v6 = input_row("Şaxnuz (Maaş)", 700, 6)
        v7 = input_row("Uşaq (Qida/Bezi)", 210, 7)
        v8 = input_row("Toyuqların dəni", 40, 8)
        v9 = input_row("Həkim/Əməliyyat", 400, 9)
        v10 = input_row("Restoran/Mcd", 150, 10)

    st.markdown("---")
    istirahet = st.select_slider("**🎡 İstirahət Büdcəsi**", options=[0, 150, 300, 450], value=300)
    
    total_plan = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+istirahet
    final_zapas = MAAS - total_plan + QAYNANA_KOMEY

    res_col1, res_col2 = st.columns(2)
    res_col1.metric("Ümumi Plan", f"{total_plan} AZN")
    res_col2.metric("Qalan Zapas", f"{final_zapas} AZN")

with tab2:
    st.markdown("### 💸 Xərcləri İzlə")
    
    # Kateqoriya seçimi üçün cari adları götürürük
    cats = [st.session_state[f"n_{i}"] for i in range(1, 11)] + ["İstirahət", "Digər"]
    
    c1, c2, c3 = st.columns([2, 1, 1])
    sel_cat = c1.selectbox("Kateqoriya", cats, label_visibility="collapsed")
    sel_val = c2.number_input("Məbləğ", value=0, step=1, format="%d", label_visibility="collapsed")
    add_btn = c3.button("Əlavə et")

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
        
        st.table(df)
        
        if st.button("Siyahını Təmizlə"):
            st.session_state.real_xercler = []
            st.rerun()
    else:
        st.info("Hələ xərc qeyd edilməyib.")
