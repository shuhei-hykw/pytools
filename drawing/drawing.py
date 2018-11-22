#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script for making PostScript of drawing.

 e.g. $ drawing.py bh1 > bh1.ps

Supported targets are as follows.
 - BH1
 - BFT
 - BAC
 - Collimator
 - FBH
 - SCH
 - TOF
 - EMULSION
 - TRIGGER
 - MATRIX
 - DAQ
 - SU3
 - OCTET
'''

import argparse
import os
import sys

import draw_bac
import draw_basic
import draw_baryon_octet
import draw_bc34
import draw_bft
import draw_collimator
import draw_daq
import draw_hodoscope
import draw_matrix
import draw_product
import draw_sdc123
import draw_su3
import draw_trigger
import settings

#_______________________________________________________________________________
supported = ['BH1', 'BFT', 'BAC', 'BH2', 'COLLIMATOR', 'BC34', 'FBH', 'SDC1',
             'SCH', 'SDC2', 'SDC3', 'TOF',
             'EMULSION',
             'TRIGGER', 'MATRIX', 'DAQ', 'SU3', 'OCTET', 'PRODUCT']

#_______________________________________________________________________________
no_view_label = True
with_wave = False

#_______________________________________________________________________________
def draw_target():
  ''' draw target '''
  if settings.target == 'COLLIMATOR':
    draw_collimator.draw()
  elif settings.target == 'EMULSION':
    draw_emulsion()
  elif settings.target == 'TRIGGER':
    draw_trigger.draw()
  elif settings.target == 'MATRIX':
    draw_matrix.draw()
  elif settings.target == 'DAQ':
    draw_daq.draw()
  elif settings.target == 'BFT':
    draw_bft.draw()
  elif settings.target == 'BH1':
    draw_hodoscope.draw_bh1()
  elif settings.target == 'BH2':
    draw_hodoscope.draw_bh2()
  elif settings.target == 'BAC':
    draw_bac.draw()
  elif settings.target == 'FBH':
    draw_hodoscope.draw_fbh()
  elif settings.target == 'SCH':
    scale = 1.7
    t = 2*scale
    widths = [11.5*scale for i in range(8)]
    height = 450*scale
    overlap = 1.0*scale
    zdiff = -t
    height_position = [-5, -25]
    overlap_position = [-5, -30]
    unit_position = [5, -25]
    scale_height = 20
    scale_height_offset = 0
    total_width_height = 15
    upstream_position = 20
    downstream_position = 25
  elif settings.target == 'TOF':
    draw_hodoscope.draw_tof()
  elif settings.target == 'BC34':
    draw_bc34.draw()
  elif settings.target == 'SDC1':
    draw_sdc123.draw_sdc1()
  elif settings.target == 'SDC2':
    draw_sdc123.draw_sdc2()
  elif settings.target == 'SDC3':
    draw_sdc123.draw_sdc3()
  elif settings.target == 'PRODUCT':
    draw_product.draw()

#_______________________________________________________________________________
def draw():
  ''' draw main function '''
  if settings.target == 'SU3':
    draw_su3.draw()
  elif settings.target == 'OCTET':
    draw_baryon_octet.draw()
  elif settings.target == 'PRODUCT':
    draw_product.draw()
  elif not settings.target in supported:
    raise Exception('%% target name \"{}\" is not supported'.format(settings.target))
  else:
    draw_basic.initialize()
    draw_target()
    print('showpage')

#_______________________________________________________________________________
def draw_emulsion():
  global scale
  full_draw = True
  unit = 1e0
  scale = 0.04*unit
  width = 10*345*scale
  #height = 10*350*scale
  height = 40
  thin_gel = 100*scale/unit
  thin_base = 180*scale/unit
  thin_full = thin_gel * 2 + thin_base
  thick_gel = 480*scale/unit # designed to be 450
  thick_base = 40*scale/unit
  thick_full = thick_gel * 2 + thick_base
  space = 0
  zigzag = 0 if full_draw else 2
  x = 10
  y = 40
  ystart = y
  lw = 0.4
  lw2 = 0.1
  fc = 0.9
  y2 = y - 0.5*(lw-lw2)
  ''' thin '''
  draw_square([x, y], thin_full, height, lw, fc)
  draw_square([x+thin_gel, y2], thin_base, height, lw2)
  draw_line_with_scale([x, y+height], thin_gel, 5, True)
  draw_line_with_scale([x+thin_gel, y+height], thin_base, 10)
  draw_line_with_scale([x+thin_gel+thin_base, y+height], thin_gel, 5)
  x = x + 2*thin_gel + thin_base + space
  height -= zigzag
  draw_square([x, y], thick_full, height, lw, fc)
  draw_square([x+thick_gel, y2], thick_base, height, lw2)
  height += zigzag
  x = x + 2*thick_gel + thick_base + space
  draw_square([x, y], thick_full, height, lw, fc)
  draw_square([x+thick_gel, y2], thick_base, height, lw2)
  draw_line_with_scale([x, y+height], thick_gel, 5)
  draw_line_with_scale([x+thick_gel, y+height], thick_base, 15)
  draw_line_with_scale([x+thick_gel+thick_base, y+height], thick_gel, 5)
  x = x + 2*thick_gel + thick_base + space
  x = x + (2*thick_gel + thick_base + space)/4
  draw_text([x-0.5-space/2, y+height*0.625], '...', False, 12)
  x = x + (2*thick_gel + thick_base + space)/4
  height += zigzag
  draw_square([x, y], thick_full, height, lw, fc)
  draw_square([x+thick_gel, y2], thick_base, height, lw2)
  height -= zigzag
  x = x + 2*thick_gel + thick_base + space
  draw_square([x, y], thin_full, height, lw, fc)
  draw_square([x+thin_gel, y2], thin_base, height, lw2)
  x = x + 2*thin_gel + thin_base
  ''' crip '''
  draw_square([9, y-1], x-8, height/4, 0, 1)
  ''' scale '''
  draw_text([10+thin_gel+thin_base/2, y+height/4-8], 'thin-type sheet')
  draw_text([(10+x)/2, y+height/4-8], '11 thick-type sheets')
  draw_text([x-thin_gel-thin_base/2, y+height/4-8], 'thin-type sheet')
  draw_text([x-thin_gel-thin_base/2, y+height+4], 'base')
  draw_arrow([x-thin_gel-thin_base/2, y+height+2], 0, -4, 3)
  draw_text([x-thin_full-thick_full+thick_gel/2, y+height+4], 'emulsion layer')
  draw_arrow([x-thin_full-thick_full+thick_gel/2, y+height+2], 0, -4, 3)
  draw_text([x+15, y], '[um]')
  width = x - 10
  if not full_draw:
    draw_line_with_scale([10, y+height+20], width, 5)
    return
  ''' entire '''
  scale = 1.0
  x = 10
  y = ystart + height + 30
  print('[1 1] 0 setdash')
  draw_polygon3d([x, y+25], [60*scale, -10*scale], [0, 70*scale], [10*scale, 5*scale], 0.1, fc)
  print('[] 0 setdash')
  draw_arrow([x, y+25], 60*scale, -10*scale, 3)
  draw_arrow([x+60*scale, y+25-10*scale], 0, 70*scale, 3)
  draw_arrow([x+60*scale, y+25-10*scale], 10*scale, 5*scale, 3)
  draw_arrow([x+70*scale, y+25-5*scale], 0, 70*scale, 3)
  print('[1 1] 0 setdash')
  #draw_arrow([x, y+25], 0, 70*scale, 3, '', 0.4)
  draw_polygon3d([x+25, y+47], [27*scale, -4.5*scale], [0, 26*scale], [0.4*scale, 0.2*scale], 0.1, 0.75)
  print('[] 0 setdash')
  draw_polygon3d([x+15, y+42], [27*scale, -4.5*scale], [0, 26*scale], [0.4*scale, 0.2*scale], 0.1, 0.75)
  draw_polygon3d([x+13, y+45], [18*scale, -3*scale], [0, 10*scale], [7*scale, 3.5*scale], 0.2, 0.5)
  draw_text([x+5, y+46], 'K', False, 6, 'Times-Italic')
  draw_text([x+5+3.5, y+48], '-', False, 7, 'Times-Italic')
  draw_arrow([x+23, y+36], 0, 10, 3)
  draw_text([x+23, y+32], 'Diamond target')
  draw_arrow([x+34, y+17], 4, 4, 3)
  draw_text([x+16, y+14], 'Emulsion module')
  draw_arrow([x+18, y+64], -4, 8, 3)
  draw_text([x+13, y+80], 'Upstream')
  draw_text([x+13, y+74], 'SSD')
  draw_arrow([x+38, y+69], 2, 4, 3)
  draw_text([x+42, y+81], 'Downstream')
  draw_text([x+42, y+75], 'SSD')
  draw_arrow([18, y+43], 12, 6, 2, '', 0.8, 3)
  # nwave = int(60/10)
  # for i in range(nwave):
  #   moveto = [x+60/nwave*i, y+95-i*10/nwave]
  #   wavew = 10
  #   waveh = 3*(i%2-0.5)
  #   for j in range(2):
  #     print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  #     print('{} {} {} {} {} {} curveto'.format(moveto[0]+wavew*1/3, moveto[1]+waveh-10/nwave*1/3,
  #                                              moveto[0]+wavew*2/3, moveto[1]+waveh-10/nwave*2/3,
  #                                              moveto[0]+wavew, moveto[1]-10/nwave))
  #     print('{} {} rmoveto'.format(-20*(i%2-0.5), -10*(i%2-0.5)))
  #     print('0.1 setlinewidth closepath')
  #   print('stroke')
  ''' circle '''
  scale = 2.0
  x = 10 + 3.7/7*width
  y = ystart + height + 35
  r = 50
  center = [x+r, y+r]
  dw = 30*scale
  ssdw1 = 1.8*scale
  ssdw2 = 2.3*scale
  air1 = 1.6*scale
  emw = 11.76*scale
  air2 = 23.8*scale - air1 - emw
  print('newpath {} {} moveto'.format(center[0]+r, center[1]))
  print('{} {} {} 0 360 arc clip'.format(center[0], center[1], r))
  draw_square([x-dw/2, y+r-dw/2], dw, dw, lw, 0.5)
  x = x + dw/2
  draw_square([x, 0], ssdw1, 300, lw, 0.75)
  draw_square([x+ssdw1+air1, 0], emw, 300, lw, fc)
  draw_square([x+ssdw1+air1+emw+air2, 0], ssdw2, 300, lw, 0.75)
  print('initclip')
  draw_text([x-dw/2, y+r+32], 'Diamond')
  draw_text([x-dw/2, y+r+27], 'target')
  draw_text([x+ssdw1+air1+emw/2, y+2*r+8], 'Emulsion')
  draw_text([x+ssdw1+air1+emw/2, y+2*r+3], 'module')
  draw_text([x+ssdw1/2-8, y+2*r+3], 'Upstream')
  draw_text([x+ssdw1/2-8, y+2*r-2], 'SSD')
  draw_text([x+ssdw1+air1+emw+air2, y+2*r+0], 'Downstream')
  draw_text([x+ssdw1+air1+emw+air2, y+2*r-5], 'SSD')
  draw_arrow([x+ssdw1+air1+emw, y-2], 0, -8, 3)
  draw_arrow([x+ssdw1+air1, y-2], 0, -8, 3)
  draw_arrow([10, y-10], (x+ssdw1+air1)-10, 0, 3)
  draw_arrow([10, y-10], 0, -4, 3)
  draw_arrow([x+ssdw1+air1+emw, y-10], 10+width-(x+ssdw1+air1+emw), 0, 3)
  draw_arrow([10+width, y-10], 0, -4, 3)
  x -= dw/2
  draw_arrow([x-10, y+r], 30, 0, 3, '', lw)
  draw_arrow([x+20, y+r], 80, 30, 2, '', lw, 2.5)
  draw_arrow([x+20, y+r], 30, -20, 3, '', lw, 2.5)
  #draw_circle([x+50, y+r-20], 0.5, 0.1)
  draw_text([x-10, y+r+2], 'K', False, 6, 'Times-Italic')
  draw_text([x-10+3.5, y+r+4], '-', False, 7, 'Times-Italic')
  draw_text([x+95, y+r+32], 'K', False, 6, 'Times-Italic')
  draw_text([x+95+3.5, y+r+34], '+', False, 4, 'Times-Italic')
  draw_text([x+50, y+r-27], 'X', False, 6, 'Symbol')
  draw_text([x+50+3.5, y+r-25], '-', False, 7, 'Times-Italic')
  draw_circle([center[0], center[1]], r, 0, 0, 360, 0.1)

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('target_name', help='drawing target name, supported as follows.\n' +
                      'BH1, BH2, BAC, FBH, EMULSION, SCH, TOF, TRIGGER, MATRIX, DAQ and SU3')
  parsed, unparsed = parser.parse_known_args()
  settings.set_target(parsed.target_name.upper())
  try:
    draw()
  except KeyboardInterrupt:
    print(sys.exc_info())
