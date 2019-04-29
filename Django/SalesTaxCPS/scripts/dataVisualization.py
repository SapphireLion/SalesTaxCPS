from django.http import HttpResponse
import io
import requests
import pandas as pd
import csv
import numpy as np
from numpy import zeros,ones
from pprint import pprint
import matplotlib.pyplot as plt
import csv

def setPlt():
    salestaxcps = pd.read_csv("./SalesTaxCPS/datasets/salestaxcps.csv")
    fig, ax = plt.subplots()

    # scatter the sepal_length against the sepal_width
    print(ax.scatter(salestaxcps['NetPayment'], salestaxcps['Removals']))
    # set a title and labels
    ax.set_title('SalesTaxCPS DataPlot')
    ax.set_xlabel('NetPayment')
    ax.set_ylabel('Removals')

def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

def showData(request):
    setPlt() # create the plot
    svg = pltToSvg() # convert plot to SVG
    plt.cla() # clean up plt so it can be re-used
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

