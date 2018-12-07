#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from settings import a4size, wdaq, hdaq
import draw_basic as db

#_______________________________________________________________________________
def draw():
  scale = 1.0
  stage = 3
  x_microscope = 15
  y_microscope = 50
  w_microscope = 75*scale
  h_microscope = 20*scale
  x_server = 155
  y_server = 50
  w_server = 50*scale
  h_server = 20*scale
  x_driver = x_microscope+w_microscope+10
  y_driver = y_microscope
  w_driver = x_server - x_microscope - w_microscope - 20
  h_driver = 20*scale
  '''microscope'''
  x = x_microscope
  y = y_microscope
  w = w_microscope
  h = h_microscope
  db.draw_square([x-5, y-5], w+10, 6*h, fill_color=0.9)
  db.draw_text([x+w/2, y+h*6+3-5], 'Microscope', text_size=7)
  ''' position encoder '''
  db.draw_square([x, y], w, h)
  db.draw_text([x, y+h+3], 'Position encoder', centering=False)
  db.draw_text([x+w/2, y+h*0.7-1.5], 'Haldenhain LS406 (x/y)')
  db.draw_text([x+w/2, y+h*0.3-1.5], 'Haldenhain MT2501 (z)')
  ''' stepping motor '''
  y += 1.75*h
  db.draw_square([x, y], w, h)
  db.draw_text([x, y+h+3], 'Stepping motor', centering=False)
  # db.draw_text([x+w/2, y+h*0.7-1.5], 'Oriental motor')
  # db.draw_text([x+w/2, y+h*0.3-1.5], 'PK566-NBC (x/y) PK543-NBC (z)')
  db.draw_text([x+w/2, y+h*0.7-1.5], 'Oriental motor PK566-NBC (x/y)')
  db.draw_text([x+w/2, y+h*0.3-1.5], 'Oriental motor PK543-NBC (z)')
  ''' LED '''
  y += 1.75*h
  db.draw_square([x, y], w, h/2)
  db.draw_text([x, y+h/2+3], 'LED', centering=False)
  db.draw_text([x+w/2, y+h/4-1.5], 'LUXEON (5W)')
  ''' CCD '''
  y += 1.25*h
  db.draw_square([x, y], w, h/2)
  db.draw_text([x, y+h/2+3], 'CCD', centering=False)
  db.draw_text([x+w/2, y+h/4-1.5], 'SONY XC-HR300')
  ''' server '''
  x = x_server
  y = y_server
  w = w_server
  h = h_server
  db.draw_square([x-5, y-5+1.75*h], w+10, 4.25*h, fill_color=0.9)
  #db.draw_square([x-5, y-5], w+10, 6*h, fill_color=0.9)
  #db.draw_text([x+w/2, y+h*6+3-5], 'Control server (Windows 7)')
  db.draw_text([x+w/2, y+h*6+3-5], 'Control server', text_size=7)
  ''' Mortor controll board '''
  y += 2*h
  db.draw_square([x, y], w, h/2)
  db.draw_text([x, y+h*0.5+3], 'Mortor control board', centering=False)
  db.draw_text([x+w/2, y+h*0.25-1.5], 'ADTEK aPCI-M59')
  ''' Image processing board '''
  y += 2.75*h
  db.draw_square([x, y], w, h/2)
  db.draw_text([x, y+h/2+3], 'Image processing board', centering=False)
  db.draw_text([x+w/2, y+h/4-1.5], 'Renesas VP-910')
  ''' driver '''
  x = x_driver
  y = y_driver
  w = w_driver
  h = h_driver
  ''' interpolate digitizer '''
  db.draw_square([x, y+0.2*h], w, 0.6*h)
  db.draw_text([x+w/2, y+0.5*h-1.5], 'Interpolate-digitizer')
  db.draw_arrow([x-10, y+0.5*h], 10, 0, 3, msize=2)
  db.draw_arrow([x+w-5, y+0.8*h], 0, 1.35*h, 3, msize=2)
  db.draw_arrow([x+w-5, y+2.15*h], 15, 0, 2, msize=2)
  # db.draw_text([x+w/2, y+0.7*h-1.5], 'Interpolatation and')
  # db.draw_text([x+w/2, y+0.3*h-1.5], 'digitizing electronics')
  # db.draw_arrow([x+w-5, y+h], 0, 1.15*h, 3, msize=2)

  # db.draw_arrow([x+w/2, y+h], 0, 0.43*h, 3, msize=2)
  # db.draw_square([x, y+0.*h], w, h*1)
  # db.draw_text([x+w/3, y+0.3*h-1.5], 'Interpolate', text_size=4)
  # db.draw_text([x+w/3, y+0.05*h-1.5], 'and digitize', text_size=4)
  ''' mortor driver '''
  y += 1.75*h
  w -= 10*scale
  db.draw_square([x, y+0.2*h], w, h*0.6)
  db.draw_text([x+w/2, y+0.5*h-1.5], 'Motor driver')
  db.draw_arrow([x-10, y+0.5*h], 10, 0, 1, msize=2)
  # db.draw_arrow([x+w/2, y+0.2*h], 0, -0.43*h, 3, msize=2)
  db.draw_arrow([x+w, y+0.6*h], 20, 0, 0, msize=2)
  #db.draw_text([x+w+7, y], 'PCI', centering=False)
  db.draw_elip([x+w+10, y+0.5*h], 1, 5, begin=45, end=315)
  ''' LED driver '''
  y += 1.5*h
  db.draw_square([x, y+0.2*h], w, h*0.6)
  db.draw_text([x+w/2, y+0.5*h-1.5], 'LED driver')
  db.draw_arrow([x-10, y+0.5*h], 10, 0, 1, msize=2)
  db.draw_arrow([x+w, y+0.5*h], 18, 0, 1, msize=2)
  db.draw_arrow([x-10, y+1.75*h], 30+w, 0, 0, msize=2)
  db.draw_arrow([x+w*0.2, y+0.8*h], 0, 0.95*h, 1, msize=2)
  db.draw_text([x+w*0.6, y+(0.8+0.95/2)*h-1.5], 'synchronize')
  # db.draw_text([x+w+9, y+(0.5)*h+5], 'Serial', text_size=4)
  # db.draw_text([x+w+9, y+(0.5)*h+1], 'to USB', text_size=4)
  db.draw_text([x+w+10+10, y+0.5*h-1.5], 'on-board USB', centering=False)
