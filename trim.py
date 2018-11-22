#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import math
import os
import sys

import ROOT

import rangeenergy

#_______________________________________________________________________________
alpha_mass = 3727.379
alpha_energy = 8.784861
theta_cut = 4. # deg

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
def show(emulsion_density, input_file, output_dir):
  ROOT.gROOT.SetBatch()
  ROOT.gStyle.SetOptStat(1110)
  ROOT.gStyle.SetOptFit(1)
  re = rangeenergy.RangeEnergy()
  c1 = ROOT.TCanvas()
  h1 = ROOT.TH1F('h1', 'h1', 100, 46, 56) # z
  h1.GetXaxis().SetTitle('Range [#mum]')
  h2 = ROOT.TH1F('h2', 'h2', 100, 0, 45) # theta
  h2.GetXaxis().SetTitle('#theta [Deg.]')
  h3 = ROOT.TH1F('h3', 'h3', 100, -180, 180) # phi
  h3.GetXaxis().SetTitle('#phi [Deg.]')
  with open(input_file, 'r') as f:
    start = False
    for line in f:
      line = line.strip()
      columns = line.split()
      if len(columns) != 4:
        continue
      if '-' in columns[0]:
        start = True
        continue
      if not start:
        continue
      event = int(columns[0])
      x = float(columns[2])*1e-4
      y = float(columns[3])*1e-4
      z = float(columns[1])*1e-4
      v = ROOT.TVector3(x, y, z)
      h2.Fill(v.Theta()*ROOT.TMath.RadToDeg())
      if v.Theta()*ROOT.TMath.RadToDeg() > theta_cut: continue
      h1.Fill(v.Mag())
      h3.Fill(v.Phi()*ROOT.TMath.RadToDeg())
  f1 = ROOT.TF1('f1', 'gaus')
  c1.Divide(2, 2)
  c1.cd(1)
  h1.Draw()
  h1.Fit('f1', 'Q')
  for i in range(3):
    m = f1.GetParameter(1)
    s = f1.GetParameter(2)
    w = 3.0
    h1.Fit('f1', 'Q', '', m - w*s, m + w*s)
  alpha_range = f1.GetParameter(1)
  alpha_straggling = f1.GetParameter(2)
  c1.cd(3)
  h2.Draw()
  c1.cd(4)
  h3.Draw()
  c1.cd(2)
  tex = ROOT.TLatex()
  tex.SetNDC()
  tex.SetTextFont(132)
  tex.SetTextSize(0.07)
  tex.DrawLatex(0.10, 0.85, '{}'.format(os.path.basename(input_file)))
  tex.DrawLatex(0.12, 0.75, 'E_{} = {:.3f} MeV'.format('{#alpha}', alpha_energy))
  tex.DrawLatex(0.12, 0.65, 'R_{} = {:.3f} #pm {:.3f} #mum ({})'
                .format('{#alpha}', alpha_range, alpha_straggling,
                        '#color['+str(ROOT.kOrange+1)+']{TRIM}'))
  tex.DrawLatex(0.12, 0.55, 'R_{} = {:.3f} #pm {:.3f} #mum ({})'
                .format('{#alpha}',
                        re.RangeFromKE(alpha_mass, alpha_energy,
                                       2, emulsion_density),
                        re.RangeStragglingFromKE(alpha_mass, alpha_energy,
                                                 2, emulsion_density),
                        '#color['+str(ROOT.kBlue+1)+']{RangeEnergy}'))
  c1.Print(os.path.join(output_dir, 'trim.pdf'))
#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('emulsion_density', type=float, nargs='?',
                      help='emulsion density (default=3.544)',
                      default=3.544)
  parser.add_argument('input_file',
                      help='default TRIM output file.')
  parser.add_argument('output_dir', nargs='?',
                      default='output/SRIM',
                      help='default canvas output directory.')
  parsed, unpased = parser.parse_known_args()
  try:
    show(parsed.emulsion_density, parsed.input_file, parsed.output_dir)
  except:
    print(sys.exc_info())
