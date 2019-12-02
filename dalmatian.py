import pandas as pd

def splitVect(data,key):
    split = []
    value = None
    for i in range(len(data)):
        if(int(data[key].iloc[i]) != value):
            if(value != None):
                emp = pd.DataFrame(data = split[-1], columns=data.columns.values)
                split[-1] = emp
            value = data[key].iloc[i]
            split.append([])
        split[-1].append(data.iloc[i])
    emp = pd.DataFrame(data = split[-1], columns=data.columns.values)
    split[-1] = emp
    return split