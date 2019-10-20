# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對 印出"終於猜對了"
# 猜錯 要告訴她 比答案大/小
# 印出猜出幾次
import random
r = random.randint(1, 10)
count = 0
while True:
	num = input('請猜數字: ')
	num = int(num)
	count = count + 1
	if r == num:
		print('猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案還要大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')	
