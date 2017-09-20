import requests
import json
import csv
import random
import time

url = 'https://api.telegram.org/bot439152091:AAGL0VrQ3Jz6vJom72JtAe-TEfBXZoaBc7Q/getUpdates'
resp = requests.get(url)
data = json.loads(resp.content)
recent = len(data['result'])-1
chatID = data['result'][recent]['message']['chat']['id']

def sendData(text,chatID):
	payload = {'chat_id': chatID, 'text': text}
	post = requests.post('https://api.telegram.org/bot439152091:AAGL0VrQ3Jz6vJom72JtAe-TEfBXZoaBc7Q/sendMessage',data=payload)

def selectQuestion():
	f = open("os.csv",'r')
	reader = csv.reader(f)
	data = random.choice(list(reader))
	f.close()
	question = data[0]
	A = "A. "+data[1].split('|')[0]
	B = "B. "+data[1].split('|')[1]
	C = "C. "+data[1].split('|')[2]
	D = "D. "+data[1].split('|')[3]
	options = A+'\n'+B+'\n'+C+'\n'+D+'\n'
	right = "Right option is: " + data[2]
	sendData(question,chatID)
	'''sendData(A,chatID)
	sendData(B,chatID)
	sendData(C,chatID)
	sendData(D,chatID)'''
	sendData(options,chatID)
	print " Question data sent"
	time.sleep(30)
	sendData(right,chatID)
	print " Answer sent"
	time.sleep(10)

def sendValues(question,A,B,C,D,right):
	sendData(question,chatID)
	sendData(A,chatID)
	sendData(B,chatID)
	sendData(C,chatID)
	sendData(D,chatID)

while True:
	selectQuestion()

