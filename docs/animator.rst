.. module: animator 

********
Animator
********

This module contains class definitions for a generic animator.
The animator is a simple engine that takes as input a list o values to be reached at certain times and interpolates the data creating a continuous set of samples.
The animator takes as input the function to be called at the specified frame-rate passing it passing it the interpolated value.
This means that the Animator doesn't block the program execution during the animation. Once started an animation runs interdependently by the program workflow.

Every Animator instance implements the following methods:

    *animate: starts the interpolation process and activate the animator timer that will call the chosen function with the selected period
    *stop: blocks the animation execution
    *duration: returns the total duration of the loaded animation. animate have to be called before in order to get results from duration method 
    *currentPosition: returns the current position of the animation in term of (animation block, sample, interpolated value)
    
==================
Animator class
==================

.. class:: Animator(frame_rate,callback_fun,interp_fun="LINEAR")

    This is the class for creating an animator. 
    * frame_rate: is the frequency used by the animator to interpolate the values and then for calling the callback passing it the interpolated value.Smooth animations for lights and LEDs are fine with values around 30Hz.
    * callback_fun: is the function that will be called at the specified frame rate passing the interpolated value.
    * interp_fun: is the string associated with the interpolation algorithm. in this version only LINEAR is supported and consequently set as default.

    
.. method:: stop()

    Blocks the animator setting the status to "IDLE". 
        
.. method:: state()

    Returns the animator state as string: RUN or IDLE 
        
.. method:: currentPosition()

    Returns the current position of the animation in term of (animation block, sample, interpolated value)
        
.. method:: animate(points)

    starts the interpolation process and activate the animator timer that will call the chosen function with the selected period passing the interpolated values
        
.. method:: duration()

    returns the total duration of the loaded animation. animate have to be called before in order to get results from duration method   
        
