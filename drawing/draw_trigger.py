#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
from settings import a4size, line_width
import settings

#_______________________________________________________________________________
def draw():
  dsize = 5
  x = 10
  y = a4size[1]-dsize*10
  ypitch = dsize*3
  l = 12
  ''' BH1 '''
  db.draw_text_box([x, y], 'BH1', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], l, 0, 3)
  db.draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  db.draw_arrow([x+l+5*dsize, y+dsize], l, 0, 3)
  db.draw_logic_or([x+2*l+(5+0.9)*dsize, y+(1-0.8*2.4)*dsize], dsize)
  db.draw_arrow([x+2*l+(8.15)*dsize, y+(1-0.8*2.4+1.2)*dsize], l, 0, 3)
  ''' BH2 '''
  y = y - ypitch
  db.draw_text_box([x, y], 'BH2', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], 3*l+5.15*dsize, 0, 3)
  db.draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  db.draw_logic_and([x+3*l+8.15*dsize, y+dsize], ypitch-0.8*dsize)
  db.draw_arrow([x+3*l+7.55*dsize+0.75*ypitch, y+0.6*dsize+0.5*ypitch], l, 0, 3)
  db.draw_arrow([x+4*l+7.55*dsize+0.75*ypitch, y-0.5*ypitch+dsize], 0, ypitch-0.4*dsize, 3)
  db.draw_arrow([x+4*l+7.55*dsize+0.75*ypitch, y-0.5*ypitch+dsize], l, 0, 3)
  ''' BAC '''
  y = y - ypitch
  db.draw_text_box([x, y], 'BAC1', dsize)
  db.draw_arrow([x+4*dsize, y+dsize], l, 0, 3)
  db.draw_arrow([x+l+4*dsize, y+dsize], 0, -0.35*ypitch, 3)
  db.draw_arrow([x+l+4*dsize, y+dsize-0.35*ypitch], l, 0, 3)
  y = y - ypitch
  db.draw_text_box([x, y], 'BAC2', dsize)
  db.draw_arrow([x+4*dsize, y+dsize], l, 0, 3)
  db.draw_arrow([x+l+4*dsize, y+dsize], 0, 0.35*ypitch, 3)
  db.draw_arrow([x+l+4*dsize, y+dsize+0.35*ypitch], l, 0, 3)
  db.draw_arrow([x+2*l+4.5*dsize, y+dsize+0.5*ypitch], 4*l+3.55*dsize, 0, 3)
  #db.draw_logic_and([x+l+4*dsize, y+dsize], ypitch)
  db.draw_logic_or([x+2*l+3.4*dsize, y+dsize+(ypitch-2.4*dsize)/2], dsize, False)
  db.draw_circle([x+5*l+7.55*dsize+0.75*ypitch-1, y+dsize+0.5*ypitch], 1)
  # K-beam
  db.draw_logic_and([x+5*l+7.55*dsize+0.75*ypitch, y+dsize+0.5*ypitch], ypitch)
  db.draw_text([x+5*l+7.55*dsize+1.125*ypitch, y+dsize+1.9*ypitch], 'K beam')
  db.draw_arrow([x+5*l+7.55*dsize+1.5*ypitch, y+dsize+ypitch], 2*l, 0, 3)
  db.draw_arrow([x+7*l+7.55*dsize+1.5*ypitch, y+dsize-ypitch], 0, 2*ypitch, 3)
  db.draw_arrow([x+7*l+7.55*dsize+1.5*ypitch, y+dsize-ypitch], l, 0, 3)
  ''' PVAC '''
  y = y - ypitch
  db.draw_text_box([x, y], 'PVAC', dsize)
  db.draw_arrow([x+4*dsize, y+dsize], 5*l+3.55*dsize+0.75*ypitch, 0, 3)
  ''' FAC '''
  y = y - ypitch
  db.draw_text_box([x, y], 'FAC', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], 3*l, 0, 3)
  db.draw_arrow([x+3*l+3*dsize, y+dsize], 0, 0.5*ypitch, 3)
  db.draw_arrow([x+3*l+3*dsize, y+dsize+0.5*ypitch], 2*l+4.55*dsize+0.75*ypitch, 0, 3)
  db.draw_circle([x+5*l+7.55*dsize+0.75*ypitch-1, y+dsize+0.5*ypitch], 1)
  # K scat
  db.draw_text([x+5*l+7.55*dsize+1.125*ypitch, y+dsize+1.4*ypitch], 'K scat')
  db.draw_logic_and([x+5*l+7.55*dsize+0.75*ypitch, y+dsize], ypitch)
  ''' TOF '''
  y = y - ypitch
  db.draw_text_box([x, y], 'TOF', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], l, 0, 3)
  db.draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  db.draw_arrow([x+l+5*dsize, y+dsize], l, 0, 3)
  db.draw_logic_or([x+2*l+5.9*dsize, y-0.92*dsize], dsize)
  db.draw_arrow([x+2*l+8.15*dsize, y+0.28*dsize], l, 0, 3)
  db.draw_arrow([x+3*l+8.15*dsize, y+0.28*dsize], 0, 0.72*dsize+ypitch, 3)
  db.draw_arrow([x+3*l+8.15*dsize, y+dsize+ypitch], 2*l-0.6*dsize+0.75*ypitch, 0, 3)
  db.draw_circle([x+1.5*l+5*dsize, y+dsize], 1, 0.1)
  db.draw_arrow([x+5*l+7.55*dsize+1.5*ypitch, y+dsize+1.5*ypitch], 3*l, 0, 3)
  # KK
  #db.draw_text([x+8*l+7.55*dsize+1.875*ypitch, y+dsize+2.4*ypitch], '(K, K)')
  db.draw_logic_and([x+8*l+7.55*dsize+1.5*ypitch, y+dsize+ypitch], ypitch)
  db.draw_arrow([x+8*l+7.55*dsize+2.25*ypitch, y+dsize+1.5*ypitch], 2*l, 0, 2)
  #db.draw_text([x+9*l+7.55*dsize+2.25*ypitch, y+2.5*dsize+1.5*ypitch], '(K,K)')
  db.draw_text([x+9*l+7.55*dsize+2.25*ypitch, y+1.5*dsize+1.5*ypitch], 'Trigger')
  db.draw_text([x+9*l+7.55*dsize+2.25*ypitch, a4size[1]-dsize*10], 'MT: Mean timer')
  y = y - ypitch
  db.draw_arrow([x+1.5*l+5*dsize, y+dsize], 0, ypitch, 3)
  db.draw_arrow([x+1.5*l+5*dsize, y+dsize], 3.5*l+2.55*dsize+0.75*ypitch, 0, 3)
  for i in range(3):
    db.draw_arrow([x+5*l+2.75*dsize+1.125*ypitch, y+dsize-i*0.24*dsize], 1.8*dsize, 0, 3)
    db.draw_circle([x+5*l+3.65*dsize+1.125*ypitch, y+dsize-(i+3)*0.24*dsize], 0.04*dsize, 0.1)
  ''' SCH '''
  y = y - ypitch
  db.draw_text_box([x, y], 'SCH', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], 5*l+4.55*dsize+0.75*ypitch, 0, 3)
  for i in range(3):
    db.draw_arrow([x+5*l+2.75*dsize+1.125*ypitch, y+dsize-i*0.24*dsize], 1.8*dsize, 0, 3)
    db.draw_circle([x+5*l+3.65*dsize+1.125*ypitch, y+dsize-(i+3)*0.24*dsize], 0.04*dsize, 0.1)
  ''' FBH '''
  y = y - ypitch
  db.draw_text_box([x, y], 'FBH', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], 5*l+4.55*dsize+0.75*ypitch, 0, 3)
  for i in range(3):
    db.draw_arrow([x+5*l+2.75*dsize+1.125*ypitch, y+dsize-i*0.24*dsize], 1.8*dsize, 0, 3)
    db.draw_circle([x+5*l+3.65*dsize+1.125*ypitch, y+dsize-(i+3)*0.24*dsize], 0.04*dsize, 0.1)
  ''' HUL Matrix '''
  db.draw_text_box([x+5*l+4.55*dsize+1.125*ypitch, y-dsize], 'HUL Matrix', dsize)
  #db.draw_text_box([x+5*l+7.55*dsize+0.75*ypitch, y-dsize], 'HUL Matrix', dsize)
  db.draw_arrow([x+5*l+10.55*dsize+1.125*ypitch, y+0.5*dsize+ypitch], 2*l-3*dsize+0.375*ypitch, 0, 3)
  db.draw_arrow([x+7*l+7.55*dsize+1.5*ypitch, y+0.5*dsize+ypitch], 0, 0.5*dsize+3*ypitch, 3)
  db.draw_arrow([x+7*l+7.55*dsize+1.5*ypitch, y+dsize+4*ypitch], l, 0, 3)
