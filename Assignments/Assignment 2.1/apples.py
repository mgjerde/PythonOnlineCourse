#!/usr/bin/env python
# coding: utf-8

# In[1]:


# apples.py

'''A Module created for the illustrative purpose of apples'''


definition = '''An apple is a sweet, edible fruit produced by an apple tree (Malus domestica). Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus.'''

types = { 'alice' : ("red","large"),
         'ambrosia' : ("red/green","medium"),
         'ananasrenette' : ("yellow","small"),
         'golden delicious' : ("yellow","large") }

def find_apples_by_color(color):
    result = []
    for name,(col,sz) in types.items():
            if color in col:
                result.append(name)
    return result

def find_apples_by_size(size):
    result = []
    for name,(col,sz) in types.items():
            if size in sz:
                result.append(name)
    return result


# In[ ]:




