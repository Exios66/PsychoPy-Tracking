import pandas as pd
from eye_tracking_analysis.feature_extraction import extract_fixation_duration

def test_extract_fixation_duration():
    df = pd.DataFrame({'AOI': ['A', 'B', 'A', 'A'], 'movement': ['fixation', 'saccade', 'fixation', 'fixation'], 'timestamp': [1, 2, 3, 4]})
    fixation_duration = extract_fixation_duration(df)
    assert fixation_duration['A'] == 3
