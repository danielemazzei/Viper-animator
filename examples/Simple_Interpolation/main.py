################################################################################
# servo motor animation 
#
#
# Created by Zerynth Team 2015 CC
# Authors: D. Mazzei, G. Baldi  
################################################################################


from community.floyd.animator import animator
import streams

s=streams.serial()

# creates a list of points to be reached by the animation, represented by tuples (position, millisecond)
# The first tuple have to be set with time=0: (desired_pos,0). This is the value from which the animation will start
pointList= [(0,0),(90,1000),(100,10000),(60,5000),(10,3000)] 

print("scheduled positions at times (ms):",pointList)

def actuate(x):
	print("-->",x)

# create an animator that runs at 10Hz passing data to actuate()
anim=animator.Animator(10,actuate)

# start the animations using the created points list
anim.animate(pointList)
    
while True:
#just print the animator position and interpolated value
    print(anim.currentPosition())
    sleep(200)