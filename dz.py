import pandas as pd
import random
# В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
print(data.info())
copy_data = data.copy()

dict_res = {"robot":[0 for i in lst if i == "robot"],
            "human":[1 for i in lst if i == "human"],}

res_df = pd.DataFrame()
res_df = pd.DataFrame(dict_res) 
# res_df["whoAmI"] = lst[:10]
res = pd.merge(data,res_df,left_index=True, right_index=True)
res.loc[(res.whoAmI == "robot"),["robot"]] = 1
res.loc[(res.whoAmI == "robot"),["human"]] = 0
print(res)