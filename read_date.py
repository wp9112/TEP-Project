import pyreadr
import pandas as pd
import os
file_path=r"D:\TEP_project\TEP_FaultFree_Training.RData"
if os.path.exists(file_path):
    print("文件已找到")
    result=pyreadr.read_r(file_path)
    print("文件中键名：",result.keys())
else:
    print("文件未找到")
    print("python当前工作目录为:",os.getcwd())
df=result['fault_free_training']
#print("\n===数据前5行===")
#print(df.head())
#print("\n===数据的所有列名===")
#print(df.columns.tolist())
print(df['xmeas_9'].mean())

  
