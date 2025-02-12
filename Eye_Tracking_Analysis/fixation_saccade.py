import numpy as np

def calculate_velocity(df):
    """Calculate gaze velocity from x, y, and timestamps."""
    df['dx'] = df['x'].diff()
    df['dy'] = df['y'].diff()
    df['dt'] = df['timestamp'].diff() / 1000  # Convert ms to seconds
    df['velocity'] = np.sqrt((df['dx']**2 + df['dy']**2) / df['dt']**2)
    return df

def classify_eye_movements(df, velocity_threshold=30):
    """Classify fixations and saccades based on velocity."""
    df['movement'] = 'fixation'
    df.loc[df['velocity'] > velocity_threshold, 'movement'] = 'saccade'
    return df
