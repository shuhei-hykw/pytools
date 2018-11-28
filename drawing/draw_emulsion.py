#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import draw_basic as db
import settings

version = 2

#_______________________________________________________________________________
def draw():
  full_draw = True
  unit = 1e0
  scale = 0.04*unit
  settings.set_scale(scale)
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
  zigzag = 2 if full_draw else 2
  x = 10
  y = 40
  ystart = y
  lw = 0.4
  lw2 = 0.1
  fc = 0.9
  y2 = y - 0.5*(lw-lw2)
  ''' thin '''
  db.draw_square([x, y], thin_full, height, lw, fc)
  db.draw_square([x+thin_gel, y2], thin_base, height, lw2)
  db.draw_line_with_scale([x, y+height], thin_gel, 5, True)
  db.draw_line_with_scale([x+thin_gel, y+height], thin_base, 10)
  db.draw_line_with_scale([x+thin_gel+thin_base, y+height], thin_gel, 5)
  x = x + 2*thin_gel + thin_base + space
  height -= zigzag
  db.draw_square([x, y], thick_full, height, lw, fc)
  db.draw_square([x+thick_gel, y2], thick_base, height, lw2)
  height += zigzag
  x = x + 2*thick_gel + thick_base + space
  db.draw_square([x, y], thick_full, height, lw, fc)
  db.draw_square([x+thick_gel, y2], thick_base, height, lw2)
  db.draw_line_with_scale([x, y+height], thick_gel, 5)
  db.draw_line_with_scale([x+thick_gel, y+height], thick_base, 15)
  db.draw_line_with_scale([x+thick_gel+thick_base, y+height], thick_gel, 5)
  x = x + 2*thick_gel + thick_base + space
  x = x + (2*thick_gel + thick_base + space)/4
  db.draw_text([x-0.5-space/2, y+height*0.625], '...', False, 12)
  x = x + (2*thick_gel + thick_base + space)/4
  height += zigzag
  db.draw_square([x, y], thick_full, height, lw, fc)
  db.draw_square([x+thick_gel, y2], thick_base, height, lw2)
  height -= zigzag
  x = x + 2*thick_gel + thick_base + space
  db.draw_square([x, y], thin_full, height, lw, fc)
  db.draw_square([x+thin_gel, y2], thin_base, height, lw2)
  x = x + 2*thin_gel + thin_base
  ''' crip '''
  db.draw_square([9, y-1], x-8, height/4, 0, 1)
  ''' scale '''
  db.draw_text([10+thin_gel+thin_base/2, y+height/4-8], 'thin-type sheet')
  db.draw_text([(10+x)/2, y+height/4-8], '11 thick-type sheets')
  db.draw_text([x-thin_gel-thin_base/2, y+height/4-8], 'thin-type sheet')
  db.draw_text([x-thin_gel-thin_base/2, y+height+4+zigzag], 'base film')
  db.draw_arrow([x-thin_gel-thin_base/2, y+height+2+zigzag], 0, -4-zigzag, 3)
  db.draw_text([x-thin_full-thick_full+thick_gel/2, y+height+4+zigzag], 'emulsion layer')
  db.draw_arrow([x-thin_full-thick_full+thick_gel/2, y+height+2+zigzag], 0, -4, 3)
  db.draw_text([x+15, y], '[um]')
  width = x - 10
  if not full_draw:
    db.draw_line_with_scale([10, y+height+20], width, 5)
    return
  ''' entire '''
  scale = 1.0
  x = 10
  y = ystart + height + 30
  print('[1 1] 0 setdash')
  db.draw_polygon3d([x, y+25], [60*scale, -10*scale], [0, 70*scale], [10*scale, 5*scale], 0.1, fc)
  print('[] 0 setdash')
  db.draw_arrow([x, y+25], 60*scale, -10*scale, 3)
  db.draw_arrow([x+60*scale, y+25-10*scale], 0, 70*scale, 3)
  db.draw_arrow([x+60*scale, y+25-10*scale], 10*scale, 5*scale, 3)
  db.draw_arrow([x+70*scale, y+25-5*scale], 0, 70*scale, 3)
  print('[1 1] 0 setdash')
  #db.draw_arrow([x, y+25], 0, 70*scale, 3, '', 0.4)
  db.draw_polygon3d([x+25, y+47], [27*scale, -4.5*scale], [0, 26*scale], [0.4*scale, 0.2*scale], 0.1, 0.75)
  print('[] 0 setdash')
  db.draw_polygon3d([x+15, y+42], [27*scale, -4.5*scale], [0, 26*scale], [0.4*scale, 0.2*scale], 0.1, 0.75)
  db.draw_polygon3d([x+13, y+45], [18*scale, -3*scale], [0, 10*scale], [7*scale, 3.5*scale], 0.2, 0.5)
  db.draw_text([x+5, y+46], 'K', False, 6, 'Times-Italic')
  db.draw_text([x+5+3.5, y+48], '-', False, 7, 'Times-Italic')
  db.draw_arrow([x+23, y+36], 0, 10, 3)
  db.draw_text([x+23, y+32], 'Diamond target')
  db.draw_arrow([x+34, y+17], 4, 4, 3)
  db.draw_text([x+16, y+14], 'Emulsion module')
  db.draw_arrow([x+18, y+64], -4, 8, 3)
  if version == 1:
    db.draw_text([x+13, y+80], 'Upstream')
    db.draw_text([x+13, y+74], 'SSD')
    db.draw_text([x+42, y+81], 'Downstream')
    db.draw_text([x+42, y+75], 'SSD')
  elif version == 2:
    db.draw_text([x+13, y+74], 'SSD1')
    db.draw_text([x+42, y+75], 'SSD2')
  db.draw_arrow([x+38, y+69], 2, 4, 3)
  db.draw_arrow([18, y+43], 12, 6, 2, '', 0.8, 3)
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
  db.draw_square([x-dw/2, y+r-dw/2], dw, dw, lw, 0.5)
  x = x + dw/2
  db.draw_square([x, 0], ssdw1, 300, lw, 0.75)
  db.draw_square([x+ssdw1+air1, 0], emw, 300, lw, fc)
  db.draw_square([x+ssdw1+air1+emw+air2, 0], ssdw2, 300, lw, 0.75)
  print('initclip')
  db.draw_text([x-dw/2, y+r+32], 'Diamond')
  db.draw_text([x-dw/2, y+r+27], 'target')
  db.draw_text([x+ssdw1+air1+emw/2, y+2*r+8], 'Emulsion')
  db.draw_text([x+ssdw1+air1+emw/2, y+2*r+3], 'module')
  if version == 1:
    db.draw_text([x+ssdw1/2-8, y+2*r+3], 'Upstream')
    db.draw_text([x+ssdw1/2-8, y+2*r-2], 'SSD')
    db.draw_text([x+ssdw1+air1+emw+air2, y+2*r+0], 'Downstream')
    db.draw_text([x+ssdw1+air1+emw+air2, y+2*r-5], 'SSD')
  elif version == 2:
    db.draw_text([x+ssdw1/2-8, y+2*r-2], 'SSD1')
    db.draw_text([x+ssdw1+air1+emw+air2+ssdw2, y+2*r-6], 'SSD2')
  db.draw_arrow([x+ssdw1+air1+emw, y-2], 0, -8, 3)
  db.draw_arrow([x+ssdw1+air1, y-2], 0, -8, 3)
  db.draw_arrow([10, y-10], (x+ssdw1+air1)-10, 0, 3)
  db.draw_arrow([10, y-10], 0, -4, 3)
  db.draw_arrow([x+ssdw1+air1+emw, y-10], 10+width-(x+ssdw1+air1+emw), 0, 3)
  db.draw_arrow([10+width, y-10], 0, -4, 3)
  x -= dw/2
  db.draw_arrow([x-10, y+r], 30, 0, 3, '', lw)
  db.draw_arrow([x+20, y+r], 80, 30, 2, '', lw, 2.5)
  db.draw_arrow([x+20, y+r], 30, -20, 3, '', lw, 2.5)
  #db.draw_circle([x+50, y+r-20], 0.5, 0.1)
  db.draw_text([x-10, y+r+2], 'K', False, 6, 'Times-Italic')
  db.draw_text([x-10+3.5, y+r+4], '-', False, 7, 'Times-Italic')
  db.draw_text([x+95, y+r+32], 'K', False, 6, 'Times-Italic')
  db.draw_text([x+95+3.5, y+r+34], '+', False, 4, 'Times-Italic')
  db.draw_text([x+50, y+r-27], 'X', False, 6, 'Symbol')
  db.draw_text([x+50+3.5, y+r-25], '-', False, 7, 'Times-Italic')
  db.draw_circle([center[0], center[1]], r, -1, 0, 360, 0.1)
