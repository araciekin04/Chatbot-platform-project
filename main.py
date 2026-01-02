from intent_classifier import detect_intent
from rag_pdf import create_pdf_rag
from data_agent import create_data_agent

pdf_qa = create_pdf_rag("EA_bilgilendirme.pdf")
data_agent = create_data_agent("diziler.csv")

DATA_INTENTS = {
    "dizi_analizi",
    "karsilastirma",
    "istatistik"
}

print("🎓 Hibrit RAG + Data Agent Sistem")
print("Çıkmak için 'exit'\n")

while True:
    question = input("❓ Soru: ")
    if question.lower() == "exit":
        break

    intent = detect_intent(question)
    print(f"🔍 Intent: {intent}")

    turkish_question = question + " (Lütfen bu soruyu TÜRKÇE cevapla ve döküman dışına çıkma.)"

    try:
        if intent in DATA_INTENTS:
            # Data Agent kısmı
            result = data_agent.invoke({"input": turkish_question})
            
            output = result['output'] if isinstance(result, dict) else result
            print(f"✅ Cevap: {output}\n")
        else:
            # RAG PDF tarafı
            result = pdf_qa.invoke({"query": turkish_question})
            output = result['result'] if isinstance(result, dict) else result
            print(f"✅ Cevap: {output}\n")
    except Exception as e:
        print(f"⚠️ Bir hata oluştu, lütfen tekrar dene.")