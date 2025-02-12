import pandas as pd
from eye_tracking_analysis.preprocessing import clean_eye_tracking_data

def test_clean_eye_tracking_data():
    df = pd.DataFrame({'x': [1, np.nan, 3], 'y': [4, 5, np.nan]})
    cleaned_df = clean_eye_tracking_data(df)
    assert cleaned_df.isnull().sum().sum() == 0
