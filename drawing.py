#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script for making PostScript of detector drawing.

 e.g. $ drawing.py bh1 > bh1.ps

Supported detectors are as follows.
 - BH1
 - BAC
 - Collimator
 - FBH
 - SCH
 - TOF
'''

import argparse
import datetime
import math
import os
import sys

#_______________________________________________________________________________
a4size = [210, 297]
scale = 1
detector_name = ''
default_text_size = 5

#_______________________________________________________________________________
def draw_arrow(moveto, width, height, mark=0): # mark = 0:both 1:first 2:last 3:none
  ''' draw arrow '''
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  if width == 0:
    theta = 0.5*math.pi
  else:
    theta = math.atan(height/width)
  if mark == 0 or mark == 1:
    print('{} {} rlineto'.format(math.cos(theta) + 0.5*math.sin(theta),
                                 math.sin(theta) - 0.5*math.cos(theta)))
    print('{} {} rlineto'.format(-math.sin(theta), math.cos(theta)))
    print('{} {} rlineto'.format(-math.cos(theta) + 0.5*math.sin(theta),
                                 -math.sin(theta) - 0.5*math.cos(theta)))
  print('{} {} rlineto'.format(width, height))
  if mark == 0 or mark == 2:
    print('{} {} rlineto'.format(-math.cos(theta) + 0.5*math.sin(theta),
                                 -math.sin(theta) - 0.5*math.cos(theta)))
    print('{} {} rlineto'.format(-math.sin(theta), math.cos(theta)))
    print('{} {} rlineto'.format(math.cos(theta) + 0.5*math.sin(theta),
                                 math.sin(theta) - 0.5*math.cos(theta)))
  print('closepath gsave fill grestore {} setlinewidth stroke'.format(0.0001 if mark != 3 else 0.1))

#_______________________________________________________________________________
def draw_circle(moveto, r, a=0, b=360, line_width=0.1, fill_color=1.0):
  ''' draw circle '''
  print('newpath {} {} moveto'.format(moveto[0]+r, moveto[1]))
  print('{} {} {} {} {} arc closepath'.format(moveto[0], moveto[1], r, a, b))
  if fill_color > 0:
    print('{} setgray gsave fill grestore'.format(fill_color))
  print('0.0 setgray')
  if line_width > 0:
    print('{} setlinewidth stroke'.format(line_width))

#_______________________________________________________________________________
def draw_detector():
  ''' draw detector '''
  global scale
  line_width = 0.4
  '''bh1'''
  if detector_name == 'BH1':
    scale = 1.0
    t = 5*scale
    widths = [30, 20, 16, 12, 8, 8, 8, 12, 16, 20, 30]
    for i in range(len(widths)):
      widths[i] *= scale
    height = 66*scale
    overlap = 1*scale
    zdiff = t
    height_position = [-5, -10]
    overlap_position = [-5, -20]
    unit_position = [5, -20]
    scale_height = 20
    scale_height_offset = 0
    total_width_height = 18
    upstream_position = 20
    downstream_position = 35
  '''bh2'''
  if detector_name == 'BH2':
    t = 6
    widths = [120]
    height = 40
  '''bac'''
  if detector_name == 'BAC':
    scale = 0.5
    xoffset = -40
    width = 160*scale
    height = 75*scale
    t1 = 11.5*4*scale
    t2 = 90*scale
    pmt = [2.6*25.4*scale, 60*scale]
    '''front view'''
    draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2], width, height, line_width, 0.8)
    draw_square([(a4size[0]-width)/2+4+xoffset, (a4size[1])/2-pmt[1]], pmt[0], pmt[1])
    draw_square([(a4size[0]-width)/2-4+xoffset+width, (a4size[1])/2-pmt[1]], -pmt[0], pmt[1])
    draw_line_with_scale([(a4size[0]-width)/2+xoffset, a4size[1]/2+height+5], width, 5)
    draw_line_with_scale([(a4size[0]-width)/2-5+xoffset, a4size[1]/2], -5, height, True)
    print('{} {} moveto'.format((a4size[0]-width+pmt[0])/2+4+xoffset, a4size[1]/2+1))
    print('(Silica aerogel) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show')
    print('{} {} moveto'.format((a4size[0]-width+pmt[0])/2+4+xoffset, a4size[1]/2-pmt[1]+1))
    print('(PMT R6683) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show')
    # '''top view'''
    # draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2], width, t2, line_width, 1.0)
    # for i in range(4):
    #   draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2+i*t1/4], width, 11.5*scale, line_width, 0.8)
    # draw_circle([(a4size[0]-width)/2+xoffset+20, (a4size[1]+t2)/2], pmt[0]/2, 0.1, -1)
    # draw_circle([(a4size[0]-width)/2+xoffset-20+width, (a4size[1]+t2)/2], pmt[0]/2, 0.1, -1)
    xoffset += 90
    '''side view'''
    draw_square([(a4size[0]-pmt[0])/2+xoffset, a4size[1]/2], pmt[0], -pmt[1], line_width, 1.0)
    for i in range(4):
      draw_square([(a4size[0]-t2)/2+i*t1/4+xoffset, a4size[1]/2], 11.5*scale, height, line_width, 0.8)
    draw_line_with_scale([(a4size[0]-t2)/2+xoffset, a4size[1]/2+height+5], t1, 5)
    draw_line_with_scale([(a4size[0]-t2)/2+xoffset, a4size[1]/2-5], t2, -5)
    # draw_line_with_scale([(a4size[0]-t2)/2-5+xoffset, a4size[1]/2], -5, height, True)
    print('newpath {} {} moveto'.format((a4size[0]+t2)/2+xoffset, a4size[1]/2))
    print('{} {} rlineto'.format(-t2, 0))
    print('{} {} rlineto'.format(0, height))
    print('{} {} rlineto closepath stroke'.format(t1, 0))
    print('{} {} moveto'.format(a4size[0]/2-22+xoffset, a4size[1]/2+(height-pmt[1])/2))
    print('(Upstream) dup stringwidth pop 0 exch -2 div 0 exch rmoveto')
    print('(Upstream) dup stringwidth pop -2 div 0 rmoveto 90 rotate show -90 rotate')
    print('{} {} moveto'.format(a4size[0]/2+45+xoffset, a4size[1]/2+(height-pmt[1])/2))
    print('(Downstream) dup stringwidth pop 0 exch -2 div 0 exch rmoveto')
    print('(Downstream) dup stringwidth pop -2 div 0 rmoveto 90 rotate show -90 rotate')
    print('{} {} moveto'.format(a4size[0]/2-40+xoffset, a4size[1]/2+50))
    # print('(width = {}) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show'
    #       .format(int(width/scale) if width/scale - int(width/scale) == 0 else width/scale))
    # print('{} {} moveto'.format((a4size[0])/2+xoffset, a4size[1]/2-pmt[1]+1))
    # print('(PMT) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show')
    return
  ''' Collimator '''
  if detector_name == 'Collimator':
    scale = 0.2
    t = 400*scale
    t_tan = 200*scale
    width = 400*scale
    w_tan = 140*scale
    height = [30*scale, 40*scale]
    open_tan = [120*scale, 110*scale] # 2016
    # open_tan = [180*scale, 160*scale] # 2017
    gap_tan = [(width-w_tan*2-open_tan[0])/2, (width-w_tan*2-open_tan[1])/2,]
    lead = [100*scale, 50*scale, 200*scale, 0.8]
    fcolor = 0.95
    unit_position = [a4size[0]-100*scale+open_tan[0], a4size[1]/2-20]
    draw_text(unit_position, '[mm]')
    # front view
    xoffset = (a4size[0]-width)/2-45
    yoffset = a4size[1]/2 + t_tan - height[0]/2 - height[1]
    draw_square([xoffset, yoffset], width, height[1], line_width, fcolor)
    draw_square([xoffset+gap_tan[1], yoffset+height[1]], w_tan, height[0], line_width, fcolor)
    draw_square([xoffset+gap_tan[0], yoffset+height[1]], w_tan, height[0], line_width, fcolor)
    draw_square([xoffset+width-gap_tan[1], yoffset+height[1]], -w_tan, height[0], line_width, fcolor)
    draw_square([xoffset+width-gap_tan[0], yoffset+height[1]], -w_tan, height[0], line_width, fcolor)
    draw_square([xoffset, yoffset+height[0]+height[1]], width, height[1], line_width, fcolor)
    for i in range(8):
      draw_square([xoffset+(i%4)*lead[0], yoffset+height[0]+height[1]*2+int(i/4)*lead[1]],
                  lead[0], lead[1], line_width, lead[3])
      draw_square([xoffset+(i%4)*lead[0], yoffset-int(1+i/4)*lead[1]],
                  lead[0], lead[1], line_width, lead[3])
    #draw_line_with_scale([xoffset, yoffset-lead[1]*2], width, -10)
    draw_line_with_scale([xoffset, yoffset+lead[1]*2+height[0]+height[1]*2], width, 8)
    draw_line_with_scale([xoffset, yoffset-lead[1]], -4, lead[1], True)
    draw_line_with_scale([xoffset, yoffset], -4, height[1], True)
    draw_line_with_scale([xoffset+gap_tan[0], yoffset+height[1]], -4, height[0], True)
    draw_line_with_scale([xoffset, yoffset-lead[1]*2], -18+gap_tan[0],
                         height[0]+height[1]*2+lead[1]*4, True)
    draw_text([xoffset+width/2, 260], 'Front view', False, 6 )
    draw_text([xoffset+6.5, yoffset-lead[1]*2+1.5], 'Lead')
    # cross-sectional view
    xoffset = (a4size[0]-width)/2+open_tan[0]+40
    yoffset = a4size[1]/2
    draw_square([xoffset, yoffset], width, t, line_width, fcolor)
    draw_square([xoffset+gap_tan[0], yoffset], w_tan, t_tan, line_width, fcolor)
    draw_square([xoffset+width-w_tan-gap_tan[0], yoffset], w_tan, t_tan, line_width, fcolor)
    draw_square([xoffset+gap_tan[1], yoffset+t_tan], w_tan, t_tan, line_width, fcolor)
    draw_square([xoffset+width-w_tan-gap_tan[1], yoffset+t_tan], w_tan, t_tan, line_width, fcolor)
    # draw_line_with_scale([xoffset, yoffset], width, -20)
    draw_line_with_scale([xoffset, yoffset], -4+gap_tan[0], t_tan, True)
    draw_line_with_scale([xoffset, yoffset+t_tan], -4+gap_tan[0], t_tan, True)
    draw_line_with_scale([xoffset, yoffset], -15+gap_tan[0], t, True)
    draw_line_with_scale([xoffset+gap_tan[0], yoffset], w_tan, -10)
    draw_line_with_scale([xoffset+w_tan+gap_tan[0], yoffset], open_tan[0], -10)
    draw_line_with_scale([xoffset+w_tan+gap_tan[1], yoffset+t], open_tan[1], 5)
    draw_text([xoffset+11+gap_tan[0], yoffset+1.5], 'Tungsten')
    draw_text([xoffset+width/2, yoffset+t+15], 'Downstream')
    draw_text([xoffset+width/2, yoffset-20], 'Upstream')
    draw_text([xoffset+width/2, 260], 'Cross-sectional top view', False, 6)
    return
  '''fbh'''
  if detector_name == 'FBH':
    scale = 2.0
    t = 2*scale
    widths = [7.5*scale for i in range(16)]
    height = 35*scale
    overlap = 2.5*scale
    zdiff = -t
    height_position = [-5, -25]
    overlap_position = [-5, -30]
    unit_position = [5, -25]
    scale_height = 20
    scale_height_offset = 0
    total_width_height = 15
    upstream_position = 20
    downstream_position = 25
  '''sch'''
  if detector_name == 'SCH':
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
  '''tof'''
  if detector_name == 'TOF':
    scale = 0.25
    t = 30*scale
    widths = [80*scale for i in range(8)]
    height = 1800*scale
    overlap = 5*scale
    zdiff = -t
    height_position = [-5, -25]
    overlap_position = [-5, -30]
    unit_position = [5, -25]
    scale_height = 20
    scale_height_offset = 5
    total_width_height = 18
    upstream_position = 25
    downstream_position = 18 + t*2
  n = len(widths)
  total_width = sum(widths) - overlap*(n-1)
  ycenter = 50
  '''height, overlap and unit'''
  draw_text([(a4size[0] - total_width)/2 + height_position[0], ycenter + height_position[1]],
            'height = {}'
            .format(int(height/scale) if height/scale - int(height/scale) == 0 else height/scale))
  # draw_text([(a4size[0] - total_width)/2 + overlap_position[0], ycenter + overlap_position[1]],
  #           'overlap = {}'
  #           .format(int(overlap/scale) if overlap/scale - int(overlap/scale) == 0 else overlap/scale))
  draw_text([(a4size[0] + total_width)/2 + unit_position[0], ycenter + unit_position[1]], '[mm]')
  '''top view'''
  print('%% top view')
  for i in range(n):
    x = ((a4size[0] - total_width)/2
            if i == 0 else x + widths[i - 1] - overlap)
    if ((detector_name == 'TOF' and (i == n/2 or i == n/2-1)) or
        (detector_name == 'SCH' and (i == n/2 or i == n/2-1))):
      if i == n/2:
        draw_text([a4size[0]/2, ycenter], '...', False, 10)
      continue
    draw_square([x, ycenter + zdiff*(1-i%2)], widths[i], t, line_width, 0.8) # (i%2+1)*0.9
    if detector_name == 'FBH' or detector_name == 'SCH':
      draw_circle([x + widths[i]/2, ycenter + zdiff*(1-i%2) + 0.5*scale], 0.5*scale)
      if i > 0:
        continue
    if detector_name == 'SCH' and i > 0:
      continue
    if detector_name == 'TOF' and i > 0:
      continue
    if detector_name == 'BH1' and i > 5:
      continue
    draw_line_with_scale([x, ycenter + zdiff*(1-i%2)],
                         widths[i], ((-scale_height*(i%2-0.5))*zdiff/t +
                                     (i%2)*scale_height_offset))
    if i == 0:
      draw_line_with_scale([x, ycenter + zdiff*(1-i%2)], -10, t, True)
  draw_line_with_scale([(a4size[0] - total_width)/2, ycenter], total_width,
                       total_width_height)
  draw_arrow([(a4size[0] + total_width)/2-widths[0], ycenter+zdiff], 0, t, 3)
  draw_line_with_scale([(a4size[0] + total_width)/2-widths[0], ycenter+zdiff], overlap, -scale_height/2)
  draw_text([a4size[0]/2, ycenter - upstream_position], 'Upstream')
  draw_text([a4size[0]/2, ycenter + downstream_position], 'Downstream')
  '''front view'''
  # ycenter = 80
  # print('%% front view')
  # even_odd = [i*2 for i in range(int(n/2)+1 if n%2 == 1 else int(n/2))]
  # even_odd += [i*2+1 for i in range(int(n/2))]
  # for i, seg in enumerate(even_odd):
  #   x = int((a4size[0] - total_width)/2 + sum(widths[:seg-n]) - seg*overlap)
  #   draw_square([x, ycenter], widths[seg], height, line_width, (seg%2+1)*0.8)
  # draw_line_with_scale([(a4size[0] - total_width)/2, ycenter], -10, height, True)
  # draw_line_with_scale([(a4size[0] - total_width)/2, ycenter+height], total_width, 10)

#_______________________________________________________________________________
def draw_line_with_scale(moveto, width, height, rotate=False):
  ''' draw line with scale '''
  if detector_name != 'BACp':
    for i in range(2):
      if rotate:
        print('newpath {} {} moveto'.format(moveto[0], moveto[1]+i*height))
        print('{} {} rlineto'.format(width, 0))
      else:
        print('newpath {} {} moveto'.format(moveto[0]+i*width, moveto[1]))
        print('{} {} rlineto'.format(0, height))
      print('closepath 0.1 setlinewidth stroke')
  if rotate:
    moveto[0] += width * 0.75
    draw_arrow(moveto, 0, height)
    if detector_name == 'Collimator':
      moveto[0] += 2.5
      if height/scale < 60:
        moveto[0] -= 2
    else:
      moveto[0] += -2
      if detector_name == 'TOF':
        moveto[0] += 1
  else:
    if width/scale > 5:
      moveto[1] += height * 0.75
      draw_arrow(moveto, width, 0)
    else:
      moveto[1] += height * 0.75
      moveto[0] += -4
      draw_arrow(moveto, 4, 0, 2)
      moveto[0] += 4 + width
      draw_arrow(moveto, 4, 0, 1)
      moveto[0] += -width/2 + 3
      if detector_name == 'FBH':
        moveto[0] += -width/2 + 5
        moveto[1] += -6
  print('{} {} moveto'.format(moveto[0] if rotate else moveto[0] + 0.5*width,
                              moveto[1]+height/2 if rotate else moveto[1]+1))
  if rotate:
    print('({}) dup stringwidth pop 0 exch -2 div 0 exch rmoveto'
          .format(int(height/scale) if height/scale - int(height/scale) == 0 else height/scale))
  real_length = (1805 if detector_name == 'TOF' and width > 100 else
                 673 if detector_name == 'SCH' and width > 100 else
                 height/scale if rotate else width/scale)
  print('({}) dup stringwidth pop -2 div 0 rmoveto {} show {}'
        .format(int(real_length) if real_length - int(real_length) == 0 else real_length,
                '90 rotate' if rotate else '',
                '-90 rotate' if rotate else ''))

#_______________________________________________________________________________
def draw_square(moveto, width, height, line_width=0.1, fill_color=0):
  ''' draw square '''
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  print('{} {} rlineto'.format(width, 0))
  print('{} {} rlineto'.format(0, height))
  print('{} {} rlineto closepath'.format(-width, 0))
  if fill_color > 0:
    print('{} setgray gsave fill grestore'.format(fill_color))
  if line_width > 0:
    print('0.0 setgray {} setlinewidth stroke'.format(line_width))

#_______________________________________________________________________________
def draw():
  ''' draw main function '''
  if len(detector_name) == 0:
    raise Exception('%% No detector name')
  print('%!PS-Adobe-3.0 EPSF-3.0')
  print('%%Title: drawing of {}'.format(detector_name))
  print('%%Creator: Shuhei Hayakawa')
  print('%%CreationDate: {}'.format(datetime.datetime.now()))
  print('%%Orientation: Portrait')
  print('%%Pages: 1')
  print('%%EndComments')
  print('')
  print('/Times-Roman findfont {} scalefont setfont'.format(default_text_size))
  print('2.8571429 2.8571429 scale % change unit to [mm]')
  draw_detector()
  print('showpage')

#_______________________________________________________________________________
def draw_text(moveto, text, rotate=False, text_size=5):
  ''' draw text '''
  print('{} {} moveto'.format(moveto[0], moveto[1]))
  print('/Times-Roman findfont {} scalefont setfont'.format(text_size))
  print('({}) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show'.format(text))
  print('/Times-Roman findfont {} scalefont setfont'.format(default_text_size))

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('detector_name', help='target detector name')
  parsed, unparsed = parser.parse_known_args()
  detector_name = parsed.detector_name.upper()
  try:
    draw()
  except:
    print(sys.exc_info()[1])
