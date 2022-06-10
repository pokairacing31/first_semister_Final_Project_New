from sqlite3 import Row
import pandas as pd

output_file_list=[['Final_Project\clothes_shop_zz.csv']]
for obj in output_file_list:
        df = pd.read_csv(obj[0],sep=',')
        new_df = df.dropna()
        print(new_df)
        new_df.to_csv(obj[0],index=None,index_label=None)
