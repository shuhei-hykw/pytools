#!/usr/bin/env python3

'''
Script for making PostScript of drawing.

 e.g. $ drawing.py bh1 > bh1.ps

Supported targets are as follows.
 - BH1
 - BFT
 - BAC
 - Collimator
 - FBH
 - FBH_MPPC
 - PVAC
 - FAC
 - SCH
 - SCH_MPPC
 - MPPC_CIRCUIT
 - TOF
 - SSD
 - DIAMOND
 - EMULSION
 - CASSETTE
 - TRIGGER
 - MATRIX
 - DAQ
 - MICROSCOPE
 - PATTERN
 - TRACKFOLLOW
 - SU3
 - OCTET
 - THORIUM
 - IBUKI
 - IBUKI-TRACK8
'''

import argparse
import os
import sys

import draw_bac
import draw_basic
import draw_baryon_octet
import draw_bc34
import draw_bft
import draw_cassette
import draw_collimator
import draw_daq
import draw_diamond
import draw_emulsion
import draw_fac
import draw_hodoscope
import draw_ibuki
import draw_ibuki_track8
import draw_matrix
import draw_microscope
import draw_mppc
import draw_pattern_match
import draw_product
import draw_pvac
import draw_sdc123
import draw_ssd
import draw_su3
import draw_thorium
import draw_trackfollow
import draw_trigger
import settings

#_______________________________________________________________________________
supported = ['BH1', 'BFT', 'BAC', 'BH2', 'COLLIMATOR', 'BC34', 'FBH',
             'FBH_MPPC', 'MPPC_CIRCUIT', 'PVAC', 'FAC', 'SDC1',
             'SCH', 'SCH_MPPC', 'SDC2', 'SDC3', 'TOF',
             'SSD', 'DIAMOND', 'EMULSION', 'CASSETTE', 'MICROSCOPE',
             'TRACKFOLLOW',
             'TRIGGER', 'MATRIX', 'DAQ', 'SU3', 'OCTET', 'PRODUCT',
             'PATTERN', 'THORIUM', 'IBUKI', 'IBUKI-TRACK8']

#_______________________________________________________________________________
no_view_label = True
with_wave = False

#_______________________________________________________________________________
def draw_target():
  ''' draw target '''
  if settings.target == 'COLLIMATOR':
    draw_collimator.draw()
  elif settings.target == 'SSD':
    draw_ssd.draw()
  elif settings.target == 'DIAMOND':
    draw_diamond.draw()
  elif settings.target == 'EMULSION':
    draw_emulsion.draw()
  elif settings.target == 'CASSETTE':
    draw_cassette.draw()
  elif settings.target == 'TRACKFOLLOW':
    draw_trackfollow.draw()
  elif settings.target == 'TRIGGER':
    draw_trigger.draw()
  elif settings.target == 'MATRIX':
    draw_matrix.draw()
  elif settings.target == 'DAQ':
    draw_daq.draw()
  elif settings.target == 'BFT':
    draw_bft.draw()
  elif settings.target == 'BH1':
    draw_hodoscope.draw_bh1()
  elif settings.target == 'BH2':
    draw_hodoscope.draw_bh2()
  elif settings.target == 'BAC':
    draw_bac.draw()
  elif settings.target == 'FBH':
    draw_hodoscope.draw_fbh()
  elif settings.target == 'FBH_MPPC':
    draw_mppc.draw_fbh()
  elif settings.target == 'MPPC_CIRCUIT':
    draw_mppc.draw_circuit()
  elif settings.target == 'PVAC':
    draw_pvac.draw()
  elif settings.target == 'FAC':
    draw_fac.draw()
  elif settings.target == 'SCH':
    draw_hodoscope.draw_sch()
  elif settings.target == 'SCH_MPPC':
    draw_mppc.draw_sch()
  elif settings.target == 'TOF':
    draw_hodoscope.draw_tof()
  elif settings.target == 'BC34':
    draw_bc34.draw()
  elif settings.target == 'SDC1':
    draw_sdc123.draw_sdc1()
  elif settings.target == 'SDC2':
    draw_sdc123.draw_sdc2()
  elif settings.target == 'SDC3':
    draw_sdc123.draw_sdc3()
  elif settings.target == 'PRODUCT':
    draw_product.draw()
  elif settings.target == 'MICROSCOPE':
    draw_microscope.draw()
  elif settings.target == 'PATTERN':
    draw_pattern_match.draw()
  elif settings.target == 'IBUKI':
    draw_ibuki.draw()
  elif settings.target == 'IBUKI-TRACK8':
    draw_ibuki_track8.draw()

#_______________________________________________________________________________
def draw():
  ''' draw main function '''
  if settings.target == 'SU3':
    draw_su3.draw()
  elif settings.target == 'OCTET':
    draw_baryon_octet.draw()
  elif settings.target == 'PRODUCT':
    draw_product.draw()
  elif settings.target == 'THORIUM':
    draw_thorium.draw()
  elif not settings.target in supported:
    raise Exception('%% target name \"{}\" is not supported'.format(settings.target))
  else:
    draw_basic.initialize()
    draw_target()
    print('showpage')

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  help_out = ('drawing target name, supported as follows. '
              + str(supported).replace('[', '').replace(']', ''))
  parser.add_argument('target_name', help=help_out)
  parsed, unparsed = parser.parse_known_args()
  settings.set_target(parsed.target_name.upper())
  try:
    draw()
  except KeyboardInterrupt:
    print(sys.exc_info())
