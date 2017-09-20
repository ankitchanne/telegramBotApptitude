from crawl import crawl,topics
import requests
from bs4 import BeautifulSoup


f = open('os.csv', 'w')
url = 'https://www.indiabix.com/computer-science/operating-systems-concepts/'
#crawl(url,f)
topics(url,f)
'''headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
req = requests.get(url,headers=headers)
soup = BeautifulSoup(req.content,'html.parser')
for div in soup.find_all(class_='div-topics-index'):
	for i in div.find_all('a'):
		link = "https://www.indiabix.com"+i['href']
		req = requests.get(link,headers=headers)
		soup2 = BeautifulSoup(req.content,headers=headers)	
for i in soup.find_all(class_='mx-pager-container'):
	for j in i.find_all('p'):
		for k in j.find_all('a'):
			if 'Next' in k.text:
				print k['href']'''