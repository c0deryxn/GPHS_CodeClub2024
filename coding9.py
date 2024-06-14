# 비트박스
def myFunction():
	sprite.wait_for_seconds(2)
	for count in range(3):
		robokit_rs.set_servo_angle(2, 90)
		sprite.wait_for_seconds(0.2)
		sprite.wait_for_seconds(0.1)
		sprite.wait_for_seconds(0.1)
		robokit_rs.set_servo_angle(2, 70)
		sprite.wait_for_seconds(0.2)
	for count in range(3):
		robokit_rs.set_servo_angle(4, -90)
		sprite.wait_for_seconds(0.2)
		sprite.wait_for_seconds(0.1)
		sprite.wait_for_seconds(0.1)
		robokit_rs.set_servo_angle(4, -70)
		sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(2, 90)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(4, -90)
	sprite.wait_for_seconds(0.2)

# 클래식
def myFunction_1():
	sprite.wait_for_seconds(2)
	for count in range(2):
		robokit_rs.set_servo_angle(3, 15)
		sprite.wait_for_seconds(0.2)
		sprite.wait_for_seconds(0.5)
		sprite.wait_for_seconds(0.5)
		robokit_rs.set_servo_angle(3, 0)
		sprite.wait_for_seconds(0.5)
	for count in range(2):
		robokit_rs.set_servo_angle(5, -15)
		sprite.wait_for_seconds(0.2)
		sprite.wait_for_seconds(0.5)
		sprite.wait_for_seconds(0.5)
		robokit_rs.set_servo_angle(5, 0)
		sprite.wait_for_seconds(0.5)
	robokit_rs.set_servo_angle(3, 0)
	sprite.wait_for_seconds(0.2)
	robokit_rs.set_servo_angle(5, 0)
	sprite.wait_for_seconds(0.2)

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

# 댄스
def myFunction_3():
	sprite.wait_for_seconds(2)
	for count in range(2):
		for count_1 in range(3):
			robokit_rs.set_servo_angle(2, 90)
			robokit_rs.set_servo_angle(4, -54)
			sprite.wait_for_seconds(0.6)
			robokit_rs.set_servo_angle(2, 55)
			robokit_rs.set_servo_angle(4, -90)
			sprite.wait_for_seconds(0.6)
		robokit_rs.set_servo_angle(2, 90)
		robokit_rs.set_servo_angle(4, -54)
		sprite.wait_for_seconds(0.25)
		robokit_rs.set_servo_angle(2, 55)
		robokit_rs.set_servo_angle(4, -90)
		sprite.wait_for_seconds(0.25)
		robokit_rs.set_servo_angle(2, 90)
		robokit_rs.set_servo_angle(4, -54)
		sprite.wait_for_seconds(0.25)
	robokit_rs.set_servo_angle(2, 90)
	robokit_rs.set_servo_angle(3, 0)
	robokit_rs.set_servo_angle(4, -90)
	robokit_rs.set_servo_angle(5, 0)

def green_flag_clicked():
	myFunction_2()
	while True:
		if 클래식:
			myFunction_1()
		if 비트박스:
			myFunction()
		if 댄스:
			myFunction_3()

def green_flag_clicked1():
