import pandas as pd


def missingness_table(data: pd.DataFrame) -> pd.DataFrame:
    """Return missing counts and percentages for all variables."""
    return pd.DataFrame({
        "missing_count": data.isna().sum(),
        "missing_percentage": data.isna().mean() * 100,
    }).sort_values("missing_percentage", ascending=False)


def categorical_frequencies(data: pd.DataFrame, columns) -> dict:
    """Return frequency/percentage tables for categorical variables."""
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


def quality_checks(data: pd.DataFrame) -> dict:
    """Run the main Phase 1 data-quality checks."""
    bmi_outside_range = data.loc[
        (data["BMXBMI"] < 10) | (data["BMXBMI"] > 80),
        ["SEQN", "RIDAGEYR", "BMXBMI"],
    ]

    nonpositive_body = data.loc[
        (data["BMXWT"] <= 0) | (data["BMXHT"] <= 0),
        ["SEQN", "BMXWT", "BMXHT"],
    ]

    calculated_bmi = data["BMXWT"] / (data["BMXHT"] / 100) ** 2
    bmi_difference = calculated_bmi - data["BMXBMI"]

    return {
        "missingness": missingness_table(data),
        "ridstatr_counts": data["RIDSTATR"].value_counts(dropna=False),
        "age_below_zero": data.loc[
            data["RIDAGEYR"] < 0, ["SEQN", "RIDAGEYR"]
        ],
        "age_below_one": data.loc[
            data["RIDAGEYR"] < 1, ["SEQN", "RIDAGEYR"]
        ],
        "bmi_outside_10_80": bmi_outside_range,
        "nonpositive_body_measurements": nonpositive_body,
        "bmi_difference_summary": bmi_difference.describe(),
        "bmi_difference": bmi_difference,
    }
