import numpy as np
from scipy.signal import savgol_filter

def clean_eye_tracking_data(df):
    """Interpolate missing values and smooth coordinates."""
    df['x'] = df['x'].interpolate()
    df['y'] = df['y'].interpolate()
    df['x'] = savgol_filter(df['x'], window_length=7, polyorder=2)
    df['y'] = savgol_filter(df['y'], window_length=7, polyorder=2)
    return df
