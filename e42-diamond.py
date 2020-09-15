#!/usr/bin/env python3

import argparse
import numpy
import os
import sys
import uncertainties

#______________________________________________________________________________
measurements = { # [mm]
  # x
  'width': [30.03, 30.13, 30.16, 30.14, 30.19,
            30.15, 30.12, 30.41, 30.61, 30.56,
            30.52, 30.60, 30.46, 30.65, 30.63,
            30.32, 30.58, 30.21, 30.18, 30.05],
  # y
  'height': [20.27, 20.28, 20.24, 20.29, 20.31,
             20.29, 20.26, 20.29, 20.32, 20.24,
             20.22, 20.25, 20.26, 20.25, 20.23,
             20.22, 20.11, 20.19, 20.16, 20.20],
  # z
  'thickness': [20.03, 20.06, 20.49, 20.35, 20.12,
                20.31, 20.34, 20.32, 20.30, 20.23,
                20.37, 20.24, 20.17, 19.99, 20.11,
                20.08, 20.04, 20.19, 20.09, 20.11],
  'weight': [39.973]
}

#_______________________________________________________________________________
def show():
  values = {}
  for key in measurements:
    a = numpy.array(measurements[key])
    v = uncertainties.ufloat(a.mean(), a.std(ddof=(1 if len(a) > 1 else 0)))
    print(f'{key:10} : {v.n:10.5f} +/- {v.s:.5f} ',
          f'{"[g]" if key == "weight" else "[mm]"}')
    values[key] = v
  volume = values['thickness'] * values['width'] * values['height']
  volume *= 1e-3
  print(f'{"volume":10} : {volume.n:10.5f} +/- {volume.s:.5f}  [cm3]')
  density = values['weight'] / volume
  print(f'{"density":10} : {density.n:10.5f} +/- {density.s:.5f}  [g/cm3]')
  density *= 1e-1*values['thickness']
  print(f'{"":10}   {density.n:10.5f} +/- {density.s:.5f}  [g/cm2]')

#______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parsed, unpased = parser.parse_known_args()
  try:
    show()
  except:
    print(sys.exc_info())
