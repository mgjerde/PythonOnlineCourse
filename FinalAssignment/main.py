import json
from math import prod
from turtle import color
from numpy import isin
import pandas as pd
import os
import matplotlib.pyplot as plt

pricelist = pd.read_excel("data/pricelist.xlsx")

with open("data/shoppinglists.json", mode="r") as file_in:
    a = json.load(file_in)

class Family:
    def __init__(self, name, shoppinglist):
        self.name = name
        self.shoppinglist = shoppinglist
    def shoplist(self):
        return self.shoppinglist
    def __str__(self):
        return self.name
    
all = []
for family in a:
    all.append(Family(family,a[family]))

for aa in all:
    df = pricelist[pricelist["Product"].isin(aa.shoplist())]
    dfsum = df["Price"].groupby(df["Shop"]).sum()
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_xlabel("Price",size=14)
    
    # ax1.bar_label(ax1.barh)

    # ["g" if x==max_val else "b" for x in output]
    plots = dfsum.plot.barh(ax=ax1, color=["green" if x==dfsum.min() else "red" if x==dfsum.max() else "orange" for x in dfsum ],xlim=(dfsum.min()*0.99,dfsum.max()*1.01), align="center")
    ax1.bar_label(plots.containers[0],size=10)
    fig.savefig(f"output/{aa}.png")
    # print(aa.shoplist())
    


# class shoppinglist:
#     pass

# with os.scandir("data/shoppinglists") as shoppinglists:
#     for file in shoppinglists:
#         a = list()

#         with open(file,mode="r",encoding="utf-8") as file_in:
#             for product in file_in:
#                 # print(product.removeprefix("\n"))
#                 a.append(product.removesuffix("\n"))
        # print(a)
# df = pricelist[pricelist["Name"].isin(a)]
# print(df)



        