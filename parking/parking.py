import RPi.GPIO as GPIO                  
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)                   
                
in1 = 3
in2 = 4
in3 = 17
in4 = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)


time.sleep(5)

def forward():
    print('forward')
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    
def back():
    print(back)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
        
def right():
    print('right')
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
 
   
def left():
    print('left')
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    

def stop(time=0):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    print('stop')

def dist():
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    time.sleep(0.1)                                   #Delay

    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                           #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:                
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor

    distance = pulse_duration* 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
    distance = round(distance,2)                 #Round to two decimal points
    return distance

p=0
count=0
forward()
while True:
    if(p==1):
         stop()
         now = time.time()
         while(time.time()<=now+1.2):
             left()
         stop()  
         now = time.time()
         while(time.time()<=now+0.7):
             back()      
         print ('park')
         stop()
         break
    distance=dist()
    
    if(distance>30):
       
        now = time.time()
        while(time.time()<=now+0.3):
             distance=dist()
             print (distance)   
             if(distance<30):
                  p=0
                  break
             p=1
