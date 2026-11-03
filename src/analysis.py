import pandas as pd

from .descriptive import bmi_by_age, bmi_by_age_and_sex, weighted_bmi_mean


def adult_analysis(data: pd.DataFrame):
    """Run the descriptive analysis for the main adult research question."""
    adult = data[data["RIDAGEYR"] >= 20].copy()

    adult["AgeGroup"] = pd.cut(
        adult["RIDAGEYR"],
        bins=[19, 39, 59, 80],
        labels=["20–39", "40–59", "60+"],
    )

    return {
        "adult_data": adult,
        "bmi_by_age": bmi_by_age(adult),
        "bmi_by_age_and_sex": bmi_by_age_and_sex(adult),
        "weighted_comparison": weighted_bmi_mean(adult),
    }
