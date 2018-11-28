#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ROOT

import draw_basic as db
from settings import a4size, line_width
import settings

output_name = 'product.ps'

#_______________________________________________________________________________
def draw_kminus(moveto):
  db.draw_text(moveto, 'K', font='Times-Italic')
  moveto[0] += 3
  moveto[1] += 2
  db.draw_text(moveto, '-', text_size=7)

#_______________________________________________________________________________
def draw_kplus(moveto):
  db.draw_text(moveto, 'K', font='Times-Italic')
  moveto[0] += 3
  moveto[1] += 2
  db.draw_text(moveto, '+', text_size=4)

#_______________________________________________________________________________
def draw_lambda(moveto):
  moveto[1] -= 2
  db.draw_text(moveto, 'L', font='Symbol')

#_______________________________________________________________________________
def draw_ximinus(moveto, sign=True):
  moveto[0] -= 1
  moveto[1] -= 2
  db.draw_text(moveto, 'X', font='Symbol')
  if sign:
    moveto[0] += 3
    moveto[1] += 2
    db.draw_text(moveto, '-', text_size=7)

#_______________________________________________________________________________
def draw():
  ROOT.gROOT.SetBatch()
  c1 = ROOT.TCanvas('c1', 'c1', 2000, 2000)
  t1 = ROOT.TLatex()
  t1.SetTextAlign(22)
  t1.SetTextSize(0.03)
  l1 = ROOT.TLine()
  lx = 0.15
  ly = 0.05
  a1 = ROOT.TArrow(0, 0, 1, 1, 0.02, '|>')
  a1.SetAngle(40)
  a1.SetLineWidth(2)
  ''' (K-, K+) '''
  xstart = 0.05
  ystart = 0.95
  arc1 = ROOT.TArc()
  ell1 = ROOT.TEllipse()
  arc1.SetFillColor(ROOT.kGray)
  ell1.SetFillColor(0)
  arc1.DrawArc(xstart+0.035+lx, ystart-0.04-ly, 0.07)
  arc1.SetFillColor(0)
  arc1.DrawArc(xstart+0.035+lx, ystart-0.02-ly, 0.02)
  t1.SetTextFont(132)
  t1.DrawLatexNDC(xstart+0.04, ystart-0.10-ly, 'target nucleus')
  t1.SetTextAlign(11)
  t1.DrawLatexNDC(xstart+0.58, ystart-0.035-1.5*ly,
                  'stopped and captured at emulsion')
  t1.SetTextAlign(22)
  t1.SetTextFont(12)
  t1.DrawLatexNDC(xstart-0.01, ystart, 'K^{-}')
  t1.DrawLatexNDC(xstart+0.09+2*lx, ystart, 'K^{+}')
  t1.DrawLatexNDC(xstart+0.035+lx, ystart-0.02-ly, 'p')
  t1.DrawLatexNDC(xstart+0.08+1.5*lx, ystart-0.035-1.5*ly, '#Xi^{-}')
  a1.DrawArrow(xstart+0.01, ystart-0.01, xstart+0.01+lx, ystart-0.01-ly)
  a1.DrawArrow(xstart+0.06+lx, ystart-0.01-ly,
               xstart+0.06+2*lx, ystart-0.01)
  a1.DrawArrow(xstart+0.06+lx, ystart-0.03-ly,
               xstart+0.06+1.5*lx, ystart-0.03-1.5*ly)
  a1.SetLineStyle(7)
  a1.DrawArrow(xstart+0.08+1.6*lx, ystart-0.035-1.6*ly,
               xstart+0.08+2*lx, ystart-0.035-2*ly)
  a1.SetLineStyle(0)
  a1.SetLineWidth(4)
  ''' Xi atom '''
  xstart += 0.5
  ystart += -0.2
  ell1.DrawEllipse(xstart, ystart, 0.12, 0.07, 0, 360, 0)
  arc1.DrawArc(xstart-0.085, ystart+0.05, 0.02)
  arc1.SetFillColor(ROOT.kGray)
  arc1.DrawArc(xstart, ystart, 0.025)
  wave = ROOT.TF1('wave', ('{} + {}*TMath::Sin(x*{})'
                           .format(ystart, 0.01, 200, 1)),
                  xstart+0.06, xstart+0.18)
  wave.SetLineColor(ROOT.kBlack)
  wave.Draw('same')
  t1.DrawLatexNDC(xstart-0.085, ystart+0.05, '#Xi^{-}')
  t1.SetTextFont(132)
  t1.DrawLatexNDC(xstart, ystart-0.10, '#Xi^{-}-atom')
  t1.DrawLatexNDC(xstart+0.23, ystart, 'X-ray')
  t1.SetTextFont(12)
  a1.DrawArrow(xstart-0.14, ystart-0.05,
               xstart-0.25, ystart-0.11)
  ''' Xi nucleus '''
  xstart -= 0.35
  ystart += -0.2
  arc1.DrawArc(xstart, ystart, 0.07)
  arc1.SetFillColor(0)
  arc1.DrawArc(xstart-0.015, ystart+0.01, 0.02)
  t1.DrawLatexNDC(xstart-0.015, ystart+0.01, '#Xi^{-}')
  t1.SetTextFont(132)
  t1.DrawLatexNDC(xstart, ystart-0.10, '#Xi^{-}-nucleus')
  t1.SetTextFont(12)
  ''' fragment '''
  a1.DrawArrow(xstart+0.15, ystart-0.02, xstart+0.3, ystart-0.04)
  a1.DrawArrow(xstart+0.12, ystart-0.096, xstart+0.3, ystart-0.24)
  a1.DrawArrow(xstart, ystart-0.16, xstart, ystart-0.24)
  arc1.SetFillColor(ROOT.kGray)
  arc1.DrawArc(xstart+0.45, ystart-0.06, 0.07)
  arc1.DrawArc(xstart+0.45, ystart-0.26, 0.06)
  arc1.DrawArc(xstart+0.35, ystart-0.38, 0.06)
  arc1.DrawArc(xstart-0.02, ystart-0.36, 0.06)
  arc1.SetFillColor(0)
  arc1.DrawArc(xstart+0.42, ystart-0.05, 0.02)
  arc1.DrawArc(xstart+0.48, ystart-0.07, 0.02)
  t1.DrawLatexNDC(xstart+0.42, ystart-0.05, '#Lambda')
  t1.DrawLatexNDC(xstart+0.48, ystart-0.07, '#Lambda')
  arc1.DrawArc(xstart+0.46, ystart-0.25, 0.02)
  arc1.DrawArc(xstart+0.34, ystart-0.37, 0.02)
  t1.DrawLatexNDC(xstart+0.46, ystart-0.25, '#Lambda')
  t1.DrawLatexNDC(xstart+0.34, ystart-0.37, '#Lambda')
  arc1.DrawArc(xstart, ystart-0.37, 0.02)
  arc1.DrawArc(xstart+0.07, ystart-0.30, 0.02)
  t1.DrawLatexNDC(xstart, ystart-0.37, '#Lambda')
  t1.DrawLatexNDC(xstart+0.07, ystart-0.30, '#Lambda')
  t1.SetTextAlign(12)
  t1.SetTextFont(132)
  t1.DrawLatexNDC(xstart+0.53, ystart-0.09, 'double-#Lambda hypernucleus')
  t1.DrawLatexNDC(xstart+0.53, ystart-0.35, 'twin #Lambda hypernuclei')
  t1.SetTextAlign(22)
  t1.DrawLatexNDC(xstart+0.02, ystart-0.45, 'single-#Lambda hypernucleus')
  print('draw ... {}'.format(output_name))
  c1.Print(output_name)

  # xstart = 10
  # ystart = a4size[1] - 50
  # ''' (K-, K+) '''
  # draw_kminus([xstart-3, ystart+1])
  # draw_kplus([xstart+53, ystart+1])
  # db.draw_circle([xstart+26, ystart-15], r=10, fc=0.8)
  # db.draw_circle([xstart+25, ystart-12], r=4, fc=1)
  # db.draw_text([xstart+25, ystart-13], 'p', font='Times-Italic')
  # db.draw_text([xstart+20, ystart-30], 'target nuclei')
  # db.draw_arrow([xstart, ystart], 20, -10, 2)
  # db.draw_arrow([xstart+30, ystart-10], 20, 10, 2)
  # db.draw_arrow([xstart+30, ystart-15], 10, -5, 2)
  # draw_ximinus([xstart+43, ystart-23])
  # draw_ximinus([xstart+50, ystart-13])
  # db.draw_text([xstart+71, ystart-15], 'production via \(')
  # draw_kminus([xstart+89, ystart-15])
  # db.draw_text([xstart+92, ystart-15], ',')
  # db.draw_text([xstart+71, ystart-15], 'production via \(')
  # ''' Xi atom '''
  # xstart = 80
  # ystart -= 30
  # db.draw_circle([xstart+80, ystart-30], r=6, fc=0.8)
  # db.draw_elip([xstart+80, ystart-30], 20, 0.6)
  # db.draw_circle([xstart+60, ystart-30], r=4)
  # draw_ximinus([xstart+60, ystart-30])
  # draw_ximinus([xstart+75, ystart-46])
  # db.draw_text([xstart+85, ystart-48], 'atom')
