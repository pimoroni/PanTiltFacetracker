#from RPIO import PWM
from Adafruit_PWM_Servo_Driver import PWM
import time

servo = PWM(0x40)
servo.setPWMFreq(50)

TILT = 1
PAN = 0

def turn(s,deg):
  #print("Turning to %d degrees" % deg)
  pwm = 570.0 + ((deg/180.0) * 1700.0)

  '''pulseLength = 1000000
  pulseLength /= 50 
  pulseLength /= 4096
  pwm *= 1000
  pwm /= pulseLength
  pwm = int(pwm)
  '''
  pwm = (4096.0/20000.0) * pwm
  pwm = int(pwm)

  #print("Using %d" % pwm)
  servo.setPWM(s, 0, pwm)

'''
twitch = 0.005

turn(TILT,60)

exit()

while True:
  for x in range(0,180):
    turn(PAN,x)
    turn(TILT,90)
    time.sleep(twitch)
  time.sleep(0.5)
  for x in reversed(range(0,180)):
    turn(PAN,x)
    turn(TILT,90)
    time.sleep(twitch)
  time.sleep(0.5)
'''
