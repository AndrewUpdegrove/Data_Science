import pandas as pd
import numpy as np
import tables
import h5py
import openpyxl
import json


filepath = input("Filepath to the hdf5 file")
output = input("Name of the excel file you would like created")
js = input("Name of ouput json file")

output = output + ".xlsx"
js = js + ".json"

df = pd.read_hdf(filepath)
df.to_excel(output)


f = h5py.File(filepath, 'r')
set = f['survey_results/axis0']
ref = f['survey_results/metaref']

metadata = {}
metadata['items'] = []
for x in range(len(ref)):
    vals = f[ref[x]][()]
    if (np.size(vals) == None):
        vals = ""
    elif (not type(vals) == str):
        vals = vals.tolist()
    metadata['items'].append({
        'Columns' : set[x].astype(str),
        'Datatype' : f[ref[x]].attrs['datatype'],
        'Values' : vals
    })

with open(js, 'w') as outfile:
    json.dump(metadata, outfile, indent=4)
