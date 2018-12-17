#!/usr/bin/env python

import argparse

hashid = {'ibuki': '20864938633496-0'}

#_______________________________________________________________________________
def parse_hashid(hashid):
  sub = hashid & 0x7
  eve = (hashid >>  3) & 0x1fffff
  run = (hashid >> 24) & 0xfff
  mod = (hashid >> 36) & 0x7f
  ver = (hashid >> 43) & 0x1f
  who = (hashid >> 48) & 0x1
  print('hashid = {} {}'.format(hashid, bin(hashid)))
  print('who = {:8d}'.format(who))
  print('ver = {:8d}'.format(ver))
  print('mod = {:8d}'.format(mod))
  print('run = {:8d}'.format(run))
  print('eve = {:8d}'.format(eve))
  print('sub = {:8d}'.format(sub))

#_______________________________________________________________________________
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('hashid', type=int,
                      help='hashid')
  parsed, unparsed = parser.parse_known_args()
  try:
    parse_hashid(parsed.hashid)
  except:
    print(sys.exc_info())
