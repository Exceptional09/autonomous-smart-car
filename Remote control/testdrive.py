import motermodule as mot
import keyboardmodule as km
km.init()
 
while True:
    if km.getKey('w'):
        print('forward')
        mot.forward(10)
    elif km.getKey('s'):
        print('backward')
        mot.backward(10)
    elif km.getKey('q'):
        print('fleft')
        mot.frontleft(10)
    elif km.getKey('e'):
        print('fright')
        mot.frontright(10)
    elif km.getKey('a'):
        print('bleft')
        mot.backright(10)
    elif km.getKey('d'):
        print('bright')
        mot.backleft(10)
    else:
        mot.stop(0)
 
