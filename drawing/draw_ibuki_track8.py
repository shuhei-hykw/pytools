#!/usr/bin/env python3

import json
import math

import draw_basic as db
import settings

json_list = ['input/drawing/Ibuki-track8.json']

#______________________________________________________________________________
def cos(deg):
  return math.cos(deg*math.pi/180.)
#______________________________________________________________________________
def sin(deg):
  return math.sin(deg*math.pi/180.)

#______________________________________________________________________________
def draw():
  scale = 1.0
  settings.set_scale(scale)
  xstart = 100
  ystart = 100
  json_array = []
  for file_name in json_list:
    with open(file_name, 'r') as f:
      json_array.append(json.load(f))
  w = 141.5*2
  h = 200*2
  print('newpath {} {} moveto'.format(xstart-w/2, ystart-h/2+70))
  print('{} {} rlineto'.format(w, 0))
  print('{} {} rlineto'.format(0, h))
  print('{} {} rlineto clip'.format(-w, 0))
  ''' vertexA '''
  vertex = [[xstart, ystart]]
  for iv in range(len(json_list)):
    for frag in json_array[iv][0]['Fragments']:
      rx = frag['Range'][0] * cos(frag['Phi'][0])
      ry = frag['Range'][0] * sin(frag['Phi'][0])
      lw = 1.5 if frag['ID'] == 0 else 1.0
      if frag['ID'] == 10:
        vertex[iv][0] += 1
        vertex[iv][1] -= 1
        print('[1 2] 0 setdash')
        r1 = 5
        theta = 30
        moveto = [vertex[iv][0]-r1*math.cos(math.radians(theta)),
                  vertex[iv][1]+r1*math.sin(math.radians(theta))]
        print(f'{moveto[0]} {moveto[1]} {r1} {180+theta} {360-theta} arc')
        print('stroke')
        l1 = 7
        moveto = [moveto[0] - r1*math.cos(math.radians(theta)),
                  moveto[1] - r1*math.sin(math.radians(theta))]
        db.draw_line(moveto, 0, l1, lw=lw*0.6)
        moveto[1] += l1
        db.draw_line(moveto, -1, 2, lw=lw*0.6)
        # print('newpath {moveto[0]} {moveto[1]} moveto')
        # print(f'0 {-l1} rlineto')
        # print(f'{-2} {-3} rlineto')
        # r2 = 2
        # moveto = [vertex[iv][0] - r1 - r2,
        #           vertex[iv][1] - l]
        # print(f'{moveto[0]} {moveto[1]} {r2} {270} {360} arc')
        print('stroke')
        # print('0.0 setgray')
        # print(f'{lw*0.6} setlinewidth stroke')
        db.draw_text([moveto[0]+rx+3, moveto[1]+ry+1],
                     'e', text_size=6)
        db.draw_text([moveto[0]+rx+5.5, moveto[1]+ry+2.5],
                     '-', text_size=6)
      else:
        print('[] 0 setdash')
        moveto = [vertex[iv][0], vertex[iv][1]]
        # if frag['ID'] == 9:
        #   moveto[0] += -0.5
        #   moveto[1] += 0.5
        db.draw_arrow([moveto[0], moveto[1]], rx, ry, 3, lw=lw*0.6)
        if frag['ID'] == 8:
          db.draw_text([moveto[0]+rx-4, moveto[1]+ry-6],
                       '#8', text_size=6)
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
