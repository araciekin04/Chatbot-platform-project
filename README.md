# Chatbot-project
🤖 PDF Soruları İçin Akıllı Asistan (RAG Chatbot)
Bu proje, elinizdeki PDF dosyalarını (şu an için bir bilgilendirme dökümanı) okuyan ve içindeki bilgilerle ilgili sorularınıza yanıt veren bir chatbot uygulamasıdır. Klasik chatbotlardan farkı, sadece genel bilgilerle değil, yüklediğiniz dökümana sadık kalarak cevap vermesidir.

🌟 Neler Yapabiliyor?
Niyetinizi Anlıyor: Sorduğunuz sorunun dökümanla mı ilgili yoksa genel bir sohbet mi olduğunu ayırt eder (intent_classifier.py).

PDF Analizi: Bilgileri PDF'ten çekerken "halüsinasyon" görmez, yani kafasından bir şeyler uydurmaz (rag_pdf.py).

Veri Analizi: Eğer döküman dışında tablolarınız (CSV) varsa onları da sorgulayabilir (data_agent.py).

Kendini Test Ediyor: Verdiği cevapların ne kadar doğru olduğunu bilimsel bir yöntemle ölçer ve raporlar (ragas_report.py).

📊 Test Sonuçlarım
Sistemi kurduktan sonra doğruluğunu ölçmek için Ragas kullandım ve aldığım sonuçlar şöyle:

Faithfulness (Sadakat): 1.0 / 1.0 (Model dökümana %100 sadık kalıyor).

Context Recall (Bilgi Bulma): 1.0 / 1.0 (Aranan bilgiyi döküman içinde %100 bulabiliyor).

🛠️ Nasıl Çalıştırılır?
Kütüphaneleri yükleyin: pip install -r requirements2.txt

.env dosyası oluşturup içine Google API Key'inizi yazın.

python main.py yazarak uygulamayı başlatın.

📁 Proje Yapısı
main.py: Uygulamanın giriş kapısı.

intent_classifier.py: Soruyu hangi modüle göndereceğini seçen zeka.

rag_pdf.py: PDF'i okuyan ve içinden bilgi cımbızlayan kısım.

data_agent.py: Tablolarla ilgilenen ajan.

ragas_report.py: Başarı oranını hesaplayan test dosyamız.