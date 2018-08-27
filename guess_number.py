import random
num = random.randint(1, 100)
guess_time = 0
while True:
	guess_num = int(input('請猜數字: '))
	if guess_num == num:
		print('終於猜對了!')
		guess_time = guess_time + 1
		print('你總共猜了', guess_time, '次')
		break
	elif guess_num > num:
		print('你猜的數字比答案大')
		guess_time = guess_time + 1
		print('你已經猜了', guess_time, '次')
	else:
		print('你猜的數字比答案小')
		guess_time = guess_time + 1
		print('你已經猜了', guess_time, '次')