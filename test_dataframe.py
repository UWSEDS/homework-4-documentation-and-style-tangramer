
'''homework 4 with correct pep8 code style of homework 3
   This module has two module functions and three test functions.
   read_function() and data_frame_check() are module functions. read_function()
   takes in a file path or url and convert it into dataframe. data_frame_check()
   checks the data to see if it has the correct form.
   test_dataframe1(),test_dataframe2(),test_dataframe3() are three test functions
   to verify if the three criteria mentioned in data_frame_check() are successfully
   fulfilled.
'''
import numpy as np
import pandas as pd

# python module with 2 functions

# function to read in one csv data file and convert it into a dataframe
def read_function(url):
    '''function to read in one csv data file and convert it into a dataframe:
       the function takes in a file path or url as an argument and then turn
       the data in that address to a dataframe
    '''
    dataframe = pd.read_csv(url)
    return dataframe

# function to check if the dataframe is of the correct form. Based on three criteria:
# 1 values of the columns are of the correct type
# 2 there are no invalid inputs
# 3 there are at least one row of data
def data_frame_check(data_frame):
    '''
    function to check if the dataframe is of the correct form. Based on three criteria:
    1 values of the columns are of the correct type
    2 there are no invalid inputs
    3 there are at least one row of data
    The function takes in a dataframe as argument and returns True if all the criteria
    are matched. Otherwise the function will throw errors according to the exceptions in
    the dataframe
    '''
    if len(data_frame) >= 1:
        if not data_frame.isnull().values.any():
            for col in data_frame.columns:
                if not len(set(map(type, data_frame[col]))) == 1:
                    raise TypeError("values of the columns are not of the correct type!")
        else:
            raise ValueError("there are invalid input values")
    else:
        raise IndexError("the dataframe has less than one row!")
    return True

#2 Test cases:
#Add 3 tests to the module that:

#exception test to check for nan values.
def test_dataframe1():
    '''exception test to check for nan values.
       The function takes in a dataframe that has some columns with missing values
       or Nan values as an argument and then tries to throw a ValueError. If a
       ValueError is caught, the output is pass
    '''
    data1 = {'col1': [1, 2], 'col2': [3, np.nan]}
    df1 = pd.DataFrame(data=data1)
    try:
        data_frame_check(df1)
    except ValueError:
        pass

#exception test to Check that all columns have values of the corect type.
def test_dataframe2():
    '''exception test to Check that all columns have values of the corect type:
       The function takes in a dataframe that has some columns with incompatible
       data types like a string value in column of numbers as an argument and
       then tries to throw a TypeError. If TyprError is caught, the output is pass
    '''
    data2 = {'col1': [1, 2], 'col2': [3, "a"]}
    df2 = pd.DataFrame(data=data2)
    try:
        data_frame_check(df2)
    except TypeError:
        pass

#exception test to verify that the dataframe has at least one row.
def test_dataframe3():
    '''exception test to verify that the dataframe has at least one row:
       The function takes in a dataframe that has only columns but no data
       as an argument and then tries to throw a Index Error. If an IndexError
       is caught, the output is pass
    '''
    data3 = {'col1':[], 'col2':[]}
    df3 = pd.DataFrame(data=data3)
    try:
        data_frame_check(df3)
    except IndexError:
        pass
