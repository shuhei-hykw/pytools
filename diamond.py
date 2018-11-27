#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import numpy
import os
import sys
import uncertainties

#_______________________________________________________________________________
measurements = { # [mm]
  'thickness': [30.45, 30.35, 30.35,
                30.45, 30.65, 30.60,
                30.45, 30.35, 30.35,
                30.45, 30.40, 30.35,
                30.45, 30.40, 30.45,
                30.45, 30.40, 30.35],
  'width': [50.50, 50.55, 50.50,
            50.70, 50.65, 50.65,
            50.65, 50.60, 50.60,
            51.00, 50.90, 51.00,
            50.50, 50.55, 50.55,
            50.45, 50.45, 50.45],
  'height': [30.35, 30.35, 30.35,
             30.40, 30.35, 30.35,
             30.35, 30.30, 30.30,
             30.25, 30.30, 30.35,
             30.30, 30.25, 30.25,
             30.25, 30.20, 30.20],
  'weight': [151.40]
}

#_______________________________________________________________________________
def show():
  values = {}
  for key in measurements:
    a = numpy.array(measurements[key])
    v = uncertainties.ufloat(a.mean(), a.std(ddof=(1 if len(a) > 1 else 0)))
    print('{:10} : {:10.5f} +/- {:.5f}  {}'
          .format(key, v.n, v.s, '[g]' if key == 'weight' else '[mm]'))
    values[key] = v
  volume = values['thickness'] * values['width'] * values['height']
  volume *= 1e-3
  print('{:10} : {:10.5f} +/- {:.5f}  [cm3]'.format('volume', volume.n, volume.s))
  density = values['weight'] / volume
  print('{:10} : {:10.5f} +/- {:.5f}  [g/cm3]'.format('density', density.n, density.s))
  density *= 1e-1*values['thickness']
  print('{:10}   {:10.5f} +/- {:.5f}  [g/cm2]'.format('', density.n, density.s))

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parsed, unpased = parser.parse_known_args()
  try:
    show()
  except:
    print(sys.exc_info())
