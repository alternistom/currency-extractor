

# v.1.0 Initial 


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


print("                                                  __          ______                __             ")
print("  _______  _______________  ____  _______  __   _/ /___  _  _/_  __/________ ______/ /_____  _____")
print(" / ___/ / / / ___/ ___/ _ \/ __ \/ ___/ / / /  / __/ _ \| |/_// / / ___/ __ `/ ___/ __/ __ \/ ___/")
print("/ /__/ /_/ / /  / /  /  __/ / / / /__/ /_/ /  (_  )  __/>  < / / / /  / /_/ / /__/ /_/ /_/ / /    ")
print("\___/\__,_/_/  /_/   \___/_/ /_/\___/\__, /  /  _/\___/_/|_|/_/ /_/   \__,_/\___/\__/\____/_/     ")
print("                                    /____/   /_/                                                   ")
print(" v.1.0 by tamas.fabian@dealogic.com")
print("")
print(" last updated on:      Jan-16-2019")  
print(" initially created on: Jan-16-2019")                                                        
print("")


date = input("► Please input date in YYYY-MM-DD format: ")


base_url = "http://www.xe.com/currencytables/?from=USD&date="
my_url = base_url + str(date)
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("tbody")
container = containers[0]
rows = container.findAll("tr")
value = container.findAll("td", {"class":"historicalRateTable-rateHeader"})

eurName = rows[1].a.text
gbpName = rows[2].a.text
brlName = rows[22].a.text
chfName = rows[7].a.text
jpyName = rows[9].a.text
dkkName = rows[31].a.text
nokName = rows[28].a.text
sekName = rows[19].a.text
audName = rows[4].a.text
cadName = rows[5].a.text
hkdName = rows[15].a.text
zarName = rows[17].a.text
clpName = rows[39].a.text
inrName = rows[3].a.text
lacName = "LAC"
croName = "CRO"
myrName = rows[8].a.text
sgdName = rows[6].a.text
nzdName = rows[11].a.text
phpName = rows[18].a.text
idrName = rows[20].a.text
plnName = rows[34].a.text
arsName = rows[41].a.text
mxnName = rows[16].a.text
ronName = rows[53].a.text
czkName = rows[42].a.text
thbName = rows[12].a.text
hufName = rows[13].a.text
rubName = rows[30].a.text
usdName = "USD"

eurValue = value[3].text
gbpValue = value[5].text
brlValue = value[45].text
chfValue = value[15].text
jpyValue = value[19].text
dkkValue = value[63].text
nokValue = value[57].text
sekValue = value[39].text
audValue = value[9].text
cadValue = value[11].text
hkdValue = value[31].text
zarValue = value[35].text
clpValue = value[79].text
inrValue = value[7].text
lacValue = float(inrValue)*100000
croValue = float(inrValue)*10000000
myrValue = value[17].text
sgdValue = value[13].text
nzdValue = value[23].text
phpValue = value[37].text
idrValue = value[41].text
plnValue = value[69].text
arsValue = value[83].text
mxnValue = value[33].text
ronValue = value[107].text
czkValue = value[85].text
thbValue = value[25].text
hufValue = value[27].text
rubValue = value[61].text
usdValue = 1.0000000000

currencyName = [eurName, gbpName, brlName, chfName, jpyName, dkkName, nokName, sekName, audName, cadName, hkdName, zarName, clpName, inrName, lacName, croName, myrName, sgdName, nzdName, phpName, idrName, plnName, arsName, mxnName, ronName, czkName, thbName, hufName, rubName, usdName]
currencyValue = [eurValue, gbpValue, brlValue, chfValue, jpyValue, dkkValue, nokValue, sekValue, audValue, cadValue, hkdValue, zarValue, clpValue, inrValue, lacValue, croValue, myrValue, sgdValue, nzdValue, phpValue, idrValue, plnValue, arsValue, mxnValue, ronValue, czkValue, thbValue, hufValue, rubValue, usdValue]

#print(currencyName)
#print(currencyValue)

with open('Currencies_' + str(date) +'.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(currencyName, currencyValue))

print(str(f.name) + " was saved in the folder the Python script is located.")

print("    __                        ____               ")
print("   / /_  ____ __   _____     / __/_  ______      ")
print("  / __ \/ __ `/ | / / _ \   / /_/ / / / __ \     ")
print(" / / / / /_/ /| |/ /  __/  / __/ /_/ / / / /     ")
print("/_/ /_/\__,_/ |___/\___/  /_/  \__,_/_/ /_/      ")
print("         __                       _              ")
print("   _____/ /_____  _________ ___  (_)___  ____ _  ")
print("  / ___/ __/ __ \/ ___/ __ `__ \/ / __ \/ __ `/  ")
print(" (__  ) /_/ /_/ / /  / / / / / / / / / / /_/ /   ")
print("/____/\__/\____/_/  /_/ /_/ /_/_/_/ /_/\__, /    ")
print("   __  __                            _/__///     ")
print("  / /_/ /_  ___     _________ ______/ /_/ /__    ")
print(" / __/ __ \/ _ \   / ___/ __ `/ ___/ __/ / _ \   ")
print("/ /_/ / / /  __/  / /__/ /_/ (__  ) /_/ /  __/   ")
print("\__/_/ /_/\___/   \___/\__,_/____/\__/_/\___/    ")
print("                                                 ")