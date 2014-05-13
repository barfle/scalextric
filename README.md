Internet controlled SCALEXTRIC with Raspberry Pi!
=================================================

Prerequisities
---------------
What you will need:
* SCALEXTRIC basic set including car
* Power supply 12-14VDC capable of 1-2A.
* Spare SCALEXTRIC controller (likely will be sacrificed)
* Raspberry Pi
* dataplicity account (it's free)
* Gertboard

I don't have a SCALEXTRIC digital set so I've no way to know if this project will work with one.  Accordingly I suggest you do so only if you know what you are doing.

Wiring
-------
You do not need the SCALEXTRIC power supply for this project, so just disconnect it.  We will be connecting our own power supply.

Disassemble the SCALEXTRIC controller (there are three screws needed to open it).  There are three coloured wires on the end of the cabling inside the controller: red, black and green. Each wire with have a tiny flat round plug on the end. You will later screw these wires into the Gertboard headers which are too narrow for the flat round plugs on the end so you may as well cut them off now rather than fiddle about trying to save the controller.  The green wire will carry current during operation but is not needed, so tape it up with some electrical tape to keep it safe.

Prep the Gertboard, noting the correct orientation.  Fit a jumper to the top two pins on J7 (it won't work without this, I tried it).  Connect GP18 on J2 to MOTA on J5.  Connect GP17 on J2 to MOTB on J5.  Connect your 12-14VDC power supply Ground to the ground pin on J19 (marked with an upside down T symbol).  Connect the +ve terminal of your 12-14VDC power supply to MOT+ on J19.  Connect the black wire of your SCALEXTRIC controller cable to MOTA on J19 and the red wire to MOTB on J19.  Connect the other one to the lane where you anticipate running your car.  That's the wiring done.

Raspberry Pi setup
------------------
Prep the Pi with the usual NOOBS.

Install python-dev and wiringpi packages which are needed to interface with the Gertboard via PWM.

sudo apt-get install python-dev # if you don't, wiringpi will fail to install
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

Load the kernel module for the device:

sudo modprobe spi_bcm2708

Run a test
----------
<insert test code here for car at low speed>

<insert test code here for car at zero speed>

Cool.  Now to control it from the internet.....

<copy stuff from Raspberry Pi sinewave>
<adapt>
