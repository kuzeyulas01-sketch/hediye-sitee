import streamlit as st
import os

# Sayfa Ayarları ve Kalp İkonu
st.set_page_config(page_title="Sana Özel Kelime Kartları", page_icon="❤️", layout="centered")

# 🔐 GÜVENLİK VE GİRİŞ KONTROLÜ
DOGRU_KULLANICI = "ecomelo"
DOGRU_SIFRE = "ivandor"

if "giris_yapildi" not in st.session_state:
    st.session_state["giris_yapildi"] = False

if not st.session_state["giris_yapildi"]:
    st.title("🔒 Özel Kelime Kartları")
    st.write("Bu siteye sadece yetkili kişiler erişebilir. Lütfen giriş yap:")
    kullanici_adi = st.text_input("Kullanıcı Adı:")
    sifre = st.text_input("Şifre:", type="password")
    if st.button("Giriş Yap 🚀", use_container_width=True):
        if kullanici_adi == DOGRU_KULLANICI and sifre == DOGRU_SIFRE:
            st.session_state["giris_yapildi"] = True
            st.rerun()
        else:
            st.error("Hatalı kullanıcı adı veya şifre! ❌")
    st.stop()

# ---------------------------------------------------------------------
# 📚 TXT DOSYASINDAN KELİMELERİ OTOMATİK OKUYAN SİSTEM
# ---------------------------------------------------------------------
KELIMELER = []

# Dosya okuma hatasını önlemek için daha güvenli bir yöntem
if os.path.exists("kelimeler.txt"):
    with open("kelimeler.txt", "r", encoding="utf-8", errors="ignore") as f:
        for satir in f:
            satir_temiz = satir.strip()
            if not satir_temiz:  # Boş satırları atla
                continue
            if " - " in satir_temiz:
                parcalar = satir_temiz.split(" - ", 1)
                ing = parcalar[0].strip()
                tr = parcalar[1].strip()
                KELIMELER.append({"ing": ing, "tr": tr})

# ⚙️ ARAYÜZ TASARIMI
st.title("🇬🇧 Kelime Öğrenme Kartlarım 🇹🇷")
st.write("Sana özel hazırladığım kelime kartlarına tıklayarak anlamlarını görebilirsin. ✨")

# Çıkış Yap Butonu
col_baslik, col_cikis = st.columns([4, 1])
with col_cikis:
    if st.button("Çıkış Yap 🚪"):
        st.session_state["giris_yapildi"] = False
        st.rerun()

st.divider()

# Eğer kelimeler yüklenemediyse ekranda uyarı göster (Sorunu anlamak için)
if not KELIMELER:
    st.error("⚠️ kelimeler.txt dosyasından kelimeler okunamadı! Lütfen dosyanın içinde kelimelerin 'kelime - anlamı' şeklinde yazıldığından emin ol.")
else:
    st.subheader(f"📚 Toplam {len(KELIMELER)} Kelime Kartın Var")

    # Kart Arama Çubuğu
    arama = st.text_input("🔍 Kelime Ara (İngilizce):", placeholder="Aramak istediğin kelimeyi yaz...")

    # Kartları Listeleme Alanı
    for index, kart in enumerate(KELIMELER):
        if arama.lower() not in kart['ing'].lower():
            continue
            
        with st.expander(f"📦 {kart['ing'].upper()}", expanded=False):
            st.markdown(f"### Anlamı:")
            st.info(f"💡 {kart['tr']}")
            st.write("---")
            st.caption("❤️ *Bu kelimeyi öğrendiysen bir sonraki karta geçebilirsin!*")
