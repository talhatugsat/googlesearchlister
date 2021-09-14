import requests
from bs4 import BeautifulSoup
import time
from pyfiglet import Figlet
import subprocess, platform

f = Figlet(font='slant')
print (f.renderText('Leaver'))

google = input("Lütfen google adresini giriniz: ")
word = input("Lütfen aramak istediğiniz kelimeleri giriniz: ")
sayfa = input("Arama sonucunun kaç sayfasının listesinin çıkacağını giriniz: ")
dosyadi = input("Lütfen çıktı dosyasının adını giriniz: ")

urlfile = open(dosyadi + ".txt", "x")

sayi = 0
yazi = "Arama başlatılıyor."

if platform.system()=="Windows":
    subprocess.Popen("cls", shell=True).communicate()
else:
    print("\033c", end="")

print (f.renderText('Leaver'))
for i in range(1,4):
    yazi = yazi + "."
    print(yazi)
    time.sleep(0.2)

while True:
    page = requests.get(google + '/search?q=' + word + '&start=' + str(sayi), {"content-type":"text", "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36"})
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.findAll("a")
    for link in links:
        if (link["href"].find("google.com") == -1 and link["href"].find(".google.") == -1 and link["href"].find("/imgres?imgurl=") == -1 and (link["href"].find("https://") != -1 or link["href"].find("http://") != -1)):
            urlfile.write(link["href"].replace("/url?q=", "") + "\n")
    sayi = sayi + 10

    if sayi == (int(sayfa) * 10):
        break

print("İşlem bitti, 5 saniye sonra kapanıyor.")
time.sleep(5)
urlfile.close()