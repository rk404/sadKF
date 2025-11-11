import pandas as pd
from scipy import stats
df = pd.read_csv("data/dailyActivity_merged.csv")
steps = df['TotalSteps'].dropna()

n = len(steps)
mean_steps = steps.mean()
sd_steps = steps.std(ddof=1)

t_stat, p_val = stats.ttest_1samp(steps, 10000)
p_one_sided = p_val / 2 if t_stat > 0 else 1 - p_val / 2

cohen_d = (mean_steps - 10000) / sd_steps

from statsmodels.stats.power import TTestPower

analysis = TTestPower()
alpha = 0.05

power = analysis.solve_power(effect_size=cohen_d, nobs=n, alpha=alpha, alternative='larger')
print(f"Moc testu = {power:.3f}")