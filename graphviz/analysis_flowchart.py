#!/usr/bin/env python3

import graphviz

#______________________________________________________________________________
version = 1
#version = 2
cobo_num = 8
file_shape = 'note'
#file_shape = 'parallelogram'
analyzer_shape = 'oval'
#analyzer_shape = 'box'
raw_color = '#ff7777'
analyzer_color = '#77ffff'
root_color = '#ffff77'
hddaq_raw_label = 'HDDAQ RawData'
tpc_raw_label = 'GET RawData'
usr_label = 'k18-analyzer/usr'
hodo_label = 'Hodoscope.root'
k18_label = 'K18Tracking.root'
kurama_label = 'KuramaTracking.root'
kk_label = 'DstKKAna.root'
ll_label = 'DstLLAna.root'
dst_label = 'k18-analyzer/dst'
hit_label = 'TpcHit'
tpc_label = 'hyptpc-analyzer'

#______________________________________________________________________________
if __name__ == '__main__':
  # formats of png, pdf, and svg are supported
  graph = graphviz.Digraph(format='pdf', graph_attr={'layout': 'dot',
                                                     'rankdir': 'LR'})
  # raw
  with graph.subgraph(name='raw') as raw:
    raw.attr(rank='same')
    raw.node_attr.update(shape=file_shape, style='filled', fillcolor=raw_color)
    raw.node(hddaq_raw_label, hddaq_raw_label)
    for i in range(cobo_num):
      raw.node(f'{tpc_raw_label} {i}', f'{tpc_raw_label} {i}')
  # first decode
  with graph.subgraph(name='decode') as decode:
    decode.attr(rank='same')
    decode.node_attr.update(shape=analyzer_shape,
                            style='filled', fillcolor=analyzer_color)
    decode.node(usr_label, usr_label)
    if version == 1:
      for i in range(cobo_num):
        decode.node(f'{tpc_label} {i}', tpc_label)
    elif version == 2:
      decode.node(tpc_label, tpc_label)
  # first root
  with graph.subgraph(name='root1') as root:
    root.attr(rank='same')
    root.node_attr.update(shape=file_shape,
                          style='filled', fillcolor=root_color)
    root.node(hodo_label, hodo_label)
    root.node(k18_label, k18_label)
    root.node(kurama_label, kurama_label)
    if version == 1:
      for i in range(cobo_num):
        root.node(f'{hit_label} {i}', f'{hit_label}_{i}.root')
    elif version == 2:
      root.node(hit_label, f'{hit_label}.root')
  # k18analyzer/dst1
  with graph.subgraph(name='dst1') as dst:
    dst.attr(rank='same')
    dst.node_attr.update(shape=analyzer_shape,
                         style='filled', fillcolor=analyzer_color)
    dst.node(f'{dst_label} kk', dst_label)
    dst.node(f'{dst_label} tpc', dst_label)
  # dst.root
  with graph.subgraph(name='root2') as root:
    root.attr(rank='same')
    root.node_attr.update(shape=file_shape,
                          style='filled', fillcolor=root_color)
    root.node(kk_label, kk_label)
    root.node('TpcTracking', 'TpcTracking.root')
  # k18analyzer/dst2
  with graph.subgraph(name='dst2') as dst:
    dst.attr(rank='same')
    dst.node_attr.update(shape=analyzer_shape,
                         style='filled', fillcolor=analyzer_color)
    dst.node(f'{dst_label} ll', dst_label)
  # final.root
  with graph.subgraph(name='root3') as root:
    root.attr(rank='same')
    root.node_attr.update(shape=file_shape,
                          style='filled', fillcolor=root_color)
    root.node(ll_label, ll_label)
  # edge w/o arrowhead
  with graph.subgraph(name='edge1') as edge:
    edge.edge_attr.update(arrowhead='none')
    edge.edge(hddaq_raw_label, usr_label)
    edge.edge(hodo_label, f'{dst_label} kk')
    edge.edge(k18_label, f'{dst_label} kk')
    edge.edge(kurama_label, f'{dst_label} kk')
    for i in range(cobo_num):
      if version == 1:
        edge.edge(f'{tpc_raw_label} {i}', f'{tpc_label} {i}')
        edge.edge(f'{hit_label} {i}', f'{dst_label} tpc')
      elif version == 2:
        edge.edge(f'{tpc_raw_label} {i}', tpc_label)
        if i == 0:
          edge.edge(hit_label, f'{dst_label} tpc')
    edge.edge('TpcTracking', f'{dst_label} ll')
    edge.edge(kk_label, f'{dst_label} ll')
  graph.edge(usr_label, hodo_label)
  graph.edge(usr_label, k18_label)
  graph.edge(usr_label, kurama_label)
  graph.edge(f'{dst_label} kk', kk_label)
  # GET part
  for i in range(cobo_num):
    if version == 1:
      graph.edge(f'{tpc_label} {i}', f'{hit_label} {i}')
    elif version == 2:
      if i == 0:
        graph.edge(tpc_label, hit_label)
    # edge_label=(' k18-analyzer/dst' if i == 0 else '')
  # graph.node('TpcCluster', 'TpcCluster', fillcolor=root_color)
  graph.edge(f'{dst_label} tpc', 'TpcTracking')
  # graph.edge(f'{dst_label} tpc', 'TpcCluster')
  graph.edge(f'{dst_label} ll', ll_label)
  graph.render('flowchart', view=True)
