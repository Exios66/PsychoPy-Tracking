from .data_loader import load_eye_tracking_data
from .preprocessing import clean_eye_tracking_data
from .fixation_saccade import calculate_velocity, classify_eye_movements

def process_eye_tracking(filepath):
    """API function to load and process eye-tracking data."""
    df = load_eye_tracking_data(filepath)
    df = clean_eye_tracking_data(df)
    df = calculate_velocity(df)
    df = classify_eye_movements(df)
    return df
