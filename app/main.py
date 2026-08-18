import pandas as pd


def get_adult_statistics() -> dict:
    df = pd.read_csv("data/adult.csv")
    return {
        "total_records": len(df),
        "mean_age": df["age"].mean()
    }

