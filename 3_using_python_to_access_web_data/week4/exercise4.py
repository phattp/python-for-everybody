from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
numlist = []

for tag in tags:
    results = re.findall('[0-9]+', str(tag))
    
    if not results: continue

    for result in results:
        num = int(result)
        numlist.append(num)

sum_num = sum(numlist)
print(sum_num)
