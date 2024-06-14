import random

# 1. 오른다리 걷기
def myFunction():
	robokit_rs.set_servo_angle(4, -63)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 107)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, -26)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, -22)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)

# 감정표현
def myFunction_1():
	sprite.set_variable("myVariable_1", 0)
	sprite.set_variable("myVariable_1", random.randint(1, 4))
	sprite.wait_for_seconds(2)
	if (sprite.get_variable("myVariable_1") == 1):
		for count in range(2):
			sprite.wait_for_seconds(0.2)
			sprite.wait_for_seconds(0.2)
	if (sprite.get_variable("myVariable_1") == 2):
		for count in range(5):
			sprite.wait_for_seconds(0.2)
			sprite.wait_for_seconds(0.2)
	if (sprite.get_variable("myVariable_1") == 3):
		for count in range(3):
			sprite.wait_for_seconds(0.3)
			sprite.wait_for_seconds(0.3)
			sprite.wait_for_seconds(0.3)
	if (sprite.get_variable("myVariable_1") == 4):
		for count in range(5):
			sprite.wait_for_seconds(0.1)
			sprite.wait_for_seconds(0.1)
			sprite.wait_for_seconds(0.1)

# 인식
def myFunction_2():
	for count in range(3):
		robokit_rs.set_servo_angle(2, 65)
		robokit_rs.set_servo_angle(2, -65)
		sprite.wait_for_seconds(0.3)
		robokit_rs.set_servo_angle(2, 65)
		robokit_rs.set_servo_angle(2, -65)
		sprite.wait_for_seconds(0.5)

# 기본자세
def myFunction_3():
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 0)
	sprite.wait_for_seconds(0.2)

# 걷기
def myFunction_4():
	sprite.wait_for_seconds(2)
	myFunction_3()
	myFunction()
	myFunction_7()
	myFunction_8()
	myFunction_9()

# 노래하기
def myFunction_5():
	sprite.wait_for_seconds(2)
	for count in range(3):
		robokit_rs.set_servo_angle(3, 20)
		robokit_rs.set_servo_angle(5, 20)
		sprite.wait_for_seconds(0.2)
		sprite.wait_for_seconds(0.1)
		sprite.wait_for_seconds(0.1)
		robokit_rs.set_servo_angle(3, 0)
		robokit_rs.set_servo_angle(5, 0)
		sprite.wait_for_seconds(0.2)
		robokit_rs.set_servo_angle(3, -20)
		robokit_rs.set_servo_angle(5, -20)
		sprite.wait_for_seconds(0.2)
		sprite.wait_for_seconds(0.1)
		sprite.wait_for_seconds(0.1)
		robokit_rs.set_servo_angle(3, 0)
		robokit_rs.set_servo_angle(5, 0)
		sprite.wait_for_seconds(0.2)

# 춤 추기
def myFunction_6():
	sprite.wait_for_seconds(2)
	for count in range(2):
		for count_1 in range(3):
			robokit_rs.set_servo_angle(2, 90)
			robokit_rs.set_servo_angle(4, -55)
			sprite.wait_for_seconds(0.6)
			robokit_rs.set_servo_angle(2, 55)
			robokit_rs.set_servo_angle(4, -90)
			sprite.wait_for_seconds(0.6)
		robokit_rs.set_servo_angle(2, 90)
		robokit_rs.set_servo_angle(4, -55)
		sprite.wait_for_seconds(0.25)
		robokit_rs.set_servo_angle(2, 55)
		robokit_rs.set_servo_angle(4, -90)
		sprite.wait_for_seconds(0.25)
		robokit_rs.set_servo_angle(2, 90)
		robokit_rs.set_servo_angle(4, -55)
		sprite.wait_for_seconds(0.25)
		robokit_rs.set_servo_angle(2, 90)
		robokit_rs.set_servo_angle(3, 0)
		robokit_rs.set_servo_angle(4, -90)
		robokit_rs.set_servo_angle(5, 0)

# 2. 왼다리 크게걷기
def myFunction_7():
	robokit_rs.set_servo_angle(2, 57)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -116)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 13)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 27)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 27)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)

# 3. 오른다리 크게걷기
def myFunction_8():
	robokit_rs.set_servo_angle(4, -63)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 107)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, -26)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, -22)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)

# 4. 왼다리 걸어 기본자세
def myFunction_9():
	robokit_rs.set_servo_angle(2, 57)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -116)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 3)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 10)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 0)
	sprite.wait_for_seconds(0.2)

def green_flag_clicked():
	myFunction_3()
	while True:
		if null:
			myFunction_2()
			myFunction_6()
		if null:
			myFunction_2()
			myFunction_5()
		if null:
			myFunction_2()
			myFunction_4()
		if null:
			myFunction_2()
			myFunction_1()


# 기본자세
def myFunction():
	robokit_rs.set_servo_angle(2, -30)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, 30)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 0)
	sprite.wait_for_seconds(0.2)

# 오른다리 크게걷기
def myFunction_1():
	robokit_rs.set_servo_angle(4, -63)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 107)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, -26)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, -22)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)

# 왼다기 크게걷기
def myFunction_2():
	robokit_rs.set_servo_angle(2, 57)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -116)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 13)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 27)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 27)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)

# 왼발 걸어 기본자세
def myFunction_3():
	robokit_rs.set_servo_angle(2, 57)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -116)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 3)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 10)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 0)
	sprite.wait_for_seconds(0.2)

# 오른다리 걷기
def myFunction_4():
	robokit_rs.set_servo_angle(4, -63)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 107)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, -26)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, -22)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)

def green_flag_clicked():
	myFunction()
