import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

fandango = pd.read_csv("fandango_scrape.csv")

print(fandango.head())
print(fandango.info())
print(fandango.describe())


plt.figure(figsize=(12,5))
