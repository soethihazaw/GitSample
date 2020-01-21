import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()
# list the data types for each column
print(df.dtypes)