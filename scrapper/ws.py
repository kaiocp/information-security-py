from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

#temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

#print(soup.title.string)

#print(soup.a)

#print(soup.p.string)

#print(soup.find('admin'))





