import pandas as pd

def load_eye_tracking_data(filepath):
    """Load eye-tracking CSV file into a DataFrame."""
    return pd.read_csv(filepath)
