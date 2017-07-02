#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
net exploration
Created on Sat Jul  1 14:14:14 2017

@author: steven
"""
import os
import pandas as pd
import pandana as pdna
import time
import geojson
#%%
import urbanaccess as ua
from urbanaccess.config import settings
from urbanaccess.gtfsfeeds import feeds
from urbanaccess import gtfsfeeds
from urbanaccess.gtfs.gtfsfeeds_dataframe import gtfsfeeds_dfs
from urbanaccess.network import ua_network, load_network
#%%
if os.path.exists('data/final_net.h5'):
    urbanaccess_net = ua.network.load_network(filename='final_net.h5')
else:
    pass
#%%
temp = urbanaccess_net.net_nodes
nodes = temp[temp['net_type'] == 'transit']
#%%
nodes.to_csv(
        'pvta_nodes.csv',
        columns=[u'id', u'    ', u'stop_name', u'x', u'y']
        )
#%%
# ogr2ogr -f "GeoJSON" pvta_nodes.geojson pvta_nodes.csv -oo X_POSSIBLE_NAMES=x -oo Y_POSSIBLE_NAMES=y -oo KEEP_GEOM_COLUMNS=NO
#%%
edges = urbanaccess_net.net_edges[
        urbanaccess_net.net_edges['net_type'] == 'transit'
        ]
#%%
#[ 'from', 'edge_id', 'oneway', 'ref', u'route_type', u'sequence',
#         u'to', u'unique_route_id', u'unique_trip_id', u'weight',
#         u'from_int', u'to_int']
#%%
#_nodes = urbanaccess_net.net_nodes
#_edges = urbanaccess_net.net_edges
#%%
tmp = pd.concat([edges.join(nodes.set_index('id'), on='to', lsuffix='_l', rsuffix='_r'), edges.join(nodes.set_index('id'), on='from', lsuffix='_l', rsuffix='_r')])