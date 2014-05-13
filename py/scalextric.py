from dataplicity.client.task import Task, onsignal

import wiringpi
import sys
from time import sleep

class SetSpeedTask(Task):
    """Regulates the speed of the motor"""

    def on_startup (self):
        wiringpi.wiringPiSetupGpio()                # Initialise wiringpi GPIO
        wiringpi.pinMode(18,2)                      # Set up GPIO 18 to PWM mode
        wiringpi.pinMode(17,1)                      # GPIO 17 to output
        wiringpi.digitalWrite(17, 0)                # port 17 off for rotation one way
        wiringpi.pwmWrite(18,0)                     # set pwm to zero initially

    def poll(self):
        """Called on a schedule defined in dataplicity.conf"""
        self.updateSpeed() 

    def updateSpeed (self):
        pwm_speed = int(round((self.speed * 1024) / 100, 0))
        print "Setting speed: "+str(pwm_speed)
        wiringpi.pwmWrite(18, pwm_speed)

    @onsignal('settings_update', 'scalextric')
    def on_settings_update(self, name, settings):
        """Catches the 'settings_update' signal for 'scalextric'"""
        # This signal is sent on startup and whenever settings are changed by the server
        str_speed = settings.get('track', 'speed')
        self.speed = 0
        try:
            self.speed = int(str_speed)
        except:
            pass

        self.updateSpeed()
