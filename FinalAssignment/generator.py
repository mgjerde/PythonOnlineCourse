import random as rand
import pandas as pd
import json

def pricewithfluctuation(shop: str,price: float):
    '''
    Function that takes the price given, adds between 0-15% to this value and returns a tuple with the shopname and the new price

    Parameters
    ----------
        shop `string`: Identifying name of the Shop
        price `int`: The base price of the product

    Returns
    -------
        `tuple`: Tuple with the name of the shop and the adjustet price
    '''
    return (shop,round(( price + (price * rand.uniform(0,15)/100)),2))

def generatepricelist(filename: str):
    '''
    Function that takes all lines in the file, gives each a price between 10 and 250 and then creates a generator with all priced products

    Parameters
    ----------
        filename `string`: Location of a file with products seperated by lineshifts
    
    Returns
    -------
        `generator`: Generator with all given products with fluctuating prices from different shops
    '''
    with open(filename, mode="r",encoding="utf-8") as file_in:
        for item in file_in:
            name = item.removesuffix("\n")
            price = rand.randint(10,250) 
            yield {"Name": name,"Prices":[pricewithfluctuation("Kiwi",price), pricewithfluctuation("Rema", price), pricewithfluctuation("Prix", price),pricewithfluctuation("Bunnpris",price)]}

def createshoppinglists(filename: str, families: list):
    '''
    Function that creates a json that contains all the familynames and 1-20 purchases

    Parameters
    ----------
        filename `string`: File to save the shoppinglists to
        families `list`: A list of families to generate a shoppinglist for
    '''
    with open(filename, mode="w",encoding="utf-8") as file_out:
        shoppinglists = dict()
        for family in families:
            shoppinglists[family] = list(df.groupby(df["Product"]).mean().sample(rand.randint(1,20)).index)
        json.dump(shoppinglists,file_out,indent=4)


pricelist = generatepricelist("data/fooditems.txt")

df = pd.DataFrame()
for product in pricelist:
    for price in product["Prices"]:
        df = df.append({"Product": product["Name"], "Shop": price[0],"Price":price[1]}, ignore_index=True)
df.to_excel("data/pricelist.xlsx",index=False)

createshoppinglists("data/shoppinglists.json",["Bollestad","Matberg","Bacon","Schjøtt","Knoblauch","Bouillabaisse"])