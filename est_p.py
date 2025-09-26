import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.patches as patches

# Tworzenie rysunku koncepcyjnego estymacji punktowej i przedziałowej
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Parametry populacji
true_mean = 50  # Prawdziwa średnia populacji
true_std = 10   # Prawdziwe odchylenie standardowe populacji
sample_size = 30

# Generowanie próby
np.random.seed(42)
sample = np.random.normal(true_mean, true_std, sample_size)

# Estymacja punktowa
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)

# Estymacja przedziałowa (95% przedział ufności)
se_mean = sample_std / np.sqrt(sample_size)
t_critical = stats.t.ppf(0.975, sample_size - 1)
ci_lower = sample_mean - t_critical * se_mean
ci_upper = sample_mean + t_critical * se_mean

# Wykres 1: Estymacja punktowa
ax1.hist(sample, bins=8, alpha=0.7, color='lightblue', edgecolor='black', density=True, label='Próba')

# Prawdziwa średnia populacji
ax1.axvline(true_mean, color='red', linewidth=3, linestyle='--', label=f'Prawdziwa średnia μ = {true_mean}')

# Estymator punktowy (średnia z próby)
ax1.axvline(sample_mean, color='green', linewidth=3, label=f'Estymator punktowy x̄ = {sample_mean:.2f}')

# Dodanie krzywej normalnej dla populacji
x_range = np.linspace(true_mean - 3*true_std, true_mean + 3*true_std, 1000)
population_curve = stats.norm.pdf(x_range, true_mean, true_std)
ax1.plot(x_range, population_curve, 'r-', alpha=0.8, linewidth=2, label='Rozkład populacji')

ax1.set_title('ESTYMACJA PUNKTOWA\nJeden punkt jako oszacowanie parametru', fontsize=14, fontweight='bold')
ax1.set_xlabel('Wartość', fontsize=12)
ax1.set_ylabel('Gęstość', fontsize=12)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Wykres 2: Estymacja przedziałowa
ax2.hist(sample, bins=8, alpha=0.7, color='lightblue', edgecolor='black', density=True, label='Próba')

# Prawdziwa średnia populacji
ax2.axvline(true_mean, color='red', linewidth=3, linestyle='--', label=f'Prawdziwa średnia μ = {true_mean}')

# Estymator punktowy
ax2.axvline(sample_mean, color='green', linewidth=3, label=f'Estymator punktowy x̄ = {sample_mean:.2f}')

# Przedział ufności
ax2.axvspan(ci_lower, ci_upper, alpha=0.3, color='orange', label=f'95% Przedział ufności\n[{ci_lower:.2f}, {ci_upper:.2f}]')
ax2.axvline(ci_lower, color='orange', linewidth=2, linestyle=':')
ax2.axvline(ci_upper, color='orange', linewidth=2, linestyle=':')

# Dodanie krzywej normalnej dla populacji
ax2.plot(x_range, population_curve, 'r-', alpha=0.8, linewidth=2, label='Rozkład populacji')

ax2.set_title('ESTYMACJA PRZEDZIAŁOWA\nZakres wartości z określonym poziomem ufności', fontsize=14, fontweight='bold')
ax2.set_xlabel('Wartość', fontsize=12)
ax2.set_ylabel('Gęstość', fontsize=12)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Dodatkowy wykres ilustrujący koncepcję przedziału ufności
fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Symulacja wielu próbek i ich przedziałów ufności
n_samples = 20
sample_means = []
confidence_intervals = []

np.random.seed(123)
for i in range(n_samples):
    sample_i = np.random.normal(true_mean, true_std, sample_size)
    mean_i = np.mean(sample_i)
    std_i = np.std(sample_i, ddof=1)
    se_i = std_i / np.sqrt(sample_size)
    ci_i = [mean_i - t_critical * se_i, mean_i + t_critical * se_i]
    
    sample_means.append(mean_i)
    confidence_intervals.append(ci_i)
    
    # Sprawdź czy przedział zawiera prawdziwą średnią
    color = 'green' if ci_i[0] <= true_mean <= ci_i[1] else 'red'
    
    # Rysowanie przedziału
    ax.plot([ci_i[0], ci_i[1]], [i, i], color=color, linewidth=2, alpha=0.7)
    ax.plot(mean_i, i, 'o', color=color, markersize=8)

# Prawdziwa średnia populacji
ax.axvline(true_mean, color='blue', linewidth=3, linestyle='--', label=f'Prawdziwa średnia μ = {true_mean}')

# Obliczenie ile przedziałów zawiera prawdziwą średnią
contains_true_mean = sum(1 for ci in confidence_intervals if ci[0] <= true_mean <= ci[1])
coverage_rate = contains_true_mean / n_samples * 100

ax.set_title(f'INTERPRETACJA PRZEDZIAŁU UFNOŚCI\n{contains_true_mean}/{n_samples} przedziałów ({coverage_rate:.0f}%) zawiera prawdziwą średnię populacji', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('Wartość', fontsize=12)
ax.set_ylabel('Numer próby', fontsize=12)
ax.set_ylim(-1, n_samples)
ax.grid(True, alpha=0.3)

# Legenda
green_patch = patches.Patch(color='green', label='Przedział zawiera μ')
red_patch = patches.Patch(color='red', label='Przedział nie zawiera μ')
ax.legend(handles=[green_patch, red_patch], fontsize=11)

plt.tight_layout()
plt.show()

# Podsumowanie koncepcji
print("="*60)
print("PODSTAWOWE KONCEPCJE ESTYMACJI")
print("="*60)
print()
print("1. ESTYMACJA PUNKTOWA:")
print(f"   • Jeden punkt jako oszacowanie parametru populacji")
print(f"   • Przykład: x̄ = {sample_mean:.2f} jako estymator μ = {true_mean}")
print()
print("2. ESTYMACJA PRZEDZIAŁOWA:")
print(f"   • Zakres wartości z określonym poziomem ufności")
print(f"   • Przykład: 95% P.U. = [{ci_lower:.2f}, {ci_upper:.2f}]")
print()
print("3. INTERPRETACJA PRZEDZIAŁU UFNOŚCI:")
print(f"   • Jeśli powtórzymy procedurę 100 razy,")
print(f"   • około 95 przedziałów będzie zawierało prawdziwą μ")
print(f"   • W naszej symulacji: {coverage_rate:.0f}% przedziałów zawierało μ")
print("="*60)