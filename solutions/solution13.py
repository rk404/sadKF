import pandas as pd
from statsmodels.stats.proportion import proportions_ztest, proportion_confint, proportion_effectsize
from statsmodels.stats.power import NormalIndPower

import kagglehub

# https://www.kaggle.com/datasets/stackoverflow/stack-overflow-2023-developers-survey

path = kagglehub.dataset_download("stackoverflow/stack-overflow-2023-developers-survey")

import os

for file in os.listdir(path):
    print(file)


df = pd.read_csv(f"{path}/survey_results_public.csv")
print(df.shape)
print(df.columns[:20])


# Pokaż kolumny zawierające "AI" lub "artificial"
[x for x in df.columns if "AI" in x or "artificial" in x.lower()]

print(df["AISelect"].value_counts(dropna=False))

positive = {
    "Yes, I use AI tools regularly",
    "Yes, I use AI tools sometimes"
}

ai_use = df["AISelect"].astype(str).isin(positive).astype(int)


n = len(ai_use)
count = ai_use.sum()
p_hat = count / n
p0 = 0.60
alpha = 0.05

print(f"\nLiczba obserwacji: {n}")
print(f"Liczba użytkowników AI: {count}")
print(f"Oszacowana proporcja p̂ = {p_hat:.3f}")

# --- 6. Test jednej proporcji ---
stat, p_val = proportions_ztest(count, n, value=p0, alternative='larger')
ci_low, ci_high = proportion_confint(count, n, alpha=alpha, method="wilson")
h = proportion_effectsize(p_hat, p0)

# --- 7. Moc testu ---
power = NormalIndPower().solve_power(effect_size=h, nobs1=n, alpha=alpha, alternative='larger')

# --- 8. Wyniki ---
print(f"\nZ = {stat:.3f}, p = {p_val:.4f}")
print(f"95% CI (Wilson): ({ci_low:.3f}, {ci_high:.3f})")
print(f"Cohen’s h = {h:.3f}")
print(f"Moc testu = {power:.3f}")

if p_val < alpha:
    print("✅ Odrzucamy H0 — ponad 60% programistów używa AI regularnie lub czasami.")
else:
    print("❌ Brak podstaw do odrzucenia H0.")
    
    
    import matplotlib.pyplot as plt

# 🔹 policz częstości odpowiedzi
ai_counts = df["AISelect"].value_counts(dropna=False).sort_values(ascending=True)

# 🔹 wykres słupkowy
plt.figure(figsize=(8, 5))
bars = plt.barh(ai_counts.index, ai_counts.values)

# 🔹 opisy i estetyka
plt.title("Użycie narzędzi AI wśród programistów (Stack Overflow Survey 2023)", fontsize=13)
plt.xlabel("Liczba respondentów")
plt.ylabel("Odpowiedź")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()

# 🔹 etykiety liczbowo na słupkach
for bar in bars:
    plt.text(bar.get_width() + 500, bar.get_y() + bar.get_height()/2,
             f"{int(bar.get_width()):,}", va='center')

plt.show()
