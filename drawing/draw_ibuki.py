#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import math

import draw_basic as db
import settings

json_list = ['input/kinema/e07twin_mod047pl10_A.json',
             'input/kinema/e07twin_mod047pl10_B.json',
             'input/kinema/e07twin_mod047pl10_C.json']

#_______________________________________________________________________________
def cos(deg):
  return math.cos(deg*math.pi/180.)
#_______________________________________________________________________________
def sin(deg):
  return math.sin(deg*math.pi/180.)

#_______________________________________________________________________________
def draw():
  scale = 1.0
  settings.set_scale(scale)
  xstart = 100
  ystart = 100
  json_array = []
  for file_name in json_list:
    with open(file_name, 'r') as f:
      json_array.append(json.load(f))
  w = 141.5
  h = 200
  print('newpath {} {} moveto'.format(xstart-w/2, ystart-h/2+70))
  print('{} {} rlineto'.format(w, 0))
  print('{} {} rlineto'.format(0, h))
  print('{} {} rlineto clip'.format(-w, 0))
  # r = 90
  # print('newpath {} {} moveto'.format(xstart+r, ystart+20))
  #print('{} {} {} 0 360 arc clip'.format(xstart, ystart+20, r))
  ''' vertexA '''
  vertex = [[xstart, ystart]]
  for iv in range(3):
    for frag in json_array[iv][0]['Fragments']:
      rx = frag['Range'][0] * cos(frag['Phi'][0])
      ry = frag['Range'][0] * sin(frag['Phi'][0])
      lw = 1.5 if frag['ID'] == 0 else 1.0
      if frag['ID'] == 6 or frag['ID'] == 8 or frag['ID'] == 9:
        print('[0.5 2] 0 setdash')
      else:
        print('[] 0 setdash')
      db.draw_arrow([vertex[iv][0], vertex[iv][1]], rx, ry, 3, lw=lw*0.6)
      # if frag['Nuclide'] == 'Xi':
      #   db.draw_text([vertex[iv][0]+rx-6, vertex[iv][1]+ry],
      #                'X', text_size=10, font='Symbol')
      #   db.draw_text([vertex[iv][0]+rx-1, vertex[iv][1]+ry+4],
      #                '-', text_size=10)
      # else:
      #   tpos = ([vertex[iv][0]+rx/2+5, vertex[iv][1]+ry/2]
      #           if frag['ID'] == 1 else
      #           [vertex[iv][0]+rx/2+6, vertex[iv][1]+ry/2]
      #           if frag['ID'] == 2 else
      #           [vertex[iv][0]+rx/2-30, vertex[iv][1]+ry/2+6]
      #           if frag['ID'] == 3 else
      #           [vertex[iv][0]+rx/2, vertex[iv][1]+ry/2])
      #   db.draw_text(tpos, '#{}'.format(frag['ID']), text_size=10)
      if iv == 0 and frag['ID'] == 1:
        vertex.append([vertex[iv][0]+rx, vertex[iv][1]+ry])
      if iv == 0 and frag['ID'] == 2:
        vertex.append([vertex[iv][0]+rx, vertex[iv][1]+ry])
  print('initclip')
