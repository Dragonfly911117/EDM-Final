# EDM Final Project

## Introduction

This is a final project for EDM(Educational Data Mining, ~~not Electronic Dance Music~~) course.

## Data-preprocessing

The data is
from [Kaggle](https://www.kaggle.com/datasets/whenamancodes/alcohol-effects-on-study?select=Portuguese.csv).  
We use the Portuguese data in this project.  
Then we use [data_preprocess.py](models/data_preprocess.py) to handle non-numerical data

## PCA(optional)

We then follow [tutorial](https://leemeng.tw/essence-of-principal-component-analysis.html) here to do PCA and see if
there's any difference.

## Results:

1. Logistic Regression:<br>
    - Logistic Regression<br>
      ![Logistic Regression](plots/lr.png)<br>
    - Logistic Regression with PCA preprocessing<br>
      ![Logistic Regression with PCA](plots/pca_lr.png)<br>
2. k-Nearest Neighbors:<br>
    - k-Nearest Neighbors<br>
      ![k-Nearest Neighbors(train:test=8:2)](plots/knn_(8_2).png)<br>
      ![k-Nearest Neighbors(train:test=7:3)](plots/knn_(7_3).png)<br>
    - k-Nearest Neighbors with PCA preprocessing<br>
      ![k-Nearest Neighbors with PCA(train:test=8:2)](plots/pca_knn_(8_2).png)<br>
      ![k-Nearest Neighbors with PCA(train:test=7:3)](plots/pca_knn_(7_3).png)<br>
