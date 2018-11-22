#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import ROOT

from settings import a4size

output_name = 'baryon_octet.ps'

#_______________________________________________________________________________
def draw():
  ROOT.gROOT.SetBatch()
  cx = 2000
  cy = 2000
  c1 = ROOT.TCanvas('c1', 'c1', cx, cy)
  t1 = ROOT.TLatex()
  t1.SetTextFont(132)
  t1.SetTextSize(0.04)
  l1 = ROOT.TLine()
  l1.SetLineWidth(2)
  width = 0.6
  height = 0.2*math.sqrt(3)+0.2
  xstart = (1.0 - width)/2
  ystart = 0.5
  a1 = ROOT.TArrow(xstart, ystart, xstart+width, ystart, 0.02, '|>')
  a1.SetNDC()
  l = 0.02*math.sqrt(3)
  xspace = 0.05
  a1.SetAngle(40)
  a1.SetLineWidth(2)
  # a1.DrawArrow(xstart, ystart, xstart+width, ystart)
  # a1.DrawArrow(xstart+width/2, ystart-height/2,
  #              xstart+width/2, ystart+height/2)
  x = [0.3, 0.4, 0.5, 0.6, 0.7]
  y = [0.5-0.1*math.sqrt(3)*cx/cy, 0.5, 0.5+0.1*math.sqrt(3)*cx/cy]
  xmargin = 0.1
  ymargin = xmargin*cx/cy
  a1.DrawArrow(xstart, y[0]-ymargin, xstart+width, y[0]-ymargin)
  a1.DrawArrow(x[0]-xmargin, ystart-height/2, x[0]-xmargin, ystart+height/2)
  l1.DrawLineNDC(x[0], y[1], x[4], y[1])
  for j in range(2):
    for i in range(4):
      l1.DrawLineNDC(x[1], y[j*2], x[3], y[j*2])
      if i == 0 or i == 2:
        l1.DrawLineNDC(x[i], y[1], x[i+1], y[j*2])
        l1.DrawLineNDC(x[i+2], y[1], x[i+1], y[j*2])
  t1.SetTextAlign(22)
  for i in range(3):
    t1.DrawLatexNDC(xstart-0.04, y[i], '{}'.format(-2+i))
    t1.DrawLatexNDC(x[i*2], y[0]-ymargin-0.03, '{}'.format(-1+i))
  t1.SetTextFont(12)
  t1.DrawLatexNDC(0.54+width/2, y[0]-ymargin, 'I_{3}')
  t1.DrawLatexNDC(xstart, 0.54+height/2, 'S')
  t1.SetTextFont(132)
  t1.DrawLatexNDC(x[1]-0.02, y[2]+0.07, 'n')
  t1.DrawLatexNDC(x[3]+0.02, y[2]+0.07, 'p')
  t1.DrawLatexNDC(x[1]-0.02, y[2]+0.03, '(udd)')
  t1.DrawLatexNDC(x[3]+0.02, y[2]+0.03, '(uud)')
  t1.DrawLatexNDC(x[0]-0.04, y[1]+0.02, '#Sigma^{#minus}')
  t1.DrawLatexNDC(x[0]-0.04, y[1]-0.025, '(dds)')
  t1.DrawLatexNDC(x[2]-0.065, y[1]+0.025, '#Lambda')
  t1.DrawLatexNDC(x[2]-0.065, y[1]-0.025, '(uds)')
  t1.DrawLatexNDC(x[2]+0.065, y[1]+0.025, '#Sigma^{0}')
  t1.DrawLatexNDC(x[2]+0.065, y[1]-0.025, '(uds)')
  t1.DrawLatexNDC(x[4]+0.04, y[1]+0.02, '#Sigma^{+}')
  t1.DrawLatexNDC(x[4]+0.04, y[1]-0.025, '(uus)')
  t1.DrawLatexNDC(x[1]-0.02, y[0]-0.02, '#Xi^{#minus}')
  t1.DrawLatexNDC(x[1]-0.02, y[0]-0.06, '(dss)')
  t1.DrawLatexNDC(x[3]+0.02, y[0]-0.02, '#Xi^{0}')
  t1.DrawLatexNDC(x[3]+0.02, y[0]-0.06, '(uss)')
  print('draw ... {}'.format(output_name))
  c1.Print(output_name)
