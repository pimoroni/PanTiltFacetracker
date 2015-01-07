from Adafruit_PWM_Servo_Driver import PWM
'''
Tiny mini Pan/Tilt library
By default, tilt is on channel 1
and pan on channel 0
'''
servo = PWM(0x40)
servo.setPWMFreq(50)

TILT = 1
PAN  = 0

def pan(deg):
  _turn(PAN,deg)

def tilt(deg):
  _turn(TILT,deg)

def _turn(s,deg):
  pwm = 570.0 + ((deg/180.0) * 1700.0)

  pwm = (4096.0/20000.0) * pwm
  pwm = int(pwm)

  servo.setPWM(s, 0, pwm)
