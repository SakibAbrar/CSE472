
ONE_HOT_ENCODING = "OneHot"
MIN_MAX_ENCODING = "MinMax"


DS1_MISSING_VALUE_FILL_MAPPING = {
    "TotalCharges": "mean",
}

DS1_ENCODER_MAPPING = {
    "customerID": None,
    "gender": {"Male": 1, "Female": 0},
    "SeniorCitizen": None,
    "Partner": {"Yes": 1, "No": 0},
    "Dependents": {"Yes": 1, "No": 0},
    "tenure": MIN_MAX_ENCODING,
    "PhoneService": {"Yes": 1, "No": 0},
    "MultipleLines": ONE_HOT_ENCODING,
    "InternetService": ONE_HOT_ENCODING,
    "OnlineSecurity": ONE_HOT_ENCODING,
    "OnlineBackup": ONE_HOT_ENCODING,
    "DeviceProtection": ONE_HOT_ENCODING,
    "TechSupport": ONE_HOT_ENCODING,
    "StreamingTV": ONE_HOT_ENCODING,
    "StreamingMovies": ONE_HOT_ENCODING,
    "Contract": ONE_HOT_ENCODING,
    "PaperlessBilling": {"Yes": 1, "No": 0},
    "PaymentMethod": ONE_HOT_ENCODING,
    "MonthlyCharges": MIN_MAX_ENCODING,
    "TotalCharges": MIN_MAX_ENCODING,
    "Churn": {"Yes": 1, "No": -1},
}
