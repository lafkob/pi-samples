#####Board setup
Green, yellow, red LEDs set up running off of (GPIO) pin #s 7, 11, 15.
Each LED has a 220 ohm resistor wired up after the LED, leading into the negative rail (and subsequently the GND pin on the pi cobbler).


#####src/main/python

Run these with 'sudo python' if you are logged in as a non-root user.

-cleanup_GPIO.py will clean up the state of the board channels. Some of the scripts do not do this (ie: led on scripts)
