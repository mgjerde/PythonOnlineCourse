import json
import pandas as pd
import matplotlib.pyplot as plt
import os

class Family:
    '''
    This is a class made to represent each of the families imported from the json file
        
    Parameters
    ----------
        name `string`: Name of the family
        shoppinglist `list`: A list of all the purchases of the family
    '''
    def __init__(self, name: str, shoppinglist: list):
        self.__name = name
        self.__shoppinglist = shoppinglist
       
    def createfigure(self,foldername:str):
        '''
        Function that creates a graph and saves it to a file in the given folder.

        Parameters
        ----------
            foldername `string`: The folder the files should be stored in
        '''
        pricelist = pd.read_excel("data/pricelist.xlsx")
        df = pricelist[pricelist["Product"].isin(self.__shoppinglist)]
        dfsum = df["Price"].groupby(df["Shop"]).sum()
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.set_xlabel("Price",size=14)
        plots = dfsum.plot.barh(ax=ax1, color=["green" if x==dfsum.min() else "red" if x==dfsum.max() else "orange" for x in dfsum ], xlim=(dfsum.min()*0.99,dfsum.max()*1.01), align="center")
        ax1.bar_label(plots.containers[0],size=10)
        if not os.path.isdir(foldername):
            try:
                os.makedirs(foldername)
            except OSError as error:
                print(f"Could not create folder ({error})")
        fig.savefig(f"{foldername}/{self.__name}.png")

with open("data/shoppinglists.json", mode="r") as file_in:
    shoppinglists = json.load(file_in)
    for family in shoppinglists:
        fam = Family(family,shoppinglists[family])
        fam.createfigure("output")
        