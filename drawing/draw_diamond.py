#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import draw_basic as db
import settings

#_______________________________________________________________________________
def draw():
  scale = 1.0
  settings.set_scale(scale)
  diamond = {}
  fbh = {}
  diamond['thickness'] = 30*scale
  diamond['height'] = 30*scale
  fbh['frame'] = [35*scale, 84*scale, 7*scale]
  fbh['window'] = [30*scale, 3*scale]
  fbh['scintillator'] = [32-4.25*scale, 35*scale, 2*scale]
  xstart = 30
  ystart = 100
  lw = 0.4
  ''' FBH '''
  x = xstart
  y = ystart
  fc = 0.6
  db.draw_square([x, y-fbh['frame'][1]/2],
                 fbh['frame'][0], fbh['frame'][2], lw, fc)
  db.draw_square([x, y+fbh['frame'][1]/2],
                 fbh['frame'][0], -fbh['frame'][2], lw, fc)
  db.draw_square([x+fbh['frame'][0], y-fbh['window'][0]/2],
                 -fbh['window'][1], -(fbh['frame'][1]-fbh['window'][0])/2,
                 lw, fc)
  db.draw_square([x+fbh['frame'][0], y+fbh['window'][0]/2],
                 -fbh['window'][1], (fbh['frame'][1]-fbh['window'][0])/2,
                 lw, fc)
  db.draw_square([x+fbh['scintillator'][0]-fbh['scintillator'][2],
                  y-fbh['scintillator'][1]/2],
                 fbh['scintillator'][2], fbh['scintillator'][1], lw, 1)
  db.draw_square([x+fbh['scintillator'][0],
                  y-fbh['scintillator'][1]/2],
                 fbh['scintillator'][2], fbh['scintillator'][1], lw, 1)
  ''' Diamond '''
  x += fbh['scintillator'][0] + fbh['scintillator'][2]
  y = ystart
  fc = 0.5
  db.draw_square([x, y-diamond['height']/2],
                 diamond['thickness'], diamond['height'], lw, fc)
