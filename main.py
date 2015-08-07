################################################################################
# servo motor animation 
#
#
# Created by VIPER Team 2015 CC
# Authors: D. Mazzei, G. Baldi  
################################################################################


import servo
import animator 
import streams

s=streams.serial()

# creates a list of points to be reached by the servo motor using touples (position, millisecond)
# The first touple have to be set with time=0: (desired_pos,0). This is the value from which the animation will start
# In this case servo motor position in degree are scheduled
pointList= [(0,0),(90,1000),(100,10000),(60,5000),(10,3000)] 

print("scheduled positions at times (ms):",pointList)

# create a servo motor attaching it to the pin D11. Specification of the PWM feature using the Viper pin mapping signature is required. 
# min max defaults in this case are selected for working properly with Hitech servomotors
MyServo=servo.Servo(D11.PWM,900,2100)

# create an animator that runs at 100Hz passing data to the MyServo.moveToDegree function  
anim=animator.Animator(100,MyServo.moveToDegree)

# start the animations using the created points list
anim.animate(pointList)
    
while True:
#just print the animator position and interpolated value
    print(anim.currentPosition())
    sleep(200)