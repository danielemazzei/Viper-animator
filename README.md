========================
Viper Animator Library
=========================

This module contains class definitions for a generic animator to be used in Viper www.viperize.it
The animator is a simple engine that takes as input a list o values to be reached at certain times and interpolates the data creating a continuous set of samples.
The animator takes as input the function to be called at the specified frame-rate passing it passing it the interpolated value.
This means that the Animator doesn't block the program execution during the animation. Once started an animation runs interdependently by the program workflow.

The main contains a Viper example where the animator is used for controlling a servo motor.
Viper servo library is also required https://github.com/danielemazzei/Viper-servo-library

Author: Daniele Mazzei
Contributor: Giacomo Baldi

License GPL3, copyright Viper Team 2015

info www.viperize.it