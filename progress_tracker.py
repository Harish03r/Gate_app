import os
import pandas as pd

def log_result(test_name, score, details, path="data/progress.csv"):
    # ✅ Make sure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    df = pd.DataFrame([[test_name, score, details]])
    
    # ✅ If file does not exist, write with header
    if not os.path.isfile(path):
        df.to_csv(path, mode="w", header=["Test Name", "Score", "Details"], index=False)
    else:
        df.to_csv(path, mode="a", header=False, index=False)
def analyze_progress(path="data/progress.csv"):
    """Reads past test records and gives both raw history and summary stats."""
    if not os.path.isfile(path):
        return {"history": pd.DataFrame(), "summary": {}}

    df = pd.read_csv(path)

    # summary stats
    summary = {
        "Total Tests": len(df),
        "Average Score": df["Score"].mean() if not df.empty else 0,
        "Best Score": df["Score"].max() if not df.empty else 0,
    }

    return {"history": df, "summary": summary}
