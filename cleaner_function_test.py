from sqlite3 import Row
import pandas as pd

output_file_list=[['shilin_indep_suite_output.csv']]
for obj in output_file_list:
        df = pd.read_csv(obj[0],sep=',')
        new_df = df.dropna()
        print(new_df)
        new_df.to_csv(obj[0],index=None,index_label=None)
