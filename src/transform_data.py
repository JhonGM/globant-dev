import csv
import pandas as pd
import numpy as np


def read_files(filename):

    try:
        df = pd.read_csv(f"files\{filename}.csv")
        df = df.replace(np.nan, None)
        data = df.to_dict(orient="records")

        return data
    except:
        return "The specified file was not found"
