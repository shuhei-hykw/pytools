#!/usr/bin/env python3.8

import ROOT

r = 10

#______________________________________________________________________________
def run():
  ROOT.gROOT.SetBatch()
  n = 3
  scale = 2000
  c1 = ROOT.TCanvas('c1', 'c1', scale*n, scale)
  c1.Divide(n, 1)
  graphs = []
  for i in range(n):
    c1.cd(i + 1)
    g = ROOT.TGraph()
    g.SetMarkerStyle(8)
    g.Draw('AP')
    graphs.append(g)
  x0 = ROOT.gRandom.Rndm() * 10
  y0 = ROOT.gRandom.Rndm() * 10
  for i in range(100):
    theta = ROOT.gRandom.Rndm() * 360. * ROOT.TMath.DegToRad()
    x = r * ROOT.TMath.Cos(theta)
    y = r * ROOT.TMath.Sin(theta)
    graphs[0].SetPoint(i, x - x0, y - y0)
    u = x / (x*x + y*y)
    v = - y / (x*x + y*y)
    graphs[1].SetPoint(i, u, v)
  # for
  # graphs[2]
  c1.Print('conformal_transformation.pdf')

#______________________________________________________________________________
if __name__ == '__main__':
  run()
