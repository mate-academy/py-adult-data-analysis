import pandas as pd


def get_adult_statistics() -> dict:
    df = pd.read_csv("data/adult.csv")
    
    gender_counts = df["gender"].value_counts().to_dict()
    avg_age_women = float(df[df["gender"] == "Female"]["age"].mean())
    
    country_col = "native-country" if "native-country" in df.columns else df.columns[-1]
    germany_percentage = float((df[country_col] == "Germany").mean() * 100) if "Germany" in df[country_col].values else 0.0
    
    return {
        "gender_counts": gender_counts,
        "avg_age_women": avg_age_women,
        "germany_percentage": germany_percentage,
        "total_records": len(df),
        "mean_age": float(df["age"].mean()),
        "max_age": int(df["age"].max()),
        "min_age": int(df["age"].min())
    }


if __name__ == "__main__":
    print(get_adult_statistics())

