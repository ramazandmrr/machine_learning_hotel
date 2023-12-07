import re

def izmiri_cikar_ve_kaydet(girendata, cikandata):
    try:
        with open(girendata, 'r', encoding='utf-8') as file:
            veri = file.read()
        
        veri = veri.lower()
        veri = re.sub(r'\.', '', veri)
        # 'izmir' kelimesini kaldır
        veri_temiz = re.sub(r'\btl\b', '', veri)


        with open(cikandata, 'w', encoding='utf-8') as output_file:
            output_file.write(veri_temiz)

    except FileNotFoundError:
        print(f"{girendata} dosya bulunamadı...")

# Örnek kullanım
izmiri_cikar_ve_kaydet('data.csv', 'data.csv')
