#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import draw_basic as db
import settings

version = 2

#_______________________________________________________________________________
def draw():
  scale = 0.05
  settings.set_scale(scale)
  xstart = 30
  ystart = 100
  x = xstart
  y = ystart
  w_emul = 70
  h_emul = 480*scale
  h_base = 40*scale
  h_all = h_emul*2 + h_base
  xlens = x + w_emul - 20
  ylens = y + h_all + 20
  wlens = 10
  hlens = 0.2
  wimage = 100*scale
  himage = 10*scale
  wimage2 = wimage*2
  himage2 = himage*5
  tan = h_all / w_emul * 2.
  ''' Emulsion '''
  db.draw_square([x, y], w_emul, h_all, fill_color=0.9)
  db.draw_arrow([xlens-w_emul/2, ylens-h_all-20], w_emul/2, h_all, 1, lw=0.5, msize=2)
  db.draw_square([x, y+h_emul], w_emul, h_base)
  db.draw_square([x-2, y-2], 4, h_all+4, fill_color=1, line_width=0)
  db.draw_text([x+2, y+h_all+1.5], 'Emulsion sheet', centering=False)
  label_offset = -15
  db.draw_text([x+label_offset, y+h_emul*0.5+1], 'emulsion')
  db.draw_text([x+label_offset, y+h_emul*0.5-4], 'layer')
  db.draw_text([x+label_offset, y+h_emul*1.5+h_base+1], 'emulsion')
  db.draw_text([x+label_offset, y+h_emul*1.5+h_base-4], 'layer')
  db.draw_text([x+label_offset, y+h_emul+h_base/2-1.5], 'base film')
  db.draw_text([x+w_emul/2-13, y+4], 'track', centering=False)
  db.draw_text([x+5, y+h_emul*0.5], '480', rotate=True)
  db.draw_text([x+3.5, y+h_emul+h_base/2], '40', rotate=True)
  db.draw_text([x+5, y+h_emul*1.5+h_base], '480', rotate=True)
  # db.draw_line_with_scale([x+5, y], 0, h_emul, rotate=True)
  # db.draw_line_with_scale([x+2.5, y+h_emul], 0, h_base, rotate=True)
  # db.draw_line_with_scale([x+5, y+h_emul+h_base], 0, h_emul, rotate=True)
  ''' Lens '''
  db.draw_polygon([xlens-8, ylens], [[8, 20],
                                     [8, -20],
                                     [-8, -20],
                                     [-8, 20]], fill_color=1)
  db.draw_elip([xlens, ylens], wlens, hlens)
  db.draw_text([xlens-38, ylens+4], 'Objective lens', centering=False)
  ''' micro image '''
  xoffset = 40
  db.draw_polygon([xlens+wimage, ylens-22], [[xoffset-wimage2*2, -0],
                                             [0, 4],
                                             [wimage2*2.5, 0],
                                             [0, -himage2*8],
                                             [-wimage2*2.5, 0],
                                             [0, himage2*5]], fill_color=1)
  n = 6
  for i in range(n+4):
    ximage = xlens - wimage/2 - (i+0.5)*himage/tan
    yimage = ylens - 20 - (i+1)*himage
    db.draw_square([ximage, yimage], wimage, himage, fill_color=-1)
    if i >= n:
      continue
    ximage2 = xlens - wimage/2 - (i+0.5)*himage2/tan
    yimage2 = ylens - 20 - (i+1)*himage2
    if abs(i-(n-0.5)/2.) <= 1:
      db.draw_circle([ximage2+xoffset+wimage2*3/4, yimage2+himage2/2], 0.2, fc=0)
      if i == n/2:
        db.draw_circle([ximage2+xoffset+wimage2*3/4+himage2/tan/2, yimage2+himage2], 0.2, fc=0)
    else:
      db.draw_square([ximage2+xoffset, yimage2], wimage2, himage2, fill_color=-1)
  db.draw_arrow([xlens+xoffset-himage2*6/tan+wimage/2, ylens-20-himage2*6],
                himage2*6/tan, himage2*6, 1, lw=0.1, msize=1)
  db.draw_text([xlens+xoffset+wimage2+4, ylens-20-himage2*1-1.5],
               'interval = 3   m/cos', centering=False)
  db.draw_text([xlens+xoffset+wimage2+28, ylens-20-himage2*1-1.5],
               'm', centering=False, font='Symbol')
  db.draw_text([xlens+xoffset+wimage2+43, ylens-20-himage2*1-1.5],
               'q', centering=False, font='Symbol')
  # db.draw_text([xlens+xoffset+wimage2+4, ylens-20-himage2*3-1.5],
  #              '10 images (interval = 3   m)', centering=False)
  # db.draw_text([xlens+xoffset+wimage2+51, ylens-20-himage2*3-1.5],
  #              'm', centering=False, font='Symbol')
  x = xlens+xoffset-wimage2
  y = ylens-20-himage2*10-1.5
  db.draw_text([x, y], '1. taking 10 images', centering=False)
  db.draw_text([x, y-8], '2. tracking with image processing', centering=False)
  db.draw_text([x, y-16], '3. renewing track position and angle', centering=False)
  db.draw_text([x, y-24], '4. iterating 1. to 3. until stop', centering=False)
