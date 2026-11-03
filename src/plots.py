from pathlib import Path
import matplotlib.pyplot as plt


def _save(fig, output_dir: Path, filename: str):
    output_dir.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(output_dir / filename, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close(fig)


def plot_bmi_distribution(data, output_dir):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(data["BMXBMI"].dropna(), bins=30)
    ax.set_xlabel("BMI (kg/m²)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of BMI")
    _save(fig, output_dir, "bmi_distribution.png")


def plot_age_distribution(data, output_dir):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(data["RIDAGEYR"].dropna(), bins=30)
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Age")
    _save(fig, output_dir, "age_distribution.png")


def plot_bmi_by_sex(data, output_dir):
    fig, ax = plt.subplots(figsize=(8, 5))
    data.boxplot(column="BMXBMI", by="RIAGENDR", ax=ax)
    ax.set_xlabel("Sex (1 = Male, 2 = Female)")
    ax.set_ylabel("BMI (kg/m²)")
    ax.set_title("BMI by Sex")
    fig.suptitle("")
    _save(fig, output_dir, "bmi_by_sex.png")


def plot_bmi_by_age(data, output_dir):
    fig, ax = plt.subplots(figsize=(8, 5))
    data.boxplot(column="BMXBMI", by="AgeGroup", ax=ax)
    ax.set_xlabel("Age group")
    ax.set_ylabel("BMI (kg/m²)")
    ax.set_title("BMI by Age Group")
    fig.suptitle("")
    _save(fig, output_dir, "bmi_by_age_group.png")


def plot_bmi_by_age_and_sex(data, output_dir):
    plot_data = data.copy()
    plot_data["AgeSexGroup"] = (
        plot_data["AgeGroup"].astype(str)
        + " / "
        + plot_data["RIAGENDR"].map({1.0: "Male", 2.0: "Female"}).fillna("Unknown")
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    plot_data.boxplot(column="BMXBMI", by="AgeSexGroup", ax=ax)
    ax.set_xlabel("Age group / Sex")
    ax.set_ylabel("BMI (kg/m²)")
    ax.set_title("BMI by Age Group and Sex")
    fig.suptitle("")
    _save(fig, output_dir, "bmi_by_age_and_sex.png")


def plot_bmi_vs_age(data, output_dir):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(data["RIDAGEYR"], data["BMXBMI"], alpha=0.2)
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("BMI (kg/m²)")
    ax.set_title("BMI vs Age")
    _save(fig, output_dir, "bmi_vs_age.png")
