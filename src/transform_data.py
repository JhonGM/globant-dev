import csv
import pandas as pd
import numpy as np

def read_files(filename):

    df = pd.read_csv(f"files\{filename}.csv")
    df = df.replace(np.nan, None)
    json = df.to_dict(orient="records")

    return json