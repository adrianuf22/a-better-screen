# A Better Screen

This repository has some scripts to change screen configurations - to better (or not) - tested by me along of the last months and without any warranty - use by your own risk.

## NEWS

- Added `scres` script to enable XRANDR with Samsung panels or another panels with resolution locked at optimal resolutions (The native maximum resolution). This script uses `--panning` and `--scale` arguments to zooming the image size and scaling to correct size.

### How to use

````
$ ./bin/scres [width] [height]
````

## Motivation
My Acer laptop has a good hardware except by the monitor screen, still an HD (1366x768) screen :(, so, using CVT and XRANDR I could change the resolution to 1600x900 (Great) or 1920x1080 (Not good).

After some adjusts and tests, I could make simple scripts using the builtin commands from my OS to improve the quality of my monitor screen, changing the resolution for something more wide and adjusting the gamma and brightness to keep working with a poor screen without strain my eyes after hours of work.

## Setup/Run on start
This scripts could be moved to main **bin** directory enable execution from any part of OS like any other application, use the script `install.sh` to create SYMLinks to main **bin**.

To keep configurations after restart, edit the file `a-better-screen.desktop` at `resources` directory, setting up the values and scripts that you would like to exec after restart at the `Exec` param of this file and run the script `autostart.sh` to configure.

![image](https://user-images.githubusercontent.com/721525/88596480-8f0f1680-d03b-11ea-8841-9eaff4cf9293.png)

Reference: [Desktop Application Autostart Specification](https://developer.gnome.org/autostart-spec/)

## Custom Resolution

Change your screen resolution to a custom resolution (even its is higher or lower than vendor specification).

````
$ ./bin/chres [width] [height]
````

To change resolution to 1600 width X 900 height:
````
$ ./bin/chres 1600 900
````

This script uses **cvt** and **xrandr** commands to generate the new screen params and apply the resolution (Also, add to resolutions options on Monitor Settings).

> **!!! IMPORTANT !!!** Some vendors dont recommends the usage of resolution higher than the specification, use by your own risk.

### Screen resolutions
- 4:3 aspect ratio resolutions: 640×480, 800×600, 960×720, 1024×768, 1280×960, 1400×1050, 1440×1080, 1600×1200, 1856×1392, 1920×1440, and 2048×1536.
- 16:10 aspect ratio resolutions: 1280×800, 1440×900, 1680×1050, 1920×1200 and 2560×1600.
- 16:9 aspect ratio resolutions: 1024×576, 1152×648, 1280×720 (HD), 1366×768, 1600×900, 1920×1080 (FHD), 2560×1440, 3840×2160 (4K), and 7680 x 4320 (8K)

From: https://www.digitalcitizen.life/what-screen-resolution-or-aspect-ratio-what-do-720p-1080i-1080p-mean

## Set gamma to red screen
This script is a set of predefined params to change the screen color incresing the red color and using warm temperatures, avoiding the blue. Was originally writed to works with **xgamma** command, but was not possible to change the screen temperature and white color is not affected. Now, **Redshift** is the command behind the scene.

Usage:
````
$ ./gamma [red] [green] [blue] [temperature]
````
Default: red=0.9, green=0.7, blue=0.5 and temperature is 5500

**Presets:**

- **--no-blue**: Warm temperature, Intense red, low green and no blue.
- **--less-blue**: Warm temperature and red near to high value, green and blue has mid values.
- **--cold-red**: Cold temperature with red near to high and green above of mid value, blue still in mid value.
