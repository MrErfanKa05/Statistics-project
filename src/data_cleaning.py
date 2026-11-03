import pandas as pd


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Apply the cleaning decisions used in Phase 1."""
    data = data.copy()

    # SAS import can represent zero as a very small floating-point value.
    data.loc[data["RIDAGEYR"] < 1, "RIDAGEYR"] = 0

    # Special codes documented in the exploratory work.
    data["DMDEDUC2"] = data["DMDEDUC2"].replace(9, pd.NA).astype("Float64")
    data["DMDMARTZ"] = data["DMDMARTZ"].replace([77, 99], pd.NA).astype("Float64")
    data["DMDYRUSR"] = data["DMDYRUSR"].replace([77, 99], pd.NA).astype("Float64")

    return data


def create_age_groups(data: pd.DataFrame) -> pd.DataFrame:
    """Create the adult age groups used for the main project question."""
    data = data.copy()
    adult = data[data["RIDAGEYR"] >= 20].copy()

    adult["AgeGroup"] = pd.cut(
        adult["RIDAGEYR"],
        bins=[19, 39, 59, 80],
        labels=["20–39", "40–59", "60+"],
        include_lowest=False,
    )
    return adult
