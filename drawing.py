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
 - EMULSION
 - TRIGGER
 - MATRIX
 - DAQ
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
no_view_label = True
wdaq = 50
hdaq = 10

#_______________________________________________________________________________
def draw_arrow(moveto, width, height, mark=0, color='black'): # mark = 0:both 1:first 2:last 3:none
  ''' draw arrow '''
  if width == 0 and height == 0: return
  lw = 0.1 if detector_name == 'DAQ' else 0.1
  msize = 1.5 if detector_name == 'DAQ' else 1.0
  print('0 setgray')
  if color == 'red': print('0.9 0 0 setrgbcolor')
  elif color == 'green': print('0 0.8 0 setrgbcolor')
  elif color == 'blue': print('0 0 0.9 setrgbcolor')
  elif color == 'cyan': print('0.9 0 0 0 setcmykcolor')
  elif color == 'magenta': print('0 0.9 0 0 setcmykcolor')
  elif color == 'orange': print('0 0.53 1 0 setcmykcolor')
  elif color == 'purple': print('0 0.9 0 0.4 setcmykcolor')
  elif color == 'yellow': print('0 0 0.9 0 setcmykcolor')
  elif color == 'tag': lw = 0.5
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  if width == 0:
    theta = 0.5*math.pi
  else:
    theta = math.atan(height/width)
  if mark == 0 or mark == 1:
    print('{} {} rlineto'.format(msize*(math.cos(theta) + 0.5*math.sin(theta)),
                                 msize*(math.sin(theta) - 0.5*math.cos(theta))))
    print('{} {} rlineto'.format(msize*(-math.sin(theta)), msize*(math.cos(theta))))
    print('{} {} rlineto'.format(msize*(-math.cos(theta) + 0.5*math.sin(theta)),
                                 msize*(-math.sin(theta) - 0.5*math.cos(theta))))
    m1 = [moveto[0] + msize*(math.cos(theta) + 0.5*math.sin(theta)),
          moveto[1] + msize*(math.sin(theta) - 0.5*math.cos(theta))]
    m2 = [m1[0] - msize*math.sin(theta), m1[1] + msize*math.cos(theta)]
    mi = [0.5*(m1[0] + m2[0]), 0.5*(m1[1] + m2[1])]
  else:
    mi = moveto
  print('{} {} rlineto'.format(width, height))
  if mark == 0 or mark == 2:
    print('{} {} rlineto'.format(msize*(-math.cos(theta) + 0.5*math.sin(theta)),
                                 msize*(-math.sin(theta) - 0.5*math.cos(theta))))
    print('{} {} rlineto'.format(-msize*math.sin(theta), msize*math.cos(theta)))
    print('{} {} rlineto'.format(msize*(math.cos(theta) + 0.5*math.sin(theta)),
                                 msize*(math.sin(theta) - 0.5*math.cos(theta))))
    m3 = [moveto[0] + msize*(-math.cos(theta) + 0.5*math.sin(theta)) + width,
          moveto[1] + msize*(-math.sin(theta) - 0.5*math.cos(theta)) + height]
    m4 = [m3[0] - msize*math.sin(theta), m3[1] + msize*math.cos(theta)]
    mf = [0.5*(m3[0] + m4[0]), 0.5*(m3[1] + m4[1])]
  else:
    mf = [moveto[0] + width, moveto[1] + height]
  print('closepath gsave fill grestore {} setlinewidth stroke'
        .format(0.0001 if mark != 3 else lw))
  if mark != 3:
    print('newpath {} {} moveto'.format(mi[0], mi[1]))
    print('{} {} rlineto'.format(mf[0] - mi[0], mf[1] - mi[1]))
    print('closepath gsave fill grestore {} setlinewidth stroke'.format(lw))

#_______________________________________________________________________________
def draw_circle(moveto, r, fill_color=1.0, a=0, b=360, line_width=0.1):
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
  ''' EMULSION '''
  if 'EMULSION' in detector_name:
    return draw_emulsion()
  ''' TRIGGER '''
  if 'TRIG' in detector_name:
    return draw_trigger()
  if 'MATRIX' in detector_name:
    return draw_matrix()
  if 'DAQ' in detector_name:
    return draw_daq()
  ''' BFT '''
  if detector_name == 'BFT':
    scale = 12.0
    phi = 1.0*scale
    d = phi*math.sqrt(3)/2
    n = 20
    xcenter = a4size[0]/2
    ycenter = a4size[1]/2
    for i in range(n):
      if i == n/2 or i == n/2-1 or i == n/2+1 or i == n/2-2:
        continue
      draw_circle([xcenter+phi*i/2-phi*(n/4-0.25), ycenter + d*(i%2)], phi/2)
    draw_text([xcenter, ycenter+d/2], '...', False, 10)
    draw_text([xcenter, ycenter-phi-10-2.5], 'Upstream')
    draw_text([xcenter, ycenter+d+phi+10], 'Downstream')
    draw_line_with_scale([xcenter-phi*(n+1)/4, ycenter-phi/2], phi, -10)
    return
  ''' BH1 '''
  if detector_name == 'BH1':
    scale = 0.5
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
    total_width_height = 26
    upstream_position = 18
    downstream_position = 30
    pmt = [22*scale, 88*scale]
    light_guide = [20*scale, 90*scale, 10*scale]
    light_guide_seg = [0, 1, 3, 5, 7, 9, 10]
    view_position = -105
    front_view_offset = 30
    pmt_name = 'PMT H6524MOD'
    sci_name = 'Scintillator BC420'
    pmt_position = [-21, -6]
    light_guide_position = [-22, 15]
    sci_position = [-25, 2]
  ''' BH2 '''
  if detector_name == 'BH2':
    scale = 0.25
    t = 6*scale
    widths = [120*scale]
    height = 40*scale
    overlap = 0
    pmt = [60*scale, 200*scale]
    light_guide = [55*scale, 95*scale, 15*scale]
    light_guide_seg = [0]
    zdiff = 0
    height_position = [-5, -10]
    overlap_position = [-5, -20]
    unit_position = [5, -20]
    scale_height = 20
    scale_height_offset = 0
    total_width_height = 26
    upstream_position = 12
    downstream_position = 21
    view_position = -70
    front_view_offset = 30
    #pmt_name = 'PMT H2431-50'
    pmt_name = 'PMT H10570'
    sci_name = 'Scintillator BC420'
    pmt_position = [-16, -6]
    light_guide_position = [-22, 5]
    sci_position = [-27, 2]
  ''' BAC '''
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
  ''' FBH '''
  if detector_name == 'FBH':
    scale = 1.2
    t = 2*scale
    phi = 1*scale
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
    pmt = [4*scale, 2*scale]
    light_guide = [1*scale, 20*scale, 0*scale]
    light_guide_seg = []
    view_position = -105
    front_view_offset = 30
    pmt_name = 'MPPC circuit board'
    sci_name = 'Scintillator EJ-212'
    pmt_position = [-len(widths)*pmt[0]/2-21, 1+pmt[1]]
    light_guide_position = [-len(widths)*pmt[0]/2-18, height/2+light_guide[1]/2]
    sci_position = [-sum(widths)/2+2*scale, 4]
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
  ''' TOF '''
  if detector_name == 'TOF':
    scale = 0.08
    t = 30*scale
    widths = [80*scale for i in range(24)]
    height = 1800*scale
    overlap = 5*scale
    zdiff = -t
    height_position = [-5, -25]
    overlap_position = [-5, -30]
    unit_position = [15, -15]
    scale_height = 20
    scale_height_offset = 5
    total_width_height = 18
    upstream_position = 15
    downstream_position = 18 + t*2
    pmt = [60*scale, 235*scale]
    light_guide = [55*scale, 160*scale, 20*scale]
    light_guide_seg = []
    view_position = -70
    front_view_offset = 30
    pmt_name = 'PMT H1949'
    sci_name = 'Scintillator BC420'
    pmt_position = [-86, -4]
    light_guide_position = [-92, 140]
    sci_position = [-93, 2]
  ''' BC3,4 '''
  if 'BC' in detector_name:
    scale = 12.0
    wire_spacing = [3*scale, 4*scale] # anode-anode, anode-cathode
    width = wire_spacing[0]*3.5
    xcenter = a4size[0]/2
    ycenter = a4size[1]/2 - wire_spacing[1]
    for i in range(3):
      draw_arrow([xcenter-width/2, ycenter+i*wire_spacing[1]], width, 0, 3)
      if i != 0:
        for w in range(int(width/wire_spacing[0])+1):
          draw_circle([xcenter-width/2+w*wire_spacing[0], ycenter+(i-0.5)*wire_spacing[1]], 1,
                      1.0 if i == 1 else 0.1)
          draw_circle([xcenter-width/2+(w+0.5)*wire_spacing[0], ycenter+(i-0.5)*wire_spacing[1]], 1,
                      0.1 if i == 1 else 1.0)
    draw_text([xcenter-width/2, ycenter+1.5*wire_spacing[1]-6.5], 'Anode')
    draw_text([xcenter-width/2, ycenter+1.5*wire_spacing[1]-13], 'wire')
    draw_text([xcenter-width/2+wire_spacing[0]/2, ycenter+1.5*wire_spacing[1]-6.5], 'Potential')
    draw_text([xcenter-width/2+wire_spacing[0]/2, ycenter+1.5*wire_spacing[1]-13], 'wire')
    draw_text([xcenter-width/2+15, ycenter+2*wire_spacing[1]+1.5], 'Cathode plane')
    #draw_text([xcenter-wire_spacing[0]/4+20, ycenter-wire_spacing[1]/4], 'Charged particle')
    draw_text([xcenter+wire_spacing[0]/4+20, ycenter+wire_spacing[1]*2.25], 'Charged particle')
    draw_arrow([xcenter-wire_spacing[0]/4, ycenter-wire_spacing[1]/4],
               wire_spacing[0]/2, wire_spacing[1]/2+wire_spacing[1]*2, 2)
    draw_line_with_scale([xcenter-width/2, ycenter+1.5*wire_spacing[1]], wire_spacing[0], 10)
    draw_line_with_scale([xcenter-width/2+wire_spacing[0]*3, ycenter+1.5*wire_spacing[1]],
                         -6, wire_spacing[1]/2, True)
    draw_arrow([xcenter+wire_spacing[0]/4*0.4, ycenter+1.5*wire_spacing[1]], wire_spacing[0]/4*0.6-1, 0)
    draw_arrow([xcenter-wire_spacing[0]/4+1, ycenter+0.5*wire_spacing[1]], wire_spacing[0]/4*0.6-1, 0)
    draw_text([xcenter+wire_spacing[0]/4+7.5, ycenter+1.5*wire_spacing[1]-6.5], 'Drift length')
    draw_text([xcenter-wire_spacing[0]/4-7.5, ycenter+0.5*wire_spacing[1]+5.], 'Drift length')
    draw_text([xcenter+width/2, ycenter-wire_spacing[1]/4], '[mm]')
    return
  ''' SDC1 '''
  if detector_name == 'SDC1':
    scale = 4.0
    wire_spacing = 6*scale # anode-anode and field-field
    r = 2*math.sqrt(3)*scale
    width = wire_spacing*4
    xcenter = a4size[0]/2
    ycenter = a4size[1]/2 - wire_spacing
    for i in range(8):
      for w in range(int(width/wire_spacing)+1):
        draw_circle([xcenter-width/2+(w+0.5*(i%2))*wire_spacing, ycenter+i*r*0.5], 1,
                    0.1 if i == 2 or i == 5 else 1.0)
    draw_text([xcenter-width/2-14, ycenter+3*r-1], 'Field wire')
    draw_text([xcenter-width/2-15, ycenter+r-1], 'Anode wire')
    # #draw_text([xcenter-wire_spacing[0]/4+20, ycenter-wire_spacing[1]/4], 'Charged particle')
    draw_text([xcenter+wire_spacing/4+22, ycenter+r*4.5], 'Charged particle')
    draw_arrow([xcenter+wire_spacing/8, ycenter-r],
               wire_spacing/4, 5.5*r, 2)
    draw_line_with_scale([xcenter-width/2, ycenter-1], wire_spacing, -4)
    length = math.sqrt(pow(5.5*r, 2) + pow(wire_spacing/4, 2))/(1.05*scale)
    normal_vector = [5.5*r/length, -wire_spacing/4/length]
    draw_arrow([xcenter+0.25*wire_spacing+0.2*scale, ycenter+2.5*r+0.1*scale],
               normal_vector[0], normal_vector[1])
    draw_arrow([xcenter+1+0.01*scale, ycenter+r-0.01*scale],
               normal_vector[0], normal_vector[1])
    draw_text([xcenter+r+5, ycenter+2.5*r+2.5], 'Drift length', False, 4)
    draw_text([xcenter-5, ycenter+r+2.5], 'Drift length', False, 4)
    draw_text([xcenter+width/2+r*2, ycenter-wire_spacing/2], '[mm]')
    return
  n = len(widths)
  total_width = sum(widths) - overlap*(n-1)
  has_pmt = (True if detector_name == 'BH1' or detector_name == 'BH2'
             or detector_name == 'TOF' else False)
  mizo = (pmt[0]-light_guide[0])/2 #if has_pmt else 0
  '''front view'''
  ycenter = (a4size[1] - pmt[1]*2 - light_guide[1]*2 if detector_name == 'BH1' else
             a4size[1] - pmt[1]*3 - light_guide[1]*2 if detector_name == 'BH2' else
             a4size[1]/2 - height/2 - 34*scale if detector_name == 'FBH' else
             a4size[1]/2 - height/2)
  if not no_view_label:
    draw_text([a4size[0]/2+view_position, ycenter+height/2+front_view_offset], 'Front view', False, 6)
  print('%% front view')
  if n%2 == 1:
    even_odd = [i*2 for i in range(int(n/2)+1 if n%2 == 1 else int(n/2))]
    even_odd += [i*2+1 for i in range(int(n/2))]
  else:
    even_odd = [i*2+1 for i in range(int(n/2)+1 if n%2 == 1 else int(n/2))]
    even_odd += [i*2 for i in range(int(n/2))]
  for i, seg in enumerate(even_odd):
    if detector_name == 'TOF':
      if i == n/2: draw_text([a4size[0]/2, ycenter+height/2], '...', False, 10)
      if abs(seg -n/2+0.5) < 2: continue
    x = (a4size[0] - total_width)/2 + sum(widths[:seg-n]) - seg*overlap
    draw_square([x, ycenter], widths[seg], height, line_width,
                ((seg%2+1 if n%2 == 1 else 2-seg%2)*0.8))
    if detector_name == 'TOF' or detector_name == 'FBH':
      x += (widths[seg] - pmt[0])/2
      if detector_name == 'FBH': x = a4size[0]/2+(-n/2+seg)*pmt[0]
      y = ycenter-pmt[1]-light_guide[1]
      xsci = (a4size[0] - total_width)/2 + sum(widths[:seg-n]) - seg*overlap
      if detector_name == 'FBH': xsci += (widths[seg] - phi)/2
      draw_polygon([x+mizo+light_guide[0], y+pmt[1]+light_guide[2]],
                   [[0, -light_guide[2]],
                    [-light_guide[0], 0],
                    [0, light_guide[2]],
                    [xsci-x-mizo, light_guide[1]-light_guide[2]],
                    [widths[seg] if detector_name == 'TOF' else phi, 0]], 0.3, 1.0)
      y = ycenter+height+light_guide[1]
      draw_square([x, y], pmt[0], pmt[1], 0.3)
      draw_polygon([x+mizo+light_guide[0], y-light_guide[2]],
                   [[0, light_guide[2]],
                    [-light_guide[0], 0],
                    [0, -light_guide[2]],
                    [xsci-x-mizo, -light_guide[1]+light_guide[2]],
                    [widths[seg] if detector_name == 'TOF' else phi, 0],
                   ], 0.3, 1.0)
      draw_arrow([x+mizo, y-light_guide[2]], light_guide[0], 0, 3)
  if detector_name == 'FBH':
    draw_square([(a4size[0]-total_width)/2, y], total_width, pmt[1], 0.3, 0.4)
    draw_square([(a4size[0]-n*pmt[0])/2, y+pmt[1]], n*pmt[0], pmt[1], 0.3)
    draw_text([(a4size[0]-total_width)/2-22, y], 'Fiber fixing frame')
    draw_arrow([(a4size[0]-total_width)/2-2, y+pmt[1]/2], 4, 0, 3)
  for i, seg in enumerate(light_guide_seg):
    j = i
    if detector_name == 'BH1':
      if i == len(light_guide_seg) - 2:
        j = i + 1
      if i == len(light_guide_seg) - 1:
        j = i - 1
    seg = light_guide_seg[j]
    x = a4size[0]/2+(-len(light_guide_seg)/2+j)*pmt[0]
    y = ycenter-pmt[1]-light_guide[1]
    xsci = (a4size[0] - total_width)/2 + sum(widths[:seg-n]) - seg*overlap
    draw_polygon([x+mizo+light_guide[0], y+pmt[1]],
                 [[-light_guide[0], 0],
                  [xsci-x-mizo, light_guide[1]],
                  [widths[seg], 0]], 0.3, 1.0)
    y = ycenter+height+light_guide[1]
    draw_square([x, y], pmt[0], pmt[1], 0.3)
    xsci = (a4size[0] - total_width)/2 + sum(widths[:seg-n]) - seg*overlap
    draw_polygon([x+mizo+light_guide[0], y-light_guide[2]],
                 [[0, light_guide[2]],
                  [-light_guide[0], 0],
                  [0, -light_guide[2]],
                  [xsci-x-mizo, -light_guide[1]+light_guide[2]],
                  [widths[seg], 0],
                 ], 0.3, 1.0)
  draw_square([(a4size[0]-total_width)/2, ycenter-light_guide[1]-1], total_width,
              light_guide[1]*0.5, 0)
  for i in range(1 if detector_name == 'BH1' or detector_name == 'BH2' else 0):
    y = ycenter-light_guide[1]+(2*i-1)*light_guide[2]+(1-i)*(height+light_guide[1]*2)
    draw_arrow([a4size[0]/2+(-len(light_guide_seg)/2)*pmt[0]+mizo, y],
               light_guide[0], 0, 3)
    if detector_name == 'BH1':
      draw_arrow([a4size[0]/2+(-len(light_guide_seg)/2+1)*pmt[0]+mizo, y],
                 pmt[0]*(len(light_guide_seg)-2) - mizo*2, 0, 3)
      draw_arrow([a4size[0]/2+(len(light_guide_seg)/2-1)*pmt[0]+mizo, y],
                 light_guide[0], 0, 3)
  draw_line_with_scale([(a4size[0] - total_width)/2, ycenter], -10, height, True)
  draw_text([a4size[0]/2-len(light_guide_seg)/2*pmt[0]+pmt_position[0],
             ycenter+height+light_guide[1]+pmt[1]+pmt_position[1]],
            pmt_name)
  draw_arrow([a4size[0]/2-len(light_guide_seg)/2*pmt[0]+pmt_position[0] +
              (21 if detector_name == 'FBH' else 13 if detector_name == 'TOF' else
               19 if detector_name == 'BH1' else 14.5),
              ycenter+height+light_guide[1]+pmt[1]+pmt_position[1]], 4, -2, 3)
  draw_text([a4size[0]/2-len(light_guide_seg)/2*pmt[0]+light_guide_position[0],
             ycenter+light_guide[1]+light_guide_position[1]],
            'Acrylic light guide' if has_pmt else 'WLS fiber')
  draw_arrow([a4size[0]/2-len(light_guide_seg)/2*pmt[0]+light_guide_position[0] +
              (11.5 if detector_name == 'FBH' else 19),
              ycenter+light_guide[1]+light_guide_position[1]], 4, -2, 3)
  draw_text([a4size[0]/2-len(light_guide_seg)/2*pmt[0]+sci_position[0],
             ycenter+height+sci_position[1]], sci_name)
  draw_arrow([a4size[0]/2-len(light_guide_seg)/2*pmt[0]+sci_position[0]+19,
              ycenter+height+sci_position[1]], 4, -8, 3)
  nwave = int(total_width/5)
  for i in range(nwave):
    for j in range(2):
      draw_wave([(a4size[0]-total_width)/2+total_width/nwave*i,
                 (ycenter-light_guide[1]*0.7+j*1 if detector_name == 'BH2' else
                  ycenter-light_guide[1]*0.6+j*1 if detector_name == 'BH1' else
                  ycenter-light_guide[1]*0.8+j*1 if detector_name == 'TOF' else
                  ycenter-light_guide[1]*0.7+j*1 )],
                total_width/nwave, 3*(i%2-0.5))
  '''top view'''
  ycenter = 30 if detector_name == 'FBH' else 50 if detector_name != 'TOF' else 30
  print('%% top view')
  if not no_view_label:
    draw_text([a4size[0]/2+view_position, ycenter+t+2], 'Cross-sectional', False, 6)
    draw_text([a4size[0]/2+view_position, ycenter-2], 'top view', False, 6)
  for i in range(n):
    x = ((a4size[0] - total_width)/2
            if i == 0 else x + widths[i - 1] - overlap)
    if ((detector_name == 'TOF' and (abs(i -n/2+0.5) < 2)) or
        (detector_name == 'SCH' and (i == n/2 or i == n/2-1))):
      if i == n/2:
        draw_text([a4size[0]/2, ycenter], '...', False, 10)
      continue
    draw_square([x, ycenter + zdiff*(1-i%2)], widths[i], t, line_width,
                ((i%2+1)*0.8 if n%2 == 1 else (2-i%2)*0.8))
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
    if i == 0:
      draw_line_with_scale([x, ycenter + zdiff*(1-i%2)], -10, t, True)
    draw_line_with_scale([x, ycenter + zdiff*(1-i%2)],
                         widths[i], ((-scale_height*(i%2-0.5))*zdiff/t + (i%2)*scale_height_offset
                                     if abs(zdiff)>0 else t+10))
  if n > 1:
    draw_line_with_scale([(a4size[0] - total_width)/2, ycenter], total_width,
                         total_width_height)
  draw_arrow([(a4size[0] + total_width)/2-widths[0], ycenter+zdiff], 0, t, 3)
  if overlap > 0:
    draw_line_with_scale([(a4size[0] + total_width)/2-widths[0], ycenter+zdiff], overlap, -scale_height/2)
  draw_text([a4size[0]/2, ycenter - upstream_position], 'Upstream')
  draw_text([a4size[0]/2, ycenter + downstream_position], 'Downstream')
  '''height, overlap and unit'''
  # draw_text([(a4size[0] - total_width)/2 + height_position[0], ycenter + height_position[1]],
  #           'height = {}'
  #           .format(int(height/scale) if height/scale - int(height/scale) == 0 else height/scale))
  # draw_text([(a4size[0] - total_width)/2 + overlap_position[0], ycenter + overlap_position[1]],
  #           'overlap = {}'
  #           .format(int(overlap/scale) if overlap/scale - int(overlap/scale) == 0 else overlap/scale))
  draw_text([(a4size[0] + total_width)/2 + unit_position[0], ycenter + unit_position[1]], '[mm]')

#_______________________________________________________________________________
def draw_line_with_scale(moveto, width, height, rotate=False):
  ''' draw line with scale '''
  rwidth = width/scale
  if abs(rwidth - round(rwidth)) < 0.0001:
    rwidth = round(rwidth)
  if detector_name == 'EMULSION':
    lr = -1 if rotate else 1
    rotate= False
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
    if detector_name == 'Collimator' or 'BC' in detector_name:
      moveto[0] += 2.5
      if height/scale < 60:
        moveto[0] -= 2
    else:
      if height < 10:
        moveto[0] += -3
      if detector_name == 'TOF':
        moveto[0] += 1
  else:
    if detector_name == 'EMULSION' and width > 2:
      moveto[1] += height * 0.75
      draw_arrow(moveto, width, 0)
      moveto[1] += height * 0.25
      if rwidth == 100:
        moveto[0] += lr*width*0.75
    elif width > 5 or 'BC' in detector_name or detector_name == 'BFT':
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
    print('({}) dup stringwidth pop 0 exch -2 div 0 exch rmoveto'.format(rwidth))
  real_length = (11760 if detector_name == 'EMULSION' and rwidth > 1000 else
                 1805 if detector_name == 'TOF' and width > 100 else
                 673 if detector_name == 'SCH' and width > 100 else
                 height/scale if rotate else rwidth)
  print('({}) dup stringwidth pop -2 div 0 rmoveto {} show {}'
        .format(round(real_length) if abs(real_length - round(real_length)) < 0.001 else real_length,
                '90 rotate' if rotate else '',
                '-90 rotate' if rotate else ''))

#_______________________________________________________________________________
def draw_polygon(moveto, array, line_width=0.1, fill_color=1.0):
  ''' draw polygon '''
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  for l in array:
    print('{} {} rlineto'.format(l[0], l[1]))
  print('closepath')
  if fill_color <= 1.0:
    print('{} setgray gsave fill grestore'.format(fill_color))
  if line_width > 0:
    print('0.0 setgray {} setlinewidth stroke'.format(line_width))

#_______________________________________________________________________________
def draw_square(moveto, width, height, line_width=0.1, fill_color=1.0):
  ''' draw square '''
  if detector_name == 'DAQ':
    line_width = 0.1
  print('0 setgray')
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  print('{} {} rlineto'.format(width, 0))
  print('{} {} rlineto'.format(0, height))
  print('{} {} rlineto closepath'.format(-width, 0))
  if fill_color >= 0:
    print('{} setgray gsave fill grestore 0 setgray'.format(fill_color))
  if line_width > 0:
    print('{} setlinewidth gsave stroke grestore'.format(line_width))

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
def draw_wave(moveto, width, height):
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  print('{} {} {} {} {} {} curveto'.format(moveto[0]+width*1/3, moveto[1]+height,
                                           moveto[0]+width*2/3, moveto[1]+height,
                                           moveto[0]+width, moveto[1]))
  print('gsave 0.1 setlinewidth stroke closepath')

#_______________________________________________________________________________
def draw_text(moveto, text, rotate=False, text_size=5):
  ''' draw text '''
  print('0 setgray')
  print('/Times-Roman findfont {} scalefont setfont'.format(text_size))
  print('{} {} moveto'.format(moveto[0], moveto[1]))
  if rotate:
    print('({}) dup stringwidth pop 0 exch -2 div 0 exch rmoveto'.format(text))
  print('({}) dup stringwidth pop 2 div 0 exch sub 0 rmoveto {} show {}'
        .format(text, '90 rotate' if rotate else '', '-90 rotate' if rotate else ''))
  print('/Times-Roman findfont {} scalefont setfont'.format(default_text_size))

#_______________________________________________________________________________
def draw_text_box(moveto, text, text_size=5.):
  ''' draw text box '''
  t = text.split()
  w = (text_size*max(len(t[0]), len(t[1])) if len(t) > 1 else text_size*len(text))
  h = text_size*9 if len(t) > 1 else text_size*2
  if detector_name == 'DAQ':
    w = wdaq
    h = hdaq
  draw_square(moveto, w, h, 0.1, 0.95 if 'RM' in text else -1)
  print('0 setgray')
  print('/Times-Roman findfont {} scalefont setfont'.format(text_size))
  print('{} {} moveto'.format(moveto[0]+w/2, moveto[1]))
  print('({}) dup stringwidth pop neg 2 div 0 rmoveto'.format(text))
  print('0 {} rmoveto show'.format(h/2.-text_size/3))
  print('/Times-Roman findfont {} scalefont setfont'.format(default_text_size))

#_______________________________________________________________________________
def draw_logic_or(moveto, size=1.0, etcline=True):
  ''' draw AND logic '''
  width = 3.0*size
  height = 2.4*size
  if etcline:
    for i in range(3):
      draw_arrow([moveto[0]-width*0.3, moveto[1]+height*(0.8-i*0.1)], width*0.6, 0, 3)
      draw_circle([moveto[0], moveto[1]+height*(0.5-i*0.1)], 0.04*size, 0.1)
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  for i in range(2):
    width = width*0.3 if i == 1 else width
    offset = width*0.2 if i == 0 else 0
    print('{} {} {} {} {} {} curveto'.format(moveto[0]+width, moveto[1]+height*(1+i%2)/3-offset,
                                             moveto[0]+width, moveto[1]+height*(2-i%2)/3+offset,
                                             moveto[0], moveto[1]+height*(1-i%2)))
  print('closepath gsave 1 setgray fill grestore 0 setgray 0.1 setlinewidth stroke')

#_______________________________________________________________________________
def draw_logic_and(moveto, size=1.0, etcline=False):
  ''' draw AND logic '''
  width = 1.*size
  height = 1.5*size
  #moveto[1] = moveto[1] - 0.25*size
  moveto[1] = moveto[1] + 0.5*size
  if etcline:
    for i in range(3):
      draw_arrow([moveto[0]-width*0.3, moveto[1]+height*(0.8-i*0.1)], width*0.6, 0, 3)
      draw_circle([moveto[0]-width*0.15, moveto[1]+height*(0.5-i*0.1)], 0.04*size, 0.1)
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  # print('{} {} {} {} {} {} curveto'.format(moveto[0]+width, moveto[1]+height*1/3,
  #                                          moveto[0]+width, moveto[1]+height*2/3,
  #                                          moveto[0], moveto[1]+height))
  print('{} {} {} {} {} arc closepath'.format(moveto[0], moveto[1], height/2, -90, 90))
  print('gsave 1 setgray fill grestore 0 setgray 0.1 setlinewidth stroke')

#_______________________________________________________________________________
def draw_emulsion():
  global scale
  unit = 1e0
  scale = 0.04*unit
  width = 10*345*scale
  #height = 10*350*scale
  height = 40
  thin_gel = 100*scale/unit
  thin_base = 180*scale/unit
  thick_gel = 480*scale/unit # designed to be 450
  thick_base = 40*scale/unit
  space = 0
  zigzag = 2
  x = 10
  y = 40
  lw = 0.4
  fc = 0.9
  ''' thin '''
  draw_square([x, y], thin_gel, height, lw, fc)
  draw_square([x+thin_gel, y], thin_base, height, lw)
  draw_square([x+thin_gel+thin_base, y], thin_gel, height, lw, fc)
  draw_line_with_scale([x, y+height], thin_gel, 5, True)
  draw_line_with_scale([x+thin_gel, y+height], thin_base, 10)
  draw_line_with_scale([x+thin_gel+thin_base, y+height], thin_gel, 5)
  x = x + 2*thin_gel + thin_base + space
  height -= zigzag
  draw_square([x, y], thick_gel, height, lw, fc)
  draw_square([x+thick_gel, y], thick_base, height, lw)
  draw_square([x+thick_gel+thick_base, y], thick_gel, height, lw, fc)
  height += zigzag
  x = x + 2*thick_gel + thick_base + space
  draw_square([x, y], thick_gel, height, lw, fc)
  draw_square([x+thick_gel, y], thick_base, height, lw)
  draw_square([x+thick_gel+thick_base, y], thick_gel, height, lw, fc)
  draw_line_with_scale([x, y+height], thick_gel, 5)
  draw_line_with_scale([x+thick_gel, y+height], thick_base, 15)
  draw_line_with_scale([x+thick_gel+thick_base, y+height], thick_gel, 5)
  x = x + 2*thick_gel + thick_base + space
  x = x + (2*thick_gel + thick_base + space)/4
  draw_text([x-0.5-space/2, y+height*0.625], '...', False, 12)
  x = x + (2*thick_gel + thick_base + space)/4
  height += zigzag
  draw_square([x, y], thick_gel, height, lw, fc)
  draw_square([x+thick_gel, y], thick_base, height, lw)
  draw_square([x+thick_gel+thick_base, y], thick_gel, height, lw, fc)
  height -= zigzag
  x = x + 2*thick_gel + thick_base + space
  draw_square([x, y], thin_gel, height, lw, fc)
  draw_square([x+thin_gel, y], thin_base, height, lw)
  draw_square([x+thin_gel+thin_base, y], thin_gel, height, lw, fc)
  x = x + 2*thin_gel + thin_base
  ''' crip '''
  draw_square([9, y-1], x-8, height/4, 0, 1)
  ''' scale '''
  draw_line_with_scale([10, y+height+20], x-10, 5)
  draw_text([10+thin_gel+thin_base/2, y+height/4-8], 'thin plate')
  draw_text([(10+x)/2, y+height/4-8], '11 thick plates')
  draw_text([x-thin_gel-thin_base/2, y+height/4-8], 'thin plate')
  draw_text([x+15, y], '[um]')

#_______________________________________________________________________________
def draw_trigger():
  dsize = 5
  x = 10
  y = a4size[1]-dsize*10
  ypitch = dsize*3
  l = 12
  ''' BH1 '''
  draw_text_box([x, y], 'BH1', dsize)
  draw_arrow([x+3*dsize, y+dsize], l, 0, 3)
  draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  draw_arrow([x+l+5*dsize, y+dsize], l, 0, 3)
  draw_logic_or([x+2*l+(5+0.9)*dsize, y+(1-0.8*2.4)*dsize], dsize)
  draw_arrow([x+2*l+(8.15)*dsize, y+(1-0.8*2.4+1.2)*dsize], l, 0, 3)
  ''' BH2 '''
  y = y - ypitch
  draw_text_box([x, y], 'BH2', dsize)
  draw_arrow([x+3*dsize, y+dsize], 3*l+5.15*dsize, 0, 3)
  draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  draw_logic_and([x+3*l+8.15*dsize, y+dsize], ypitch-0.8*dsize)
  draw_arrow([x+3*l+7.55*dsize+0.75*ypitch, y+0.6*dsize+0.5*ypitch], l, 0, 3)
  draw_arrow([x+4*l+7.55*dsize+0.75*ypitch, y-0.5*ypitch+dsize], 0, ypitch-0.4*dsize, 3)
  draw_arrow([x+4*l+7.55*dsize+0.75*ypitch, y-0.5*ypitch+dsize], l, 0, 3)
  ''' BAC '''
  y = y - ypitch
  draw_text_box([x, y], 'BAC1', dsize)
  draw_arrow([x+4*dsize, y+dsize], l, 0, 3)
  draw_arrow([x+l+4*dsize, y+dsize], 0, -0.35*ypitch, 3)
  draw_arrow([x+l+4*dsize, y+dsize-0.35*ypitch], l, 0, 3)
  y = y - ypitch
  draw_text_box([x, y], 'BAC2', dsize)
  draw_arrow([x+4*dsize, y+dsize], l, 0, 3)
  draw_arrow([x+l+4*dsize, y+dsize], 0, 0.35*ypitch, 3)
  draw_arrow([x+l+4*dsize, y+dsize+0.35*ypitch], l, 0, 3)
  draw_arrow([x+2*l+4.5*dsize, y+dsize+0.5*ypitch], 4*l+3.55*dsize, 0, 3)
  #draw_logic_and([x+l+4*dsize, y+dsize], ypitch)
  draw_logic_or([x+2*l+3.4*dsize, y+dsize+(ypitch-2.4*dsize)/2], dsize, False)
  draw_circle([x+5*l+7.55*dsize+0.75*ypitch-1, y+dsize+0.5*ypitch], 1)
  # K-beam
  draw_logic_and([x+5*l+7.55*dsize+0.75*ypitch, y+dsize+0.5*ypitch], ypitch)
  draw_text([x+5*l+7.55*dsize+1.125*ypitch, y+dsize+1.9*ypitch], 'K beam')
  draw_arrow([x+5*l+7.55*dsize+1.5*ypitch, y+dsize+ypitch], 2*l, 0, 3)
  draw_arrow([x+7*l+7.55*dsize+1.5*ypitch, y+dsize-ypitch], 0, 2*ypitch, 3)
  draw_arrow([x+7*l+7.55*dsize+1.5*ypitch, y+dsize-ypitch], l, 0, 3)
  ''' PVAC '''
  y = y - ypitch
  draw_text_box([x, y], 'PVAC', dsize)
  draw_arrow([x+4*dsize, y+dsize], 5*l+3.55*dsize+0.75*ypitch, 0, 3)
  ''' FAC '''
  y = y - ypitch
  draw_text_box([x, y], 'FAC', dsize)
  draw_arrow([x+3*dsize, y+dsize], 3*l, 0, 3)
  draw_arrow([x+3*l+3*dsize, y+dsize], 0, 0.5*ypitch, 3)
  draw_arrow([x+3*l+3*dsize, y+dsize+0.5*ypitch], 2*l+4.55*dsize+0.75*ypitch, 0, 3)
  draw_circle([x+5*l+7.55*dsize+0.75*ypitch-1, y+dsize+0.5*ypitch], 1)
  # K scat
  draw_text([x+5*l+7.55*dsize+1.125*ypitch, y+dsize+1.4*ypitch], 'K scat')
  draw_logic_and([x+5*l+7.55*dsize+0.75*ypitch, y+dsize], ypitch)
  ''' TOF '''
  y = y - ypitch
  draw_text_box([x, y], 'TOF', dsize)
  draw_arrow([x+3*dsize, y+dsize], l, 0, 3)
  draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  draw_arrow([x+l+5*dsize, y+dsize], l, 0, 3)
  draw_logic_or([x+2*l+5.9*dsize, y-0.92*dsize], dsize)
  draw_arrow([x+2*l+8.15*dsize, y+0.28*dsize], l, 0, 3)
  draw_arrow([x+3*l+8.15*dsize, y+0.28*dsize], 0, 0.72*dsize+ypitch, 3)
  draw_arrow([x+3*l+8.15*dsize, y+dsize+ypitch], 2*l-0.6*dsize+0.75*ypitch, 0, 3)
  draw_circle([x+1.5*l+5*dsize, y+dsize], 1, 0.1)
  draw_arrow([x+5*l+7.55*dsize+1.5*ypitch, y+dsize+1.5*ypitch], 3*l, 0, 3)
  # KK
  #draw_text([x+8*l+7.55*dsize+1.875*ypitch, y+dsize+2.4*ypitch], '(K, K)')
  draw_logic_and([x+8*l+7.55*dsize+1.5*ypitch, y+dsize+ypitch], ypitch)
  draw_arrow([x+8*l+7.55*dsize+2.25*ypitch, y+dsize+1.5*ypitch], 2*l, 0, 2)
  #draw_text([x+9*l+7.55*dsize+2.25*ypitch, y+2.5*dsize+1.5*ypitch], '(K,K)')
  draw_text([x+9*l+7.55*dsize+2.25*ypitch, y+1.5*dsize+1.5*ypitch], 'Trigger')
  draw_text([x+9*l+7.55*dsize+2.25*ypitch, a4size[1]-dsize*10], 'MT: Mean timer')
  y = y - ypitch
  draw_arrow([x+1.5*l+5*dsize, y+dsize], 0, ypitch, 3)
  draw_arrow([x+1.5*l+5*dsize, y+dsize], 3.5*l+2.55*dsize+0.75*ypitch, 0, 3)
  for i in range(3):
    draw_arrow([x+5*l+2.75*dsize+1.125*ypitch, y+dsize-i*0.24*dsize], 1.8*dsize, 0, 3)
    draw_circle([x+5*l+3.65*dsize+1.125*ypitch, y+dsize-(i+3)*0.24*dsize], 0.04*dsize, 0.1)
  ''' SCH '''
  y = y - ypitch
  draw_text_box([x, y], 'SCH', dsize)
  draw_arrow([x+3*dsize, y+dsize], 5*l+4.55*dsize+0.75*ypitch, 0, 3)
  for i in range(3):
    draw_arrow([x+5*l+2.75*dsize+1.125*ypitch, y+dsize-i*0.24*dsize], 1.8*dsize, 0, 3)
    draw_circle([x+5*l+3.65*dsize+1.125*ypitch, y+dsize-(i+3)*0.24*dsize], 0.04*dsize, 0.1)
  ''' FBH '''
  y = y - ypitch
  draw_text_box([x, y], 'FBH', dsize)
  draw_arrow([x+3*dsize, y+dsize], 5*l+4.55*dsize+0.75*ypitch, 0, 3)
  for i in range(3):
    draw_arrow([x+5*l+2.75*dsize+1.125*ypitch, y+dsize-i*0.24*dsize], 1.8*dsize, 0, 3)
    draw_circle([x+5*l+3.65*dsize+1.125*ypitch, y+dsize-(i+3)*0.24*dsize], 0.04*dsize, 0.1)
  ''' HUL Matrix '''
  draw_text_box([x+5*l+4.55*dsize+1.125*ypitch, y-dsize], 'HUL Matrix', dsize)
  #draw_text_box([x+5*l+7.55*dsize+0.75*ypitch, y-dsize], 'HUL Matrix', dsize)
  draw_arrow([x+5*l+10.55*dsize+1.125*ypitch, y+0.5*dsize+ypitch], 2*l-3*dsize+0.375*ypitch, 0, 3)
  draw_arrow([x+7*l+7.55*dsize+1.5*ypitch, y+0.5*dsize+ypitch], 0, 0.5*dsize+3*ypitch, 3)
  draw_arrow([x+7*l+7.55*dsize+1.5*ypitch, y+dsize+4*ypitch], l, 0, 3)

#_______________________________________________________________________________
def draw_daq():
  scale = 1.0
  draw_tof = True
  x = 10
  ystart = a4size[1]-35
  l = 30
  w1 = 10*3/4
  w2 = 10*2/4
  w3 = 10*1/4
  wctrl = 45
  wdata = 30
  wtag = 15
  ypitch = 12
  ctrig = 'red'
  cbusy = 'green'
  cdata = 'orange'
  ctag = 'tag'
  cctrl = 'cyan'
  y = ystart - hdaq
  draw_arrow([x, y], l, 0, 2)
  draw_text([x+0.5*l, y+3], 'Spill gate')
  y -= ypitch
  draw_arrow([x, y], l, 0, 2)
  draw_text([x+0.5*l, y+3], 'DAQ gate')
  y -= ypitch
  draw_arrow([x, y], l, 0, 2, ctrig)
  draw_text([x+0.5*l, y+3], 'Trigger')
  x += l
  draw_square([x, y-0.5*ypitch], 0.75*l, 3*ypitch)
  # draw_text([x+0.5*l, y+1.5*ypitch], 'Master')
  # draw_text([x+0.5*l, y+1.*ypitch], 'Trigger')
  # draw_text([x+0.5*l, y+0.5*ypitch], 'Module')
  draw_text([x+0.375*l, y+1.5*ypitch], 'MTM')
  draw_arrow([x+0.75*l, y+2*ypitch], a4size[0]-80-x-0.75*l, 0, 0, ctag)
  draw_text([x+1.125*l, y+2*ypitch+2], 'Ethernet cable', False, 3)
  draw_arrow([x+1.125*l, y+2*ypitch], -2, -5, 3, 0)
  draw_arrow([x+1.125*l, y+2*ypitch], 2, -5, 3, 0)
  draw_arrow([x+0.85*l, y+2*ypitch-5], 0.275*l-2, 0, 3)
  draw_arrow([x+1.125*l+2, y+2*ypitch-5], 0.275*l-2, 0, 3)
  draw_arrow([x+0.85*l, y+2*ypitch-15], 0.55*l, 0, 3)
  draw_arrow([x+0.85*l, y+2*ypitch-15], 0, 10, 3)
  draw_arrow([x+1.4*l, y+2*ypitch-15], 0, 10, 3)
  draw_arrow([x+0.925*l, y+2*ypitch-8], 0.4*l, 0, 2, ctrig)
  draw_arrow([x+0.925*l, y+2*ypitch-10], 0.4*l, 0, 2, 'blue')
  draw_arrow([x+0.925*l, y+2*ypitch-12], 0.4*l, 0, 1, cbusy)
  ''' subsystem '''
  x = a4size[0] - 80
  y = ystart - 3/4*hdaq
  ''' vme01 '''
  draw_text_box([x, y], 'XVB601')
  y -= hdaq
  draw_text_box([x, y], 'VME RM')
  draw_arrow([x-w1, y+0.5*hdaq], w1, 0, 3, ctrig)
  draw_arrow([x-w1, y+0.5*hdaq], 0, -11/6*hdaq, 3, ctrig)
  draw_arrow([x-w2, y+0.25*hdaq], w2, 0, 2, cbusy)
  draw_arrow([x-w2, y+0.25*hdaq], 0, -23/12*hdaq, 3, cbusy)
  y -= hdaq
  draw_text_box([x, y], 'QDC CAEN V792')
  draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, ctrig)
  draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  y -= hdaq
  draw_text_box([x, y], 'HRTDC CAEN V775')
  draw_square([x+wdaq, y], 10, 4*hdaq)
  draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, ctrig)
  draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  for i in range(3): draw_arrow([x+wdaq, y+(i+0.5)*hdaq], w1, 0, 3, cdata)
  draw_arrow([x+wdaq+w1, y+0.5*hdaq], 0, 3*hdaq, 3, cdata)
  draw_arrow([x+wdaq, y+3.5*hdaq], w1, 0, 1, cdata)
  draw_arrow([x-wctrl, y+11/3*hdaq], wctrl, 0, 2, cctrl)
  draw_arrow([x-wdata, y+10/3*hdaq], wdata, 0, 3, cdata)
  draw_text([x+wdaq+25, y+2*hdaq], 'VME bus', True)
  ''' vme04 '''
  y -= 1.5*hdaq
  draw_text_box([x, y], 'XVB601')
  y -= hdaq
  draw_text_box([x, y], 'VME RM')
  draw_arrow([x-wtag, y+3/4*hdaq], wtag, 0, 2, ctag)
  draw_arrow([x-(4*w1 + wctrl if draw_tof else w1), y+2/4*hdaq],
             (4*w1 + wctrl if draw_tof else w1), 0, 3, ctrig)
  draw_arrow([x-(4*w1 + wctrl if draw_tof else w1), y+2/4*hdaq],
             0, (-4/6*hdaq if draw_tof else -5/6*hdaq), 3, ctrig)
  draw_arrow([x-w2, y+1/4*hdaq], w2, 0, 2, cbusy)
  draw_arrow([x-w2, y+1/4*hdaq], 0, -11/12*hdaq, 3, cbusy)
  y -= hdaq
  draw_text_box([x, y], 'NOTICE TDC64M')
  draw_arrow([x-(3*w1 + wctrl - 0.5*hdaq if draw_tof else w1), y+2/3*hdaq],
             (3*w1 + wctrl - 0.5*hdaq if draw_tof else w1), 0, 2, ctrig)
  if draw_tof:
    draw_text([x-(7*w1 + wctrl), y+3/6*hdaq-1.8], 'TOF')
    draw_arrow([x-(4*w1 + wctrl), y+5/6*hdaq], w1, 0, 3, ctrig)
    draw_arrow([x-(6*w1 + wctrl), y+3/6*hdaq], 3*w1, 0, 3)
    draw_logic_and([x-(3*w1 + wctrl), y+2/6*hdaq], hdaq/1.5)
  draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  draw_square([x+wdaq, y], 10, 3*hdaq)
  for i in range(2): draw_arrow([x+wdaq, y+(i+0.5)*hdaq], w1, 0, 3, cdata)
  draw_arrow([x+wdaq+w1, y+0.5*hdaq], 0, 2*hdaq, 3, cdata)
  draw_arrow([x-wctrl, y+8/3*hdaq], wctrl, 0, 2, cctrl)
  draw_arrow([x-wdata, y+7/3*hdaq], wdata, 0, 3, cdata)
  draw_arrow([x+wdaq, y+5/2*hdaq], w1, 0, 1, cdata)
  draw_text([x+wdaq+25, y+1.5*hdaq], 'VME bus', True)
  ''' vme07 '''
  y -= 1.5*hdaq
  draw_text_box([x, y], 'XVB601')
  y -= hdaq
  draw_text_box([x, y], 'VME RM')
  draw_arrow([x-wtag, y+3/4*hdaq], wtag, 0, 2, ctag)
  draw_arrow([x-w1, y+2/4*hdaq], w1, 0, 3, ctrig)
  draw_arrow([x-w1, y+2/4*hdaq], 0, -5/6*hdaq, 3, ctrig)
  draw_arrow([x-w2, y+1/4*hdaq], w2, 0, 2, cbusy)
  draw_arrow([x-w2, y+1/4*hdaq], 0, -11/12*hdaq, 3, cbusy)
  y -= hdaq
  draw_text_box([x, y], 'APVDAQ')
  draw_square([x+wdaq, y], 10, 3*hdaq)
  draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, ctrig)
  draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  for i in range(2): draw_arrow([x+wdaq, y+(i+0.5)*hdaq], w1, 0, 3, cdata)
  draw_arrow([x+wdaq+w1, y+0.5*hdaq], 0, 2*hdaq, 3, cdata)
  draw_arrow([x+wdaq, y+5/2*hdaq], w1, 0, 1, cdata)
  draw_arrow([x-wctrl, y+8/3*hdaq], wctrl, 0, 2, cctrl)
  draw_arrow([x-wdata, y+7/3*hdaq], wdata, 0, 3, cdata)
  draw_text([x+wdaq+25, y+1.5*hdaq], 'VME bus', True)
  ''' COPPER '''
  y -= 1.5*hdaq
  draw_text_box([x, y], 'Front-end PC')
  y -= hdaq
  draw_text_box([x, y], 'VME RM')
  draw_arrow([x-wtag, y+2/4*hdaq], wtag, 0, 2, ctag)
  y -= hdaq
  draw_text_box([x, y], 'COPPER Lite')
  draw_square([x+wdaq, y], 10, 2*hdaq)
  draw_arrow([x+wdaq+w3, y+1/4*hdaq], 0, hdaq, 3, cbusy)
  draw_arrow([x+wdaq, y+1/4*hdaq], w3, 0, 3, cbusy)
  draw_arrow([x+wdaq, y+5/4*hdaq], w3, 0, 1, cbusy)
  draw_arrow([x+wdaq, y+7/4*hdaq], w1, 0, 3, ctrig)
  draw_arrow([x+wdaq, y+6/4*hdaq], w2, 0, 3, 'blue')
  draw_arrow([x+wdaq, y+3/4*hdaq], w1, 0, 1, ctrig)
  draw_arrow([x+wdaq, y+2/4*hdaq], w2, 0, 1, 'blue')
  draw_arrow([x+wdaq+w1, y+3/4*hdaq], 0, hdaq, 3, ctrig)
  draw_arrow([x+wdaq+w2, y+2/4*hdaq], 0, hdaq, 3, 'blue')
  draw_arrow([x-wctrl, y+14/5*hdaq], wctrl, 0, 2, cctrl)
  draw_arrow([x-wdata, y+13/5*hdaq], wdata, 0, 3, cdata)
  draw_arrow([x-w1, y+12/5*hdaq], w1, 0, 3, cctrl)
  draw_arrow([x-w1, y+12/5*hdaq], 0, -26/15*hdaq, 3, cctrl)
  draw_arrow([x-w2, y+11/5*hdaq], w2, 0, 2, cdata)
  draw_arrow([x-w2, y+11/5*hdaq], 0, -28/15*hdaq, 3, cdata)
  draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, cctrl)
  draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cdata)
  draw_text([x+wdaq+21.7, y+1*hdaq], 'J0 bus', True)
  ''' EASIROC '''
  y -= 1.5*hdaq
  draw_text_box([x, y], 'Front-end PC')
  y -= hdaq
  draw_text_box([x, y], 'EASIROC')
  draw_arrow([x-wctrl, y+9/5*hdaq], wctrl, 0, 2, cctrl)
  draw_arrow([x-wdata, y+8/5*hdaq], wdata, 0, 3, cdata)
  draw_arrow([x-w1, y+7/5*hdaq], w1, 0, 3, cctrl)
  draw_arrow([x-w2, y+6/5*hdaq], w2, 0, 2, cdata)
  draw_arrow([x-w1, y+7/5*hdaq], 0, -9/15*hdaq, 3, cctrl)
  draw_arrow([x-w2, y+6/5*hdaq], 0, -9/15*hdaq, 3, cdata)
  draw_arrow([x-w1, y+4/5*hdaq], w1, 0, 2, cctrl)
  draw_arrow([x-w2, y+3/5*hdaq], w2, 0, 3, cdata)
  draw_arrow([x-w1, y+2/5*hdaq], w1, 0, 2, ctrig)
  draw_arrow([x-w2, y+1/5*hdaq], w2, 0, 3, cbusy)
  ''' EM '''
  # y -= 1.5*hdaq
  # draw_text_box([x, y], 'BIT3')
  # y -= hdaq
  # draw_text_box([x, y], 'VME RM')
  y -= 1.5*hdaq
  draw_text_box([x, y], 'EM controller PC')
  draw_arrow([x-wctrl, y+3/4*hdaq], wctrl, 0, 2, cctrl)
  draw_arrow([x-wdata, y+1/2*hdaq], wdata, 0, 3, cdata)
  ''' HUL MATRIX '''
  y -= 1.5*hdaq
  draw_text_box([x, y], 'SBS BIT3 618')
  y -= hdaq
  draw_text_box([x, y], 'VME RM')
  draw_square([x+wdaq, y], 10, 2*hdaq)
  draw_arrow([x-wtag, y+3/4*hdaq], wtag, 0, 2, ctag)
  draw_arrow([x-w1, y+2/4*hdaq], w1, 0, 3, ctrig)
  draw_arrow([x-w1, y+2/4*hdaq], 0, 39/10*hdaq, 3, ctrig)
  draw_arrow([x-w1, y+2/4*hdaq], 0, -5/6*hdaq, 3, ctrig)
  draw_arrow([x-w2, y+1/4*hdaq], w2, 0, 2, cbusy)
  draw_arrow([x-w2, y+1/4*hdaq], 0, 79/20*hdaq, 3, cbusy)
  draw_arrow([x-w2, y+1/4*hdaq], 0, -11/12*hdaq, 3, cbusy)
  draw_arrow([x+wdaq+w1, y+0.5*hdaq], 0, hdaq, 3, cdata)
  draw_arrow([x+wdaq, y+1/2*hdaq], w1, 0, 3, cdata)
  draw_arrow([x+wdaq, y+3/2*hdaq], w1, 0, 1, cdata)
  draw_arrow([x-w3, y+3/2*hdaq], w3, 0, 3, cdata)
  draw_arrow([x-w3, y+3/2*hdaq], 0, 5/4*hdaq, 3, cdata)
  draw_arrow([x-w3, y+11/4*hdaq], w3, 0, 2, cdata)
  draw_text([x+wdaq+25, y+hdaq], 'VME bus', True)
  y -= hdaq
  draw_text_box([x, y], 'HUL MATRIX')
  draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, ctrig)
  draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  ''' HUL SCALER '''
  y -= 1.5*hdaq
  draw_text_box([x, y], 'Front-end PC')
  draw_arrow([x-wctrl, y+4/5*hdaq], wctrl, 0, 2, cctrl)
  draw_arrow([x-wdata, y+3/5*hdaq], wdata, 0, 3, cdata)
  draw_arrow([x-w1, y+2/5*hdaq], w1, 0, 3, cctrl)
  draw_arrow([x-w2, y+1/5*hdaq], w2, 0, 2, cdata)
  y -= hdaq
  draw_text_box([x, y], 'HUL SCALER')
  draw_arrow([x-wtag, y+3/4*hdaq], wtag, 0, 2, ctag)
  draw_arrow([x-w1, y+2/4*hdaq], w1, 0, 2, cctrl)
  draw_arrow([x-w2, y+1/4*hdaq], w2, 0, 3, cdata)
  draw_arrow([x-w1, y+2/4*hdaq], 0, 18/20*hdaq, 3, cctrl)
  draw_arrow([x-w2, y+1/4*hdaq], 0, 19/20*hdaq, 3, cdata)
  draw_arrow([x-wtag, y+3/4*hdaq], 0, ystart-y-7/4*hdaq, 3, ctag)
  draw_arrow([x-wctrl, y+9/5*hdaq], 0, 671/30*hdaq, 3, cctrl)
  draw_arrow([x-wdata, y+8/5*hdaq], 0, 667/30*hdaq, 3, cdata)
  ''' EB '''
  x = 15
  y = ystart - 8*ypitch if draw_tof else ystart - 7*ypitch
  draw_text([x+0.5*wdaq, y+3], 'Main DAQ computer')
  for i, name in enumerate(['Controller', 'Event builder', 'Event distributer', 'Recorder']):
    draw_text_box([x, y-(i+1)*hdaq], name)
    draw_arrow([x+wdaq, y-(i+(1/2 if i == 0 else 1/4 if i == 1 else 1/3))*hdaq],
               (a4size[0] - 80 - x - wdaq - wctrl if i == 0 else w1), 0,
               3 if i == 0 else 1, cctrl)
    draw_arrow([x+wdaq, y-(i+(1/2 if i == 1 else 2/3))*hdaq],
               (0 if i == 0 else a4size[0] - 80 - x - wdaq - wdata
                if i == 1 else w2), 0, 3 if i == 0 else 1, cdata)
  draw_arrow([x+wdaq, y-7/4*hdaq], w2, 0, 3, cdata)
  draw_arrow([x+wdaq+w2, y-11/3*hdaq], 0, 23/12*hdaq, 3, cdata)
  draw_arrow([x+wdaq+w1, y-10/3*hdaq], 0, 34/12*hdaq, 3, cctrl)
  draw_text_box([x, y-7*hdaq], 'Online monitor')
  draw_arrow([x+wdaq, y-6.5*hdaq], w2, 0, 1, cdata)
  draw_arrow([x+wdaq+w2, y-11/3*hdaq], 0, -17/6*hdaq, 3, cdata)
  ''' Legend '''
  x = 15
  y = 55
  ypitch = 8
  draw_arrow([x, y], l, 0, 2, ctrig)
  draw_text([x+0.5*l, y+2], 'Trigger', False, 4)
  y -= ypitch
  draw_arrow([x, y], l, 0, 2, 'blue')
  draw_text([x+0.5*l, y+2], 'Event tag', False, 4)
  y -= ypitch
  draw_arrow([x, y], l, 0, 2, cbusy)
  draw_text([x+0.5*l, y+2], 'Busy', False, 4)
  y -= ypitch
  draw_arrow([x, y], l, 0, 2, cdata)
  draw_text([x+0.5*l, y+2], 'Data transfer', False, 4)
  y -= ypitch
  draw_arrow([x, y], l, 0, 2, cctrl)
  draw_text([x+0.5*l, y+2], 'Slow control', False, 4)

#_______________________________________________________________________________
def draw_matrix():
  pass

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
