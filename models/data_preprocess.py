# This file is used to convert the categorical data to numerical data, and write it back to the csv file
# Thus, It only has to be run once

import pandas as pd
from sklearn.preprocessing import LabelEncoder


if __name__ == "__main__":
    data = pd.read_csv('../data/student-por.csv')
    stander_scaler = LabelEncoder()
    data['sex'] = stander_scaler.fit_transform(data['sex'])
    data['school'] = stander_scaler.fit_transform(data['school'])
    data['address'] = stander_scaler.fit_transform(data['address'])
    data['famsize'] = stander_scaler.fit_transform(data['famsize'])
    data['Pstatus'] = stander_scaler.fit_transform(data['Pstatus'])
    data['Mjob'] = stander_scaler.fit_transform(data['Mjob'])
    data['Fjob'] = stander_scaler.fit_transform(data['Fjob'])
    data['reason'] = stander_scaler.fit_transform(data['reason'])
    data['guardian'] = stander_scaler.fit_transform(data['guardian'])
    data['schoolsup'] = stander_scaler.fit_transform(data['schoolsup'])
    data['famsup'] = stander_scaler.fit_transform(data['famsup'])
    data['paid'] = stander_scaler.fit_transform(data['paid'])
    data['activities'] = stander_scaler.fit_transform(data['activities'])
    data['nursery'] = stander_scaler.fit_transform(data['nursery'])
    data['higher'] = stander_scaler.fit_transform(data['higher'])
    data['internet'] = stander_scaler.fit_transform(data['internet'])
    data['romantic'] = stander_scaler.fit_transform(data['romantic'])

    # write it back to the csv file
    data.to_csv('../data/student-por.csv', index=False)
