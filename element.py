#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import sys

#_______________________________________________________________________________
weight = {'H': 1.008, 'C': 12.011, 'N': 14.007, 'O': 15.999,
          #'S': 32.066,
          'Br': 79.904, 'Ag': 107.87, 'I': 126.9}

emulsion= [{'type': 'ET-07D', 'Ag/gel': 3.16, 'AgVolumeFraction': 0.45,
            'emulsion_density': 3.63,
            'density': { 'I': 0.034, 'Ag': 1.675, 'Br': 1.22, 'S': 0.0067,
                         'C': 0.31, 'O': 0.226, 'N': 0.1, 'H': 0.05 } },
           {'type': 'GIF', 'Ag/gel': 3.16, 'AgVolumeFraction': 0.43,
            'emulsion_density': 3.53,
            'density': { 'I': 0.033, 'Ag': 1.60, 'Br': 1.166, 'S': 0.0067,
                         'C': 0.326, 'O': 0.23, 'N': 0.11, 'H': 0.05 } },
           {'type': 'OPERA', 'Ag/gel': 1.52, 'AgVolumeFraction': 0.30,
            'emulsion_density': 2.85,
            'density': { 'I': 0.023, 'Ag': 1.116, 'Br': 0.081, 'S': 0.745,
                         'C': 0.4, 'O': 0.29, 'N': 0.13, 'H': 0.065 } }]

#_______________________________________________________________________________
def show():
  for e in emulsion:
    print(('=== ' + e['type'] + ' ' + '='*80)[:80])
    print('    [g/cm3]  [mol/cm3] [atomic]   [mass]')
    h = e['density']['H']
    total_mol = 0
    total_den = 0
    mol = {}
    for d in weight:
      mol[d] = e['density'][d] / weight[d]
      total_mol += mol[d]
      total_den += e['density'][d]
    for d in weight:
      print('{:3} {:9.3f} {:8.4f} {:8.4f} {:8.4f}'
            .format(d, e['density'][d], mol[d],
                    mol[d]/total_mol, e['density'][d]/total_den))
    print('{:3} {:9.4f} {:8.3f}'
          .format('', total_mol, total_den))
    print()

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parsed, unpased = parser.parse_known_args()
  try:
    show()
  except:
    print(sys.exc_info())
