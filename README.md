========================
Zerynth Animator Library
========================

This module contains class definitions for a generic animator to be used in Zerynth.
The animator is a simple engine that takes as input a list o values to be reached at certain times and interpolates the data creating a continuous set of samples.
The animator takes as input the function to be called at the specified frame-rate passing it passing it the interpolated value.
This means that the Animator doesn't block the program execution during the animation. Once started an animation runs interdependently by the program workflow.

The main contains a Zerynth example where the animator is used for controlling a servo motor.
Zerynth servo library is also required

Author: Daniele Mazzei
Contributor: Giacomo Baldi

License GPL3, copyright Zerynth Team 2015

info www.zerynth.com