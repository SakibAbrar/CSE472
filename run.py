import numpy as np
import pandas as pd
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()

HEADERS = [
    "customerID", "gender", "SeniorCitizen", "Partner",
    "Dependents", "tenure", "PhoneService", "MultipleLines",
    "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
    "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
    "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges", "Churn"
]

raw_df = pd.read_csv(
    "./dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv", sep=',')


trying = min_max_scaler.fit_transform(raw_df[["tenure"]])


print(pd.unique(raw_df['gender']))
