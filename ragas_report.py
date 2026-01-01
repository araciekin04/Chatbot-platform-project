import os
import time
import pandas as pd
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import _faithfulness, _context_recall
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings # HuggingFace için bunu ekledik
from rag_pdf import create_pdf_rag

# 1. MODELLERİ HAZIRLA
# Değerlendirici zeka (Gemini)
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

# Embedding modeli (PDF'i okurken kullandığın HuggingFace modelinin aynısı olmalı!)
# EĞER MODEL İSMİN FARKLIYSA BURAYI DEĞİŞTİR:
hf_model_name = "sentence-transformers/all-MiniLM-L6-v2" 
hf_embeddings = HuggingFaceEmbeddings(model_name=hf_model_name)

# 2. RAG SİSTEMİNİ ÇALIŞTIR VE VERİ TOPLA
pdf_qa = create_pdf_rag("EA_bilgilendirme.pdf")

questions = [
    "Üyelik tipleri nelerdir?",
    "Standart üyelik ücreti kaç TL?",
    "Premium üyelikte kaç ekran var?",
    "Kullanılmış olan üyelik süresi için ücret iadesi yapılır mı?",
    "Ücret iadesi hangi durumlarda yapılır?"
]

# BURASI ÖNEMLİ: Manuel olarak gerçek cevapları ekliyoruz ki Recall 0 çıkmasın
ground_truths = [
    "Üyelik tipleri Standart Üyelik, Plus Üyelik ve Premium Üyelik.",
    "Standart üyelik ücreti aylık 70 TL'dir.", # PDF'indeki gerçek rakamı yaz
    "Premium üyelikte aynı anda 4 ekran izlenebilir.", # PDF'indeki gerçek rakamı yaz
    "Hayır. Kullanılmış üyelik süresi için herhangi bir ücret iadesi yapılmaz.",
    "Sistemsel hata durumunda ücret iadesi yapılır."
]

data = []
print("PDF'ten yanıtlar çekiliyor...")

for i, q in enumerate(questions):
    result = pdf_qa.invoke({"query": q})
    
    data.append({
        "question": q,
        "answer": result["result"],
        "contexts": [doc.page_content for doc in result["source_documents"]],
        "ground_truth": ground_truths[i] # Gerçek cevapları buradan alıyor
    })
    time.sleep(2) # Kota dostu bekleme

dataset = Dataset.from_list(data)

# 3. DEĞERLENDİRME (EVALUATE)
print("Ragas değerlendirmesi başladı...")
results = evaluate(
    dataset=dataset,
    metrics=[_faithfulness, _context_recall],
    llm=gemini_llm,
    embeddings=hf_embeddings # Gemini yerine HuggingFace verdik!
)

# 4. RAPORLAMA
print("\n--- TEST SONUÇLARI ---")
print(results)

# Sonuçları Excel'e kaydetmek istersen:
results.to_pandas().to_excel("ragas_raporu.xlsx")