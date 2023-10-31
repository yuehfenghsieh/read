data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
print('總共有', len(data), '筆留言')	

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('請輸入想要輸入的單字為:')
	if word == 'q':
		print('感謝搜尋')
		break
	elif word in wc:
		print(word, '的輸入次數為', wc[word])
	else:
		print('對話內容沒有這個字哦')