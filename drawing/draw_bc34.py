#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import draw_basic as db
import settings

#_______________________________________________________________________________
def draw(scale=8.0, track=False):
  settings.set_scale(scale)
  wire_spacing = [3*scale, 4*scale] # anode-anode, anode-cathode
  width = wire_spacing[0]*4.5
  xcenter = settings.a4size[0]/2
  ycenter = settings.a4size[1]/2 - wire_spacing[1]
  for i in range(3):
    db.draw_arrow([xcenter-width/2, ycenter+i*wire_spacing[1]], width, 0, 3)
    if i != 0:
      for w in range(int(width/wire_spacing[0])+1):
        db.draw_circle([xcenter-width/2+w*wire_spacing[0], ycenter+(i-0.5)*wire_spacing[1]], 1,
                    1.0 if i == 1 else 0)
        db.draw_circle([xcenter-width/2+(w+0.5)*wire_spacing[0], ycenter+(i-0.5)*wire_spacing[1]], 1,
                    0 if i == 1 else 1.0)
  db.draw_text([xcenter-width/2, ycenter+1.5*wire_spacing[1]-6.5], 'Anode')
  db.draw_text([xcenter-width/2, ycenter+1.5*wire_spacing[1]-12], 'wire')
  db.draw_text([xcenter-width/2, ycenter+0.5*wire_spacing[1]-6.5], 'Potential')
  db.draw_text([xcenter-width/2, ycenter+0.5*wire_spacing[1]-12], 'wire')
  db.draw_text([xcenter-width/2+15, ycenter+2*wire_spacing[1]+1.5], 'Cathode plane')
  if track:
    db.draw_text([xcenter+wire_spacing[0]/4+20, ycenter+wire_spacing[1]*2.25], 'Charged particle')
    db.draw_arrow([xcenter-wire_spacing[0]/4, ycenter-wire_spacing[1]/4],
                  wire_spacing[0]/2, wire_spacing[1]/2+wire_spacing[1]*2, 2)
    db.draw_arrow([xcenter+wire_spacing[0]/4*0.4, ycenter+1.5*wire_spacing[1]], wire_spacing[0]/4*0.6-1, 0)
    db.draw_arrow([xcenter-wire_spacing[0]/4+1, ycenter+0.5*wire_spacing[1]], wire_spacing[0]/4*0.6-1, 0)
    db.draw_text([xcenter+wire_spacing[0]/4+1.5, ycenter+1.5*wire_spacing[1]-6.5], 'Drift')
    db.draw_text([xcenter+wire_spacing[0]/4+1.5, ycenter+1.5*wire_spacing[1]-13], 'length')
    db.draw_text([xcenter-wire_spacing[0]/4-1.5, ycenter+0.5*wire_spacing[1]+11.5], 'Drift')
    db.draw_text([xcenter-wire_spacing[0]/4-1.5, ycenter+0.5*wire_spacing[1]+5.], 'length')
  db.draw_line_with_scale([xcenter-width/2, ycenter+1.5*wire_spacing[1]], wire_spacing[0], 10)
  db.draw_line_with_scale([xcenter-width/2+wire_spacing[0]*3, ycenter+1.5*wire_spacing[1]],
                          -6, wire_spacing[1]/2, True)
  db.draw_text([xcenter+width/2, ycenter-wire_spacing[1]/4], '[mm]')
