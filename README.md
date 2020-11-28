# piconsole-mod-bigtemppanel
Code to incorporate a panel in the WeatherFlow PiConsole with a large font, high-visibility temperature reading.

Written by Steve Cody
Special thanks for python assistance from Pete Davis, and John Ullrey.
Contact:  github@codycrew.net

This code is specifically made to work with the WeatherFlow PiConsole written by Peter Davis.
You can find his code at https://github.com/peted-davis/WeatherFlow_PiConsole

Dependencies
WeatherFlow PiConsole v4.x or greater

Caveats
Please use this code at your own risk.  I'm not a developer.  I like to tinker and make things work.

Background
I have a WeatherFlow Tempest weather station and love the PiConsole Pete Davis has written.  I have it sitting in my living room
and like to be able to see the weather readings.  The issue I had is that I couldn't see the outside temperature on the PiConsole
from across the room. 

This mod simply adds another Panel choice called BigTemp.  It gives you an easily readible, bright font, outside temperature reading.  

To install:

Stop the PiConsole with wfpiconsole stop.

Ensure you have a backup of the original /home/pi/wfpiconsole/wfpiconsole.kv and /home/pi/wfpiconsole/main.py files.

copy wfpiconsole.include.kv to the /home/pi/wfpiconsole directory
copy bigtempinclude.py to the /home/pi/wfpiconsole/lib directory

Change ownership on both files to pi
chown pi:pi /home/pi/wfpiconsole/lib/bigtempinclude.py
chown pi:pi /home/pi/wfpiconsole/wfpiconsole.include.kv

Modify /home/pi/wfpiconsole/wfpiconsole.kv

Insert the following line on line 27:
#:include wfpiconsole.include.kv

Modify /home/pi/wfpiconsole/main.py

Insert the following lines starting at line 226
from lib.bigtempinclude      import BigTempPanel
from lib.bigtempinclude      import BigTempButton

Modify /home/pi/wfpiconsole/wfpiconsole.ini
Beginning around line 50, modify the PrimaryPanel or SecondaryPanel section to enable the BigTemp panel in whichever position you like.
For example:
PanelOne = BigTemp

After modifying the files, you can start the PiConsole with wfpiconsole start.  You should see the new panel.


After modifying both files, start your PiConsole with wfpiconsole start.

That's it.  If you have any issues, email me.
