# Chatbot-project
🤖 🤖 EA Dizi Platformu Chatbot
Bu proje, yapılandırılmamış PDF dökümanları ve yapılandırılmış CSV verileri üzerinde akıllı sorgulama yapabilen bir Retrieval-Augmented Generation (RAG) asistanıdır. Sistem, basit bir chatbotun ötesinde, kullanıcı niyetini analiz ederek doğru veri kaynağına yönlendirme yapan bir Multi-Agent (Çok Ajanlı) mimariye sahiptir.

🚀 Öne Çıkan Özellikler
Akıllı Niyet Sınıflandırma (Intent Classifier): Kullanıcı sorgusunu analiz ederek; genel sohbet, PDF döküman sorgusu veya veri analizi (CSV) arasında otomatik seçim yapar.

Gelişmiş RAG Motoru: PDF dökümanlarını anlamsal parçalara (chunk) bölerek, HuggingFace embedding modelleriyle yüksek doğruluklu arama yapar.

Veri Analiz Ajanı: data_agent.py ile CSV formatındaki tablolar üzerinde analizler gerçekleştirir ve kullanıcıya özet bilgiler sunar.

Doğrulanmış Yanıtlar: Sistemin performansı akademik Ragas framework'ü ile ölçülmüş ve halüsinasyon oranı minimuma indirilmiştir.

🧠 Sistem Mimarisi ve Akış



    A[Kullanıcı Sorusu] --> B{Intent Classifier}
    B -- "Genel Sohbet" --> C[Gemini 1.5 Flash]
    B -- "Döküman Sorgusu" --> D[RAG PDF Modülü]
    B -- "Veri Analizi" --> E[Data Agent CSV]
    
    D --> F[HuggingFace Embedding & Vektör Arama]
    F --> G[Bağlam/Context Getirme]
    G --> C
    
    E --> H[Pandas/Data Analysis]
    H --> C
    
    C --> I[Doğrulanmış Yanıt]
    I --> J[Ragas Değerlendirme]
    
Sistem, gelen her soruyu bir karar mekanizmasından geçirir:

Girdi Analizi: intent_classifier.py sorunun kapsamını belirler.

Yönlendirme: * Eğer soru dökümanla ilgiliyse -> rag_pdf.py devreye girer.

Eğer soru tablo verisiyse -> data_agent.py veriyi analiz eder.

Üretim: Google Gemini, gelen bağlamı (context) kullanarak yanıtı oluşturur.

📈 Performans Raporu (RAGAS)
Sistemin güvenilirliği, dökümana sadakat ve bilgi getirme başarısı üzerinden test edilmiştir:

Metrik	Skor	Açıklama
Faithfulness	1.00	Modelin döküman dışına çıkmadığını ve uydurma bilgi üretmediğini kanıtlar.
Context Recall	1.00	Aranan bilginin döküman içerisinde %100 başarıyla bulunduğunu gösterir.
🛠️ Kurulum ve Çalıştırma
Gereksinimleri Yükleyin:

```bash
# Bağımlılıkları yükleyin
pip install -r requirements2.txt
```
```bash
# API Anahtarını Ayarlayın: Kök dizinde bir .env dosyası oluşturun
GOOGLE_API_KEY=senin_api_anahtarin
```
```bash
# Uygulamayı başlatın
streamlit run app.py
```
# Proje dosya yapısı

```bash
📂 Proje Dosya Yapısı
.
├── app.py                  # Streamlit Kullanıcı Arayüzü
├── main.py                 # Karar Mekanizması & Router Mantığı
├── intent_classifier.py    # Niyet Sınıflandırıcı (Zeka Katmanı)
├── rag_pdf.py              # RAG Motoru & PDF İşleme (LangChain)
├── data_agent.py           # CSV Veri Analiz Ajansı
├── ragas_report.py         # Performans & Doğruluk Testleri (Validation)
├── EA_bilgilendirme.pdf     # Ana Bilgi Kaynağı (PDF)
├── diziler.csv              # Yapılandırılmış Veri Seti (CSV)
├── requirements2.txt       # Gerekli Kütüphaneler
├── .env                    # API Anahtarları (Gizli)
└── .gitignore              # GitHub Dışı Tutulacak Dosyalar