import numpy as np
from scipy import stats
mean_sleep_time = np.mean(dane)
se_mean = stats.sem(dane)
relative_error = (se_mean/mean_sleep_time)*100

lower,upp = stats.t.interval(0.95, len(dane)-1, loc= mean_sleep_time, scale=se_mean)
print(f"Średni czas snu: {mean_sleep_time:.2f}")
print(f"Błąd standardowy w godzinach: {se_mean:.2f}")
print(f"Błąd standardowy średniej w %: {relative_error:.2f}")
print(f"95% przedział ufności średniej: ({lower:.2f},{upp:.2f})")