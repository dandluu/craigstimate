import os
import numpy as np
import pandas as pd
import sklearn
import pickle
import json
from sklearn.preprocessing import LabelEncoder


model = None



def predict_rent(reg, typ, sqfeet, bed, baths, pets, smoking, laundry, parking):
    
    global model
    if model is None:
        with open('./app/artifacts/pipeline.pickle', 'rb') as f:
            model = pickle.load(f)
        # print("model loaded")
    
    # print(reg, typ, sqfeet, bed, baths, pets, smoking, laundry, parking)
    # features = [reg, typ, sqfeet, bed, baths, pets, smoking, laundry, parking]
    # ftype =[type(i) for i in features]


    sqfeet = int(sqfeet)
    beds = int(bed)
    baths = int(baths)

    if pets == 'Yes':
        pets = 1
    else:
        pets = 0

    if smoking == 'Yes':
        smoking = 1
    else:
        smoking = 0

    x = np.array([reg, typ, sqfeet, beds, baths,
                   pets, smoking, laundry, parking])
    x1 = np.expand_dims(x, axis=0)
    x2 = pd.DataFrame(x1, columns=['region', 'type', 'sqfeet',
                                   'beds', 'baths',
                                   'pets_allowed', 'smoking_allowed',
                                   'laundry_options', 'parking_options'])

    if sqfeet < 500 or sqfeet > 3000:
        return f'{round(model.predict(x2)[0])}, but this is likely an inaccurate estimate, use a square footage within a range of 500-3000'

    return round(model.predict(x2)[0])
