import h5py
import pandas as pd
import xlrd
import tables
import numpy as np

filepath = '../DataScience/Favorite Beverage Survey.xlsx'

data = pd.read_excel(filepath, dtype=str)

data.to_hdf('beverage_survey.hdf5', key='survey_results',mode = 'a', encoding='utf-8')


#make a datset of the values for a column and make title the column attribute and make datatype the datatype attribute
#and have the metadata
f = h5py.File('beverage_survey.hdf5', mode = 'a')

f.create_dataset('survey_results/metaref',(9,),dtype=h5py.ref_dtype)
m = f.create_group('survey_results/meta')
grp = f['survey_results']

dt = h5py.string_dtype()

m.create_dataset('col1', dtype=float)
m['col1'].attrs['datatype'] = "ISO8601 Date/Time String"

col2data = np.array(["Tea", "Coffee", "Milk", "Smoothie", "Hot Chocolate", "Lemonade", "Fizzy", "Beverage", "Fresh Juice", "Others"])
m.create_dataset('col2', data = col2data.astype(dt))
m['col2'].attrs['datatype'] = "Varchar"

m.create_dataset('col3', dtype=float)
m['col3'].attrs['datatype'] = "Varchar"

col4data = np.array(["Once daily", "Twice daily", "More than twice daily", "Once weekly", "Twice weekly", "More than twice weekly", "Not that often"])
m.create_dataset('col4', data = col4data.astype(dt))
m['col4'].attrs['datatype'] = "Varchar"

col5data = np.array(["<18", "18-25", "26-35", "46-55", "56-65", ">65"])
m.create_dataset('col5', data = col5data.astype(dt))
m['col5'].attrs['datatype'] = "Varchar"

m.create_dataset('col6', dtype=float)
m['col6'].attrs['datatype'] = "Varchar"

col7data = np.array(["< $ 3.00", "$ 3.00 - 5.00", "$ 5.00 - 7.00", "$ 7.00 - 10.00", "$ 10.00 - 15.00", "> $ 15.00"])
m.create_dataset('col7', data = col4data.astype(dt))
m['col7'].attrs['datatype'] = "Varchar"

col8data = np.array(["Donuts", "Scones", "Muffins", "CakeSandwich", "Bagel", "Salad","Others", "Nothing"])
m.create_dataset('col8', data = col4data.astype(dt))
m['col8'].attrs['datatype'] = "Varchar"

m.create_dataset('col9', dtype=float)
m['col9'].attrs['datatype'] = "Varchar"

refer = [m['col1'].ref, m['col2'].ref, m['col3'].ref, m['col4'].ref, m['col5'].ref,m['col6'].ref,m['col7'].ref, m['col8'].ref, m['col9'].ref]


for x in range(len(refer)):
    grp['metaref'][x] = refer[x]
