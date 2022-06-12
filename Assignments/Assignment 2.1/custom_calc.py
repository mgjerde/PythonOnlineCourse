#!/usr/bin/env python
# coding: utf-8

# In[2]:


def addition(numbers: list):
    '''
    Takes the numbers given in the list and returns the numbers added together
    '''
    sum = 0                     # This sets the starting sum as 0
    for number in numbers:      # goes through every number in the list
        sum += number           # Adds the number in the list to the sum
    print(sum)


# In[5]:


def subtraction(numbers: list):
    '''
    Takes the first number in the list and then subtracts every subsequent number
    '''
    sum = numbers[0]            # This sets the starting sum as the first number in the list
    for number in numbers[1:]:  # goes through every number in the list past the first one
        sum -= number           # Subtracts the numbers beyond the first one from the sum
    print(sum)


# In[7]:


def multiplication(numbers: list):
    '''
    Multiplies the numbers in the given list together
    '''
    sum = numbers[0]            # This sets the starting sum as the first number in the list
    for number in numbers[1:]:  # Goes through every number in the list past the first one
        sum *= number           # Multiplies the numbers from the list beyond the first one
    print(sum)


# In[8]:


def divison(numbers: list):
    '''
    Takes the first number in the list and then divides every subsequent number from the value of the previous calculations
    '''
    sum = numbers[0]            # This sets the starting sum as the first number in the list
    for number in numbers[1:]:  # goes through every number in the list past the first one
        sum /= number           # Divides the value this number with the previous calculations
    print(sum)


# In[9]:


def power(numbers: list):
    '''
    Raises the value of the first number by the power of the next number in the list, and then 
    '''
    sum = numbers[0]            # This sets the starting sum as the first number in the list
    for number in numbers[1:]:  # goes through every number in the list past the first one
        sum **= number          # Raises the sum by the power of the number in the list
    print(sum)

