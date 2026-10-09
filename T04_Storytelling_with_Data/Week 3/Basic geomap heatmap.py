# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:07:25 2023

@author: jbrweelden
"""

import folium
import pandas as pd
from folium.plugins import HeatMap

df = pd.read_csv('Starbucks.csv')
## print(df)

map_1 = folium.Map(location=[41, 14], tiles='cartodbpositron', zoom_start=2)
HeatMap(data=df[['latitude', 'longitude']], radius=0).add_to(map_1)
map_1
map_1.save('Starbucks.html')