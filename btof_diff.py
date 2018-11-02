#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys

import ROOT

#_______________________________________________________________________________
particle = [{'name': 'mu', 'pdg': 13},
            {'name': 'pi', 'pdg': 211},
            {'name': 'K', 'pdg': 321},
            {'name': 'p', 'pdg': 2212}]

#_______________________________________________________________________________
# def life(pdg_code):
#   return ROOT.TDatabasePDG.Instance().GetParticle(pdg_code).Mass()

#_______________________________________________________________________________
def mass(pdg_code):
  return ROOT.TDatabasePDG.Instance().GetParticle(pdg_code).Mass()

#_______________________________________________________________________________
def beta(p, m):
  return ROOT.TMath.Sqrt(ROOT.TMath.Sq(p/m) / (1. + ROOT.TMath.Sq(p/m)))

#_______________________________________________________________________________
def gamma(beta):
  return 1. / ROOT.TMath.Sqrt(1. - ROOT.TMath.Sq(beta))

#_______________________________________________________________________________
def tof(path, beta):
  return path / beta / ROOT.TMath.C()

#_______________________________________________________________________________
def show(flight_path, momentum):
  print('flight path = {} m'.format(flight_path))
  print('momengum    = {} GeV/c'.format(momentum))
  func = []
  btof = 0
  btof_kaon = tof(flight_path, beta(momentum, mass(321)))
  btof_pion = tof(flight_path, beta(momentum, mass(211)))
  for p in particle:
    m = mass(p['pdg'])
    b = beta(momentum, m)
    g = gamma(b)
    t = tof(flight_path, b)
    diff = t - btof_kaon
    print('{:4} ( {:7.5} GeV/c2) :  beta={:7.5f}, gamma={:9.5f} btof = {:8.5f} ns ({:8.5f} ns)'
          .format(p['name'], mass(p['pdg']), b, g, t*1e9, diff*1e9))

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  default_path = 10.334
  default_mom = 1.81
  parser.add_argument('flight_path', nargs='?',
                      type=float, default=default_path,
                      help=('flight path length between BH1 and BH2 (default={}).'
                            .format(default_path)))
  parser.add_argument('momentum', nargs='?',
                      type=float, default=default_mom,
                      help=('flight path length between BH1 and BH2 (default={}).'
                            .format(default_mom)))
  parsed, unpased = parser.parse_known_args()
  try:
    show(parsed.flight_path, parsed.momentum)
  except:
    print(sys.exc_info())
