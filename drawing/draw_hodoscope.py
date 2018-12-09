#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import draw_basic as db
from settings import a4size, line_width
import settings

draw_unit = False

#_______________________________________________________________________________
def draw(scintillator, pmt, light_guide, label_position, scale_height,
         full_width, wave=None, beam=None, with_dash=False, label_abc='',
         front_draw=True):
  n = len(scintillator['widths'])
  total_width = sum(scintillator['widths']) - scintillator['overlap']*(n-1)
  has_pmt = (True if settings.target == 'BH1' or settings.target == 'BH2'
             or settings.target == 'TOF' else False)
  mizo = (pmt['width']-light_guide['width'])/2 #if has_pmt else 0
  if settings.target == 'SCH':
    a4size[0] += 55
  '''front view'''
  ycenter = (a4size[1] - pmt['height']*2 - light_guide['height']*2 - 10
             if settings.target == 'BH1' else
             a4size[1] - pmt['height']*3 - light_guide['height']*2 - 10
             if settings.target == 'BH2' else
             a4size[1]/2 - scintillator['height']/2 - 56
             if settings.target == 'FBH' else
             a4size[1]/2 - 65
             if settings.target == 'SCH' else
             a4size[1]/2 - scintillator['height']/2 - 10)
  if front_draw:
    print('%% front view')
    if len(label_abc) > 0:
      db.draw_text([(a4size[0] - total_width)/2 + beam,
                    ycenter + scintillator['height'] + light_guide['height']
                    + pmt['height'] + 10],
                    label_abc, text_size=7)
    if beam is not None:
      db.draw_text([(a4size[0] - total_width)/2 + beam - 1,
                    (ycenter + scintillator['height']/2
                     if settings.target == 'SCH' else
                     ycenter + scintillator['height']/3
                     if (settings.target == 'TOF' or
                         settings.target == 'FBH') else ycenter)],
                   'Beam', True)
      db.draw_beam_mark([(a4size[0] - total_width)/2 + beam,
                         (ycenter + scintillator['height']/2
                          if settings.target == 'SCH' else
                          ycenter + scintillator['height']/3
                          if (settings.target == 'TOF' or
                              settings.target == 'FBH') else ycenter)],
                        5, lw=0.2)
    if n%2 == 1:
      even_odd = [i*2 for i in range(int(n/2)+1 if n%2 == 1 else int(n/2))]
      even_odd += [i*2+1 for i in range(int(n/2))]
    else:
      even_odd = [i*2+1 for i in range(int(n/2)+1 if n%2 == 1 else int(n/2))]
      even_odd += [i*2 for i in range(int(n/2))]
    for i, seg in enumerate(even_odd):
      if settings.target == 'TOF':# or settings.target == 'SCH':
        if i == n/2:
          db.draw_text([a4size[0]/2, ycenter+scintillator['height']/2],
                       '...', False, 10)
        if abs(seg -n/2+0.5) < 2: continue
      x = ((a4size[0] - total_width)/2 + sum(scintillator['widths'][:seg-n])
           - seg*scintillator['overlap'])
      db.draw_square([x, ycenter], scintillator['widths'][seg],
                     scintillator['height'], line_width,
                     ((seg%2+1 if n%2 == 1 else 2-seg%2)*0.8))
      if settings.target == 'TOF' or settings.target == 'FBH':
        x += (scintillator['widths'][seg] - pmt['width'])/2
        if settings.target == 'FBH': x = a4size[0]/2+(-n/2+seg)*pmt['width']
        y = ycenter-pmt['height']-light_guide['height']
        xsci = ((a4size[0] - total_width)/2
                + sum(scintillator['widths'][:seg-n])
                - seg*scintillator['overlap'])
        if settings.target == 'FBH':
          xsci += (scintillator['widths'][seg] - scintillator['phi'])/2
        db.draw_polygon([x+mizo+light_guide['width'],
                         y+pmt['height']+light_guide['neck']],
                        [[0, -light_guide['neck']],
                         [-light_guide['width'], 0],
                         [0, light_guide['neck']],
                         [xsci-x-mizo, light_guide['height']-light_guide['neck']],
                         ([scintillator['widths'][seg]
                           if settings.target == 'TOF' else
                           scintillator['phi'], 0])], 0.3, 1.0)
        y = ycenter+scintillator['height']+light_guide['height']
        db.draw_square([x, y], pmt['width'], pmt['height'], 0.3)
        db.draw_polygon([x+mizo+light_guide['width'], y-light_guide['neck']],
                     [[0, light_guide['neck']],
                      [-light_guide['width'], 0],
                      [0, -light_guide['neck']],
                      [xsci-x-mizo, -light_guide['height']+light_guide['neck']],
                      [(scintillator['widths'][seg]
                        if settings.target == 'TOF' else scintillator['phi']), 0],
                     ], 0.3, 1.0)
        db.draw_arrow([x+mizo, y-light_guide['neck']],
                      light_guide['width'], 0, 3)
      if settings.target == 'SCH':
        x = a4size[0]/2 - 307.5*settings.scale - pmt['width']/2
        x += (seg%16)*pmt['width']
        x += int(seg/16)*170*settings.scale
        xsci = ((a4size[0] - total_width)/2
                + sum(scintillator['widths'][:seg-n])
                - seg*scintillator['overlap'])
        xsci += (scintillator['widths'][seg] - scintillator['phi'])/2
        y = ycenter+scintillator['height']+light_guide['height']
        db.draw_square([x, y], pmt['width'], pmt['height'], 0.3)
        db.draw_polygon([x+mizo+light_guide['width'], y-light_guide['neck']],
                     [[0, light_guide['neck']],
                      [-light_guide['width'], 0],
                      [0, -light_guide['neck']],
                      [xsci-x-mizo, -light_guide['height']+light_guide['neck']],
                      [(scintillator['widths'][seg]
                        if settings.target == 'TOF' else scintillator['phi']), 0],
                     ], 0.3, 1.0)
    if settings.target == 'FBH':
      db.draw_square([(a4size[0]-150*settings.scale)/2, y],
                     150*settings.scale, pmt['height'], 0.3, 0.4)
      db.draw_square([(a4size[0]-90*settings.scale)/2, y+pmt['height']],
                     90*settings.scale, pmt['height'], 0.3)
      db.draw_text([(a4size[0]-total_width)/2-36, y+4.5],
                   'Fiber fixing frame')
      db.draw_arrow([(a4size[0]-total_width)/2-17, y+3.5], 4, -2, 3)
      print('[1 1] 0 setdash')
      db.draw_square([(a4size[0]-110*settings.scale)/2,
                      ycenter+2.5*settings.scale],
                     110*settings.scale, 30*settings.scale, 0.3, -1)
      print('[] 0 setdash')
      db.draw_text([(a4size[0]+110*settings.scale)/2+5,
                    ycenter+2.5*settings.scale-4.5], 'Frame window')
      db.draw_line_with_scale([(a4size[0]-110*settings.scale)/2,
                               ycenter+2.5*settings.scale], -5,
                              30*settings.scale,
                              rotate=True)
    if settings.target == 'SCH':
      frame_width = 750*settings.scale
      frame_height = 600*settings.scale
      window_width = 710*settings.scale
      window_height = 434*settings.scale
      t = 8*settings.scale
      fc = 0.6
      db.draw_square([(a4size[0]-frame_width)/2, ycenter-8*settings.scale],
                     frame_width, t, line_width, fc)
      db.draw_square([(a4size[0]-frame_width)/2, ycenter-8*settings.scale],
                     frame_width,
                     frame_height, line_width, -1)
      db.draw_square([(a4size[0]-frame_width)/2,
                      ycenter+scintillator['height']+light_guide['height']],
                     frame_width, t, line_width, fc)
      db.draw_square([(a4size[0]-frame_width)/2,
                      ycenter+frame_height-t],
                     frame_width, -t, line_width, fc)
      board_width = 139*settings.scale
      for i in range(4):
        x = a4size[0]/2 - 255*settings.scale - board_width/2
        x += i*170*settings.scale
        db.draw_square([x,
                        ycenter+scintillator['height']
                        +light_guide['height']+t],
                       board_width,
                       5*settings.scale, line_width)
      db.draw_square([(a4size[0]-frame_width)/2, ycenter-8*settings.scale],
                     t, frame_height, line_width, fc)
      db.draw_square([(a4size[0]+frame_width)/2, ycenter-8*settings.scale],
                     -t, frame_height, line_width, fc)
      print('[1 1] 0 setdash')
      db.draw_square([(a4size[0]-window_width)/2,
                      ycenter+8*settings.scale],
                     window_width, window_height, line_width, -1)
      print('[] 0 setdash')
      db.draw_text([(a4size[0]-frame_width)/2-15,
                    ycenter-6], 'Frame window')
      db.draw_arrow([(a4size[0]-frame_width)/2+0.5,
                     ycenter-4], 6, 4+t, 3)
      db.draw_line_with_scale([(a4size[0] - total_width)/2, ycenter-t],
                              total_width, -10)
      db.draw_line_with_scale([(a4size[0] - frame_width)/2, ycenter],
                              -24, scintillator['height'], True)
      db.draw_line_with_scale([(a4size[0] - frame_width)/2,
                               ycenter+t],
                              -5, window_height, True)
      # scale = 0.4
      # db.draw_square([(a4size[0]+total_width)/2+20, ycenter],
      #                150*scale, 70*scale, 0.3, 0.4)
      # db.draw_square([(a4size[0]+total_width)/2+20+20*scale,
      #                 ycenter+20*scale],
      #                110*scale, 30*scale, 0.3, 0.8)
    for i, seg in enumerate(light_guide['segments']):
      j = i
      if settings.target == 'BH1':
        if i == len(light_guide['segments']) - 2:
          j = i + 1
        if i == len(light_guide['segments']) - 1:
          j = i - 1
      seg = light_guide['segments'][j]
      x = a4size[0]/2+(-len(light_guide['segments'])/2+j)*pmt['width']
      y = ycenter-pmt['height']-light_guide['height']
      xsci = ((a4size[0] - total_width)/2
              + sum(scintillator['widths'][:seg-n])
              - seg*scintillator['overlap'])
      db.draw_polygon([x+mizo+light_guide['width'], y+pmt['height']],
                      [[-light_guide['width'], 0],
                       [xsci-x-mizo, light_guide['height']],
                       [scintillator['widths'][seg], 0]], 0.3, 1.0)
      y = ycenter+scintillator['height']+light_guide['height']
      db.draw_square([x, y], pmt['width'], pmt['height'], 0.3)
      xsci = ((a4size[0] - total_width)/2
              + sum(scintillator['widths'][:seg-n])
              - seg*scintillator['overlap'])
      db.draw_polygon([x+mizo+light_guide['width'], y-light_guide['neck']],
                      [[0, light_guide['neck']],
                       [-light_guide['width'], 0],
                       [0, -light_guide['neck']],
                       [xsci-x-mizo, -light_guide['height']+light_guide['neck']],
                       [scintillator['widths'][seg], 0]], 0.3, 1.0)
    if settings.target != 'SCH':
      db.draw_square([(a4size[0]-total_width)/2,
                      ycenter-light_guide['height']-1],
                     total_width, light_guide['height']*0.5, 0)
      for i in range(1 if settings.target == 'BH1' or
                     settings.target == 'BH2' else 0):
        y = (ycenter - light_guide['height']
             + (2*i-1)*light_guide['neck']
             + (1-i)*(scintillator['height'] + light_guide['height']*2))
        db.draw_arrow([a4size[0]/2 + (-len(light_guide['segments'])/2)
                       * pmt['width']+mizo, y],
                      light_guide['width'], 0, 3)
        if settings.target == 'BH1':
          db.draw_arrow([a4size[0]/2 + (-len(light_guide['segments'])/2+1)
                         * pmt['width']+mizo, y],
                        pmt['width']*(len(light_guide['segments'])-2) - mizo*2,
                        0, 3)
          db.draw_arrow([a4size[0]/2 + (len(light_guide['segments'])/2-1)
                         *pmt['width']+mizo, y],
                     light_guide['width'], 0, 3)
      db.draw_line_with_scale([(a4size[0] - total_width)/2, ycenter],
                              -5, scintillator['height'], True)
    db.draw_text([a4size[0]/2 - len(light_guide['segments'])/2*pmt['width']
                  + pmt['label'][0],
                  ycenter + scintillator['height'] + light_guide['height']
                  + pmt['height'] + pmt['label'][1]],
                 pmt['name'])
    db.draw_arrow([a4size[0]/2 - len(light_guide['segments'])/2*pmt['width']
                   + pmt['label'][0]
                   + (21 if settings.target == 'SCH' else
                      21 if settings.target == 'FBH' else
                      13 if settings.target == 'TOF' else
                      19 if settings.target == 'BH1' else 14.5),
                   ycenter+scintillator['height'] + light_guide['height']
                   + pmt['height'] + pmt['label'][1]], 4, -2, 3)
    db.draw_text([a4size[0]/2 - len(light_guide['segments'])/2*pmt['width']
                  + light_guide['label'][0],
                  ycenter + light_guide['height'] + light_guide['label'][1]],
                 'Acrylic light guide' if has_pmt else
                 'Fiber Kuraray PSFY-11J')
    db.draw_arrow([a4size[0]/2 - len(light_guide['segments'])/2*pmt['width']
                   + light_guide['label'][0]
                   + (25.5 if settings.target == 'FBH' else
                      25.5 if settings.target == 'SCH' else 19),
                   ycenter + light_guide['height'] + light_guide['label'][1]],
                  16.5 if settings.target == 'SCH' else 4, -2, 3)
    db.draw_text([a4size[0]/2 - len(light_guide['segments'])/2*pmt['width']
                  + scintillator['label'][0],
                  ycenter + scintillator['height'] + scintillator['label'][1]],
                 scintillator['name'])
    db.draw_arrow([a4size[0]/2 - len(light_guide['segments'])/2*pmt['width']
                   + scintillator['label'][0]+20,
                   ycenter+scintillator['height'] + scintillator['label'][1]],
                  14 if settings.target == 'SCH' else 4,
                  -7 if settings.target == 'SCH' else -8, 3)
    if wave is not None:
      nwave = int(total_width/wave[0])
      for i in range(nwave):
        for j in range(2):
          db.draw_wave([(a4size[0]-total_width)/2+total_width/nwave*i,
                        (ycenter-light_guide['height']*0.5-wave[1]-j)],
                       total_width/nwave, wave[1]*(i%2-0.5))
    if with_dash:
      print('[1 1] 0 setdash')
      db.draw_line([(a4size[0]-total_width)/2, ycenter-light_guide['height']*0.5-2], total_width, 0, lw=0.2)
      print('[] 0 setdash')
  '''top view'''
  ycenter = (50 if settings.target == 'SCH' else
             30 if settings.target == 'FBH' else
             50 if settings.target != 'TOF' else 30)
  print('%% top view')
  if beam is not None and settings.target != 'SCH':
    db.draw_text([(a4size[0] - total_width)/2 + beam - 1,
                  ycenter + scintillator['thickness']/2], 'Beam', True)
    db.draw_arrow([(a4size[0] - total_width)/2 + beam,
                   ycenter + scintillator['thickness']/2 - 8], 0, 16, 2,
                  lw=0.4, msize=2)
  if settings.target == 'SCH':
    zoom = 10
    settings.scale *= zoom
    for i in range(n):
      scintillator['widths'][i] *= zoom
    scintillator['thickness'] *= zoom
    scintillator['overlap'] *= zoom
    scintillator['zdiff'] *= zoom
    scintillator['phi'] *= zoom
    n = 6
    total_width = 100
    db.draw_elip([a4size[0]/2-17, ycenter-3], 55, 0.3)
    db.draw_square([a4size[0]/2-42, ycenter-3+55*0.3-5], 50, 10,
                   0)
    db.draw_text([a4size[0]/2-17, ycenter-5+55*0.3],
                 'Cross-sectional view')
    print('newpath {} {} moveto'.format(a4size[0]/2-20, ycenter))
    print('{} {} {} 0 360 arc clip'.format(a4size[0]/2-20, ycenter, 48))
  for i in range(n):
    x = ((a4size[0] - total_width)/2 if i == 0 else
         x + scintillator['widths'][i - 1] - scintillator['overlap'])
    if ((settings.target == 'TOF' and (abs(i -n/2+0.5) < 2))):
    #or (settings.target == 'SCH' and (i == n/2 or i == n/2-1))):
      if i == n/2:
        db.draw_text([a4size[0]/2, ycenter], '...', False, 10)
      continue
    db.draw_square([x, ycenter + scintillator['zdiff']*(1-i%2)],
                   scintillator['widths'][i], scintillator['thickness'],
                   line_width, ((i%2+1)*0.8 if n%2 == 1 else (2-i%2)*0.8))
    if settings.target == 'FBH' or settings.target == 'SCH':
      db.draw_circle([x + scintillator['widths'][i]/2,
                      ycenter + scintillator['zdiff']*(1-i%2)
                      + scintillator['phi']/2],
                     scintillator['phi']/2)
      if ((i == 4 and settings.target == 'FBH') or
          (i == 1 and settings.target == 'SCH')):
        db.draw_line_with_scale([x+scintillator['widths'][i]/2
                                 -scintillator['phi']/2,
                                 ycenter + scintillator['zdiff']*(1-i%2)],
                                scintillator['phi'], -10)
      if i > 0:
        continue
    if settings.target == 'SCH' and i > 0:
      continue
    if settings.target == 'TOF' and i > 0:
      continue
    if settings.target == 'BH1' and i > 5:
      continue
    if i == 0:
      db.draw_line_with_scale([x, ycenter + scintillator['zdiff']*(1-i%2)],
                              -5, scintillator['thickness'], True)
    db.draw_line_with_scale([x, ycenter + scintillator['zdiff']*(1-i%2)],
                            scintillator['widths'][i],
                            ((-scale_height[0]*(i%2-0.5))
                             *scintillator['zdiff']
                             /scintillator['thickness']
                             + (i%2)*scale_height[1]
                             if abs(scintillator['zdiff'])>0 else
                             scintillator['thickness']+10))
  if n > 1 and settings.target != 'SCH':
    db.draw_line_with_scale([(a4size[0] - total_width)/2, ycenter],
                            total_width, full_width[1])
  if scintillator['overlap'] > 0:
    if settings.target == 'SCH':
      db.draw_arrow([(a4size[0] - total_width)/2
                     + scintillator['widths'][0]*3
                     - scintillator['overlap']*3,
                     ycenter + scintillator['zdiff']*(1-n%2)],
                    0, scintillator['thickness'], 3)
      db.draw_line_with_scale([(a4size[0] - total_width)/2
                               + scintillator['widths'][0]*3
                               - scintillator['overlap']*3,
                               ycenter + scintillator['zdiff']*(1-n%2)],
                              scintillator['overlap'],
                              (-scale_height[0]*(n%2-0.5)
                               * scintillator['zdiff']
                               / scintillator['thickness']
                               + n%2*scale_height[1]))
    else:
      db.draw_arrow([(a4size[0] + total_width)/2-scintillator['widths'][0],
                     ycenter+scintillator['zdiff']],
                    0, scintillator['thickness'], 3)
      db.draw_arrow([(a4size[0] + total_width)/2-scintillator['widths'][0],
                     ycenter], 0, scintillator['zdiff'], 3)
      db.draw_arrow([(a4size[0] + total_width)/2-scintillator['widths'][0]
                     + scintillator['overlap'], ycenter],
                    0, scintillator['zdiff'], 3)
      db.draw_line_with_scale([(a4size[0] + total_width)/2
                               - scintillator['widths'][0],
                               ycenter + scintillator['zdiff']*(1-n%2)],
                              scintillator['overlap'],
                              (-scale_height[0]*(n%2-0.5)
                               * scintillator['zdiff']
                               / scintillator['thickness']
                               + n%2*scale_height[1]))
  if 'up' in label_position:
    db.draw_text([a4size[0]/2, ycenter + label_position['up']], 'Upstream')
  if 'down' in label_position:
    db.draw_text([a4size[0]/2, ycenter + label_position['down']], 'Downstream')
  if draw_unit:
    db.draw_text([(a4size[0] + total_width)/2 + label_position['unit'][0],
                  ycenter + label_position['unit'][1]], '[mm]')

#_______________________________________________________________________________
def draw_bh1(scale=0.5):
  settings.set_scale(scale)
  scintillator = {}
  pmt = {}
  light_guide = {}
  label_position = {}
  scintillator['thickness'] = 5*scale
  scintillator['widths'] = [30, 20, 16, 12, 8, 8, 8, 12, 16, 20, 30]
  for i in range(len(scintillator['widths'])):
    scintillator['widths'][i] *= scale
  scintillator['name'] = 'Scintillator BC-420'
  scintillator['label'] = [-26, 4]
  scintillator['height'] = 66*scale
  scintillator['overlap'] = 1*scale
  scintillator['zdiff'] = scintillator['thickness']
  pmt['width'] = 22*scale
  pmt['height'] = 88*scale
  pmt['name'] = 'PMT H6524MOD'
  pmt['label'] = [-21, -6]
  light_guide['width'] = 20*scale
  light_guide['height'] = 90*scale
  light_guide['neck'] = 10*scale
  light_guide['segments'] = [0, 1, 3, 5, 7, 9, 10]
  light_guide['label'] = [-22, 15]
  label_position['unit'] = [5, -20]
  # label_position['up'] = -18
  # label_position['down'] = 30
  scale_height = [20, 0]
  full_width = [-1, 26]
  wave = [10, 3]
  beam = -30
  draw(scintillator, pmt, light_guide, label_position, scale_height, full_width,
       wave, beam, label_abc='(a)')

#_______________________________________________________________________________
def draw_bh2(scale=0.25):
  settings.set_scale(scale)
  scintillator = {}
  pmt = {}
  light_guide = {}
  label_position = {}
  scintillator['thickness'] = 6*scale
  scintillator['widths'] = [120*scale]
  scintillator['name'] = 'Scintillator EJ-212'
  scintillator['label'] = [-29, 4]
  scintillator['height'] = 40*scale
  scintillator['overlap'] = 0*scale
  scintillator['zdiff'] = 0*scale
  pmt['width'] = 60*scale
  pmt['height'] = 200*scale
  pmt['name'] = 'PMT H10570'
  pmt['label'] = [-16, -6]
  light_guide['width'] = 48*scale
  light_guide['height'] = 100*scale
  light_guide['neck'] = 10*scale
  light_guide['segments'] = [0]
  light_guide['label'] = [-21, 5]
  label_position['unit'] = [5, -20]
  # label_position['up'] = -12
  # label_position['down'] = 21
  scale_height = [20, 0]
  full_width = [-1, 26]
  wave = [7, 3]
  beam = -30
  draw(scintillator, pmt, light_guide, label_position, scale_height, full_width,
       wave, beam, label_abc='(b)')

#_______________________________________________________________________________
def draw_fbh(scale=1.2):
  settings.set_scale(scale)
  scintillator = {}
  pmt = {}
  light_guide = {}
  label_position = {}
  scintillator['thickness'] = 2*scale
  scintillator['widths'] = [7.5*scale for i in range(16)]
  scintillator['phi'] = 1*scale
  scintillator['name'] = 'Scintillator EJ-212'
  w = sum(scintillator['widths'])
  scintillator['label'] = [-w/2+2*scale-1, 6]
  scintillator['height'] = 35*scale
  scintillator['overlap'] = 2.5*scale
  scintillator['zdiff'] = -scintillator['thickness']
  pmt['width'] = 4*scale
  pmt['height'] = 2*scale
  pmt['name'] = 'MPPC circuit board'
  pmt['label'] = [-16*pmt['width']/2, 1+pmt['height']]
  light_guide['width'] = 1*scale
  light_guide['height'] = 20*scale
  light_guide['neck'] = 0*scale
  light_guide['segments'] = []
  light_guide['label'] = [-16*pmt['width']/2-32,
                          scintillator['height']/2 + light_guide['height']/2]
  label_position['unit'] = [5, -25]
  scale_height = [20, 0]
  full_width = [-1, 15]
  wave = [7, 3]
  beam = -45
  draw(scintillator, pmt, light_guide, label_position, scale_height, full_width, wave, beam)

#_______________________________________________________________________________
def draw_sch(scale=0.2):
  settings.set_scale(scale)
  scintillator = {}
  pmt = {}
  light_guide = {}
  label_position = {}
  scintillator['thickness'] = 2*scale
  scintillator['widths'] = [11.5*scale for i in range(64)]
  scintillator['phi'] = 1*scale
  scintillator['name'] = 'Scintillator EJ-212'
  w = sum(scintillator['widths'])
  scintillator['label'] = [-500*scale, 6]
  scintillator['height'] = 450*scale
  scintillator['overlap'] = 1.0*scale
  scintillator['zdiff'] = -scintillator['thickness']
  pmt['width'] = 7*scale
  pmt['height'] = 2*scale
  pmt['name'] = 'MPPC circuit board'
  pmt['label'] = [-240*scale, 19*scale]
  light_guide['width'] = 1*scale
  light_guide['height'] = 76*scale
  light_guide['neck'] = 0*scale
  light_guide['segments'] = []
  light_guide['label'] = [-520*scale,
                          scintillator['height']]
  label_position['unit'] = [5, -25]
  scale_height = [20, 0]
  full_width = [-1, 15]
  beam = -50
  draw(scintillator, pmt, light_guide, label_position, scale_height, full_width, beam=beam, front_draw=True)

#_______________________________________________________________________________
def draw_tof(scale=0.06):
  settings.set_scale(scale)
  scintillator = {}
  pmt = {}
  light_guide = {}
  label_position = {}
  scintillator['thickness'] = 30*scale
  scintillator['widths'] = [80*scale for i in range(24)]
  scintillator['name'] = 'Scintillator EJ-200'
  scintillator['label'] = [-1280*scale, 50*scale]
  scintillator['height'] = 1800*scale
  scintillator['overlap'] = 5*scale
  scintillator['zdiff'] = -scintillator['thickness']
  pmt['width'] = 60*scale
  pmt['height'] = 235*scale
  pmt['name'] = 'PMT H1949'
  pmt['label'] = [-1160*scale, -4*scale]
  light_guide['width'] = 55*scale
  light_guide['height'] = 160*scale
  light_guide['neck'] = 20*scale
  light_guide['segments'] = []
  light_guide['label'] = [-1260*scale, 1800*scale]
  label_position['unit'] = [15, -15]
  # label_position['up'] = -15
  # label_position['down'] = 18 + 30*scale*2
  scale_height = [20, 5]
  full_width = [-1, 18]
  wave = [10, 3]
  beam = -30
  draw(scintillator, pmt, light_guide, label_position, scale_height, full_width, wave, beam)
