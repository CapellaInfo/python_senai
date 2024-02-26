import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from pandas_profiling import ProfileReport
pd.options.display.float_format = '{:,.2f}'.format
# %matplotlib inline

base = pd.read_csv("melb_data.csv")