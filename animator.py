"""
.. module: animator 

This module contains class definitions for a generic animator.
The animator is a simple engine that takes as input a list o values to be reached at certain times and interpolates the data creating a continuous set of samples.
The animator takes as input the function to be called at the specified frame-rate passing it passing it the interpolated value.
This means that the Animator doesn't block the program execution during the animation. Once started an animation runs interdependently by the program workflow.

Every Animator instance implements the following methods:

    *animate: starts the interpolation process and activate the animator timer that will call the chosen function with the selected period
    *stop: blocks the animation execution
    *duration: returns the total duration of the loaded animation. animate have to be called before in order to get results from duration method 
    *currentPosition: returns the current position of the animation in term of (animation block, sample, interpolated value)
    

"""

import timers

class Animator():  

    """
==================
Animator class
==================

.. class:: Animator(frame_rate,callback_fun,interp_fun="LINEAR")

    This is the class for creating an animator. 
    * frame_rate: is the frequency used by the animator to interpolate the values and then for calling the callback passing it the interpolated value.Smooth animations for lights and LEDs are fine with values around 30Hz.
    * callback_fun: is the function that will be called at the specified frame rate passing the interpolated value.
    * interp_fun: is the string associated with the interpolation algorithm. in this version only LINEAR is supported and consequently set as default.

    """   
        
    def __init__(self, frame_rate,callback_fun,interp_fun="LINEAR"):
        self.frameRate=frame_rate
        self.period=1000//frame_rate
        self.interpolator=interp_fun
        self.timer=timers.timer()
        self.animation=[]
        self.totDuration=0
        self.pointList=[]        
        self.callback=callback_fun
        self.currentBlock=0
        self.currentStep=0
        self.currentValue=0
        self.state="IDLE"
    

        
    def run(self):
    #while  True:
        if self.state=="RUN":

            if self.currentBlock == len(self.animation)-1: 
                if self.currentStep == self.animation[self.currentBlock][0]:
                    self.currentValue+=self.animation[self.currentBlock][1]
                    self.state="IDLE"
                    break
            elif self.currentStep == self.animation[self.currentBlock][0]:
                self.currentBlock+=1
                self.currentStep=0   

            self.currentValue+=self.animation[self.currentBlock][1]
            self.currentStep+=1

            self.callback(self.currentValue)     

        """
.. method:: stop()
    Blocks the animator setting the status to "IDLE". 
        """ 

    def stop(self):
        self.state="IDLE"


        """
.. method:: state()
    Returns the animator state as string: RUN or IDLE 
        """ 

    def state(self):
        return self.state

        """
.. method:: currentPosition()
    Returns the current position of the animation in term of (animation block, sample, interpolated value)
        """         

    def currentPosition(self):
        return [self.currentBlock,self.currentStep, self.currentValue]   
    
    
    
    def interpolate(self,points):
        
        for i in range(0,len(points)-1):
            
            samples=points[i+1][1]//self.period
            increment=(points[i+1][0]-points[i][0])/samples
            self.animation.append([samples, increment])
            self.totDuration+=points[i+1][1]

        self.totDuration+=points[0][1]       
    
        """
.. method:: animate()
    starts the interpolation process and activate the animator timer that will call the chosen function with the selected period passing the interpolated values
        """         

    def animate(self, points):
        self.interpolate(points)
                  
        self.state="RUN"
        self.currentBlock=0
        self.currentStep=0
        self.currentValue= points[0][0]  #set the staring value at the first scheduled position
        self.timer.interval(self.period,self.run)
        self.timer.start()        
        #self.__run()

    
    """
.. method:: animate()
    returns the total duration of the loaded animation. animate have to be called before in order to get results from duration method   
    """         

    def duration(self):
        return self.totDuration    
                