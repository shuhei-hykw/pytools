#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from settings import wmtx, hmtx
import draw_basic as db

#_______________________________________________________________________________
def draw():
  xstart = 20
  ystart = 200
  ypitch = 24
  l = 20
  nseg = [24, 64, 16, 16]
  for i, name in enumerate(['TOF', 'SCH', 'FBH-U', 'FBH-D']):
    db.draw_text([xstart, ystart-i*ypitch], name)
    db.draw_text([xstart+0.25*l, ystart-i*ypitch-10], nseg[i])
    db.draw_arrow([xstart-0.5*l, ystart-5-i*ypitch], (4.5 if i <= 1 else 1.5 if i == 2 else 1.25)*l,
                  0, 3)
    db.draw_arrow([xstart-2, ystart-7-i*ypitch], 4, 4, 3)
    if i < 3:
      db.draw_circle([xstart+4*l-0.25*(3.5-i)*l,
                   ystart-5-13/6*ypitch if i == 2 else ystart-5-i*ypitch], 1, 0)
      db.draw_text_box([xstart+4*l, ystart-5-i*ypitch-hmtx*(2/3 if i == 0 else 2/4)],
                    'Matrix 2D' if i == 0 else 'Matrix 3D' if i == 1 else 'TDC')
  # db.draw_elip([xstart+8*l, ystart-4-2*ypitch], 18, 0.5)
  # db.draw_text([xstart+8*l, ystart-5-2*ypitch], 'network')
  db.draw_arrow([xstart+0.75*l, ystart-5-3*ypitch], 0, 2/3*ypitch, 3)
  db.draw_arrow([xstart+0.75*l, ystart-5-7/3*ypitch], 0.25*l, 0, 3)
  db.draw_logic_and([xstart+1.*l, ystart-5-(9/4+1/6)*ypitch], ypitch/2)
  db.draw_arrow([xstart+1.*l+0.375*ypitch, ystart-5-(7/3-1/6)*ypitch], 3*l-0.375*ypitch, 0, 3)
  db.draw_text([xstart+2*l+0.175*ypitch, ystart-3-(7/3-1/6)*ypitch], 'Clustering', False, 4)
  db.draw_text([xstart+3.25*l, ystart-7-(7/3-1/6)*ypitch-3], '31')
  db.draw_arrow([xstart+3*l, ystart-7-(7/3-1/6)*ypitch], 4, 4, 3)
  for i in range(4):
    db.draw_square([xstart+2*l+0.175*ypitch-8+(i%2)*2, ystart-15-(7/3-1/6)*ypitch-i*5], 2, 7.5)
    db.draw_square([xstart+2*l+0.175*ypitch+5, ystart-15-(7/3-1/6)*ypitch-i*5], 2, 7.5, 0.1, -1)
  db.draw_arrow([xstart+2*l+0.175*ypitch-2, ystart-15-(7/3-1/6)*ypitch-3.75], 5, 0, 2)
  db.draw_arrow([xstart+(4-0.25*3.5)*l, ystart-5], 0, -13/6*ypitch+1/2*hmtx, 3)
  db.draw_arrow([xstart+(4-0.25*3.5)*l, ystart-5-ypitch+1/4*hmtx], 0.25*3.5*l, 0, 3)
  db.draw_arrow([xstart+(4-0.25*3.5)*l, ystart-5-13/6*ypitch+1/2*hmtx], 0.25*3.5*l, 0, 3)
  db.draw_arrow([xstart+4*l+wmtx, ystart-5-1/6*hmtx], 1*l, 0, 3)

  db.draw_arrow([xstart+(4-0.25*2.5)*l, ystart-5-ypitch], 0, ypitch-1/3*hmtx, 3)
  db.draw_arrow([xstart+(4-0.25*2.5)*l, ystart-5-ypitch], 0, -7/6*ypitch+1/4*hmtx, 3)
  db.draw_arrow([xstart+(4-0.25*2.5)*l, ystart-5-1/3*hmtx], 0.25*2.5*l, 0, 3)
  db.draw_arrow([xstart+(4-0.25*2.5)*l, ystart-5-13/6*ypitch+1/4*hmtx], 0.25*2.5*l, 0, 3)
  db.draw_arrow([xstart+4*l+wmtx, ystart-5-ypitch], 0.5*l, 0, 3)
  db.draw_arrow([xstart+4.5*l+wmtx, ystart-5-ypitch], 0, 2/3*ypitch-1/6*hmtx, 3)
  db.draw_arrow([xstart+4.5*l+wmtx, ystart-5-1/3*ypitch-1/6*hmtx], 0.5*l, 0, 3)
  db.draw_circle([xstart+5*l+wmtx-1, ystart-5-1/3*ypitch-1/6*hmtx], 1) #
  db.draw_logic_and([xstart+5*l+wmtx, ystart-5-5/12*ypitch-1/6*hmtx], ypitch/2)
  db.draw_arrow([xstart+5*l+wmtx+0.375*ypitch, ystart-5-1/6*ypitch-1/6*hmtx], 1.5*l, 0, 2)
  db.draw_text([xstart+5.75*l+wmtx+0.375*ypitch, ystart-2-1/6*ypitch-1/6*hmtx], 'Accept', False, 5)

  db.draw_arrow([xstart+(4-0.25*1.5)*l, ystart-5-13/6*ypitch], 0, 7/6*ypitch-1/4*hmtx, 3)
  db.draw_arrow([xstart+(4-0.25*1.5)*l, ystart-5-ypitch-1/4*hmtx], 0.25*1.5*l, 0, 3)
    # db.draw_arrow([xstart+0.5*l, ystart-5-i*ypitch], l, 0, 2)
    # db.draw_text_box([xstart+0.5*l+wdaq, ystart-5-i*ypitch-hdaq/2], 'width')
