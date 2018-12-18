#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import math
import os
import sys

import ROOT

newaxis_array = []

#_______________________________________________________________________________
def reverse_axis(h):
  h.GetYaxis().SetLabelOffset(999)
  h.GetYaxis().SetTickLength(0)
  ROOT.gPad.Update()
  newaxis = ROOT.TGaxis(ROOT.gPad.GetUxmin(),
                        ROOT.gPad.GetUymax(),
                        ROOT.gPad.GetUxmin()-0.001,
                        ROOT.gPad.GetUymin(),
                        h.GetYaxis().GetXmin(),
                        h.GetYaxis().GetXmax(),
                        510,"");
  newaxis.SetLabelFont(132);
  newaxis.SetLabelOffset(-0.03);
  newaxis.Draw()
  newaxis_array.append(newaxis)

#_______________________________________________________________________________
def show(input_file, output_dir):
  ROOT.gROOT.SetBatch()
  c1 = ROOT.TCanvas('c1', 'c1', 2000, 1600)
  ROOT.gPad.SetBottomMargin(0.2)
  garray = []
  x = 0
  prev_name = None
  name_label = []
  plot_label = []
  with open(input_file, 'r') as f:
    for line in f:
      line = line.strip()
      columns = line.split()
      if len(columns) >= 3:
        if line[0] == '#': continue
        name = columns[0]
        bxi_n = float(columns[1])
        bxi_s = float(columns[2])
        if name != prev_name:
          if len(columns) >= 4:
            name_label.append([columns[3], x, -bxi_n])
          g = ROOT.TGraphErrors()
          garray.append(g)
          x = int(x) + 1
        else:
          if name == 'Wilkinson':
            x += 0.05
        if len(columns) >= 5:
          plot_label.append([columns[4], x, -bxi_n])
        ip = g.GetN()
        g.SetPoint(ip, x, -bxi_n)
        g.SetPointError(ip, 0, bxi_s)
        prev_name = name
        print(columns)
  h = ROOT.TH2F('h', 'h',
                len(name_label), 0.5, len(name_label)+.5,
                10, -5., 1.)
  for i in range(len(name_label)+1):
    if i > 0: h.GetXaxis().SetBinLabel(i, name_label[i-1][0])
    #if i > 1: h.Fill(name_label[i-2][0], 0, 0)
  #h.GetXaxis().LabelsOption('v')
  h.GetYaxis().SetTitle('-B_{#Xi^{#minus}} [MeV]')
  h.Draw('Q')
  # reverse_axis(h)
  # b1 = ROOT.TBox(pos[0]-0.2, -7.5, pos[0]+0.8, -2)
  # b1.SetFillColor(18)
  # b1.Draw()
  for i, g in enumerate(garray):
    g.Draw('PZ' if i == 0 else 'PZ')
    g.SetMarkerStyle([21, 4, 5, 8][i])
    g.SetMarkerSize(4.)
    g.GetYaxis().SetTitle('-B_{#Xi} [MeV]')
    # g.GetXaxis().SetLimits(0.,x+1)
    # g.GetYaxis().SetRangeUser(-8,2)
  tex = ROOT.TLatex()
  tex.SetTextAlign(11)
  tex.SetTextFont(132)
  tex.SetTextSize(0.03)
  for l in plot_label:
    tex.DrawLatex(l[1]+0.06, l[2]+0.1, l[0])
    print(l)
  # a1 = ROOT.TArrow()
  # a1.SetLineWidth(1)
  #a1.DrawArrow(pos[0]-0.2, pos[1], pos[0]+0.2, pos[1], 0.002, '<|>')
  tex.SetTextAlign(21)
  pos = [0, -5.9]
  # tex.DrawLatex(pos[0], pos[1]+0.1, '#Xi^{#minus}#plus^{7,8}Li')
  tex.DrawLatex(pos[0]+1, pos[1]+0.1, '#Xi^{#minus}#plus^{12}C')
  tex.DrawLatex(pos[0]+2, pos[1]+0.1, '#Xi^{#minus}#plus^{12}C')
  tex.DrawLatex(pos[0]+3, pos[1]+0.1, '#Xi^{#minus}#plus^{14}N')
  tex.DrawLatex(pos[0]+4, pos[1]+0.1, '#Xi^{#minus}#plus^{14}N')
  tex.DrawLatex(pos[0]+4, pos[1]+0.45, 'present data')
  c1.Print(os.path.join(output_dir, 'bxi.ps'))
  c1.Print(os.path.join(output_dir, 'bxi.pdf'))

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('input_file', nargs='?',
                      default='input/graph/ListBXi.txt',
                      help='default input file.')
  parser.add_argument('output_dir', nargs='?',
                      default='output/graph',
                      help='default canvas output directory.')
  parsed, unpased = parser.parse_known_args()
  try:
    show(parsed.input_file, parsed.output_dir)
  except:
    print(sys.exc_info())
