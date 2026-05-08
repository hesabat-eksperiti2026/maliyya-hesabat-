# maliyya-hesabat-import streamlit as st

st.set_page_config(page_title="Maliyyə Analizi", page_icon="📊")
st.title("📊 Aylıq Maliyyə Planlaması")

gelir = 3000
st.info(f"Ümumi Aylıq Büdcə: {gelir} AZN")

with st.sidebar:
    st.header("📌 Sabit Öhdəliklər")
    kredit = st.number_input("Maliyyə öhdəliyi 1", value=650)
    komunal = st.number_input("Kommunal xərclər", value=150)
    aile_ayirma = st.number_input("Ailə daxili ayırmalar", value=700)
    diger_ohdelik = st.number_input("Digər öhdəliklər", value=150)
    meiset_taminat = st.number_input("Məişət təminatı", value=300)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🛒 İstehlak")
    bazarlig = st.number_input("Əsas alış-veriş", value=500)
    nagliyyat = st.number_input("Nəqliyyat/Rabitə", value=90)
with col2:
    st.subheader("🏥 Sağlamlıq/Baxım")
    saglamliq = st.number_input("Tibbi xərclər", value=400)
    ferdi_baxim = st.number_input("Fərdi baxım", value=50)

st.divider()
asude_vaxt = st.slider("🎡 Asudə vaxt büdcəsi", 0, 500, 100)

cemi = (kredit + komunal + aile_ayirma + diger_ohdelik + meiset_taminat + 
        bazarlig + nagliyyat + saglamliq + ferdi_baxim + asude_vaxt)
qalan = gelir - cemi

if qalan < 0:
    st.error(f"⚠️ Limit keçilib: {abs(qalan)} AZN")
else:
    st.success(f"✅ Sərbəst qalıq: {qalan} AZN")
    st.metric("Gündəlik limit", f"{(qalan + bazarlig)/30:.2f} AZN")
