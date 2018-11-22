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
def show(input_file, output_dir):
  ROOT.gROOT.SetBatch()
  re = rangeenergy.RangeEnergy()
  c1 = ROOT.TCanvas()
  g1 = ROOT.TGraph() # dedx elec.
  g2 = ROOT.TGraph() # dedx nuclear
  g3 = ROOT.TGraphErrors() # range
  g4 = ROOT.TGraph() # longitudinal straggling
  g5 = ROOT.TGraph() # lateral straggling
  g6 = ROOT.TGraph() # total straggling
  g7 = ROOT.TGraphErrors() # range (RangeEnergy)
  g8 = ROOT.TGraphErrors() # straggling ratio
  ipoint = 0
  with open(input_file, 'r') as f:
    for line in f:
      line = line.strip()
      columns = line.split()
      if len(columns) == 10:
        ion_energy = calc_energy([columns[0], columns[1]])
        if ion_energy < 1.0:
          continue
        dedx_elec = float(columns[2])
        dedx_nucl = float(columns[3])
        pro_range = calc_range([columns[4], columns[5]])
        pro_range = calc_range([columns[4], columns[5]])
        long_strg = calc_range([columns[6], columns[7]])
        late_strg = calc_range([columns[8], columns[9]])
        tota_strg = long_strg
        # tota_strg = math.sqrt(pow(long_strg, 2) + pow(late_strg, 2))
        g1.SetPoint(ipoint, ion_energy, dedx_elec)
        g2.SetPoint(ipoint, ion_energy, dedx_nucl)
        g3.SetPoint(ipoint, ion_energy, pro_range)
        g3.SetPointError(ipoint, 0, tota_strg)
        g4.SetPoint(ipoint, ion_energy, long_strg)
        g5.SetPoint(ipoint, ion_energy, late_strg)
        g6.SetPoint(ipoint, ion_energy, tota_strg)
        re_range = re.RangeFromKE(alpha_mass, ion_energy, 2, 3.5443)
        re_strg = re.RangeStragglingFromKE(alpha_mass, ion_energy, 2, 3.5443)
        g7.SetPoint(ipoint, ion_energy, re_range)
        g7.SetPointError(ipoint, ion_energy, re_strg)
        g8.SetPoint(ipoint, ion_energy, re_strg/tota_strg)
        print(ion_energy, pro_range, tota_strg)
        ipoint = ipoint + 1
      else:
        print(line)
  f1 = ROOT.TF1('f1', 'pol5')
  g1.SetMinimum(0.)
  # g1.Draw('AL')
  g2.SetMarkerColor(ROOT.kRed)
  # g2.Draw('P')
  g3.SetLineWidth(0)
  g3.SetFillColor(ROOT.kOrange+1)
  # g4.Draw('AL')
  # g5.SetLineColor(ROOT.kRed)
  # g5.Draw('L')
  # g6.Draw('AP')
  g3.Clone().Fit('f1', '', '', 1, 20)
  alpha_range = f1.Eval(alpha_energy)
  g6.Clone().Fit('f1', '', '', 1, 20)
  alpha_straggling = f1.Eval(alpha_energy)
  g7.SetFillColor(ROOT.kBlue+1)
  g3.GetXaxis().SetTitle('Energy [MeV]')
  g3.GetYaxis().SetTitle('Range [#mum]')
  g3.Draw('A3')
  g7.Draw('3')
  c1.SetLogx()
  c1.SetLogy()
  # l1 = ROOT.TLine()
  # l1.SetLineStyle(2)
  # l1.DrawLine(alpha_energy, 0, alpha_energy, alpha_range)
  # l1.DrawLine(0, alpha_range, alpha_energy, alpha_range)
  tex = ROOT.TLatex()
  tex.SetNDC()
  tex.SetTextFont(132)
  tex.SetTextSize(0.032)
  tex.DrawLatex(0.20, 0.85, '{}'.format(os.path.basename(input_file)))
  tex.DrawLatex(0.22, 0.80, 'E_{} = {:.3f} MeV'.format('{#alpha}', alpha_energy))
  tex.DrawLatex(0.22, 0.75, 'R_{} = {:.3f} #pm {:.3f} #mum ({})'
                .format('{#alpha}', alpha_range, alpha_straggling,
                        '#color['+str(ROOT.kOrange+1)+']{SRIM}'))
  tex.DrawLatex(0.22, 0.70, 'R_{} = {:.3f} #pm {:.3f} #mum ({})'
                .format('{#alpha}',
                        re.RangeFromKE(alpha_mass, alpha_energy, 2, 3.5443),
                        re.RangeStragglingFromKE(alpha_mass, alpha_energy, 2, 3.5443),
                        '#color['+str(ROOT.kBlue+1)+']{RangeEnergy}'))
  tex.SetTextSize(0.035)
  tex.DrawLatex(0.78, 0.02, 'Energy [MeV]')
  tex.SetTextAngle(90)
  tex.DrawLatex(0.076, 0.8, 'Range [#mum]')
  c1.Modified()
  c1.Update()
  c1.Print(os.path.join(output_dir, 'srim.pdf('))
  c1.Clear()
  c1.SetLogy(0)
  g8.Draw('AL')
  tex.DrawLatex(0.076, 0.45, 'Straggling ratio (RangeEnergy/SRIM)')
  tex.SetTextAngle(0)
  tex.DrawLatex(0.78, 0.02, 'Energy [MeV]')
  c1.Print(os.path.join(output_dir, 'srim.pdf)'))

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('input_file',
                      help='default SRIM output file.')
  parser.add_argument('output_dir', nargs='?',
                      default='output/SRIM',
                      help='default canvas output directory.')
  parsed, unpased = parser.parse_known_args()
  try:
    show(parsed.input_file, parsed.output_dir)
  except:
    print(sys.exc_info())
