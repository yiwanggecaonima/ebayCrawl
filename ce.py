
from lxml import etree
import requests

link = 'https://www.ebay.com/sch/ATV-Side-by-Side-UTV-Parts-Accessories/43962/bn_562707/i.html?_fsrp=1'
response = requests.get(link,headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}).text

print(response)