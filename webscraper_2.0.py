from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run_forever_like_Forrest():
    

    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    f = open('output '+moment+'.csv', 'w')

    headers="LATER OI (CALL),CHANGE IN OI (CALL),LTP (CALL),NET CHANGE (CALL),STRIKE PRICE,NET CHANGE (PUT),LTP (PUT),CHANGE IN OI (PUT),LATER OI (PUT),\n"
    f.write(headers)


    chrome_path = r"D:\Work\Yash\Webscraper 2.0\chromedriver.exe"

    driver = webdriver.Chrome(chrome_path)

    driver.get("https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp")

    t_id = driver.find_element(By.ID, 'octable')

    tbody = t_id.find_element_by_tag_name('tbody')

    rows = tbody.find_elements(By.TAG_NAME, "tr")

    no_of_rows = len(rows) 
    
    x = 1
    for row in rows:
        if x !=no_of_rows:
            col1 = row.find_elements(By.TAG_NAME, "td")[1]
            col2 = row.find_elements(By.TAG_NAME, "td")[2]
            col3 = row.find_elements(By.TAG_NAME, "td")[5]
            col4 = row.find_elements(By.TAG_NAME, "td")[6]
            col5 = row.find_elements(By.TAG_NAME, "td")[11]
            col6 = row.find_elements(By.TAG_NAME, "td")[16]
            col7 = row.find_elements(By.TAG_NAME, "td")[17]
            col8 = row.find_elements(By.TAG_NAME, "td")[20]
            col9 = row.find_elements(By.TAG_NAME, "td")[21]
            f.write(col1.text.replace(",","")+","+col2.text.replace(",","")+","+col3.text.replace(",","")+","+col4.text.replace(",","")+","+col5.text.replace(",","")+","+col6.text.replace(",","")+","+col7.text.replace(",","")+","+col8.text.replace(",","")+","+col9.text.replace(",","")+","+"\n")
            x+=1

    f.close()

    time.sleep(900)


while True:
    run_forever_like_Forrest()
    
