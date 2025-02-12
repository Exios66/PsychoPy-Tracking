def extract_fixation_duration(df):
    """Compute fixation duration per region of interest."""
    return df[df['movement'] == 'fixation'].groupby("AOI")['timestamp'].count()

def extract_saccadic_amplitude(df):
    """Compute saccadic amplitudes."""
    df['saccade_amplitude'] = np.sqrt(np.diff(df['x'])**2 + np.diff(df['y'])**2)
    return df
