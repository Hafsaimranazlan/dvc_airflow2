import pandas as pd
import os

data=[
    {"name":'imran','roll_no':56969},
    {'name':'hamid','roll_no':56995},
    {'name':"azlan",'roll_no':56970}
]



df=pd.DataFrame(data)

os.makedirs("data",exist_ok=True)

df.to_csv("data/data.csv")