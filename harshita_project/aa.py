import pickle as pkl
import pandas as pd
with open("apply2_dict.pkl", "rb") as f:
    object = pkl.load(f)
    
df = pd.DataFrame(object)
df.to_csv(r'bccc.csv')