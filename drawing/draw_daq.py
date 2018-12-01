#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from settings import a4size, wdaq, hdaq
import draw_basic as db

#pc = 'PC'
pc = 'server'

#_______________________________________________________________________________
def draw():
  scale = 1.0
  flag_tof = True
  x = 10
  ystart = a4size[1]-35
  l = 30
  w1 = 10*3/4
  w2 = 10*2/4
  w3 = 10*1/4
  wctrl = 45
  wdata = 30
  wtag = 15
  ypitch = 12
  ctrig = 'red'
  cbusy = 'green'
  cdata = 'orange'
  ctag = 'tag'
  cctrl = 'cyan'
  y = ystart - hdaq
  db.draw_arrow([x, y], l, 0, 2)
  db.draw_text([x+0.5*l, y+3], 'Spill gate')
  y -= ypitch
  db.draw_arrow([x, y], l, 0, 2)
  db.draw_text([x+0.5*l, y+3], 'DAQ gate')
  y -= ypitch
  db.draw_arrow([x, y], l, 0, 2, ctrig)
  db.draw_text([x+0.5*l, y+3], 'Trigger')
  x += l
  db.draw_square([x, y-0.5*ypitch], 0.75*l, 3*ypitch)
  # db.draw_text([x+0.5*l, y+1.5*ypitch], 'Master')
  # db.draw_text([x+0.5*l, y+1.*ypitch], 'Trigger')
  # db.draw_text([x+0.5*l, y+0.5*ypitch], 'Module')
  db.draw_text([x+0.375*l, y+1.5*ypitch], 'MTM')
  db.draw_arrow([x+0.75*l, y+2*ypitch], a4size[0]-80-x-0.75*l, 0, 0, ctag)
  db.draw_text([x+1.125*l, y+2*ypitch+2], 'Ethernet cable', False, 3)
  db.draw_arrow([x+1.125*l, y+2*ypitch], -2, -5, 3, 0)
  db.draw_arrow([x+1.125*l, y+2*ypitch], 2, -5, 3, 0)
  db.draw_arrow([x+0.85*l, y+2*ypitch-5], 0.275*l-2, 0, 3)
  db.draw_arrow([x+1.125*l+2, y+2*ypitch-5], 0.275*l-2, 0, 3)
  db.draw_arrow([x+0.85*l, y+2*ypitch-15], 0.55*l, 0, 3)
  db.draw_arrow([x+0.85*l, y+2*ypitch-15], 0, 10, 3)
  db.draw_arrow([x+1.4*l, y+2*ypitch-15], 0, 10, 3)
  db.draw_arrow([x+0.925*l, y+2*ypitch-8], 0.4*l, 0, 2, ctrig)
  db.draw_arrow([x+0.925*l, y+2*ypitch-10], 0.4*l, 0, 2, 'blue')
  db.draw_arrow([x+0.925*l, y+2*ypitch-12], 0.4*l, 0, 1, cbusy)
  ''' subsystem '''
  x = a4size[0] - 80
  y = ystart - 3/4*hdaq
  ''' vme01 '''
  db.draw_text_box([x, y], 'GE XVB601')
  y -= hdaq
  db.draw_text_box([x, y], 'VME RM')
  db.draw_arrow([x-w1, y+0.5*hdaq], w1, 0, 3, ctrig)
  db.draw_arrow([x-w1, y+0.5*hdaq], 0, -11/6*hdaq, 3, ctrig)
  db.draw_arrow([x-w2, y+0.25*hdaq], w2, 0, 2, cbusy)
  db.draw_arrow([x-w2, y+0.25*hdaq], 0, -23/12*hdaq, 3, cbusy)
  y -= hdaq
  db.draw_text_box([x, y], 'ADC CAEN V792')
  db.draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, ctrig)
  db.draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  y -= hdaq
  db.draw_text_box([x, y], 'TDC CAEN V775')
  db.draw_square([x+wdaq, y], 10, 4*hdaq)
  db.draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, ctrig)
  db.draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  for i in range(3): db.draw_arrow([x+wdaq, y+(i+0.5)*hdaq], w1, 0, 3, cdata)
  db.draw_arrow([x+wdaq+w1, y+0.5*hdaq], 0, 3*hdaq, 3, cdata)
  db.draw_arrow([x+wdaq, y+3.5*hdaq], w1, 0, 1, cdata)
  db.draw_arrow([x-wctrl, y+11/3*hdaq], wctrl, 0, 2, cctrl)
  db.draw_arrow([x-wdata, y+10/3*hdaq], wdata, 0, 3, cdata)
  db.draw_text([x+wdaq+25, y+2*hdaq], 'VME bus', True)
  ''' vme04 '''
  y -= 1.5*hdaq
  db.draw_text_box([x, y], 'GE XVB601')
  y -= hdaq
  db.draw_text_box([x, y], 'VME RM')
  db.draw_arrow([x-wtag, y+3/4*hdaq], wtag, 0, 2, ctag)
  db.draw_arrow([x-(4*w1 + wctrl if flag_tof else w1), y+2/4*hdaq],
             (4*w1 + wctrl if flag_tof else w1), 0, 3, ctrig)
  db.draw_arrow([x-(4*w1 + wctrl if flag_tof else w1), y+2/4*hdaq],
             0, (-4/6*hdaq if flag_tof else -5/6*hdaq), 3, ctrig)
  db.draw_arrow([x-w2, y+1/4*hdaq], w2, 0, 2, cbusy)
  db.draw_arrow([x-w2, y+1/4*hdaq], 0, -11/12*hdaq, 3, cbusy)
  y -= hdaq
  db.draw_text_box([x, y], 'NOTICE TDC64M')
  db.draw_arrow([x-(3*w1 + wctrl - 0.5*hdaq if flag_tof else w1), y+2/3*hdaq],
             (3*w1 + wctrl - 0.5*hdaq if flag_tof else w1), 0, 2, ctrig)
  if flag_tof:
    db.draw_text([x-(7*w1 + wctrl), y+3/6*hdaq-1.5], 'TOF')
    db.draw_arrow([x-(4*w1 + wctrl), y+5/6*hdaq], w1, 0, 3, ctrig)
    db.draw_arrow([x-(6*w1 + wctrl), y+3/6*hdaq], 3*w1, 0, 3)
    db.draw_logic_and([x-(3*w1 + wctrl), y+2/6*hdaq], hdaq/1.5)
  db.draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  db.draw_square([x+wdaq, y], 10, 3*hdaq)
  for i in range(2): db.draw_arrow([x+wdaq, y+(i+0.5)*hdaq], w1, 0, 3, cdata)
  db.draw_arrow([x+wdaq+w1, y+0.5*hdaq], 0, 2*hdaq, 3, cdata)
  db.draw_arrow([x-wctrl, y+8/3*hdaq], wctrl, 0, 2, cctrl)
  db.draw_arrow([x-wdata, y+7/3*hdaq], wdata, 0, 3, cdata)
  db.draw_arrow([x+wdaq, y+5/2*hdaq], w1, 0, 1, cdata)
  db.draw_text([x+wdaq+25, y+1.5*hdaq], 'VME bus', True)
  ''' vme07 '''
  y -= 1.5*hdaq
  db.draw_text_box([x, y], 'GE XVB601')
  y -= hdaq
  db.draw_text_box([x, y], 'VME RM')
  db.draw_arrow([x-wtag, y+3/4*hdaq], wtag, 0, 2, ctag)
  db.draw_arrow([x-w1, y+2/4*hdaq], w1, 0, 3, ctrig)
  db.draw_arrow([x-w1, y+2/4*hdaq], 0, -5/6*hdaq, 3, ctrig)
  db.draw_arrow([x-w2, y+1/4*hdaq], w2, 0, 2, cbusy)
  db.draw_arrow([x-w2, y+1/4*hdaq], 0, -11/12*hdaq, 3, cbusy)
  y -= hdaq
  db.draw_text_box([x, y], 'APVDAQ')
  db.draw_square([x+wdaq, y], 10, 3*hdaq)
  db.draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, ctrig)
  db.draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  for i in range(2): db.draw_arrow([x+wdaq, y+(i+0.5)*hdaq], w1, 0, 3, cdata)
  db.draw_arrow([x+wdaq+w1, y+0.5*hdaq], 0, 2*hdaq, 3, cdata)
  db.draw_arrow([x+wdaq, y+5/2*hdaq], w1, 0, 1, cdata)
  db.draw_arrow([x-wctrl, y+8/3*hdaq], wctrl, 0, 2, cctrl)
  db.draw_arrow([x-wdata, y+7/3*hdaq], wdata, 0, 3, cdata)
  db.draw_text([x+wdaq+25, y+1.5*hdaq], 'VME bus', True)
  ''' COPPER '''
  y -= 1.5*hdaq
  db.draw_text_box([x, y], 'Front-end {}'.format(pc))
  y -= hdaq
  db.draw_text_box([x, y], 'VME RM')
  db.draw_arrow([x-wtag, y+2/4*hdaq], wtag, 0, 2, ctag)
  y -= hdaq
  db.draw_text_box([x, y], 'COPPER Lite')
  db.draw_square([x+wdaq, y], 10, 2*hdaq)
  db.draw_arrow([x+wdaq+w3, y+1/4*hdaq], 0, hdaq, 3, cbusy)
  db.draw_arrow([x+wdaq, y+1/4*hdaq], w3, 0, 3, cbusy)
  db.draw_arrow([x+wdaq, y+5/4*hdaq], w3, 0, 1, cbusy)
  db.draw_arrow([x+wdaq, y+7/4*hdaq], w1, 0, 3, ctrig)
  db.draw_arrow([x+wdaq, y+6/4*hdaq], w2, 0, 3, 'blue')
  db.draw_arrow([x+wdaq, y+3/4*hdaq], w1, 0, 1, ctrig)
  db.draw_arrow([x+wdaq, y+2/4*hdaq], w2, 0, 1, 'blue')
  db.draw_arrow([x+wdaq+w1, y+3/4*hdaq], 0, hdaq, 3, ctrig)
  db.draw_arrow([x+wdaq+w2, y+2/4*hdaq], 0, hdaq, 3, 'blue')
  db.draw_arrow([x-wctrl, y+14/5*hdaq], wctrl, 0, 2, cctrl)
  db.draw_arrow([x-wdata, y+13/5*hdaq], wdata, 0, 3, cdata)
  db.draw_arrow([x-w1, y+12/5*hdaq], w1, 0, 3, cctrl)
  db.draw_arrow([x-w1, y+12/5*hdaq], 0, -26/15*hdaq, 3, cctrl)
  db.draw_arrow([x-w2, y+11/5*hdaq], w2, 0, 2, cdata)
  db.draw_arrow([x-w2, y+11/5*hdaq], 0, -28/15*hdaq, 3, cdata)
  db.draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, cctrl)
  db.draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cdata)
  db.draw_text([x+wdaq+21.7, y+1*hdaq], 'J0 bus', True)
  ''' EASIROC '''
  y -= 1.5*hdaq
  db.draw_text_box([x, y], 'Front-end {}'.format(pc))
  y -= hdaq
  db.draw_text_box([x, y], 'EASIROC')
  db.draw_arrow([x-wctrl, y+9/5*hdaq], wctrl, 0, 2, cctrl)
  db.draw_arrow([x-wdata, y+8/5*hdaq], wdata, 0, 3, cdata)
  db.draw_arrow([x-w1, y+7/5*hdaq], w1, 0, 3, cctrl)
  db.draw_arrow([x-w2, y+6/5*hdaq], w2, 0, 2, cdata)
  db.draw_arrow([x-w1, y+7/5*hdaq], 0, -9/15*hdaq, 3, cctrl)
  db.draw_arrow([x-w2, y+6/5*hdaq], 0, -9/15*hdaq, 3, cdata)
  db.draw_arrow([x-w1, y+4/5*hdaq], w1, 0, 2, cctrl)
  db.draw_arrow([x-w2, y+3/5*hdaq], w2, 0, 3, cdata)
  db.draw_arrow([x-w1, y+2/5*hdaq], w1, 0, 2, ctrig)
  db.draw_arrow([x-w2, y+1/5*hdaq], w2, 0, 3, cbusy)
  ''' EM '''
  # y -= 1.5*hdaq
  # db.draw_text_box([x, y], 'BIT3')
  # y -= hdaq
  # db.draw_text_box([x, y], 'VME RM')
  y -= 1.5*hdaq
  db.draw_text_box([x, y], 'EM control {}'.format(pc))
  db.draw_arrow([x-wctrl, y+3/4*hdaq], wctrl, 0, 2, cctrl)
  db.draw_arrow([x-wdata, y+1/2*hdaq], wdata, 0, 3, cdata)
  ''' HUL MATRIX '''
  y -= 1.5*hdaq
  db.draw_text_box([x, y], 'SBS BIT3 618')
  y -= hdaq
  db.draw_text_box([x, y], 'VME RM')
  db.draw_square([x+wdaq, y], 10, 2*hdaq)
  db.draw_arrow([x-wtag, y+3/4*hdaq], wtag, 0, 2, ctag)
  db.draw_arrow([x-w1, y+2/4*hdaq], w1, 0, 3, ctrig)
  db.draw_arrow([x-w1, y+2/4*hdaq], 0, 39/10*hdaq, 3, ctrig)
  db.draw_arrow([x-w1, y+2/4*hdaq], 0, -5/6*hdaq, 3, ctrig)
  db.draw_arrow([x-w2, y+1/4*hdaq], w2, 0, 2, cbusy)
  db.draw_arrow([x-w2, y+1/4*hdaq], 0, 79/20*hdaq, 3, cbusy)
  db.draw_arrow([x-w2, y+1/4*hdaq], 0, -11/12*hdaq, 3, cbusy)
  db.draw_arrow([x+wdaq+w1, y+0.5*hdaq], 0, hdaq, 3, cdata)
  db.draw_arrow([x+wdaq, y+1/2*hdaq], w1, 0, 3, cdata)
  db.draw_arrow([x+wdaq, y+3/2*hdaq], w1, 0, 1, cdata)
  db.draw_arrow([x-w3, y+3/2*hdaq], w3, 0, 3, cdata)
  db.draw_arrow([x-w3, y+3/2*hdaq], 0, 5/4*hdaq, 3, cdata)
  db.draw_arrow([x-w3, y+11/4*hdaq], w3, 0, 2, cdata)
  db.draw_text([x+wdaq+25, y+hdaq], 'VME bus', True)
  y -= hdaq
  db.draw_text_box([x, y], 'HUL MATRIX')
  db.draw_arrow([x-w1, y+2/3*hdaq], w1, 0, 2, ctrig)
  db.draw_arrow([x-w2, y+1/3*hdaq], w2, 0, 3, cbusy)
  ''' HUL SCALER '''
  y -= 1.5*hdaq
  db.draw_text_box([x, y], 'Front-end {}'.format(pc))
  db.draw_arrow([x-wctrl, y+4/5*hdaq], wctrl, 0, 2, cctrl)
  db.draw_arrow([x-wdata, y+3/5*hdaq], wdata, 0, 3, cdata)
  db.draw_arrow([x-w1, y+2/5*hdaq], w1, 0, 3, cctrl)
  db.draw_arrow([x-w2, y+1/5*hdaq], w2, 0, 2, cdata)
  y -= hdaq
  db.draw_text_box([x, y], 'HUL SCALER')
  db.draw_arrow([x-wtag, y+3/4*hdaq], wtag, 0, 2, ctag)
  db.draw_arrow([x-w1, y+2/4*hdaq], w1, 0, 2, cctrl)
  db.draw_arrow([x-w2, y+1/4*hdaq], w2, 0, 3, cdata)
  db.draw_arrow([x-w1, y+2/4*hdaq], 0, 18/20*hdaq, 3, cctrl)
  db.draw_arrow([x-w2, y+1/4*hdaq], 0, 19/20*hdaq, 3, cdata)
  db.draw_arrow([x-wtag, y+3/4*hdaq], 0, ystart-y-7/4*hdaq, 3, ctag)
  db.draw_arrow([x-wctrl, y+9/5*hdaq], 0, 671/30*hdaq, 3, cctrl)
  db.draw_arrow([x-wdata, y+8/5*hdaq], 0, 667/30*hdaq, 3, cdata)
  ''' EB '''
  x = 15
  y = ystart - 8*ypitch if flag_tof else ystart - 7*ypitch
  db.draw_text([x+0.5*wdaq, y+3], 'Main DAQ {}'.format(pc))
  for i, name in enumerate(['Controller', 'Event builder', 'Event distributer', 'Recorder']):
    db.draw_text_box([x, y-(i+1)*hdaq], name)
    db.draw_arrow([x+wdaq, y-(i+(1/2 if i == 0 else 1/4 if i == 1 else 1/3))*hdaq],
               (a4size[0] - 80 - x - wdaq - wctrl if i == 0 else w1), 0,
               3 if i == 0 else 1, cctrl)
    db.draw_arrow([x+wdaq, y-(i+(1/2 if i == 1 else 2/3))*hdaq],
               (0 if i == 0 else a4size[0] - 80 - x - wdaq - wdata
                if i == 1 else w2), 0, 3 if i == 0 else 1, cdata)
  db.draw_arrow([x+wdaq, y-7/4*hdaq], w2, 0, 3, cdata)
  db.draw_arrow([x+wdaq+w2, y-11/3*hdaq], 0, 23/12*hdaq, 3, cdata)
  db.draw_arrow([x+wdaq+w1, y-10/3*hdaq], 0, 34/12*hdaq, 3, cctrl)
  db.draw_text_box([x, y-7*hdaq], 'Online monitor')
  db.draw_arrow([x+wdaq, y-6.5*hdaq], w2, 0, 1, cdata)
  db.draw_arrow([x+wdaq+w2, y-11/3*hdaq], 0, -17/6*hdaq, 3, cdata)
  ''' Legend '''
  x = 15
  y = 55
  ypitch = 8
  db.draw_arrow([x, y], l, 0, 2, ctrig)
  db.draw_text([x+0.5*l, y+2], 'Trigger', False, 4)
  y -= ypitch
  db.draw_arrow([x, y], l, 0, 2, 'blue')
  db.draw_text([x+0.5*l, y+2], 'Event tag', False, 4)
  y -= ypitch
  db.draw_arrow([x, y], l, 0, 2, cbusy)
  db.draw_text([x+0.5*l, y+2], 'Busy', False, 4)
  y -= ypitch
  db.draw_arrow([x, y], l, 0, 2, cdata)
  db.draw_text([x+0.5*l, y+2], 'Data transfer', False, 4)
  y -= ypitch
  db.draw_arrow([x, y], l, 0, 2, cctrl)
  db.draw_text([x+0.5*l, y+2], 'Slow control', False, 4)
