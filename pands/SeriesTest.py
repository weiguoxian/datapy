import numpy as np
import pandas as pd
g = np.array([30133, 28000,22286, 21500, 19530, 18595, 17000, 13400 ])
gpd = pd.Series(g, index=["shanghai", "beijing", "shenzhen", "guangzhou", "chongqing", "tianjing", "suzhou", "wuhan"])
print gpd
