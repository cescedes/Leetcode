'''Write a solution to find the ids of products that are both low fat and recyclable.
Return the result table in any order.
The result format is in the following example.'''
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products[(products['low_fats']=='Y')&(products['recyclable']=='Y')]
    return result[['product_id']]

'''
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products['low_fats'] == 'Y') &
    (products['recyclable'] == 'Y'), 
    ['product_id']]    
'''
