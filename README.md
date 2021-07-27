# A better screen resolution

This repository has some scripts to change screen resolution - to better (or not) - **!!! IMPORTANT !!!** Some vendors dont recommends the usage of resolution higher than the specification, use by your own risk.

## Motivation
My Acer laptop has a good hardware except by the monitor screen, still an HD (1366x768) screen :(, so, using CVT and XRANDR I could change the resolution to FullHD or greater.

After some adjusts and tests, I could make simple scripts using the builtin commands from my OS to improve the quality of my monitor screen, changing the resolution for something more wide, and adjusting the font size factor, color gamma and brightness to keep working with a poor screen without strain my eyes after hours of work.

## How to use

1. Run `./install.sh` (as sudo) to install before
2. Edit `~/.config/a-better-screen.cfg`

````
[HDMI-1]              # <-- Monitor identifier, run `xrandr` to get monitor name
resolution=1920x1080  # <-- [Required] The desired resolution
panning=2560x1440     # <-- [Optional] The panning (See below) resolution
fontScale=1.22        # <-- [Optional] To scale font size to increase text quality, recommended when panning is set
pos=2560x579          # <-- [Optional] Monitor position [X]x[Y]

# [Other monitor identifier]]
# ....
````

> **Panning**: Some panels like Samsung's panel has an "optimal resolution protection" that avoid to creates a resolution out of specs, so, we need to create a virtual resolution scaling from current resolution to a new size. The image quality is not affected, but some "flicks" can be showed when watch movies.

3. Run `chres` to apply

### Run on logon (Using .desktop approach)

- Run `autostart.sh` to configure.

Reference: [Desktop Application Autostart Specification](https://developer.gnome.org/autostart-spec/)

### Screen resolutions
- 4:3 aspect ratio resolutions: 640×480, 800×600, 960×720, 1024×768, 1280×960, 1400×1050, 1440×1080, 1600×1200, 1856×1392, 1920×1440, and 2048×1536.
- 16:10 aspect ratio resolutions: 1280×800, 1440×900, 1680×1050, 1920×1200 and 2560×1600.
- 16:9 aspect ratio resolutions: 1024×576, 1152×648, 1280×720 (HD), 1366×768, 1600×900, 1920×1080 (FHD), 2560×1440, 3840×2160 (4K), and 7680 x 4320 (8K)

From: https://www.digitalcitizen.life/what-screen-resolution-or-aspect-ratio-what-do-720p-1080i-1080p-mean

## Set gamma to red screen
This script is a set of predefined params to change the screen color incresing the red color and using warm temperatures, avoiding the blue. Was originally writed to works with **xgamma** command, but was not possible to change the screen temperature and white color is not affected. Now, **Redshift** is the command behind the scene.

Usage:
````
$ ./chcolor [red] [green] [blue] [temperature]
````
Default: red=0.9, green=0.7, blue=0.5 and temperature is 5500

**Presets:**

- **--no-blue**: Warm temperature, Intense red, low green and no blue.
- **--less-blue**: Warm temperature and red near to high value, green and blue has mid values.
- **--cold-red**: Cold temperature with red near to high and green above of mid value, blue still in mid value.
