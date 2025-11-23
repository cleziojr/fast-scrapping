import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.cnnbrasil.com.br/")
soup = BeautifulSoup(r.text, "html.parser")

item_principal = soup.select("figcaption.flex.w-full.flex-col.items-stretch.gap-2.text-wrap")[0].find("h2")
print("Título:", item_principal.get_text(strip=True))