Internet controlled SCALEXTRIC with Raspberry Pi!
=================================================
With this project I can control the speed of a car on a SCALEXTRIC system from a Raspberry Pi.  I had a look around for tips on where to start and found a few people had had a crack at it but that documentation was distributed and not so straightforward to follow, so after I figured it out I pieced it all together in one example below.  Just for good measure, I plugged the system into dataplicity and I can now control the speed of my car from the internet!

Prerequisities
---------------
What you will need:
* SCALEXTRIC set including car (not DIGITAL)
* Power supply 12-14VDC capable of 1-2A.
* Spare SCALEXTRIC controller (likely will be sacrificed)
* Raspberry Pi Model B, or Model A with WiFi
* dataplicity account (it's free)
* Gertboard (we use only the motor controller output via Raspberry Pi PWM output)

I don't have a SCALEXTRIC digital set so I've no way to know if this project will work with one.  Accordingly I suggest you do so only if you know what you are doing.

Wiring
------
You do not need the SCALEXTRIC power supply for this project, so just disconnect it for now.  We will be connecting our own power supply.

Disassemble the SCALEXTRIC controller (there are three screws needed to open it).  There are three coloured wires on the end of the cabling inside the controller: red, black and green. Each wire with have a tiny flat round plug on the end. You will later screw these wires into the Gertboard headers which are too narrow for the flat round plugs on the end so you may as well cut them off now rather than fiddle about trying to save the controller.  The green wire will carry current during operation but is not needed, so tape it up with some electrical tape to keep it safe.

Prep the Gertboard, noting the correct orientation.  Fit a jumper to the top two pins on J7 (it won't work without this, I tried it).  Connect GP18 on J2 to MOTA on J5.  Connect GP17 on J2 to MOTB on J5.  Connect your 12-14VDC power supply Ground to the ground pin on J19 (marked with an upside down T symbol).  Connect the +ve terminal of your 12-14VDC power supply to MOT+ on J19.  Connect the black wire of your SCALEXTRIC controller cable to MOTA on J19 and the red wire to MOTB on J19.  Connect the other one to the lane (track) where you anticipate running your car.  That's the wiring done.

Raspberry Pi setup and packages
-------------------------------
I followed the usual dataplicity getting started guide at http://dataplicity.com/get-started/raspberry-pi/ to set up my account, the Pi, and to register a device class generating a sine wave.

You'll need two additional packages installed at this point: python-dev and wiringpi.  These are needed to interface with the Gertboard via PWM.

You must first install python-dev or wiringpi will fail to install.

    sudo apt-get install python-dev

Then:

```
pi@raspberrypi ~ $ sudo pip install wiringpi
Downloading/unpacking wiringpi
Running setup.py egg_info for package wiringpi

Installing collected packages: wiringpi
  Running setup.py install for wiringpi
    building '_wiringpi' extension
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c WiringPi/wiringPi/lcd.c -o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/lcd.o
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c WiringPi/wiringPi/piHiPri.c -o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/piHiPri.o
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c WiringPi/wiringPi/piThread.c -o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/piThread.o
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c WiringPi/wiringPi/wiringPiFace.c -o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/wiringPiFace.o
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c wiringpi_wrap.c -o build/temp.linux-armv6l-2.7/wiringpi_wrap.o
    wiringpi_wrap.c: In function âinit_wiringpiâ:
    wiringpi_wrap.c:4456:21: warning: variable âmdâ set but not used [-Wunused-but-set-variable]
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c WiringPi/wiringPi/wiringPi.c -o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/wiringPi.o
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c WiringPi/wiringPi/wiringSerial.c -o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/wiringSerial.o
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c WiringPi/wiringPi/wiringShift.c -o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/wiringShift.o
    gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro build/temp.linux-armv6l-2.7/WiringPi/wiringPi/lcd.o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/piHiPri.o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/piThread.o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/wiringPiFace.o build/temp.linux-armv6l-2.7/wiringpi_wrap.o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/wiringPi.o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/wiringSerial.o build/temp.linux-armv6l-2.7/WiringPi/wiringPi/wiringShift.o -o build/lib.linux-armv6l-2.7/_wiringpi.so

Successfully installed wiringpi
Cleaning up...
```

Next, load the kernel module for the device:

    sudo modprobe spi_bcm2708

At this point we should have access to the Pi's PWM output, thus to the Gertboard motor control output and to the SCALEXTRIC track.

Run a test
----------
Christine Smythe of Farnell has conveniently provided a Scalextric controller example for the Gertboard which is perfect to test this out.  For convenience, I've included it as test/fsmot-wpv1p0p0.py in this repo.  

Make sure you've switched on your 12VDC power supply (note that you definitely do not require the factory supplied Scalextric power supply as you should be supplying power directly to the rails).

Run the fsmot example (must be run as sudo).  Set the increment to about 50, and the motor output to about 30-40% (circa 373): 

```
pi@raspberrypi ~/scalextric/test $ sudo python fsmot-wpv1p0p0.py
WELCOME TO THE SCALEXTRIC CONTROLLER

These are the connections for controlling the scalextric motor:
  GP17 in J2 --- MOTB (just above GP1)
  GP18 in J2 --- MOTA (just above GP4)
  + of external power source --- MOT+ in J19
  ground of external power source --- GND (any)
  one wire for your motor in MOTA in J19
  the other wire for your motor in MOTB in J19

Whilst running, the display bar shows current PWM figure in range 0 to 1023

Press f to go faster, s to go slower, ESC to exit

Choose an increment value in range 1-200 : 50
Hit <RETURN/ENTER> to begin...

0373 #######################
```

This is usually enough to start the car, so you can try placing the car on the track and see if it starts to move.  If it doesn't, try the parallel track (I wasted more time than I care to admit by powering the wrong track).  

At this point, we can control the speed of the car from the Pi using the fsmot example.

Now, control it from the internet!
----------------------------------
At this point all that remains is for us to adapt the dataplicity sinewave example to directly control the Raspberry Pi PWM output.

Modify the ui.xml to replace the sinewave example stuff with a dropdown selector to set the output speed.  For example:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui>
  <interface id="dataplicity">
    <mastertabcontainer title="${device.name}" id="dataplicity-tabs">
      <tab title="Settings">
        <form button="Update" title="Speed">
          <select title="Speed" value="${device.settings.scalextric.track.speed}" 
              destination="device.settings.scalextric.track.speed">
            <option value="0">0%</option>
            <option value="5">5%</option>
            <option value="10">10%</option>
            <option value="15">15%</option>
            <option value="20">20%</option>
            <option value="25">25%</option>
            <option value="30">30%</option>
            <option value="35">35%</option>
            <option value="40">40%</option>
            <option value="45">45%</option>
            <option value="50">50%</option>
            <option value="55">55%</option>
            <option value="60">60%</option>
            <option value="65">65%</option>
            <option value="70">70%</option>
            <option value="75">75%</option>
            <option value="80">80%</option>
            <option value="85">85%</option>
            <option value="90">90%</option>
            <option value="95">95%</option>
            <option value="100">100%</option>
          </select>  
        </form>
      </tab>
    </mastertabcontainer>
  </interface>
</ui>
```

In the case of the above XML, the final user interface looks like this:
![Finished Scalextric user interface](/images/scalextric-web.png)

The only remaining step was to stitch it all together, which I did in a couple of lines of code in scalextric.py. Like so:

```
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
```

In short the car speed is updated each time the main dataplicity thread polls it and also when any configuration changes server-side (typically because someone changed a device setting on the website).  

Run the example (as sudo).  You can change the speed at any time from your dataplicity account.  

```
[13/May/2014 15:32:47]:dataplicity:INFO: running firmware 0000000001
[13/May/2014 15:32:47]:dataplicity:DEBUG: adding /home/pi/scalextric/py to Python path
[13/May/2014 15:32:47]:dataplicity:DEBUG: added task SetSpeedTask('scalextric')
[13/May/2014 15:32:47]:dataplicity:DEBUG: adding settings 'scalextric' from path /var/dataplicity/projects.Scalextric/scalextric.conf
[13/May/2014 15:32:47]:dataplicity:DEBUG: syncing...
[13/May/2014 15:32:47]:dataplicity:DEBUG: written settings <settings "/var/dataplicity/projects.Scalextric/scalextric.conf">
[13/May/2014 15:32:49]:dataplicity:DEBUG: sending signal 'settings_update' from 'scalextric' with args (u'scalextric', <settings scalextric.conf>), {}
[13/May/2014 15:32:49]:dataplicity:DEBUG: settings file(s) changed: scalextric
[13/May/2014 15:32:49]:dataplicity:DEBUG: sync complete 1.12s
[13/May/2014 15:32:49]:dataplicity:DEBUG: starting dataplicity service with conf /home/pi/scalextric/dataplicity.conf
[13/May/2014 15:32:49]:dataplicity:DEBUG: starting task manager
[13/May/2014 15:32:49]:dataplicity:DEBUG: initializing task SetSpeedTask('scalextric')
[13/May/2014 15:32:49]:dataplicity:DEBUG: sending signal 'settings_update' from 'scalextric' with args ('scalextric', <settings scalextric.conf>), {}
[13/May/2014 15:32:49]:dataplicity:DEBUG: ready
[13/May/2014 15:32:49]:dataplicity:DEBUG: syncing...
[13/May/2014 15:32:49]:dataplicity:DEBUG: written settings <settings "/var/dataplicity/projects.Scalextric/scalextric.conf">
[13/May/2014 15:32:49]:dataplicity.task.scalextric:DEBUG: started
Setting speed: 358
[13/May/2014 15:32:49]:dataplicity:DEBUG: user Exit
[13/May/2014 15:32:49]:dataplicity:DEBUG: closing
[13/May/2014 15:32:49]:dataplicity:DEBUG: stopping tasks
[13/May/2014 15:32:49]:dataplicity:DEBUG: sending signal 'stopping' with args (), {}
[13/May/2014 15:32:49]:dataplicity.task.scalextric:DEBUG: shutdown requested
[13/May/2014 15:32:49]:dataplicity:DEBUG: sending signal 'shuttingdown' with args (), {'graceful': True}
[13/May/2014 15:32:49]:dataplicity.task.scalextric:DEBUG: stopped
[13/May/2014 15:32:49]:dataplicity:DEBUG: goodbye
```
Tada!
