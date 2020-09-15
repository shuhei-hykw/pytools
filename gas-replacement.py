#!/usr/bin/env python3

import ROOT

if __name__ == '__main__':
  myfont = 132
  ROOT.gStyle.SetLabelFont(myfont,"xyz");
  ROOT.gStyle.SetTitleFont(myfont,"xyz");
  ROOT.gStyle.SetPadGridX(1);
  ROOT.gStyle.SetPadGridY(1);
  f = ROOT.TF1('f', '1 - exp(-x)', 0, 5)
  c = ROOT.TCanvas()
  f.SetLineColor(ROOT.kBlue+1)
  f.SetLineWidth(4)
  f.SetTitle('')
  f.GetXaxis().SetTitle('(Q/V)t')
  f.GetYaxis().SetTitle('x')
  f.Draw()
  c.Print('gas-exp.pdf')
