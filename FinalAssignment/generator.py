from math import prod
import random as rand
from tokenize import Name
from nbformat import write
import pandas as pd
import json

# class shopitem:
#     def __init__(self, name, ean, price, pricefluctuation = 10):
#         self.name = name
#         self.ean = ean
#         self.price = price
#         self.pricefluctuation = pricefluctuation

#     def somefunction():
#         pass

def pricewithfluctuation(shop,price):
    return (shop,round(( price + (price * rand.uniform(0,15)/100)),2))

def generatepricelist(filename):
    with open(filename, mode="r",encoding="utf-8") as file_in: # https://www.matvaretabellen.no/
        for item in file_in:
            name = item.removesuffix("\n")
            price = rand.randint(10,100) 
            yield {"Name": name,"Prices":[pricewithfluctuation("Kiwi",price), pricewithfluctuation("Rema", price), pricewithfluctuation("Prix", price),pricewithfluctuation("Bunnpris",price)]}

pricelist = generatepricelist("data/fooditems.txt")
df = pd.DataFrame( columns=["Product","Shop","Price"])
for product in pricelist:
    for price in product["Prices"]:
        # print({"Product": product["Name"], "Shop": price[0],"Price":price[1]})
        df = df.append({"Product": product["Name"], "Shop": price[0],"Price":price[1]}, ignore_index=True)
df.to_excel("data/pricelist.xlsx",index=False)


with open(f"data/shoppinglists.json", mode="w",encoding="utf-8") as file_out:
    shoppinglists = dict()
    for family in ["Bollestad","Matberg","Bacon","Schjøtt","Knoblauch"]:
        shoppinglists[family] = list(df.groupby(df["Product"]).mean().sample(rand.randint(1,20)).index)
    json.dump(shoppinglists,file_out,indent=4)