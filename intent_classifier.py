import re

INTENT_KEYWORDS = {
    "dizi_analizi": [
        "analiz", "ortalama", "istatistik",
        "en yüksek", "en yuksek", "en yksek",
        "en dusuk", "en düşük",
        "kaç tane", "kac tane", "sayisi", "sayısı", "toplam",
        "puan", "rating",
        "sezon", "bolum", "bölüm",
        "tur", "tür", "genre"
    ],

    "karsilastirma": [
        "karsilastir", "karşılaştır",
        "fark", "kiyas", "kıyas", "vs"
    ]
}

PDF_KEYWORDS = [
    "ucret", "ücret", "fiyat", "tl",
    "uyelik", "üyelik", "abonelik",
    "iptal", "iade",
    "premium", "plus", "standart",
    "ekran", "kullanim", "kullanım",
    "ea", "platform"
]


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def detect_intent(question: str) -> str:
    q = normalize(question)

    data_score = 0
    pdf_score = 0

    # DATA skorları
    for keywords in INTENT_KEYWORDS.values():
        for kw in keywords:
            if kw in q:
                data_score += 1

    # PDF skorları
    for kw in PDF_KEYWORDS:
        if kw in q:
            pdf_score += 1

    # 🔑 KARAR MANTIĞI
    if data_score > 0 and data_score >= pdf_score:
        # hangi data intent?
        scores = {}
        for intent, keywords in INTENT_KEYWORDS.items():
            scores[intent] = sum(1 for kw in keywords if kw in q)
        return max(scores, key=scores.get)

    return "pdf_soru"

