#!/usr/bin/env python3

import os
import time
import subprocess as sb
from urllib.request import urlopen
import requests    
def clear_screen():
    sb.call("clear")

def get_public_ip():
    response = urlopen("http://ipinfo.io")
    data = response.read().decode("utf-8")
    country_line = [line for line in data.split("\n") if "country" in line][0]
    country = country_line.split(":")[1].strip()
    return country

def download_vpn_source(url, destination):
    os.system(f"wget {url} -P {destination}")
    zip_file_name = url.split("/")[-1]
    zip_file_path = os.path.join(destination, zip_file_name)
    os.system(f"unzip {zip_file_path} -d {os.path.join(destination, 'unzips')}")



def passwordCheck():
    url = "https://www.vpnbook.com/password.php?t=0.94148700%201693642130"
    response = requests.get(url)
    file_name= "passwd.jpg"
    # İsteğin içeriğini dosyaya yaz
    with open(file_name, "wb") as file:
        file.write(response.content)



def connect_to_vpn(vpn_files_path):
    vpn_files = [file for file in os.listdir(vpn_files_path) if file.endswith(".ovpn")]
    for vpn_file in vpn_files:
        vpn_file_path = os.path.join(vpn_files_path, vpn_file)
        os.system(f"openvpn {vpn_file_path}")
        time.sleep(2)
        os.system("clear")
        sonip = get_public_ip()
        if basip != sonip:
            break
        else:
            print("Bağlanamadı, diğer vpn dosyaları deneniyor...")
            time.sleep(1)
            continue

if __name__ == "__main__":
    print("vpneasy başlatılıyor")
    print("sadece vpnbook ile senkronize çalışır")
    
    time.sleep(1)

    vpn_files_path = os.path.join(os.environ["HOME"], "vpneasy")
    basip = get_public_ip()

    if os.path.exists(vpn_files_path):
        print("geçmiş temizleniyor")
        os.system(f"rm -rf {vpn_files_path}")
    else:
        print("Kurulum yapılıyor...")
    
    os.makedirs(vpn_files_path)
    os.makedirs(os.path.join(vpn_files_path, "source"))
    os.makedirs(os.path.join(vpn_files_path, "password"))
    
    download_vpn_source("https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-pl226.zip", os.path.join(vpn_files_path, "source"))
    os.system("clear")
    passwordCheck()
    os.system("open passwd.jpg")
    print("username = vpnbook")
    
    print("Kurulum tamamlandı..")
    print("Lütfen ülke seçimi yapın")

    countries = ["Poland", "Germany", "USA", "Canada", "France"]
    for idx, country in enumerate(countries, start=1):
        print(f"{idx}-) {country}")
    
    while True:
        choice = input("Ülke seçiminizi yapın: ")
        if choice.isdigit() and 1 <= int(choice) <= len(countries):
            selected_country = countries[int(choice) - 1]
            if selected_country == "Poland":
                download_vpn_source("https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-pl226.zip", os.path.join(vpn_files_path, "source"))
            elif selected_country == "Germany":
                download_vpn_source("https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-de4.zip", os.path.join(vpn_files_path, "source"))
            elif selected_country == "USA":
                download_vpn_source("https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-us1.zip", os.path.join(vpn_files_path, "source"))
            elif selected_country == "Canada":
                download_vpn_source("https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-ca222.zip", os.path.join(vpn_files_path, "source"))
            elif selected_country == "France":
                download_vpn_source("https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-fr1.zip", os.path.join(vpn_files_path, "source"))
            connect_to_vpn(os.path.join(vpn_files_path, "source", "unzips"))
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")
