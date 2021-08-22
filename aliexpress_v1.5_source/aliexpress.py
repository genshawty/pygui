#!/usr/bin/python3
# -*- coding: utf-8 -*-



import requests, time, random, os, pickle, datetime, urllib3, subprocess, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from discord_hooks import Webhook
from pypresence import Presence
from selenium.common.exceptions import TimeoutException

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_id():
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    return current_machine_id

RPC = Presence("822626345514303529")
RPC.connect()
RPC.update(
    state="Version 1.5",
    details="Aliexpress Bot",
    large_image="scpple",
    start=time.time()
)

license_key_not_found = False

try:
    with open('license_key.txt', 'r') as lickey:
        lickey1 = lickey.readlines()
        license_key = lickey1[0]
except:
    license_key_not_found = True
    license_key = input("Enter License Key: ")

def check_license_key():
    headers = {
    'Content-type': 'application/json'
    }

    data = {
        "key": license_key,
        "device": get_id(),
        "id": "604a002dd52644b19441776d",
    }

    r = requests.post('https://api.cactusweb.io/api/v1/devices', headers=headers, json=data)
    if r.status_code == 400:
        print("[log] Invalid License Key")
        time.sleep(1)
        sys.exit()
    elif r.status_code == 202:
        print("[log] The license key is successfully linked to your discord")
        time.sleep(2)
        if license_key_not_found == True:
            write_key = open('license_key.txt', 'a')
            write_key.write(license_key)
        os.system('cls')
    elif r.status_code == 200:
        print("[log] Successful login")
        time.sleep(1)
        if license_key_not_found == True:
            write_key = open('license_key.txt', 'a')
            write_key.write(license_key)
        os.system('cls')
        
check_license_key()

class Aliexpress:
    def __init__(self):
        print("Если вы используете софт первый раз, сгенирировать cookie файл можно через aliexpress_cookie_gen")
        self.cookie_name = input("Введите название полученного cookie файла: ")
        self.after_auth()    
    
    def read_webhook(self):
        with open('webhook.txt', 'r') as webhook:
            webhook1 = webhook.read().strip()
        return webhook1
        
    def after_auth(self):
        ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36']
        options1 = Options()
        options1.add_argument('headless')
        options1.add_argument("--log-level=3")
        options1.add_argument(f"user-agent={random.choice(ua)}")
        options1.add_experimental_option("excludeSwitches", ["enable-automation"])
        options1.add_experimental_option('useAutomationExtension', False)
        self.driver1 = webdriver.Chrome(options=options1)
        driver1 = self.driver1
        driver1.set_page_load_timeout(15)
        driver1.get('https://aliexpress.ru/')
        os.system('cls')
        time.sleep(1)
        with open(self.cookie_name + '.pkl', 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver1.add_cookie(cookie)
        os.system('cls')
        self.link = input("Введите ссылку на товар: ")
        a = 0
        while a != 1:
            try:
                driver1.get(self.link)
                a = 1
            except TimeoutException:
                try:
                    driver1.get(self.link)
                    a = 1
                except:
                    pass
        try:
            self.name = driver1.find_element_by_xpath('//*[@id="#content"]/div[1]/h1').text
        except:
            try:
                self.name = driver1.find_element_by_xpath('//*[@id="#content"]/div[2]/h1').text
            except:
                self.name = 'None'
        try:
            self.price = driver1.find_element_by_xpath('//*[@id="#content"]/div[4]/span[1]').text
        except:
            try:
                self.price = driver1.find_element_by_xpath('//*[@id="#content"]/div[3]/span[1]').text
            except:
                self.price = 'None'
        self.add_to_cart()
    
    def add_to_cart(self):
        driver1 = self.driver1
        while driver1.current_url.split('/')[2] != 'shoppingcart.aliexpress.ru':
            try:
                driver1.find_elements_by_class_name('sku-property-image')[0].click()
            except:
                try:    
                    driver1.find_elements_by_class_name('sku-property-image')[1].click()
                except:
                    try:
                        driver1.find_elements_by_class_name('sku-property-image')[2].click()
                    except:
                        pass
            print('['  + datetime.datetime.today().strftime("%H:%M:%S") + ']' + '[log] Waiting Product')
            try:
                driver1.find_element_by_xpath('//*[@id="#content"]/div[4]/div[2]/div[1]').click()
            except:
                driver1.refresh()
            driver1.execute_script("window.scrollTo(0, 1080)") 
            try:
                driver1.find_element_by_xpath("//*[contains(text(), 'Купить сейчас')]").click()
                self.start_time = time.time()
            except:
                pass
        else:
            print('['  + datetime.datetime.today().strftime("%H:%M:%S") + ']' + "[log] Add To Cart")
            m = 0
            
            while driver1.current_url.split('/')[4] == 'confirm_order.htm':
                try:
                    driver1.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/div[1]').click()
                except:
                    pass
                print('['  + datetime.datetime.today().strftime("%H:%M:%S") + ']' + 'Time to Refresh --->  ' +  str(m))
                m += 1
                if m >= 50:
                    print('['  + datetime.datetime.today().strftime("%H:%M:%S") + ']' + "Refresh!")
                    driver1.refresh()
                    time.sleep(0.6)
                    if m == 90:
                        print('['  + datetime.datetime.today().strftime("%H:%M:%S") + ']' + "Going back to add to cart")
                        a = 0
                        while a != 1:
                            try:
                                driver1.get(self.link)
                                a = 1
                            except TimeoutException:
                                try:
                                    driver1.get(self.link)
                                    a = 1
                                except:
                                    pass
                        self.add_to_cart()
                        
                try:
                    driver1.find_element_by_xpath('//*[@id="checkout-button"]').click()
                except:
                    pass
            else:
                print('['  + datetime.datetime.today().strftime("%H:%M:%S") + ']' + "[log] Checkouting...")
                self.send_webhook()
        
    def send_webhook(self):
        driver1 = self.driver1
        chk_time = round((time.time() - self.start_time), 2)
        embed1 = Webhook(self.read_webhook(), color=0x6dff1f)
        embed1.set_title(title="Success :white_check_mark: :white_check_mark: ")  
        embed1.add_field(name='Product Name', value=str(self.name), inline=True)
        embed1.add_field(name='Price', value=str(self.price), inline=False)
        embed1.add_field(name='Checkout Time', value=str(chk_time) + 's', inline=False)
        embed1.set_thumbnail(url='https://china-southnorth-01.oss-cn-zhangjiakou.aliyuncs.com/intl-social-service/26/374/20201110/dc6eeb81a38d43eabf64554b7c9baa07-helphub-1604994208746-rc-upload-1604993963070-17')
        embed1.add_field(name='Site', value='[Aliexpress](https://aliexpress.ru/)', inline=False)
        embed1.set_footer(text='Software Cripple', ts=True)   
        embed1.post()
        time.sleep(8)
        driver1.close()
    
Aliexpress()