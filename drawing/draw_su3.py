#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import ROOT

from settings import a4size

isospin = 'I'
output_name = 'su3.ps'

#_______________________________________________________________________________
def draw():
  ROOT.gROOT.SetBatch()
  c1 = ROOT.TCanvas('c1', 'c1', int(a4size[0])*10, int(a4size[1])*10)
  t1 = ROOT.TLatex()
  t1.SetTextFont(132)
  t1.SetTextSize(0.02)
  l1 = ROOT.TLine()
  xstart = 0.1
  ystart = 0.9
  l = 0.02*math.sqrt(3)
  xspace = 0.05
  ''' 27s '''
  x = xstart
  y = ystart
  t1.SetTextAlign(22)
  t1.DrawLatexNDC(x, y, '27_{s}')
  ty = math.sqrt(3)/2*l * a4size[0]/a4size[1]
  tx = 1/2*l
  for i in range(4):
    l1.DrawLineNDC(x+xspace+i*l, y, x+xspace+i*l+l, y)
    l1.DrawLineNDC(x+xspace+i*l, y, x+xspace+i*l+tx, y+ty)
    l1.DrawLineNDC(x+xspace+i*l, y, x+xspace+i*l+tx, y-ty)
    l1.DrawLineNDC(x+xspace+i*l+l, y, x+xspace+i*l+l-tx, y+ty)
    l1.DrawLineNDC(x+xspace+i*l+l, y, x+xspace+i*l+l-tx, y-ty)
  for j in range(2):
    sign = 2*(j%2-0.5)
    l1.DrawLineNDC(x+xspace+2*tx, y+2*sign*ty, x+xspace+2*tx+2*l, y+2*sign*ty)
    for i in range(3):
      l1.DrawLineNDC(x+xspace+i*l+tx, y+sign*ty, x+xspace+i*l+tx+l, y+sign*ty)
      l1.DrawLineNDC(x+xspace+i*l+tx, y+sign*ty, x+xspace+i*l+2*tx, y+2*sign*ty)
      l1.DrawLineNDC(x+xspace+(i+1)*l+tx, y+sign*ty, x+xspace+(i+1)*l, y+2*sign*ty)
  t1.SetTextAlign(12)
  t1.DrawLatexNDC(x+2*xspace+4*l, y+2*ty, 'S=0')
  t1.DrawLatexNDC(x+3*xspace+4*l, y+2*ty, 'NN(I=1)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y+ty, 'S=-1')
  t1.DrawLatexNDC(x+3*xspace+4*l, y+ty, '#SigmaN(I=3/2), #SigmaN-#LambdaN(I=1/2)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y, 'S=-2')
  t1.DrawLatexNDC(x+3*xspace+4*l, y, '#Sigma#Sigma(I=2), #XiN-#Sigma#Lambda-#Lambda#Lambda(I=1), #XiN-#Sigma#Sigma-#Lambda#Lambda(I=0)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y-ty, 'S=-3')
  t1.DrawLatexNDC(x+3*xspace+4*l, y-ty, '#Xi#Sigma(I=3/2), #Xi#Sigma-#Xi#Lambda(I=1/2)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y-2*ty, 'S=-4')
  t1.DrawLatexNDC(x+3*xspace+4*l, y-2*ty, '#Xi#Xi(I=1)')
  ''' 10a '''
  y -= 5.5*ty
  t1.SetTextAlign(22)
  t1.DrawLatexNDC(x, y, '#bar{10}_{a}')
  for i in range(3):
    yj = y + (0.5-i)*ty
    for j in range(i+1):
      xj = x + xspace + j*l + (3-i)*tx
      l1.DrawLineNDC(xj, yj, xj+l, yj)
      l1.DrawLineNDC(xj, yj, xj+tx, yj+ty)
      l1.DrawLineNDC(xj+l, yj, xj+l-tx, yj+ty)
  t1.SetTextAlign(12)
  t1.DrawLatexNDC(x+2*xspace+4*l, y+1.5*ty, 'S=0')
  t1.DrawLatexNDC(x+3*xspace+4*l, y+1.5*ty, 'NN(I=0)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y+0.5*ty, 'S=-1')
  t1.DrawLatexNDC(x+3*xspace+4*l, y+0.5*ty, '#SigmaN-#LambdaN(I=1/2)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y-0.5*ty, 'S=-2')
  t1.DrawLatexNDC(x+3*xspace+4*l, y-0.5*ty, '#XiN-#Sigma#Lambda(I=1/2)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y-1.5*ty, 'S=-3')
  t1.DrawLatexNDC(x+3*xspace+4*l, y-1.5*ty, '#Xi#Sigma(I=3/2)')
  ''' 10a '''
  y -= 5*ty
  t1.SetTextAlign(22)
  t1.DrawLatexNDC(x, y, '10_{a}')
  for i in range(3):
    yj = y - (1.5-i)*ty
    for j in range(i+1):
      xj = x + xspace + j*l + (3-i)*tx
      l1.DrawLineNDC(xj, yj+ty, xj+l, yj+ty)
      l1.DrawLineNDC(xj, yj+ty, xj+tx, yj)
      l1.DrawLineNDC(xj+l, yj+ty, xj+l-tx, yj)
  t1.SetTextAlign(12)
  t1.DrawLatexNDC(x+2*xspace+4*l, y+1.5*ty, 'S=-1')
  t1.DrawLatexNDC(x+3*xspace+4*l, y+1.5*ty, '#SigmaN(I=3/2)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y+0.5*ty, 'S=-2')
  t1.DrawLatexNDC(x+3*xspace+4*l, y+0.5*ty, '#XiN-#Sigma#Lambda-#Sigma#Sigma(I=1)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y-0.5*ty, 'S=-3')
  t1.DrawLatexNDC(x+3*xspace+4*l, y-0.5*ty, '#Xi#Sigma-#Xi#Lambda(I=1/2)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y-1.5*ty, 'S=-4')
  t1.DrawLatexNDC(x+3*xspace+4*l, y-1.5*ty, '#Xi#Xi(I=0)')
  ''' 8s '''
  y -= 4.5*ty
  t1.SetTextAlign(22)
  t1.DrawLatexNDC(x, y, '8_{s}')
  for i in range(2):
    xj = x+xspace+i*l + 2*tx
    l1.DrawLineNDC(xj, y, xj+l, y)
    for j in range(2):
      sign = 2*(j%2-0.5)
      l1.DrawLineNDC(xj, y, xj+tx, y+sign*ty)
      l1.DrawLineNDC(xj+2*tx, y, xj+tx, y+sign*ty)
      l1.DrawLineNDC(xj+tx, y+sign*ty, xj+(3-i*3)*tx, y+sign*ty)
  t1.SetTextAlign(12)
  t1.DrawLatexNDC(x+2*xspace+4*l, y+ty, 'S=-1')
  t1.DrawLatexNDC(x+3*xspace+4*l, y+ty, '#SigmaN-#LambdaN(I=1/2)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y, 'S=-2')
  t1.DrawLatexNDC(x+3*xspace+4*l, y, '#XiN-#Sigma#Lambda(I=1), #XiN-#Sigma#Sigma-#Lambda#Lambda(I=0)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y-ty, 'S=-3')
  t1.DrawLatexNDC(x+3*xspace+4*l, y-ty, '#Xi#Sigma-#Xi#Lambda(I=1/2)')
  ''' 8a '''
  y -= 4*ty
  t1.SetTextAlign(22)
  t1.DrawLatexNDC(x, y, '8_{a}')
  for i in range(2):
    xj = x+xspace+i*l + 2*tx
    l1.DrawLineNDC(xj, y, xj+l, y)
    for j in range(2):
      sign = 2*(j%2-0.5)
      l1.DrawLineNDC(xj, y, xj+tx, y+sign*ty)
      l1.DrawLineNDC(xj+2*tx, y, xj+tx, y+sign*ty)
      l1.DrawLineNDC(xj+tx, y+sign*ty, xj+(3-i*3)*tx, y+sign*ty)
  t1.SetTextAlign(12)
  t1.DrawLatexNDC(x+2*xspace+4*l, y+ty, 'S=-1')
  t1.DrawLatexNDC(x+3*xspace+4*l, y+ty, '#SigmaN-#LambdaN(I=1/2)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y, 'S=-2')
  t1.DrawLatexNDC(x+3*xspace+4*l, y, '#XiN-#Sigma#Lambda-#Sigma#Sigma(I=1), #XiN(I=0)')
  t1.DrawLatexNDC(x+2*xspace+4*l, y-ty, 'S=-3')
  t1.DrawLatexNDC(x+3*xspace+4*l, y-ty, '#Xi#Sigma-#Xi#Lambda(I=1/2)')
  ''' 1s '''
  y -= 3*ty
  t1.SetTextAlign(22)
  t1.DrawLatexNDC(x, y, '1_{s}')
  m1 = ROOT.TMarker(x+xspace+2*l, y, 8)
  m1.SetMarkerSize(2)
  m1.Draw()
  #t1.DrawLatexNDC(x+xspace+2*l, y-0.002, '#bullet')
  t1.SetTextAlign(12)
  t1.DrawLatexNDC(x+2*xspace+4*l, y, 'S=-2')
  t1.DrawLatexNDC(x+3*xspace+4*l, y, '#XiN-#Sigma#Sigma-#Lambda#Lambda(I=0)')
  print('draw ... {}'.format(output_name))
  c1.Print(output_name)
