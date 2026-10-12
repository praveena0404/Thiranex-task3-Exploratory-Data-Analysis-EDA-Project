import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

Path("outputs").mkdir(exist_ok=True)
df = pd.read_csv("dataset/diabetes_dataset.csv").drop_duplicates().dropna()
print("DATASET SHAPE:", df.shape)
print("\nSTATISTICAL SUMMARY\n", df.describe())
print("\nMISSING VALUES\n", df.isna().sum())
print("\nCORRELATION WITH TARGET\n", df.select_dtypes(include=np.number).corr()["target"].sort_values(ascending=False))

for col, title, filename in [("target", "Distribution of Disease Progression", "target_distribution.png"), ("bmi", "Distribution of BMI", "bmi_distribution.png")]:
    fig, ax = plt.subplots(figsize=(7, 5)); ax.hist(df[col], bins=20); ax.set(title=title, xlabel=col, ylabel="Frequency"); fig.tight_layout(); fig.savefig(f"outputs/{filename}", dpi=150); plt.close(fig)
for col, title, filename in [("bmi", "BMI vs Disease Progression", "bmi_vs_target.png"), ("age", "Age vs Disease Progression", "age_vs_target.png")]:
    fig, ax = plt.subplots(figsize=(7, 5)); ax.scatter(df[col], df["target"]); ax.set(title=title, xlabel=col, ylabel="Target"); fig.tight_layout(); fig.savefig(f"outputs/{filename}", dpi=150); plt.close(fig)
corr = df.select_dtypes(include=np.number).corr(); corr.to_csv("outputs/correlation_matrix.csv")
fig, ax = plt.subplots(figsize=(9, 7)); im = ax.imshow(corr, interpolation="nearest"); ax.set_title("Correlation Heatmap"); ax.set_xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right"); ax.set_yticks(range(len(corr.columns)), corr.columns)
for i in range(len(corr)):
    for j in range(len(corr)): ax.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", fontsize=7)
fig.colorbar(im, ax=ax); fig.tight_layout(); fig.savefig("outputs/correlation_heatmap.png", dpi=150); plt.close(fig)
df.describe().T.to_csv("outputs/statistical_summary.csv"); missing = df.isna().sum().to_frame("missing_values"); missing["percentage"] = (missing["missing_values"] / len(df) * 100).round(2); missing.to_csv("outputs/missing_values.csv")
print("\nEDA completed. See the outputs folder.")
