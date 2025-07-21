from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

if left_motor is None or right_motor is None:
    print("Error: Cannot find motor device(s). Check device names!")
else:
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    speed = 3.0
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

print("Runs")  # เพิ่มบรรทัดนี้ เพื่อแสดงว่ารันโค้ดแล้ว

while robot.step(timestep) != -1:
    pass