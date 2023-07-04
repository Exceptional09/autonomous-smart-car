import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 18
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
   

def dist():
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  while GPIO.input(ECHO)==0:
     pulse_start = time.time()
  while GPIO.input(ECHO)==1:
     pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  print( "Distance:",distance,"cm")
  return distance
in1 = 3
in2 = 4
in3 = 17
in4 = 27
en = 2
en2 = 22
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p = GPIO.PWM(en,100)
q = GPIO.PWM(en2,100)
p.start(0)
q.start(0)

while True:
   if dist()<=30:
       print("Vechile behind")
       p.start(10)
       q.start(10)
       GPIO.output(in1, GPIO.LOW)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.HIGH)
       GPIO.output(in4, GPIO.LOW)
       time.sleep(3)
       print("MOVE FORWARD")
       GPIO.output(in1, GPIO.HIGH)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.HIGH)
       GPIO.output(in4, GPIO.LOW)
   else:
       p.start(10)
       q.start(10)
       GPIO.output(in1, GPIO.HIGH)
       GPIO.output(in2, GPIO.LOW)
       GPIO.output(in3, GPIO.HIGH)
       GPIO.output(in4, GPIO.LOW)
        

   
