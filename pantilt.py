from Adafruit_PWM_Servo_Driver import PWM

servo = PWM(0x40)
servo.setPWMFreq(50)

TILT = 1
PAN = 0

def turn(s,deg):
  pwm = 570.0 + ((deg/180.0) * 1700.0)

  pwm = (4096.0/20000.0) * pwm
  pwm = int(pwm)

  servo.setPWM(s, 0, pwm)
