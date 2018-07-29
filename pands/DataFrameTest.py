import numpy as np
import pandas as pd
gp = pd.DataFrame([[30133, 2419.76], [28000,2172.90],[22286, 1350.11],                   [21500, 1137.52], [19530, 1562.45], [18595, 3016.3],                   [17000, 1375.00], [13400, 1591.76]],                  index=["shanghai", "beijing", "shenzhen", "guangzhou", "chongqing", "tianjing", "suzhou", "wuhan"],                 columns=["GDP", "Population"])
gp.index.name="City_Name" 
gp.columns.name="Items"
print gp
