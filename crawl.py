import requests
from bs4 import BeautifulSoup


def answerfor(qNo,arrayAnswers):
	limit = (qNo*4)-1
	start = limit -3
	#print len(array)
	#print type(limit)
	#print type(start)
	#print qNo, limit, start
	return arrayAnswers[start:limit+1]
	#for i in arrayAnswers[start:limit+1]:
		#print i
	#print "-------------"

def getQuestions(soup, arrayQuestions):
	for a in soup.find_all(class_='bix-td-qtxt'):
		arrayQuestions.append(a.text)

def getAnswers(soup, arrayAnswers):
	count = 1
	qNo = 0
	for b in soup.find_all(class_='bix-td-option'):
		qNo = qNo + 1
		if count%2 == 0:
			#print b.text
			arrayAnswers.append(b.text)
			count = count+1
		else:
			count =count+1
			continue

	
		#answerfor(qNo)

def getRightAnswer(soup, arrayRightAnswers):
	for i in soup.find_all(class_="bix-div-answer"):
		for j in i.find_all('p'):
			for k in j.find_all('span'):
				if k.text in 'A' or k.text in 'B' or k.text in 'C' or k.text in 'D':
					arrayRightAnswers.append(k.text)


def write(arrayQuestions, arrayRightAnswers,arrayAnswers,f):
	qNo = 0
	for i in arrayQuestions:
		qNo = qNo +1
		question = arrayQuestions[qNo-1].lstrip()
		#print question
		options = answerfor(qNo, arrayAnswers)
		#print options
		right = arrayRightAnswers[qNo-1]
		#print right
		options = ('|').join(options)
		string = '"'+question+'"'+','+'"'+options+'"'+','+'"'+right+'"'
		f.write(string.encode('ascii','ignore')+'\n')
		print "written"


def crawl(url,f):
	url = url
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	req = requests.get(url,headers=headers)
	soup = BeautifulSoup(req.content,'html.parser')
	arrayAnswers = []
	arrayQuestions = []
	arrayRightAnswers = []
	getQuestions(soup,arrayQuestions)
	getAnswers(soup, arrayAnswers)
	getRightAnswer(soup, arrayRightAnswers)
	write(arrayQuestions,arrayRightAnswers,arrayAnswers,f)
	for i in soup.find_all(class_='mx-pager-container'):
		for j in i.find_all('p'):
			for k in j.find_all('a'):
				if 'Next' in k.text:
					url = 'https://www.indiabix.com'+k['href']
					print "Going to"+ url
					crawl(url,f)


def topics(url,f):
	url = url
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	crawl(url,f)
	req = requests.get(url,headers=headers)
	soup = BeautifulSoup(req.content,'html.parser')
	for i in soup.find_all('div',class_='div-top-left'):
		for j in i.find_all('a'):
			pageLink = 'https://www.indiabix.com'+j['href']
			crawl(pageLink,f)