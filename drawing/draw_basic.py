#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import math

import settings

#_______________________________________________________________________________
def draw_beam_mark(moveto, r, lw=0.1):
  x = r*math.sqrt(2)
  y = r*math.sqrt(2)
  draw_line([moveto[0]-x/2, moveto[1]-y/2], x, y, lw=lw)
  draw_line([moveto[0]-x/2, moveto[1]+y/2], x, -y, lw=lw)
  draw_circle(moveto, r, fc=-1, lw=lw)

#_______________________________________________________________________________
def draw_line(moveto, x, y, color='black', lw=0.1, dash=None):
  ''' draw line '''
  if x == 0 and y == 0: return
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
  print('{} {} rlineto'.format(x, y))
  print('{} setlinewidth stroke'.format(lw))

#_______________________________________________________________________________
def draw_arrow(moveto, width, height, mark=0, color='black', lw=0.1, msize=1.0, mfill=0.):
  # mark = 0:both 1:first 2:last 3:none
  ''' draw arrow '''
  if width == 0 and height == 0: return
  if settings.target == 'DAQ': msize = 1.5
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
  print('closepath gsave {} setgray fill grestore {} setlinewidth stroke'
        .format(mfill, 0.0001 if mark != 3 else lw))
  if mark != 3:
    print('newpath {} {} moveto'.format(mi[0], mi[1]))
    print('{} {} rlineto'.format(mf[0] - mi[0], mf[1] - mi[1]))
    print('closepath gsave fill grestore {} setlinewidth stroke'.format(lw))

#_______________________________________________________________________________
def draw_elip(moveto, r, ratio, theta=0, fill_color=1.0, line_width=0.1):
  print('/cmtx matrix currentmatrix def')
  print('gsave {} {} translate {} rotate {} setlinewidth'
        .format(moveto[0], moveto[1], theta, line_width))
  print('newpath 1.0 {} scale 0 0 {} 0 360 arc'.format(ratio, r))
  print('cmtx setmatrix closepath stroke grestore')

#_______________________________________________________________________________
def draw_circle(moveto, r, fc=1.0, a=0, b=360, lw=0.1):
  ''' draw circle '''
  print('newpath {} {} moveto'.format(moveto[0]+r, moveto[1]))
  print('{} {} {} {} {} arc closepath'.format(moveto[0], moveto[1], r, a, b))
  if fc >= 0:
    print('{} setgray gsave fill grestore'.format(fc))
  print('0.0 setgray')
  if lw > 0:
    print('{} setlinewidth stroke'.format(lw))

#_______________________________________________________________________________
def draw_text(moveto, text, rotate=False, text_size=5, font='Times-Roman', centering=True):
  ''' draw text '''
  print('0 setgray')
  print('/{} findfont {} scalefont setfont'.format(font, text_size))
  print('{} {} moveto'.format(moveto[0], moveto[1]))
  if rotate:
    print('({}) dup stringwidth pop 0 exch -2 div 0 exch rmoveto'.format(text))
  print('({})'.format(text))
  if centering:
    print('dup stringwidth pop 2 div 0 exch sub 0 rmoveto'.format(text))
  print('{} show {}'
        .format('90 rotate' if rotate else '', '-90 rotate' if rotate else ''))
  print('/Times-Roman findfont {} scalefont setfont'.format(settings.text_size))

#_______________________________________________________________________________
def draw_text_box(moveto, text, text_size=5.):
  ''' draw text box '''
  t = text.split()
  w = (text_size*max(len(t[0]), len(t[1]))
       if len(t) > 1 else text_size*len(text))
  h = text_size*9 if len(t) > 1 else text_size*2
  if settings.target == 'DAQ':
    w = settings.wdaq
    h = settings.hdaq
  if settings.target == 'MATRIX':
    w = settings.wmtx
    h = settings.hmtx
  draw_square(moveto, w, h, 0.1, 0.95 if 'RM' in text else 1)
  print('0 setgray')
  print('/Times-Roman findfont {} scalefont setfont'.format(text_size))
  print('{} {} moveto'.format(moveto[0]+w/2, moveto[1]))
  print('({}) dup stringwidth pop neg 2 div 0 rmoveto'.format(text))
  print('0 {} rmoveto show'.format(h/2.-text_size/3))
  print('/Times-Roman findfont {} scalefont setfont'.format(settings.text_size))

  #_______________________________________________________________________________
def draw_line_with_scale(moveto, width, height, rotate=False):
  ''' draw line with scale '''
  rwidth = width/settings.scale
  if abs(rwidth - round(rwidth)) < 0.0001:
    rwidth = round(rwidth)
  if settings.target == 'EMULSION':
    lr = -1 if rotate else 1
    rotate= False
  if settings.target != 'BACp':
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
    if height < 5:
      draw_arrow([moveto[0], moveto[1]-4], 0, 4, 2)
      draw_arrow([moveto[0], moveto[1]+height], 0, 4, 1)
      moveto[0] += width*0.25
    else:
      draw_arrow(moveto, 0, height)
      if settings.target == 'COLLIMATOR' or 'BC' in settings.target:
        moveto[0] += 2.5
        if height/settings.scale < 60:
          moveto[0] -= 2
      else:
        if height < 10:
          moveto[0] += -3
        if (settings.target == 'CASSETTE' or
            settings.target == 'PVAC' or
            settings.target == 'FAC'):
          moveto[0] += 2.5
        if settings.target == 'TOF':
          moveto[0] += 1
        if 'SDC' in settings.target:
          moveto[0] += 2
  else:
    if settings.target == 'EMULSION' and width > 2:
      moveto[1] += height * 0.75
      draw_arrow(moveto, width, 0)
      moveto[1] += height * 0.25
      if rwidth == 100:
        moveto[0] += lr*width*0.75
    elif width > 5 or 'BC' in settings.target or settings.target == 'BFT':
      moveto[1] += height * 0.75
      draw_arrow(moveto, width, 0)
    else:
      moveto[1] += height * 0.75
      moveto[0] += -4
      draw_arrow(moveto, 4, 0, 2)
      moveto[0] += 4 + width
      draw_arrow(moveto, 4, 0, 1)
      moveto[0] += -width/2 + 3
      if settings.target == 'CASSETTE':
        moveto[0] += 1
        # moveto[1] += 1
      if abs(round(rwidth) - rwidth) > 0.1:
        moveto[0] += -width/2 + 3
        # moveto[1] += -6
  print('{} {} moveto'.format(moveto[0] if rotate else moveto[0] + 0.5*width,
                              moveto[1]+height/2 if rotate else moveto[1]+1))
  real_length = (11760 if settings.target == 'EMULSION' and rwidth > 1000 else
                 1805 if settings.target == 'TOF' and width > 100 else
                 673 if settings.target == 'SCH' and width > 100 else
                 height/settings.scale if rotate else rwidth)
  real_length = round(real_length) if abs(real_length - round(real_length)) < 0.001 else float('{:.2f}'.format(real_length))
  if rotate:
    print('({}) dup stringwidth pop 0 exch -2 div 0 exch rmoveto'.format(real_length))
  print('({}) dup stringwidth pop -2 div 0 rmoveto {} show {}'
        .format(real_length,
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
def draw_polygon3d(moveto, w, h, t, lw, fc):
  ''' draw_polygon3d '''
  wr = [-w[0], -w[1]]
  hr = [-h[0], -h[1]]
  tr = [-t[0], -t[1]]
  draw_polygon(moveto, [w, h, wr, hr], lw, fc)
  draw_polygon([moveto[0]+w[0]+h[0], moveto[1]+w[1]+h[1]], [hr, t, h, tr], lw, fc)
  draw_polygon([moveto[0]+w[0]+h[0], moveto[1]+w[1]+h[1]], [t, wr, tr, w], lw, fc)

#_______________________________________________________________________________
def draw_square(moveto, width, height, line_width=0.1, fill_color=1.0):
  ''' draw square '''
  if settings.target == 'DAQ':
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
def draw_triangle(moveto, width, height, line_width=0.1, fill_color=1.0, rotate=False):
  ''' draw square '''
  if settings.target == 'DAQ':
    line_width = 0.1
  print('0 setgray')
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  if rotate:
    print('{} {} rlineto'.format(0, height))
    print('{} {} rlineto closepath'.format(width, -height/2))
  else:
    print('{} {} rlineto'.format(width, 0))
    print('{} {} rlineto closepath'.format(-width/2, height))
  if fill_color >= 0:
    print('{} setgray gsave fill grestore 0 setgray'.format(fill_color))
  if line_width > 0:
    print('{} setlinewidth gsave stroke grestore'.format(line_width))

#_______________________________________________________________________________
def draw_logic_or(moveto, size=1.0, etcline=True):
  ''' draw AND logic '''
  height = 1*size
  r = height
  w = height*(0.375+1-math.sqrt(3)/2)
  if etcline:
    for i in range(3):
      draw_arrow([moveto[0]-size*0.3, moveto[1]+height*(0.8-i*0.1)],
                 size*0.6, 0, 3)
      draw_circle([moveto[0]-size*0.1, moveto[1]+height*(0.5-i*0.1)],
                  0.01*size, 0.1)
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  print('{} {} rlineto'.format(w, 0))
  print('{} {} {} {} {} arc'.format(moveto[0]+w, moveto[1]+r, r, -90, -30))
  print('{} {} {} {} {} arc'.format(moveto[0]+w, moveto[1], r, 30, 90))
  print('{} {} rlineto'.format(-w, 0))
  print('{} {} {} {} {} arcn'
        .format(moveto[0]-r*math.sqrt(3)/2, moveto[1]+r/2, r, 30, -30))
  print('closepath gsave 1 setgray fill grestore 0 setgray 0.1 setlinewidth stroke')

#_______________________________________________________________________________
def draw_logic_and(moveto, size=1.0, etcline=False):
  ''' draw AND logic '''
  height = 1*size
  r = height*0.5
  w = height*0.75
  #moveto[1] = moveto[1] - 0.25*size
  moveto[1] = moveto[1] + 0.5*size
  if etcline:
    for i in range(3):
      draw_arrow([moveto[0]-size*0.3, moveto[1]+height*(0.8-i*0.1)],
                 size*0.6, 0, 3)
      draw_circle([moveto[0]-size*0.15, moveto[1]+height*(0.5-i*0.1)],
                  0.04*size, 0.1)
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]+r))
  print('{} {} rlineto'.format(0, -height))
  print('{} {} rlineto'.format(w, 0))
  print('{} {} {} {} {} arc'.format(moveto[0]+w, moveto[1], r, -90, 90))
  print('{} {} rlineto'.format(-w, 0))
  print('closepath')
  print('gsave 1 setgray fill grestore 0 setgray 0.1 setlinewidth stroke')

#_______________________________________________________________________________
def draw_wave(moveto, width, height, stroke=True):
  print('newpath {} {} moveto'.format(moveto[0], moveto[1]))
  print('{} {} {} {} {} {} curveto'.format(moveto[0]+width*1/3, moveto[1]+height,
                                           moveto[0]+width*2/3, moveto[1]+height,
                                           moveto[0]+width, moveto[1]))
  print('gsave 0.1 setlinewidth {}'.format('stroke closepath' if stroke else ''))

#_______________________________________________________________________________
def initialize():
  print('%!PS-Adobe-3.0 EPSF-3.0')
  print('%%Title: drawing of {}'.format(settings.target))
  print('%%Creator: Shuhei Hayakawa')
  print('%%CreationDate: {}'.format(datetime.datetime.now()))
  print('%%Orientation: Portrait')
  print('%%Pages: 1')
  print('%%EndComments')
  print('')
  print('/{} findfont {} scalefont setfont'
        .format(settings.text_font, settings.text_size))
  print('2.8571429 2.8571429 scale % change unit to [mm]')
