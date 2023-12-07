from sklearn.linear_model import LinearRegression
import streamlit as st 
import pandas as pd
import joblib
model = LinearRegression()
with open("linear_regression_model.pkl", "rb") as file:
  model = joblib.load(file) 
# Tahmin fonksiyonunu tanımlayın
def predict_price(model, df):
    try:
        prediction = model.predict(df)
        return prediction[0]
    except AttributeError:
        st.error("Modeliniz 'predict' fonksiyonuna sahip değil. Lütfen doğru model tipini kullanarak eğittiğinizden emin olun.")
        return None
st.title("İlcelere göre otel fiyatları")
st.write("secmis oldugunuz özellikler icin otel fiyatı")
konum_dict = {'adalar': 0,
  'aksaray': 1,
  'altunizade mahallesi': 2,
  'arnavutköy': 3,
  'asmalı mescit': 4,
  'asmalımescit': 5,
  'ataköy': 6,
  'ataköy marina': 7,
  'atasehir': 8,
  'ataşehir': 9,
  'avcılar': 10,
  'ağva': 11,
  'bagcilar': 12,
  'bahcelievler': 13,
  'bahçelievler': 14,
  'bakırköy': 15,
  'bayrampaşa': 16,
  'bağcılar': 17,
  'başakşehir': 18,
  'beyazıt': 19,
  'beykoz': 20,
  'beylerbeyi': 21,
  'beylikdüzü': 22,
  'beyoglu': 23,
  'beyoğlu': 24,
  'beşiktaş': 25,
  'bomonti': 26,
  'bostancı': 27,
  'büyükada': 28,
  'büyükçekmece': 29,
  'caferağa': 30,
  'cankurtaran': 31,
  'cağaloğlu': 32,
  'cevizli mahallesi': 33,
  'cihangir': 34,
  'dudullu osb': 35,
  'esenler-bayrampaşa': 36,
  'esentepe': 37,
  'esenyurt': 38,
  'etiler': 39,
  'eyüp': 40,
  'fatih': 41,
  'fulya': 42,
  'galata': 43,
  'gayrettepe': 44,
  'gaziosmanpaşa': 45,
  'gungoren': 46,
  'gümüşsuyu': 47,
  'halkalı': 48,
  'harbiye': 49,
  'i̇stanbul': 50,
  'i̇stanbul aksaray': 51,
  'i̇stanbul anadolu yakası': 52,
  'i̇stanbul bahçelievler': 53,
  'i̇stanbul boğazı': 54,
  'i̇stanbul sütlüce': 55,
  'i̇çerenköy': 56,
  'kadıköy': 57,
  'kanlıca mahallesi': 58,
  'karaköy': 59,
  'karaköy-haliç': 60,
  'kartal': 61,
  'kartal-pendik': 62,
  'kavacık mahallesi': 63,
  'kayabaşı mahallesi': 64,
  'kaynarca': 65,
  'kayışdağı': 66,
  'kazlıçeşme': 67,
  'kağıthane': 68,
  'kumburgaz': 69,
  'kumkapı': 70,
  'kurtköy': 71,
  'küçükbakkalköy': 72,
  'küçükçekmece': 73,
  'laleli': 74,
  'levent': 75,
  'maltepe': 76,
  'maslak': 77,
  'mecidiyeköy': 78,
  'merter': 79,
  'moda': 80,
  'nişantaşı': 81,
  'ortaköy': 82,
  'osmanbey': 83,
  'pendik': 84,
  'rasimpaşa': 85,
  'sanayi mahallesi': 86,
  'sancaktepe': 87,
  'sarıyer': 88,
  'silivri': 89,
  'sirkeci': 90,
  'suadiye': 91,
  'sultanahmet': 92,
  'sultanahmet-sirkeci': 93,
  'taksim': 94,
  'tarabya': 95,
  'tophane': 96,
  'topkapı': 97,
  'tuzla': 98,
  'yenibosna': 99,
  'yeşilköy': 100,
  'yıldız': 101,
  'zeytinburnu': 102,
  'çağlayan mahallesi': 103,
  'ümraniye': 104,
  'üsküdar': 105,
  'şile': 106,
  'şirinevler mahallesi': 107,
  'şişli': 108}
konum = konum_dict[st.sidebar.selectbox("konum",konum_dict.keys())]
secenek_dict = {'açık büfe kahvaltı': 0,
  'her sabah kahve/hamur işi ürünler': 1,
  'izole oda kahvaltı': 2,
  'oda kahvaltı': 3,
  'sadece oda': 4,
  'ücretsiz akşam yemeği': 5}
secenek = secenek_dict[st.sidebar.selectbox("secenek",secenek_dict.keys())]
sayi_girdisi = st.sidebar.number_input("Kişi Sayısı", value=1)
gece_girdisi = st.sidebar.number_input("Gece Sayısı", value=1)
features = {'konum':konum,'secenek':secenek}
features_df = pd.DataFrame([features])
st.table(features_df)
st.write(f"Kişi sayısı: {sayi_girdisi}")
st.write(f"Gece sayısı: {gece_girdisi}")
if st.button("tahmin et"):
   pred = predict_price(model, features_df.values)
   pred = pred*sayi_girdisi*gece_girdisi
   st.write(f"Tahmin edilen deger:{pred} ")





