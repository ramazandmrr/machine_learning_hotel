from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
driver = webdriver.Edge()  # Edge tarayıcısı için webdriver kullanın
file = open("data.csv", "w", encoding="utf-8")
file.close()

driver.get("https://www.enuygun.com/otel/istanbul-1639/search/?checkInDate=18.12.2023&checkOutDate=19.12.2023&roomDetail=1&country=TR&p=search&ref=homepage&requestId=216388024c01b469e70756&funnelId=242409851021b469e70756")

time.sleep(8)

data_list = []

for i in range(1, 800):
    otel_path = f"/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[3]/div[{i}]/div/div[1]/div[2]/div[1]/h4"   
    konum_path = f"/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[3]/div[{i}]/div[1]/div[1]/div[2]/div[1]/p[1]/button/div"
    secenek_path = f"/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[3]/div[{i}]/div/div[1]/div[2]/div[1]/div[1]/span"
    fiyat_path = f"/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[3]/div[{i}]/div[1]/div[1]/div[2]/div[2]/div[2]/p[2]/span[2]"
    try:       
        otel_name = driver.find_element(By.XPATH, otel_path).text
        konum_name = driver.find_element(By.XPATH, konum_path).text
        secenek_name = driver.find_element(By.XPATH, secenek_path).text
        fiyat_name = driver.find_element(By.XPATH, fiyat_path).text
        
        ilk_cumle = konum_name.split(',')[0].strip() 
        
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight-1500)")
        time.sleep(0.25)
        
        data_list.append([otel_name,ilk_cumle,secenek_name,fiyat_name])
        print(otel_name,ilk_cumle,secenek_name,fiyat_name)                    

    except Exception as e:
        print(f"{i}. veri alınırken hata oluştu: {e}")

df = pd.DataFrame(data_list,columns=["Otel","Konum","Secenek","Fiyat"])
df.to_csv("data.csv",index=False,encoding="utf-8")

driver.quit()
