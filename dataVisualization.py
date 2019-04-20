import pandas as pd
import numpy as np
from numpy import zeros,ones
from pprint import pprint
import matplotlib.pyplot as plt

filename = 'salestaxcps.csv'
salestaxcps = pd.read_csv(filename)
fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(salestaxcps['NetPayment'], salestaxcps['Removals'])
# set a title and labels
ax.set_title('Sales Tax Dataset')
ax.set_xlabel('NetPayment')
ax.set_ylabel('Removals')