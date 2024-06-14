import random

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
