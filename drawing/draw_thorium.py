#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ROOT

import draw_basic as db
import settings

output_name = 'thorium.ps'

scale = 1

box_keeper = []
t1 = ROOT.TLatex()
t1.SetTextFont(132)
a1 = ROOT.TArrow(0, 0, 1, 1, 0.002, '|>')
a1.SetAngle(40)
a1.SetLineWidth(2)
w = 0.10*scale
h = 0.06*scale

#_______________________________________________________________________________
def draw_nuclide(x, y, nuclide, half_life, arrow=None, decay=None):
  box = ROOT.TBox(x, y, x+w, y+h)
  box.SetFillColor(0)
  box.Draw('l')
  box_keeper.append(box)
  t1.SetTextAlign(22)
  t1.SetTextSize(0.024)
  t1.DrawLatexNDC(x+w/2, y+h/2+0.1*h, nuclide)
  t1.SetTextSize(0.014)
  t1.DrawLatexNDC(x+w/2, y+h/2-0.25*h, '#tau = {}'.format(half_life))
  #db.draw_text([x+w/2, y+h/2-1.5], nuclide)
  #db.draw_text([x+w/2, y+h/2+3.5], '\325', font='ISOLatin1Encoding')
  if arrow is not None:
    if 'b' in arrow.lower():
      a1.DrawArrow(x+w*0.18, y, x+w*0.18, y-h, 0.01, '|>')
    if 'r' in arrow.lower():
      a1.DrawArrow(x+w, y+h/2, x+1.5*w, y+1.5*h, 0.01, '|>')
  if decay is not None:
    for i, d in enumerate(decay):
      t1.SetTextAlign(32)
      t1.DrawLatexNDC(x+w*1.3, y-(i+1)*h/(len(decay)+1), d+' MeV')

#_______________________________________________________________________________
def draw():
  ROOT.gROOT.SetBatch()
  c1 = ROOT.TCanvas('c1', 'c1', 2000, 2000)
  l1 = ROOT.TLine()
  lx = 0.15
  ly = 0.05
  xstart = 0.05
  ystart = 0.80
  ''' thorium series '''
  x = xstart
  y = ystart
  draw_nuclide(x, y, '^{232}Th', '1.40 #times 10^{10} y', arrow='b',
               )#decay=['78.2%  4.012', '21.7%  3.947'])
  y -= 2*h
  draw_nuclide(x, y, '^{228}Ra', '5.75 y', arrow='r')
  x += w*1.5
  y += h
  draw_nuclide(x, y, '^{228}Ac', '6.15 h', arrow='r')
  x += w*1.5
  y += h
  draw_nuclide(x, y, '^{228}Th', '1.91 y', arrow='b',
               decay=['73.4%  5.423', '26.0%  5.340'])
  y -= 2*h
  draw_nuclide(x, y, '^{224}Ra', '3.63 d', arrow='b',
               decay=['94.92%  5.685', '5.06%  5.449'])
  y -= 2*h
  draw_nuclide(x, y, '^{220}Rn', '55.6 s', arrow='b',
               decay=['99.88%  6.288', '0.11%  5.747'])
  y -= 2*h
  draw_nuclide(x, y, '^{216}Po', '0.145 s', arrow='b',
               decay=['99.99%  6.778'])
  y -= 2*h
  draw_nuclide(x, y, '^{212}Pb', '10.64 h', arrow='r')
  x += w*1.5
  y += h
  draw_nuclide(x, y, '^{212}Bi', '60.55 m', arrow='br',
               decay=['25.13%  6.051', '9.75%  6.090', '0.61%  5.768'])
  t1.SetTextAlign(32)
  t1.DrawLatexNDC(x+w*1.3, y+1.3*h, '64.06%')
  y -= 2*h
  draw_nuclide(x, y, '^{208}Tl', '3.053 m', arrow='r')
  x += w*1.5
  y += 3*h
  draw_nuclide(x, y, '^{212}Po', '0.299 #mus', arrow='b',
               decay=['100%  8.785'])
  y -= 2*h
  draw_nuclide(x, y, '^{208}Pb', 'stable')

  print('draw ... {}'.format(output_name))
  c1.Print(output_name)
