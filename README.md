# Custom Resolution
Change your screen resolution to a custom resolution (even its is higher or lower than vendor specification).

This script uses **cvt** and **xrandr** commands to generate the new screen params and apply the resolution (Also, add to resolutions options on Monitor Settings).

> **!!! IMPORTANT !!!** Some vendors dont recommends the usage of resolution higher than the specification, use by your own risk.

## Usage

````
$ ./chres [width] [height]
````

To change resolution to 1600 width X 900 height:
````
$ ./chres 1600 900
````

## Screen resolutions
- 4:3 aspect ratio resolutions: 640×480, 800×600, 960×720, 1024×768, 1280×960, 1400×1050, 1440×1080, 1600×1200, 1856×1392, 1920×1440, and 2048×1536.
- 16:10 aspect ratio resolutions: 1280×800, 1440×900, 1680×1050, 1920×1200 and 2560×1600.
- 16:9 aspect ratio resolutions: 1024×576, 1152×648, 1280×720 (HD), 1366×768, 1600×900, 1920×1080 (FHD), 2560×1440, 3840×2160 (4K), and 7680 x 4320 (8K)

From: https://www.digitalcitizen.life/what-screen-resolution-or-aspect-ratio-what-do-720p-1080i-1080p-mean

## Motivation
My Acer laptop has a good hardware except by the Monitor screen, still an HD (1366x768) screen :(, so, using CVT and XRANDR I could change the resolution to 1600x900 or 1920x1080 (Not good).
