#!/usr/bin/env python3

import argparse
import os
import sys

#______________________________________________________________________________
particle = []
index_min = 1.0
index_max = 1.3
p_min = 0.0
p_max = 2.0

#______________________________________________________________________________
def initialize():
  particle.append({'name': '#font[12]{e}', 'pdg': 11,
                   'color': ROOT.kCyan+1, 'position': [0.1, 0.1]})
  particle.append({'name': '#mu', 'pdg': 13,
                   'color': ROOT.kBlack, 'position': [0.21, 0.21]})
  particle.append({'name': '#pi', 'pdg': 211,
                   'color': ROOT.kBlue+1, 'position': [0.32, 0.32]})
  particle.append({'name': '#font[12]{K}', 'pdg': 321,
                   'color': ROOT.kGreen+1, 'position': [0.51, 0.51]})
  particle.append({'name': '#font[12]{p}', 'pdg': 2212,
                   'color': ROOT.kRed+1, 'position': [0.71, 0.71]})

#_______________________________________________________________________________
def mass(pdg_code):
  return ROOT.TDatabasePDG.Instance().GetParticle(pdg_code).Mass()

#_______________________________________________________________________________
def show(target_index, gray_scale):
  math = ROOT.TMath
  ROOT.gROOT.SetBatch()
  ROOT.gROOT.SetStyle('MyStyle')
  c1 = ROOT.TCanvas()
  h1 = ROOT.TH1F('h1', 'h1', 1, p_min, p_max)
  h1.SetMinimum(index_min)
  h1.SetMaximum(index_max)
  h1.GetXaxis().SetTitle('Momentum [GeV/#font[12]{c}]')
  h1.GetYaxis().SetTitle('Refractive index')
  h1.Draw()
  tex = ROOT.TLatex()
  tex.SetNDC()
  tex.SetTextFont(132)
  tex.SetTextSize(0.1)
  func = []
  for p in particle:
    ''' relativistic momentum
    p = g * b * m = 1 / sqrt( 1 - b^2 ) * b * m
    p / m = b / sqrt( 1 - b^2 )
    n = 1 / b = sqrt( 1 + ( m / p )^2 )
    p = m / sqrt( n^2 -1 )
    '''
    momentum_min = max( mass(p['pdg']) / math.Sqrt(math.Sq(index_max-0.005) - 1.),
                                   p_min + 0.05 )
    momentum_max = min( mass(p['pdg']) / math.Sqrt(math.Sq(index_min+0.005) - 1.),
                                   p_max - 0.05 )
    try:
      target_threshold = mass(p['pdg']) / math.Sqrt(math.Sq(target_index) - 1.)
    except ZeroDivisionError:
      target_threshold = math.QuietNaN()
    f1 = ROOT.TF1('f{}'.format(p['name']),
                  'TMath::Sqrt( 1 + [0] / ( x*x ) )',
                  0, 2)
                  #momentum_min, momentum_max)
    f1.SetLineColor(ROOT.kBlack if gray_scale else p['color'])
    f1.SetParameter(0, math.Sq(mass(p['pdg'])))
    f1.Draw('same')
    tex.SetTextColor(ROOT.kBlack if gray_scale else p['color'])
    tex.DrawLatex(p['position'][0], p['position'][1], p['name'])
    func.append(f1)
    print('{:12} ( {:7.5} GeV/c2) :  pth = {:10.5f} GeV'
          .format(p['name'], mass(p['pdg']), target_threshold))
  c1.Print('cherenkov.ps')

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('target_index', nargs='?',
                      type=float, default=1.05,
                      help='target refractive index')
  parser.add_argument('--gray-scale', '-g',
                      action='store_true', help='print with gray scale')
  parsed, unpased = parser.parse_known_args()
  try:
    import ROOT
    initialize()
    show(parsed.target_index, parsed.gray_scale)
  except:
    print(sys.exc_info())
