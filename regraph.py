#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import math
import os
import sys

import ROOT

import rangeenergy

#_______________________________________________________________________________
proton_mass = 938.272
alpha_mass = 3727.379

#_______________________________________________________________________________
def calc_energy(e):
  return float(e[0]) * (1e-6 if e[1] == 'eV' else
                        1e-3 if e[1] == 'keV' else
                        1e+0 if e[1] == 'MeV' else
                        1e+3 if e[1] == 'GeV' else
                        1e+6 )

#_______________________________________________________________________________
def calc_range(r):
  return float(r[0]) * (1e-4 if r[1] == 'A' else
                        1e-0 if r[1] == 'um' else
                        1e+3)

#_______________________________________________________________________________
def process(output_dir, emulsion_density):
  ROOT.gROOT.SetBatch()
  re = rangeenergy.RangeEnergy()
  c1 = ROOT.TCanvas()
  g1 = ROOT.TGraphErrors()
  g2 = ROOT.TGraphErrors()
  #for e in [int(x%10)*(10**int(x/10)) for x in range(15)]:
  for e in [1e-1*x for x in range(200)]:
    proton_range = re.RangeFromKE(proton_mass, e, 1, emulsion_density)
    proton_strg = re.RangeStragglingFromKE(proton_mass, e, 1, emulsion_density)
    alpha_range = re.RangeFromKE(alpha_mass, e, 2, emulsion_density)
    alpha_strg = re.RangeStragglingFromKE(alpha_mass, e, 2, emulsion_density)
    ipoint = g1.GetN()
    g1.SetPoint(ipoint, e, proton_range)
    g1.SetPointError(ipoint, 0.05, proton_strg)
    g2.SetPoint(ipoint, e, alpha_range)
    g2.SetPointError(ipoint, 0.05, alpha_strg)
    print('KE={:8.3f} R={:8.3f} S={:8.3f}'.format(e, proton_range, proton_strg))
    print('KE={:8.3f} R={:8.3f} S={:8.3f}'.format(e, alpha_range, alpha_strg))
  f1 = ROOT.TF1('f1', 'pol5')
  g1.SetMarkerStyle(1)
  #g1.SetFillStyle(3010)
  g1.SetFillColor(ROOT.kOrange+1)
  g2.SetFillColor(ROOT.kOrange+1)
  g1.Draw('a2')
  g2.Draw('a2')
  # c1.SetLogx()
  # c1.SetLogy()
  c1.Update()
  c1.Print(os.path.join(output_dir, 'regraph.pdf'))

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('output_dir', nargs='?',
                      default='output/RangeEnergy',
                      help='default canvas output directory.')
  parser.add_argument('emulsion_density', nargs='?', type=int,
                      default=3.5443,
                      help='default emulsion density (3.5443).')
  parsed, unpased = parser.parse_known_args()
  try:
    process(parsed.output_dir, parsed.emulsion_density)
  except:
    print(sys.exc_info())
