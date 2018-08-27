import random
# key in number range
range_min = int(input('輸入範圍最小值: '))
range_max = int(input('輸入範圍最大值: '))
if range_min >= range_max:
	print('最大值必須大於最小值') #number check
num = random.randint(range_min, range_max)
guess_time = 0
while True:
	guess_num = int(input('請猜數字: '))
	if guess_num == num:
		print('終於猜對了!')
		guess_time += 1
		print('你總共猜了', guess_time, '次')
		break
	elif guess_num > num:
		print('你猜的數字比答案大')
	elif guess_num < num:
		print('你猜的數字比答案小')
	guess_time += 1
	print('你已經猜了', guess_time, '次')