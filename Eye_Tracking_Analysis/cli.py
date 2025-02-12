import argparse
from .data_loader import load_eye_tracking_data
from .preprocessing import clean_eye_tracking_data
from .fixation_saccade import calculate_velocity, classify_eye_movements
from .feature_extraction import extract_fixation_duration
from .visualization import plot_fixation_heatmap

def main():
    parser = argparse.ArgumentParser(description="Eye Tracking Analysis Pipeline")
    parser.add_argument("filepath", type=str, help="Path to eye-tracking data CSV")
    args = parser.parse_args()

    # Load and process data
    df = load_eye_tracking_data(args.filepath)
    df = clean_eye_tracking_data(df)
    df = calculate_velocity(df)
    df = classify_eye_movements(df)

    # Extract features
    fixation_data = extract_fixation_duration(df)
    print("Fixation Data:\n", fixation_data)

    # Plot results
    plot_fixation_heatmap(df)

if __name__ == "__main__":
    main()
