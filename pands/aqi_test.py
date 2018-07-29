# -*- coding: utf-8 -*-
import pandas as pd
aqi_chunk = pd.read_csv("d:/datapy/datapy/pands/aqi.csv", chunksize=50, encoding="utf-8", header=0)
print aqi_chunk
tot = pd.Series([])
for city in aqi_chunk:
    tot=tot.add(city['Level'].value_counts(), fill_value=0)
print tot
