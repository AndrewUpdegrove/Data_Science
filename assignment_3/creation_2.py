import h5py
import pandas as pd
import xlrd
import tables
import numpy as np
import json


filepath = '../survey_data_collection/Opinion on Historical and Current State of the World (Responses).xlsx'

data = pd.read_excel(filepath, dtype = str, usecols = "A:W")
data.to_hdf('world_opinion_survey.hdf5', key='survey_results', mode = 'a', encoding='utf-8')

with open('../survey_data_collection/Metadata.json') as fi:
    data = json.load(fi)


f= h5py.File('world_opinion_survey.hdf5', mode = 'a')
f.create_dataset('survey_results/metaref', (len(data['meta']),), dtype=h5py.ref_dtype)
m = f.create_group('survey_results/meta')
grp = f['survey_results']
dt = h5py.string_dtype()



count = 0
for x in data['meta']:
    ok = 'col' + str(count)
    m.create_dataset(ok, data = np.array(x['Values']).astype(dt))
    m[ok].attrs['datatype'] = x['Datatype']
    grp['metaref'][count] = m[ok].ref
    count = count + 1
