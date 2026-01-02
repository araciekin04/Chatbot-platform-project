import streamlit as st
from intent_classifier import detect_intent
from rag_pdf import create_pdf_rag
from data_agent import create_data_agent

# ---------- SAYFA AYARLARI ----------
st.set_page_config(
    page_title="🎬EA Dizi Platformu Chatbot",
    page_icon="🎬​",
    layout="centered"
)

# ---------- BAŞLIK ----------
st.title("🎬​EA Dizi Platformu Chatbot🎬​")
st.write("**Üyelik Bilgileri** veya **Diziler** hakkında soru sor!")

# ---------- SİSTEMLERİ YÜKLE ----------
@st.cache_resource
def load_systems():
    pdf_qa = create_pdf_rag("EA_bilgilendirme.pdf")
    data_agent = create_data_agent("diziler.csv")
    return pdf_qa, data_agent

pdf_qa, data_agent = load_systems()

# ---------- DATA INTENTS ----------
DATA_INTENTS = {
    "dizi_analizi",
    "karsilastirma",
    "istatistik"
}


# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("ℹ️ Nasıl Çalışır?")
    
    st.subheader("Üyelik Soruları")
    st.info("• EA Dizi platformunun ücretleri nelerdir?\n• İade koşulları nelerdir?\n• Premium üyelik avantajları nelerdir?")    
    st.subheader("Dizi Soruları")
    st.info("• En yüksek puanlı diziler hangileridir?\n• Hangi tür diziler mevcuttur?\n• En çok sezonu olan dizi hangisidir?")    
    

# ---------- CHAT INTERFACE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Geçmiş mesajları göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı inputu
if prompt := st.chat_input("Sorunuzu yazın..."):
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Bot cevabı
    with st.chat_message("assistant"):
        with st.spinner("Analiz ediliyor..."):
            try:
                # Intent tespit et
                intent = detect_intent(prompt)
                
                # Intent'e göre yönlendir
                if intent in DATA_INTENTS:
                    # Veri analizi sistemi
                    
                    result = data_agent.invoke({"input": prompt})
                    answer = result['output']
                else:
                    # PDF RAG sistemi
                    result = pdf_qa.invoke({"query": prompt})
                    answer = result['result']
                
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
            except Exception as e:
                error_msg = f"❌ Bir hata oluştu: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Clear chat button
if st.sidebar.button("🗑️ Sohbeti Temizle"):
    st.session_state.messages = []
    st.rerun()