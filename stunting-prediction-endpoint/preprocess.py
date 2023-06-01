import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def check_missing_values(df):
    # Mengecek jumlah missing value pada setiap kolom
    missing_values = df.isnull().sum()
    return missing_values

def label_encoding(df):
    # Make dictionary for label encoding
    sex_encoding = {'M': 1, 'F': 0}
    asi_encoding = {'No': 0, 'Yes': 1}
    stunting_encoding = {'No': 0, 'Yes': 1}
    # Doing label encoding using map method
    df['Sex'] = df['Sex'].map(sex_encoding)
    df['ASI Eksklusif'] = df['ASI Eksklusif'].map(asi_encoding)
    df['Stunting'] = df['Stunting'].map(stunting_encoding)
    return df

def normalize_data(df):
    # Drop the first and last columns
    data = df.iloc[:, :]
    # Normalize the data using MinMaxScaler
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns)
    return normalized_df, scaler

def save_scaler(scaler, filename):
    # Save the scaler object using joblib
    joblib.dump(scaler, filename)

def load_scaler(filename):
    # Load the scaler object using joblib
    scaler = joblib.load(filename)
    return scaler

def predict_stunting(df, scaler, model):
    # Preprocess the data
    df_encoded = label_encoding(df)
    normalized_df, _ = normalize_data(df_encoded)
    # Make predictions using the TensorFlow model
    predictions = model.predict(normalized_df)
    return predictions