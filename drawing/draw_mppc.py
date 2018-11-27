#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
from settings import a4size, line_width
import settings

#_______________________________________________________________________________
def draw(board, mppc, hole, gnd, connector, sma, label='(a)'):
  xstart = (settings.a4size[0] - board['width'])/2
  ystart = 200
  '''front'''
  db.draw_square([xstart, ystart], board['width'], board['height'])
  db.draw_line_with_scale([xstart, ystart], -5, board['height'],
                          rotate=True)
  if 'FBH' in settings.target:
    if len(label) > 0:
      db.draw_text([xstart-10, ystart+board['height']+20], label, text_size=8)
    db.draw_line_with_scale([xstart, ystart+board['height']],
                            board['width'], 5)
  if 'SCH' in settings.target:
    db.draw_line_with_scale([xstart, ystart],
                            board['width'], -9)
  s = mppc['rcsize']
  fc=0.6
  for p in mppc['pitches']:
    for rc in mppc['rc']:
      db.draw_square([xstart+board['width']/2+p+rc[0],
                      ystart+mppc['height']+rc[1]], s, s)
      db.draw_square([xstart+board['width']/2+p+rc[0],
                      ystart+mppc['height']+rc[1]-s*0.25],
                     s, s*0.5, fill_color=fc)
      db.draw_square([xstart+board['width']/2+p+rc[0],
                      ystart+mppc['height']+rc[1]+s*0.75],
                     s, s*0.5, fill_color=fc)
  s = sma['rcsize']
  db.draw_square([xstart+sma['rc'][0]-0.5*s,
                  ystart+sma['rc'][1]-0.5*s], s, s)
  db.draw_square([xstart+sma['rc'][0]-0.8*s,
                  ystart+sma['rc'][1]-0.5*s], 0.4*s, s, fill_color=fc)
  db.draw_square([xstart+sma['rc'][0]+0.2*s,
                  ystart+sma['rc'][1]-0.5*s], 0.4*s, s, fill_color=fc)
  for h in hole['position']:
    db.draw_circle([xstart + h[0], ystart + h[1]], hole['diameter'])
  db.draw_square([xstart+gnd['position'][0]-gnd['size']/2,
                  ystart+gnd['position'][1]-gnd['size']/2],
                 gnd['size'], gnd['size'], fill_color=0.9)
  db.draw_square([xstart+connector['position'][0]-connector['size'][0]/2,
                  ystart+connector['position'][1]-connector['size'][1]/2],
                 connector['size'][0], connector['size'][1], fill_color=fc)
  for i in range(34):
    x = (xstart+connector['position'][0]
         + (-8+int(i/2))*2.54*settings.scale)
    y = ystart+connector['position'][1] + (1-2*(i%2))*2.54/2*settings.scale
    db.draw_square([x-0.5, y-0.5], 1, 1, fill_color=fc)
  db.draw_square([xstart+sma['position'][0]-sma['size'][0]/2,
                  ystart+sma['position'][1]-sma['size'][1]/2],
                 sma['size'][0], sma['size'][1], fill_color=0.9)
  db.draw_square([xstart+sma['position'][0]-sma['size'][0]/2,
                  ystart+sma['position'][1]-sma['size'][1]/2],
                 sma['size'][1], sma['size'][1], fill_color=0.9)
  if 'FBH' in settings.target:
    db.draw_arrow([xstart+board['width']/2, ystart+3.5], 0, -5, 3)
    db.draw_text([xstart+board['width']/2, ystart-5], 'Connector to EASIROC')
    db.draw_arrow([xstart+gnd['position'][0]-3, ystart+gnd['position'][1]-3],
                  -4, -4, 3)
    db.draw_text([xstart+gnd['position'][0]-10, ystart-5], 'GND')
    db.draw_arrow([xstart+sma['position'][0]+2, ystart+sma['position'][1]-2],
                  5, -5, 3)
    db.draw_text([xstart+sma['position'][0]+10, ystart-5], 'Bias input')
  elif 'SCH' in settings.target:
    db.draw_arrow([xstart+board['width']/2,
                   ystart+connector['position'][1]+connector['size'][1]/2-1], 0, 7, 3)
    db.draw_text([xstart+board['width']/2,
                  ystart+board['height']+4], 'Connector to EASIROC')
    db.draw_arrow([xstart+gnd['position'][0]-3,
                   ystart+gnd['position'][1]+3], -4, 7, 3)
    db.draw_text([xstart+gnd['position'][0]-10, ystart+board['height']+4], 'GND')
    db.draw_arrow([xstart+sma['position'][0]+2, ystart+sma['position'][1]+2], 5, 8, 3)
    db.draw_text([xstart+sma['position'][0]+10, ystart+board['height']+4], 'Bias input')
  db.draw_text([xstart-12, ystart+board['height']/2], 'Front', rotate=True)
  '''back'''
  ystart -= board['height'] + 25
  db.draw_square([xstart, ystart], board['width'], board['height'])
  for p in mppc['pitches']:
    db.draw_square([xstart+board['width']/2+p-mppc['size']/2,
                    ystart+mppc['height']-mppc['size']/2],
                   mppc['size'], mppc['size'], fill_color=0.8)
  for h in hole['position']:
    db.draw_circle([xstart + h[0], ystart + h[1]], hole['diameter'])
  if 'FBH' in settings.target:
    db.draw_arrow([xstart+board['width']/2+mppc['pitches'][5],
                   ystart+board['height']-5], 0, 8, 3)
    db.draw_text([xstart+board['width']/2+mppc['pitches'][5],
                  ystart+board['height']+4],
                 'Sensor of MPPC ' + mppc['type'])
  elif 'SCH' in settings.target:
    db.draw_arrow([xstart+board['width']/2+mppc['pitches'][5],
                   ystart+mppc['height']], 0, 25, 3)
    db.draw_text([xstart+board['width']/2+mppc['pitches'][5],
                  ystart+board['height']+4],
                 'Sensor of MPPC ' + mppc['type'])
  db.draw_arrow([xstart+hole['position'][-1][0],
                 ystart-1.5], 0, 1.5+hole['position'][-1][1], 3)
  db.draw_text([xstart+hole['position'][-1][0],
                ystart-5], 'Through hole')
  db.draw_text([xstart-12, ystart+board['height']/2], 'Back', rotate=True)
  db.draw_text([xstart+board['width']+10, ystart-16], '[mm]')


#_______________________________________________________________________________
def draw_circuit(scale=1, label='(b)'):
  x = 20
  y = 200
  l = 10*scale
  if len(label) > 0:
    db.draw_text([x, y+20], label, text_size=8)
  db.draw_text([x, y+2], 'Bias input')
  db.draw_arrow([x, y], 0, -2*l, 3)
  db.draw_circle([x, y-l], 1, fc=0)
  db.draw_arrow([x-l/2, y-2*l], l, 0, 3)
  db.draw_arrow([x-l/2, y-2.3*l], l, 0, 3)
  db.draw_arrow([x, y-2.3*l], 0, -l, 3)
  db.draw_triangle([x-l/2, y-3.3*l], l, -l/2*math.sqrt(3))
  db.draw_arrow([x, y-l], 2*l, 0, 3)
  y -= l
  for i in range(4):
    if i == 0:
      db.draw_arrow([x+2*l, y], 0, -3*l, 3)
      db.draw_text([x+7*l, y+0.5*l+4], 'MPPC')
      db.draw_text([x+15*l+6, y-1.5], 'Output 1')
    elif i == 1:
      db.draw_arrow([x+2*l, y], 0, -2*l, 3)
      db.draw_text([x+15*l+6, y-1.5], 'Output 2')
    elif i == 2:
      print('0 setgray [1 1] 0 setdash')
      print('newpath {} {} moveto'.format(x+2*l, y-2*l))
      print('{} {} rlineto'.format(0, 3*l))
      print('stroke closepath')
      print('[] 0 setdash')
      db.draw_circle([x+8*l, y], 0.5, fc=0)
      db.draw_circle([x+8*l, y-0.7*l], 0.5, fc=0)
      db.draw_circle([x+8*l, y-1.4*l], 0.5, fc=0)
      y -= 3*l
      continue
    elif i == 3:
      db.draw_arrow([x+2*l, y], 0, l, 3)
      db.draw_text([x+15*l+7, y-1.5], 'Output 16')
    db.draw_arrow([x+2*l, y], l, 0, 3)
    db.draw_circle([x+2*l, y], 1, fc=0)
    db.draw_square([x+3*l, y-0.15*l], l, 0.3*l)
    db.draw_arrow([x+4*l, y], 10.5*l, 0, 3)
    db.draw_circle([x+5*l, y], 1, fc=0)
    db.draw_arrow([x+5*l, y], 0, -1.5*l, 3)
    db.draw_arrow([x+5*l, y-1.5*l], l, 0, 3)
    db.draw_arrow([x+6*l, y-2*l], 0, l, 3)
    db.draw_arrow([x+6.3*l, y-2*l], 0, l, 3)
    db.draw_arrow([x+6.3*l, y-1.5*l], l, 0, 3)
    db.draw_triangle([x+7.3*l, y-2*l], l/2*math.sqrt(3), l, rotate=True)
    db.draw_arrow([x+7*l-l/4*math.sqrt(3), y-0.5*l], 0, l, 3)
    db.draw_triangle([x+7*l+l/4*math.sqrt(3), y-0.5*l],
                     -l/2*math.sqrt(3), l, rotate=True, fill_color=0)
    db.draw_circle([x+9*l, y], 1, fc=0)
    db.draw_arrow([x+9*l, y], 0, -1.5*l, 3)
    db.draw_arrow([x+9*l, y-1.5*l], 3*l, 0, 3)
    db.draw_square([x+10*l, y-1.65*l], l, 0.3*l)
    db.draw_arrow([x+12*l, y-2*l], 0, l, 3)
    db.draw_arrow([x+12.3*l, y-2*l], 0, l, 3)
    db.draw_arrow([x+12.3*l, y-1.5*l], l, 0, 3)
    db.draw_triangle([x+13.3*l, y-2*l], l/2*math.sqrt(3), l, rotate=True)
    y -= 3*l

#_______________________________________________________________________________
def draw_fbh(scale=1):
  settings.set_scale(scale)
  board = {}
  mppc = {}
  hole = {}
  gnd = {}
  connector = {}
  sma = {}
  board['width'] = 90*scale
  board['height'] = 30*scale
  mppc['type'] = 'S12571-100P'
  mppc['pitches'] = [(x-7.5)*5*scale for x in range(16)]
  mppc['height'] = 25*scale
  mppc['size'] = 2*scale
  mppc['rcsize'] = 1*scale
  mppc['rc'] = [[-0.75*mppc['rcsize'], -0.5*mppc['rcsize']],
                [-0.75*mppc['rcsize'], -2.5*mppc['rcsize']],
                [ 0.75*mppc['rcsize'], -0.5*mppc['rcsize']],
                [ 0.75*mppc['rcsize'],  1.5*mppc['rcsize']]]
  hole['diameter'] = 1*scale
  hole['position'] = [[ 3*scale, 27*scale], [ 3*scale, 20*scale],
                      [ 3*scale, 10*scale], [ 3*scale,  3*scale],
                      [87*scale, 27*scale], [87*scale, 20*scale],
                      [87*scale, 10*scale], [87*scale,  3*scale]]
  gnd['position'] = [15*scale, 6*scale]
  gnd['size'] = 10*scale
  connector['position'] = [45*scale, 6*scale]
  connector['size'] = [43.2*scale, 8*scale]
  sma['position'] = [76*scale, 6*scale]
  sma['size'] = [6.7*scale, 6.7*scale]
  sma['rcsize'] = 2*scale
  sma['rc'] = [75*scale, 11*scale]
  #sma['size'] = [15.6*scale, 6.7*scale]
  draw(board, mppc, hole, gnd, connector, sma)

#_______________________________________________________________________________
def draw_sch(scale=1):
  settings.set_scale(scale)
  board = {}
  mppc = {}
  hole = {}
  gnd = {}
  connector = {}
  sma = {}
  board['width'] = 139*scale
  board['height'] = 45*scale
  mppc['type'] = 'S10362-11-100P'
  mppc['pitches'] = [(x-7.5)*7*scale for x in range(16)]
  mppc['height'] = 22.5*scale
  mppc['size'] = 2*scale
  mppc['rcsize'] = 1*scale
  mppc['rc'] = [[-0.75*mppc['rcsize'], -0.5*mppc['rcsize']],
                [-0.75*mppc['rcsize'], -2.5*mppc['rcsize']],
                [ 0.75*mppc['rcsize'], -0.5*mppc['rcsize']],
                [ 2.25*mppc['rcsize'],  0.25*mppc['rcsize']]]
  hole['diameter'] = 1*scale
  hole['position'] = [[ 10*scale,  9.25*scale], [ 10*scale, 17.25*scale],
                      [ 10*scale, 27.75*scale], [ 10*scale, 35.75*scale],
                      [ 30*scale,  9.25*scale],
                      [ 30*scale, 27.75*scale], [ 30*scale, 35.75*scale],
                      [109*scale,  9.25*scale],
                      [109*scale, 27.75*scale], [109*scale, 35.75*scale],
                      [129*scale, 35.75*scale], [129*scale, 17.25*scale],
                      [129*scale, 27.75*scale], [129*scale,  9.25*scale]]
  gnd['position'] = [39.5*scale, 37*scale]
  gnd['size'] = 10.5*scale
  connector['position'] = [69.5*scale, 37*scale]
  connector['size'] = [43.2*scale, 8*scale]
  sma['position'] = [100.5*scale, 37*scale]
  sma['size'] = [6.7*scale, 6.7*scale]
  sma['rcsize'] = 2*scale
  sma['rc'] = [99.5*scale, 32*scale]
  #sma['size'] = [15.6*scale, 6.7*scale]
  draw(board, mppc, hole, gnd, connector, sma)
