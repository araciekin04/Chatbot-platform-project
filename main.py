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

    if intent in DATA_INTENTS:
        result = data_agent.invoke({"input": question})
        print(f"✅ Cevap: {result['output']}\n")
    else:
        result = pdf_qa.invoke({"query": question})
        print(f"✅ Cevap: {result['result']}\n")
