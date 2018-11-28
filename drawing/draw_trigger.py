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
  l = 10
  orsize = 2*dsize
  andsize = 2*dsize
  notsize = 0.4*dsize
  ''' BH1 '''
  db.draw_text_box([x, y], 'BH1', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], l, 0, 3)
  db.draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  db.draw_arrow([x+l+5*dsize, y+dsize], l, 0, 3)
  db.draw_arrow([x+2*l+(7.15)*dsize, y+(2-0.8*2)*dsize], l, 0, 3)
  db.draw_arrow([x+3*l+(7.15)*dsize, y+(2-0.8*2)*dsize], 0, -0.75*dsize, 3)
  db.draw_arrow([x+3*l+(7.15)*dsize, y+(2-0.8*2-0.75)*dsize], l, 0, 3)
  db.draw_logic_or([x+2*l+(4+0.9)*dsize, y+(1-0.8*2)*dsize], orsize)
  ''' BH2 '''
  y = y - ypitch
  db.draw_text_box([x, y], 'BH2', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], 3*l+4.15*dsize, 0, 3)
  db.draw_arrow([x+3*dsize, y+dsize], 3*l+4.15*dsize, 0, 3)
  db.draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  db.draw_arrow([x+3*l+(7.15)*dsize, y+dsize], 0, 0.75*dsize, 3)
  db.draw_arrow([x+3*l+(7.15)*dsize, y+1.75*dsize], l, 0, 3)
  db.draw_logic_and([x+4*l+7.15*dsize, y+1.2*dsize], andsize)
  db.draw_arrow([x+4*l+9.65*dsize, y+2.2*dsize], l, 0, 3)
  db.draw_arrow([x+5*l+9.65*dsize, y+2.2*dsize], 0, -2.35*dsize, 3)
  db.draw_arrow([x+5*l+9.65*dsize, y-0.15*dsize], l, 0, 3)
  ''' BAC '''
  y = y - ypitch
  db.draw_text_box([x, y], 'BAC1', dsize)
  db.draw_arrow([x+4*dsize, y+dsize], l, 0, 3)
  db.draw_arrow([x+l+4*dsize, y+dsize], 0, -0.35*ypitch, 3)
  db.draw_arrow([x+l+4*dsize, y+dsize-0.35*ypitch], 2*l, 0, 3)
  y = y - ypitch
  db.draw_text_box([x, y], 'BAC2', dsize)
  db.draw_arrow([x+4*dsize, y+dsize], l, 0, 3)
  db.draw_arrow([x+l+4*dsize, y+dsize], 0, 0.35*ypitch, 3)
  db.draw_arrow([x+l+4*dsize, y+dsize+0.35*ypitch], 2*l, 0, 3)
  db.draw_arrow([x+3*l+4.5*dsize, y+dsize+0.5*ypitch],
                2*l+5.15*dsize, 0, 3)
  db.draw_logic_or([x+2*l+4.9*dsize, y+dsize+(ypitch-2*dsize)/2],
                   orsize, False)
  db.draw_arrow([x+5*l+9.65*dsize, y+2.5*dsize], 0, 2.35*dsize, 3)
  db.draw_arrow([x+5*l+9.65*dsize, y+4.85*dsize], l, 0, 3)
  #db.draw_circle([x+2*l+6.15*dsize+notsize, y+2.5*dsize], notsize)
  db.draw_circle([x+6*l+9.65*dsize-notsize, y+4.85*dsize], notsize)
  # K-beam
  db.draw_logic_and([x+6*l+9.65*dsize, y+4.35*dsize], andsize)
  db.draw_text([x+6*l+(9.65+1.25)*dsize, y+6.8*dsize], 'K beam')
  db.draw_arrow([x+6*l+12.15*dsize, y+5.35*dsize], l, 0, 3)
  db.draw_arrow([x+7*l+12.15*dsize, y+5.35*dsize], 0, -(7.6)*dsize, 3)
  db.draw_arrow([x+7*l+12.15*dsize, y-2.25*dsize], l, 0, 3)
  ''' PVAC '''
  y = y - ypitch
  db.draw_text_box([x, y], 'PVAC', dsize)
  db.draw_arrow([x+4*dsize, y+dsize], 6*l+3.55*dsize+0.75*ypitch, 0, 3)
  ''' FAC '''
  y = y - ypitch
  db.draw_text_box([x, y], 'FAC', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], 3*l, 0, 3)
  db.draw_arrow([x+3*l+3*dsize, y+dsize], 0, 0.5*ypitch+0.75*dsize, 3)
  db.draw_arrow([x+3*l+3*dsize, y+1.75*dsize+0.5*ypitch],
                3*l+4.55*dsize+0.75*ypitch, 0, 3)
  db.draw_circle([x+6*l+9.65*dsize-notsize,
                  y+(1.75)*dsize+0.5*ypitch], notsize)
  # K scat
  db.draw_text([x+6*l+10.85*dsize, y+4.7*dsize], 'K scat')
  db.draw_logic_and([x+6*l+9.65*dsize, y+2.25*dsize], andsize)
  db.draw_arrow([x+6*l+(9.65+2.5)*dsize, y+3.25*dsize], 2*l, 0, 3)
  ''' TOF '''
  y = y - ypitch
  db.draw_text_box([x, y], 'TOF', dsize)
  db.draw_arrow([x+3*dsize, y+dsize], l, 0, 3)
  db.draw_text_box([x+l+3*dsize, y], 'MT', dsize)
  db.draw_arrow([x+l+5*dsize, y+dsize], l, 0, 3)
  db.draw_logic_or([x+2*l+5.6*dsize, y-0.6*dsize], orsize)
  db.draw_arrow([x+2*l+8.35*dsize, y+0.4*dsize], l, 0, 3)
  db.draw_arrow([x+3*l+8.35*dsize, y+0.4*dsize], 0, 2.1*dsize+ypitch, 3)
  db.draw_arrow([x+3*l+8.35*dsize, y+2.5*dsize+ypitch],
                3*l+1.3*dsize, 0, 3)
  db.draw_circle([x+1.5*l+5*dsize, y+dsize], 1, 0.1)
  # KK
  #db.draw_text([x+8*l+7.55*dsize+1.875*ypitch, y+dsize+2.4*ypitch], '(K, K)')
  db.draw_logic_and([x+8*l+12.15*dsize, y+5.25*dsize], andsize)
  db.draw_arrow([x+8*l+14.65*dsize, y+6.25*dsize], 2*l, 0, 2)
  #db.draw_text([x+9*l+7.55*dsize+2.25*ypitch, y+2.5*dsize+1.5*ypitch], '(K,K)')
  db.draw_text([x+9*l+14.65*dsize, y+6.75*dsize], 'Trigger')
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
  db.draw_arrow([x+5*l+10.55*dsize+1.125*ypitch, y+0.5*dsize+ypitch], 2*l+1.6*dsize-1.125*ypitch, 0, 3)
  db.draw_arrow([x+7*l+12.15*dsize, y+3.5*dsize], 0, 11.25*dsize, 3)
  db.draw_arrow([x+7*l+12.15*dsize, y+14.75*dsize], l, 0, 3)
