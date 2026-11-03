import pandas as pd


QUANTITATIVE_VARS = [
    "RIDAGEYR",
    "BMXWT",
    "BMXHT",
    "BMXBMI",
    "BMXWAIST",
    "BMXHIP",
]

CATEGORICAL_VARS = [
    "RIAGENDR",
    "RIDRETH3",
]


def quantitative_summary(data: pd.DataFrame, columns=QUANTITATIVE_VARS):
    """Return descriptive statistics for quantitative variables."""
    return data[columns].describe().T


def frequency_tables(data: pd.DataFrame, columns=CATEGORICAL_VARS):
    """Return frequency and percentage tables."""
    tables = {}
    for col in columns:
        counts = data[col].value_counts(dropna=False).sort_index()
        percentages = (
            data[col].value_counts(dropna=False, normalize=True).sort_index() * 100
        )
        tables[col] = pd.DataFrame({
            "count": counts,
            "percentage": percentages,
        })
    return tables


def bmi_by_sex(data: pd.DataFrame):
    """Descriptive BMI statistics by sex."""
    return data.groupby("RIAGENDR")["BMXBMI"].describe()


def bmi_by_age(data: pd.DataFrame):
    """Descriptive BMI statistics by adult age group."""
    return data.groupby("AgeGroup", observed=True)["BMXBMI"].describe()


def bmi_by_age_and_sex(data: pd.DataFrame):
    """Descriptive BMI statistics by age group and sex."""
    return (
        data.groupby(["AgeGroup", "RIAGENDR"], observed=True)["BMXBMI"]
        .agg(["count", "mean", "median", "std"])
    )


def weighted_bmi_mean(data: pd.DataFrame):
    """Compare unweighted and WTMEC2YR-weighted mean BMI."""
    unweighted = data["BMXBMI"].mean()
    valid = data[["BMXBMI", "WTMEC2YR"]].dropna()

    weighted = (
        (valid["BMXBMI"] * valid["WTMEC2YR"]).sum()
        / valid["WTMEC2YR"].sum()
    )
    return unweighted, weighted
