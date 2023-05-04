import torch
from torch.utils.data import Dataset
import pandas as pd


class CustomData(Dataset):
    def __init__(self, csv_file):
        self.filepath = csv_file
        self.data = []
        self.res = []
        self.loadData()


    def __getitem__(self, index):
        return self.data[index], self.res[index]
    
    def __len__(self):
        return len(self.data)

    def loadData(self):
        df = pd.read_csv(self.filepath)
        del df[df.columns[0]]
        for index, row in df.iterrows():
            if index == 2000:
                break
            s = [row["Hour"], row["Temp"], row["Humidity"], 
                    row["Wind_speed"], row["Visibility"], row["Solar_Radiation"], row["Rainfall"], row["Snowfall"], row["Dew_Point"]]
            s = torch.Tensor(s)
            if row["demand"] == 0:
                r = torch.Tensor([1, 0, 0])
            elif row["demand"] == 1:
                r = torch.Tensor([0, 1, 0])
            else:
                r = torch.Tensor([0, 0, 1])
            self.data.append(s)
            self.res.append(r)
        print(len(self.data))
        



if __name__ == "__main__":
    d = CustomData("./data/winterdata.csv")      