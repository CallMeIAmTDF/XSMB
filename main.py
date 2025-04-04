# https://xoso.com.vn/xsmb-03-04-2025.html
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=10000,10000")
data = {}
brower = webdriver.Chrome()
flag = False
for nam in range(2024, 2026):
    if flag:
        break
    for thang in range(1, 12):
        if flag:
            break
        for ngay in range(1, 31):
            if nam == 2025 and thang >= 4 and ngay >= 5:
                flag = True
                break
            brower.implicitly_wait(5)
            try:
                brower.get(
                    f"https://xoso.com.vn/xsmb-{f'0{ngay}' if ngay < 10 else f'{ngay}'}-{f'0{thang}' if thang < 10 else f'{thang}'}-{nam}.html")
                kq = brower.execute_script("""
                const prices = document.querySelectorAll('[class*="prize"]');
                const xsmb_data = {};
                G2 = [];
                G3 = [];
                G4 = [];
                G5 = [];
                G6 = [];
                G7 = [];
                for(i = 2; i < prices.length; i++){
                    if(i == 2) xsmb_data["DB"] = prices[i].textContent;
                    if(i == 3) xsmb_data["G1"] = prices[i].textContent;
                    if(i == 4 || i == 5) G2.push(prices[i].textContent);
                    if(i >= 6 && i <= 11) G3.push(prices[i].textContent);
                    if(i >= 12 && i <= 15) G4.push(prices[i].textContent);
                    if(i >= 16 && i <= 21) G5.push(prices[i].textContent);
                    if(i >= 22 && i <= 24) G6.push(prices[i].textContent);
                    if(i >= 25 && i <= 28) G7.push(prices[i].textContent);
                }
                xsmb_data["G2"] = G2;
                xsmb_data["G3"] = G3;
                xsmb_data["G4"] = G4;
                xsmb_data["G5"] = G5;
                xsmb_data["G6"] = G6;
                xsmb_data["G7"] = G7;
                if (G2.length == 0){
                    return null;
                }
                return xsmb_data;
                """)
                # print(nam, thang, nam, kq)
                if kq:
                    data[f'xsmb-{ngay}-{thang}-{nam}'] = kq
            except:
                pass

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
