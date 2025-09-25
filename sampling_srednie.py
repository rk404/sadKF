import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch

# Ustawienie stylu
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# === ILUSTRACJA 1: Różnica między populacją a próbkami średnich ===

fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Symulacja populacji
np.random.seed(42)
population_mean = 65
population_std = 3
population = np.random.normal(population_mean, population_std, 2000)

# Rysowanie punktów populacji jako tło
x_pop = np.random.uniform(1, 5, 2000)
y_pop = population
ax.scatter(x_pop, y_pop, alpha=0.3, s=8, color='lightblue', label='Populacja')

# Dodanie pudełka dla populacji
pop_box = FancyBboxPatch((0.5, 50), 4.5, 30, boxstyle="round,pad=0.5", 
                        facecolor='lightblue', alpha=0.2, edgecolor='navy', linewidth=2)
ax.add_patch(pop_box)

# Etykiety dla populacji
ax.text(2.75, 82, 'POPULACJA', fontsize=16, fontweight='bold', 
        ha='center', va='center', color='navy')
ax.text(2.75, 78, f'μ = {population_mean}, σ = {population_std}', fontsize=12, 
        ha='center', va='center', color='navy')

# Symulacja próbek i ich średnich
sample_size = 10
n_samples = 200
sample_means = []

for i in range(n_samples):
    sample = np.random.choice(population, sample_size)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)
    
    # Rysowanie niektórych próbek
    if i < 20:
        x_sample = np.random.uniform(7 + i*0.3, 7.5 + i*0.3, sample_size)
        ax.scatter(x_sample, sample, alpha=0.6, s=15, color='red')

# Rysowanie średnich z próbek
x_means = np.random.uniform(6, 13, n_samples)
ax.scatter(x_means, sample_means, alpha=0.8, s=30, color='darkred', 
          label=f'Średnie z próbek (n={sample_size})')

# Dodanie pudełka dla średnich
means_box = FancyBboxPatch((5.5, 60), 8, 10, boxstyle="round,pad=0.5", 
                          facecolor='lightcoral', alpha=0.2, edgecolor='darkred', linewidth=2)
ax.add_patch(means_box)

# Etykiety dla średnich
ax.text(9.5, 72, 'ŚREDNIE Z PRÓBEK', fontsize=16, fontweight='bold', 
        ha='center', va='center', color='darkred')
ax.text(9.5, 68, f'Rozkład wokół μ = {np.mean(sample_means):.1f}', fontsize=12, 
        ha='center', va='center', color='darkred')

# Strzałka
arrow = FancyArrowPatch((5, 65), (6.5, 65), arrowstyle='->', 
                       mutation_scale=20, color='darkgreen', linewidth=3)
ax.add_patch(arrow)
ax.text(5.75, 67, 'Próbkowanie', fontsize=12, ha='center', color='darkgreen', fontweight='bold')

# Linie pokazujące średnie
ax.axhline(population_mean, xmin=0.05, xmax=0.35, color='navy', linestyle='--', linewidth=2, alpha=0.8)
ax.axhline(np.mean(sample_means), xmin=0.4, xmax=0.95, color='darkred', linestyle='--', linewidth=2, alpha=0.8)

# Formatowanie
ax.set_xlim(0, 14)
ax.set_ylim(50, 85)
ax.set_xlabel('', fontsize=14)
ax.set_ylabel('Wartość', fontsize=14)
ax.set_title('Koncepcja próbkowania średnich', fontsize=18, fontweight='bold', pad=20)
ax.legend(loc='upper left', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# === ILUSTRACJA 2: Rozkłady próbkowe dla różnych n ===

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Populacja bazowa
np.random.seed(123)
population = np.random.normal(100, 15, 10000)

# Wykres populacji
ax1.hist(population, bins=50, alpha=0.7, color='lightblue', edgecolor='black', density=True)
ax1.axvline(population.mean(), color='red', linestyle='--', linewidth=3)
ax1.set_title(f'Populacja\nμ = {population.mean():.1f}, σ = {population.std():.1f}', 
              fontsize=14, fontweight='bold')
ax1.set_xlabel('Wartość')
ax1.set_ylabel('Gęstość')
ax1.grid(True, alpha=0.3)

# Funkcja do symulacji średnich
def simulate_sample_means(pop, n, num_samples=1000):
    means = []
    for _ in range(num_samples):
        sample = np.random.choice(pop, n, replace=False)
        means.append(sample.mean())
    return np.array(means)

# Rozkład próbkowy dla n=5
sample_means_n5 = simulate_sample_means(population, 5)
se_theoretical_n5 = population.std() / np.sqrt(5)
se_empirical_n5 = np.std(sample_means_n5)

ax2.hist(sample_means_n5, bins=40, alpha=0.7, color='lightgreen', edgecolor='black', density=True)
ax2.axvline(np.mean(sample_means_n5), color='red', linestyle='--', linewidth=3)
ax2.set_title(f'Średnie z próbek (n=5)\nŚrednia = {np.mean(sample_means_n5):.1f}\nSE = {se_empirical_n5:.2f} (teor: {se_theoretical_n5:.2f})', 
              fontsize=12, fontweight='bold')
ax2.set_xlabel('Średnia próbki')
ax2.set_ylabel('Gęstość')
ax2.grid(True, alpha=0.3)

# Rozkład próbkowy dla n=25
sample_means_n25 = simulate_sample_means(population, 25)
se_theoretical_n25 = population.std() / np.sqrt(25)
se_empirical_n25 = np.std(sample_means_n25)

ax3.hist(sample_means_n25, bins=40, alpha=0.7, color='lightcoral', edgecolor='black', density=True)
ax3.axvline(np.mean(sample_means_n25), color='red', linestyle='--', linewidth=3)
ax3.set_title(f'Średnie z próbek (n=25)\nŚrednia = {np.mean(sample_means_n25):.1f}\nSE = {se_empirical_n25:.2f} (teor: {se_theoretical_n25:.2f})', 
              fontsize=12, fontweight='bold')
ax3.set_xlabel('Średnia próbki')
ax3.set_ylabel('Gęstość')
ax3.grid(True, alpha=0.3)

# Wykres SE vs wielkość próby
sample_sizes = np.arange(2, 101, 2)
theoretical_se = population.std() / np.sqrt(sample_sizes)

# Symulowane SE dla kilku wielkości próby
empirical_sizes = [5, 10, 15, 25, 50, 75]
empirical_se = []
for n in empirical_sizes:
    means = simulate_sample_means(population, n, 500)
    empirical_se.append(np.std(means))

ax4.plot(sample_sizes, theoretical_se, 'b-', linewidth=3, label='Teoretyczny SE')
ax4.scatter(empirical_sizes, empirical_se, color='red', s=100, zorder=5, 
           label='Symulowany SE')
ax4.set_title('Błąd standardowy vs wielkość próby', fontsize=14, fontweight='bold')
ax4.set_xlabel('Wielkość próby (n)')
ax4.set_ylabel('Błąd standardowy (SE)')
ax4.legend(fontsize=12)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# === ILUSTRACJA 3: Wzory i kluczowe pojęcia ===

fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')

# Główny tekst z wzorami
main_text = """KLUCZOWE WZORY DLA PRÓBKOWANIA ŚREDNICH

Błąd standardowy średniej:
SE = σ / √n

Rozkład próbkowy średniej (CTG):
X̄ ~ N(μ, σ²/n)

Standaryzacja średniej z próby:
Z = (X̄ - μ) / SE = (X̄ - μ) / (σ/√n)

CENTRALNE TWIERDZENIE GRANICZNE:
• Rozkład średnich z próbek jest zawsze normalny (dla dużych n)
• Średnia rozkładu próbkowego = średnia populacji
• Odchylenie standardowe rozkładu próbkowego = σ/√n
"""

# Główne pudełko z wzorami
main_box = FancyBboxPatch((0.05, 0.4), 0.55, 0.55, boxstyle="round,pad=0.02", 
                         facecolor='lightblue', alpha=0.8, edgecolor='navy', linewidth=2)
ax.add_patch(main_box)
ax.text(0.07, 0.93, main_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', fontfamily='monospace')

# Przykład numeryczny
example_text = f"""PRZYKŁAD Z SYMULACJI:

Populacja: μ = {population.mean():.1f}, σ = {population.std():.1f}

n = 5:  SE teoretyczny = {population.std()/np.sqrt(5):.2f}
        SE symulowany = {se_empirical_n5:.2f}

n = 25: SE teoretyczny = {population.std()/np.sqrt(25):.2f}
        SE symulowany = {se_empirical_n25:.2f}

OBSERWACJA: 
Zwiększenie n z 5 do 25 (5 razy) 
zmniejsza SE o √5 ≈ 2.24 razy!

PRAKTYCZNE ZNACZENIE:
• Większa próba → mniejszy błąd standardowy
• Mniejszy SE → większa precyzja oszacowania
• SE maleje proporcjonalnie do 1/√n
"""

# Pudełko z przykładem
example_box = FancyBboxPatch((0.65, 0.15), 0.32, 0.8, boxstyle="round,pad=0.02", 
                           facecolor='lightyellow', alpha=0.8, edgecolor='orange', linewidth=2)
ax.add_patch(example_box)
ax.text(0.67, 0.93, example_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', fontfamily='monospace')

# Tytuł
ax.text(0.5, 0.98, 'Matematyczne podstawy próbkowania średnich', 
        transform=ax.transAxes, fontsize=18, fontweight='bold', 
        ha='center', va='top')

# Dolny pasek z kluczowymi wnioskami
conclusions_text = """KLUCZOWE WNIOSKI: 1) Błąd próby jest nieunikniony  2) SE quantyfikuje niepewność  3) Większe n → mniejszy SE → większa precyzja"""
conclusions_box = FancyBboxPatch((0.05, 0.02), 0.9, 0.08, boxstyle="round,pad=0.01", 
                               facecolor='lightgreen', alpha=0.8, edgecolor='green', linewidth=2)
ax.add_patch(conclusions_box)
ax.text(0.5, 0.06, conclusions_text, transform=ax.transAxes, fontsize=11,
        ha='center', va='center', fontweight='bold')

plt.show()

print("=" * 60)
print("PODSUMOWANIE SYMULACJI PRÓBKOWANIA ŚREDNICH")
print("=" * 60)
print(f"Populacja: μ = {population.mean():.2f}, σ = {population.std():.2f}")
print(f"Liczba symulacji: 1000 dla każdej wielkości próby")
print()
print("WYNIKI:")
print(f"n=5:  Średnia próbkowa = {np.mean(sample_means_n5):.2f}, SE = {se_empirical_n5:.2f}")
print(f"n=25: Średnia próbkowa = {np.mean(sample_means_n25):.2f}, SE = {se_empirical_n25:.2f}")
print()
print("WERYFIKACJA WZORU SE = σ/√n:")
print(f"n=5:  SE teoretyczny = {se_theoretical_n5:.2f}, SE empiryczny = {se_empirical_n5:.2f}")
print(f"n=25: SE teoretyczny = {se_theoretical_n25:.2f}, SE empiryczny = {se_empirical_n25:.2f}")
print()
print(f"Stosunek SE: {se_empirical_n5/se_empirical_n25:.2f} (teoretyczny: {np.sqrt(25/5):.2f})")