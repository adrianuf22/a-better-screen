#! /usr/bin/python3

import configparser
import subprocess
import os

configFile = configparser.ConfigParser()
configFile.read("$HOME/.config/a-better-screen.cfg")

fontScale=1
cmd = subprocess.run(['xrandr', '--listactivemonitors'], stdout=subprocess.PIPE, text=True)
rawOutput = cmd.stdout.split("\n")

xrand = []

activeMonitors = rawOutput[1:len(rawOutput) - 1]
for monitorDef in activeMonitors:
  definition = list(filter(lambda raw: raw != '', monitorDef.split(' ')))
  name = definition[3]

  if (not configFile.has_section(name)):
    continue

  resolution = configFile.get(name, 'resolution')
  if not resolution:
    continue

  xrand.append('--output ' + name + ' --mode ' + resolution)

  panning = configFile.get(name, 'panning', fallback=None)
  pos = configFile.get(name, 'pos', fallback=None)

  if panning:
    if pos:
      pos = pos.split('x')
      xrand.append('--panning ' + panning + '+' + pos[0] + '+' + pos[1])
    else:
      xrand.append('--panning ' + panning)
    
    xrand.append('--scale-from ' + panning)
  else:
    if pos:
      xrand.append('--pos ' + pos)

  _fontScale = float(configFile.get(name, 'fontScale', fallback=1))
  if _fontScale > fontScale:
    fontScale = _fontScale

print('xrandr ' + ' '.join(xrand))
# subprocess.run(['gsettings','set', 'org.gnome.desktop.interface', 'text-scaling-factor', str(fontScale)])