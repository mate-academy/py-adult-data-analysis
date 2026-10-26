import pandas as pd


def get_adult_statistics() -> dict:
    df = pd.read_csv("data/adult.csv")
    
    gender_counts = df["gender"].value_counts().to_dict()
    avg_age_women = float(df[df["gender"] == "Female"]["age"].mean())
    
    country_col = "native-country" if "native-country" in df.columns else [c for c in df.columns if "country" in c.lower()][0]
    germany_percentage = float((df[country_col] == "Germany").mean() * 100) if "Germany" in df[country_col].values else 0.0
    
    salary_col = "salary" if "salary" in df.columns else df.columns[-1]
    if df[salary_col].dtype == object:
        df[salary_col] = df[salary_col].str.strip().str.rstrip(".")
        
    age_high = df[df[salary_col] == ">50K"]["age"]
    age_low = df[df[salary_col] == "<=50K"]["age"]
    
    rich_age_mean = float(age_high.mean()) if not age_high.empty else 0.0
    rich_age_std = float(age_high.std()) if not age_high.empty else 0.0
    poor_age_mean = float(age_low.mean()) if not age_low.empty else 0.0
    poor_age_std = float(age_low.std()) if not age_low.empty else 0.0
    
    edu_col = "education" if "education" in df.columns else [c for c in df.columns if "edu" in c.lower()][0]
    bachelors_percentage = float((df[edu_col] == "Bachelors").mean() * 100) if "Bachelors" in df[edu_col].values else 0.0
    
    higher_edu = ["Bachelors", "Prof-school", "Assoc-acdm", "Assoc-voc", "Masters", "Doctorate"]
    if edu_col in df.columns and salary_col in df.columns:
        higher_edu_df = df[df[edu_col].isin(higher_edu)]
        lower_edu_df = df[~df[edu_col].isin(higher_edu)]
        
        higher_edu_rich_pct = float((higher_edu_df[salary_col] == ">50K").mean() * 100) if not higher_edu_df.empty else 0.0
        lower_edu_rich_pct = float((lower_edu_df[salary_col] == ">50K").mean() * 100) if not lower_edu_df.empty else 0.0
    else:
        higher_edu_rich_pct = 0.0
        lower_edu_rich_pct = 0.0

    hours_col = "hours-per-week" if "hours-per-week" in df.columns else [c for c in df.columns if "hour" in c.lower()][0]
    min_work_hours = int(df[hours_col].min()) if hours_col in df.columns else 0
    max_work_hours = int(df[hours_col].max()) if hours_col in df.columns else 0
    
    if hours_col in df.columns and salary_col in df.columns:
        min_workers = df[df[hours_col] == min_work_hours]
        rich_min_workers_pct = float((min_workers[salary_col] == ">50K").mean() * 100) if not min_workers.empty else 0.0
    else:
        rich_min_workers_pct = 0.0

    return {
        "gender_counts": gender_counts,
        "avg_age_women": avg_age_women,
        "germany_percentage": germany_percentage,
        "rich_age_mean": rich_age_mean,
        "rich_age_std": rich_age_std,
        "poor_age_mean": poor_age_mean,
        "poor_age_std": poor_age_std,
        "bachelors_percentage": bachelors_percentage,
        "higher_edu_rich_pct": higher_edu_rich_pct,
        "lower_edu_rich_pct": lower_edu_rich_pct,
        "min_work_hours": min_work_hours,
        "max_work_hours": max_work_hours,
        "rich_min_workers_pct": rich_min_workers_pct
    }


if __name__ == "__main__":
    print(get_adult_statistics())

