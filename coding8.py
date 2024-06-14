# 얼굴 분석
def myFunction():
	for count in range(4):
		sprite.wait_for_seconds(0.1)
		sprite.wait_for_seconds(0.1)
		sprite.wait_for_seconds(0.1)

# KIM 발견
def myFunction_1():
	for count in range(3):
		sprite.wait_for_seconds(0.5)
		sprite.wait_for_seconds(0.5)

# 기본자세
def myFunction_2():
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 0)
	sprite.wait_for_seconds(0.2)

# TOM 발견
def myFunction_3():
	for count in range(3):
		sprite.wait_for_seconds(0.5)
		sprite.wait_for_seconds(0.5)

# LEE 발견
def myFunction_4():
	for count in range(3):
		sprite.wait_for_seconds(0.5)
		sprite.wait_for_seconds(0.5)

# 미등록사용자 발견
def myFunction_5():
	for count in range(3):
	for count in range(3):
		sprite.wait_for_seconds(0.5)
		sprite.wait_for_seconds(0.5)

def green_flag_clicked():

def green_flag_clicked1():
	myFunction_2()
	while True:
		if any:
			myFunction()
			if Kim:
				myFunction_1()
			else:
				if LEE:
					myFunction_4()
				else:
					if TOM:
						myFunction_3()
					else:
						myFunction_5()
