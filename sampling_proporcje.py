import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Ustawienie stylu
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# === ILUSTRACJA 1: Koncepcja próbkowania proporcji ===

fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Symulacja populacji - koszykarze z różnymi umiejętnościami
np.random.seed(42)
population_p = 0.4  # prawdziwe prawdopodobieństwo sukcesu w populacji

# Tworzenie wizualnej reprezentacji populacji
# Sukces = zielone kółka, porażka = czerwone kółka
n_population = 400
successes_pop = int(n_population * population_p)
failures_pop = n_population - successes_pop

# Pozycje dla populacji
x_pop_success = np.random.uniform(1, 5, successes_pop)
y_pop_success = np.random.uniform(2, 6, successes_pop)
x_pop_failure = np.random.uniform(1, 5, failures_pop)
y_pop_failure = np.random.uniform(2, 6, failures_pop)

# Rysowanie populacji
ax.scatter(x_pop_success, y_pop_success, c='green', alpha=0.6, s=20, 
          label='Sukcesy w populacji', marker='o')
ax.scatter(x_pop_failure, y_pop_failure, c='red', alpha=0.6, s=20, 
          label='Porażki w populacji', marker='x')

# Dodanie pudełka dla populacji
pop_box = FancyBboxPatch((0.5, 1.5), 4.5, 5, boxstyle="round,pad=0.2", 
                        facecolor='lightblue', alpha=0.2, edgecolor='navy', linewidth=2)
ax.add_patch(pop_box)

# Etykiety dla populacji
ax.text(2.75, 7.2, 'POPULACJA', fontsize=16, fontweight='bold', 
        ha='center', va='center', color='navy')
ax.text(2.75, 6.8, f'Prawdziwe p = {population_p}', fontsize=12, 
        ha='center', va='center', color='navy')
ax.text(2.75, 6.4, f'Sukcesy: {successes_pop}, Porażki: {failures_pop}', fontsize=10, 
        ha='center', va='center', color='navy')

# Symulacja próbek
sample_size = 20
n_samples = 5

# Pozycje dla próbek
sample_positions = [(7, 5.5), (9, 5.5), (11, 5.5), (9, 3.5), (9, 1.5)]

sample_proportions = []
for i, (x_pos, y_pos) in enumerate(sample_positions):
    # Symulacja próbki
    sample_successes = np.random.binomial(sample_size, population_p, 1)[0]
    sample_failures = sample_size - sample_successes
    sample_prop = sample_successes / sample_size
    sample_proportions.append(sample_prop)
    
    # Pozycje punktów w próbce
    if sample_successes > 0:
        x_sample_success = np.random.uniform(x_pos-0.4, x_pos+0.4, sample_successes)
        y_sample_success = np.random.uniform(y_pos-0.4, y_pos+0.4, sample_successes)
        ax.scatter(x_sample_success, y_sample_success, c='darkgreen', alpha=0.8, s=25, marker='o')
    
    if sample_failures > 0:
        x_sample_failure = np.random.uniform(x_pos-0.4, x_pos+0.4, sample_failures)
        y_sample_failure = np.random.uniform(y_pos-0.4, y_pos+0.4, sample_failures)
        ax.scatter(x_sample_failure, y_sample_failure, c='darkred', alpha=0.8, s=25, marker='x')
    
    # Pudełko dla próbki
    sample_box = FancyBboxPatch((x_pos-0.5, y_pos-0.5), 1, 1, boxstyle="round,pad=0.1", 
                              facecolor='lightcoral', alpha=0.3, edgecolor='darkred', linewidth=1)
    ax.add_patch(sample_box)
    
    # Etykieta próbki
    ax.text(x_pos, y_pos-0.8, f'p̂ = {sample_prop:.2f}', fontsize=10, fontweight='bold',
            ha='center', va='center', color='darkred')

# Główne pudełko dla próbek
samples_box = FancyBboxPatch((6.2, 0.8), 5.6, 5.4, boxstyle="round,pad=0.2", 
                           facecolor='lightcoral', alpha=0.1, edgecolor='darkred', linewidth=2)
ax.add_patch(samples_box)

# Etykiety dla próbek
ax.text(9, 7, 'PRÓBKI', fontsize=16, fontweight='bold', 
        ha='center', va='center', color='darkred')
ax.text(9, 6.6, f'n = {sample_size} każda', fontsize=12, 
        ha='center', va='center', color='darkred')

# Strzałka
arrow = FancyArrowPatch((5.2, 4), (6.8, 4), arrowstyle='->', 
                       mutation_scale=20, color='darkgreen', linewidth=3)
ax.add_patch(arrow)
ax.text(6, 4.5, 'Losowe\npróbkowanie', fontsize=11, ha='center', color='darkgreen', fontweight='bold')

# Dodanie obszaru z proporcjami
props_text = "Proporcje z próbek:\n" + "\n".join([f"p̂{i+1} = {prop:.2f}" for i, prop in enumerate(sample_proportions)])
props_text += f"\n\nŚrednia p̂ = {np.mean(sample_proportions):.2f}"
ax.text(13.5, 4, props_text, fontsize=10, ha='left', va='center',
        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))

# Formatowanie
ax.set_xlim(0, 15)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.axis('off')

# Tytuł
plt.suptitle('Koncepcja próbkowania proporcji', fontsize=18, fontweight='bold', y=0.95)
plt.figtext(0.5, 0.02, 'Od prawdziwego p do szacunków p̂ z próbek', 
            ha='center', fontsize=12, style='italic')

# Legenda
success_patch = mpatches.Patch(color='green', label='Sukcesy')
failure_patch = mpatches.Patch(color='red', label='Porażki')
ax.legend(handles=[success_patch, failure_patch], loc='upper left')

plt.tight_layout()
plt.show()

# === ILUSTRACJA 2: Rozkłady próbkowe proporcji dla różnych n ===

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Parametry symulacji
true_p = 0.4
sample_sizes = [10, 30, 100]
n_simulations = 1000

# Funkcja do symulacji proporcji
def simulate_proportions(n, p, num_sims=1000):
    successes = np.random.binomial(n, p, num_sims)
    proportions = successes / n
    return proportions

# Teoretyczne rozkłady
def plot_theoretical_normal(ax, n, p, color='red', alpha=0.3):
    x = np.linspace(0, 1, 1000)
    mean = p
    std = np.sqrt(p * (1-p) / n)
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    ax.plot(x, y, color=color, linewidth=3, alpha=0.8, linestyle='--', 
            label=f'Teoretyczny rozkład N({mean:.2f}, {std:.3f})')
    return mean, std

# Symulacja dla n=10
props_n10 = simulate_proportions(10, true_p, n_simulations)
se_theoretical_n10 = np.sqrt(true_p * (1-true_p) / 10)
se_empirical_n10 = np.std(props_n10)

ax1.hist(props_n10, bins=30, alpha=0.7, color='lightgreen', edgecolor='black', density=True)
ax1.axvline(np.mean(props_n10), color='darkgreen', linestyle='-', linewidth=3, label=f'Średnia = {np.mean(props_n10):.3f}')
ax1.axvline(true_p, color='red', linestyle='--', linewidth=2, label=f'Prawdziwe p = {true_p}')
plot_theoretical_normal(ax1, 10, true_p, 'red', 0.5)
ax1.set_title(f'Proporcje z próbek (n=10)\nSE = {se_empirical_n10:.3f} (teor: {se_theoretical_n10:.3f})', 
              fontsize=12, fontweight='bold')
ax1.set_xlabel('Proporcja próbki')
ax1.set_ylabel('Gęstość')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# Symulacja dla n=30
props_n30 = simulate_proportions(30, true_p, n_simulations)
se_theoretical_n30 = np.sqrt(true_p * (1-true_p) / 30)
se_empirical_n30 = np.std(props_n30)

ax2.hist(props_n30, bins=30, alpha=0.7, color='lightcoral', edgecolor='black', density=True)
ax2.axvline(np.mean(props_n30), color='darkred', linestyle='-', linewidth=3, label=f'Średnia = {np.mean(props_n30):.3f}')
ax2.axvline(true_p, color='red', linestyle='--', linewidth=2, label=f'Prawdziwe p = {true_p}')
plot_theoretical_normal(ax2, 30, true_p, 'red', 0.5)
ax2.set_title(f'Proporcje z próbek (n=30)\nSE = {se_empirical_n30:.3f} (teor: {se_theoretical_n30:.3f})', 
              fontsize=12, fontweight='bold')
ax2.set_xlabel('Proporcja próbki')
ax2.set_ylabel('Gęstość')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

# Symulacja dla n=100
props_n100 = simulate_proportions(100, true_p, n_simulations)
se_theoretical_n100 = np.sqrt(true_p * (1-true_p) / 100)
se_empirical_n100 = np.std(props_n100)

ax3.hist(props_n100, bins=30, alpha=0.7, color='lightblue', edgecolor='black', density=True)
ax3.axvline(np.mean(props_n100), color='darkblue', linestyle='-', linewidth=3, label=f'Średnia = {np.mean(props_n100):.3f}')
ax3.axvline(true_p, color='red', linestyle='--', linewidth=2, label=f'Prawdziwe p = {true_p}')
plot_theoretical_normal(ax3, 100, true_p, 'red', 0.5)
ax3.set_title(f'Proporcje z próbek (n=100)\nSE = {se_empirical_n100:.3f} (teor: {se_theoretical_n100:.3f})', 
              fontsize=12, fontweight='bold')
ax3.set_xlabel('Proporcja próbki')
ax3.set_ylabel('Gęstość')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Wykres SE vs wielkość próby dla proporcji
sample_sizes_range = np.arange(5, 201, 5)
theoretical_se_props = np.sqrt(true_p * (1-true_p) / sample_sizes_range)

# Symulowane SE dla kilku wielkości próby
empirical_sizes = [10, 20, 30, 50, 100, 150]
empirical_se_props = []
for n in empirical_sizes:
    props = simulate_proportions(n, true_p, 500)
    empirical_se_props.append(np.std(props))

ax4.plot(sample_sizes_range, theoretical_se_props, 'b-', linewidth=3, label='Teoretyczny SE')
ax4.scatter(empirical_sizes, empirical_se_props, color='red', s=100, zorder=5, 
           label='Symulowany SE')
ax4.set_title('Błąd standardowy proporcji vs wielkość próby', fontsize=14, fontweight='bold')
ax4.set_xlabel('Wielkość próby (n)')
ax4.set_ylabel('Błąd standardowy SE(p̂)')
ax4.legend(fontsize=12)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# === ILUSTRACJA 3: Wzory i kluczowe pojęcia dla proporcji ===

fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')

# Główny tekst z wzorami
main_text = """KLUCZOWE WZORY DLA PRÓBKOWANIA PROPORCJI

Proporcja z próby:
p̂ = X/n  (gdzie X = liczba sukcesów)

Błąd standardowy proporcji:
SE(p̂) = √[p(1-p)/n]

Rozkład próbkowy proporcji (CTG):
p̂ ~ N(p, p(1-p)/n)

Standaryzacja proporcji z próby:
Z = (p̂ - p) / SE(p̂) = (p̂ - p) / √[p(1-p)/n]

WARUNKI STOSOWANIA PRZYBLIŻENIA NORMALNEGO:
• np ≥ 5  oraz  n(1-p) ≥ 5

CENTRALNE TWIERDZENIE GRANICZNE DLA PROPORCJI:
• Rozkład proporcji z próbek jest normalny (dla dużych n)
• Średnia rozkładu próbkowego = prawdziwe p
• Odchylenie standardowe rozkładu próbkowego = √[p(1-p)/n]
"""

# Główne pudełko z wzorami
main_box = FancyBboxPatch((0.05, 0.35), 0.55, 0.6, boxstyle="round,pad=0.02", 
                         facecolor='lightblue', alpha=0.8, edgecolor='navy', linewidth=2)
ax.add_patch(main_box)
ax.text(0.07, 0.93, main_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', fontfamily='monospace')

# Przykład numeryczny
example_text = f"""PRZYKŁAD Z SYMULACJI KOSZYKARZA:

Prawdziwe p = {true_p}

n = 10: SE teoretyczny = {se_theoretical_n10:.3f}
        SE symulowany = {se_empirical_n10:.3f}

n = 30: SE teoretyczny = {se_theoretical_n30:.3f}
        SE symulowany = {se_empirical_n30:.3f}

n = 100: SE teoretyczny = {se_theoretical_n100:.3f}
         SE symulowany = {se_empirical_n100:.3f}

OBSERWACJA: 
Zwiększenie n z 10 do 100 (10 razy) 
zmniejsza SE o √10 ≈ 3.16 razy!

PRAKTYCZNE ZASTOSOWANIA:
• Sondaże opinii publicznej
• Kontrola jakości produkcji  
• Badania kliniczne (skuteczność leku)
• Marketing (click-through rate)

REGUŁA 5:
n=10: np = 4, n(1-p) = 6 → warunek nie spełniony
n=30: np = 12, n(1-p) = 18 → warunek spełniony ✓
"""

# Pudełko z przykładem
example_box = FancyBboxPatch((0.65, 0.05), 0.32, 0.9, boxstyle="round,pad=0.02", 
                           facecolor='lightyellow', alpha=0.8, edgecolor='orange', linewidth=2)
ax.add_patch(example_box)
ax.text(0.67, 0.93, example_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', fontfamily='monospace')

# Tytuł
ax.text(0.5, 0.98, 'Matematyczne podstawy próbkowania proporcji', 
        transform=ax.transAxes, fontsize=18, fontweight='bold', 
        ha='center', va='top')

# Dolny pasek z kluczowymi wnioskami
conclusions_text = """KLUCZOWE WNIOSKI: 1) p̂ jest estymatorem p  2) SE(p̂) = √[p(1-p)/n]  3) Większe n → mniejszy SE → dokładniejszy szacunek  4) Sprawdź regułę 5!"""
conclusions_box = FancyBboxPatch((0.05, 0.02), 0.9, 0.08, boxstyle="round,pad=0.01", 
                               facecolor='lightgreen', alpha=0.8, edgecolor='green', linewidth=2)
ax.add_patch(conclusions_box)
ax.text(0.5, 0.06, conclusions_text, transform=ax.transAxes, fontsize=11,
        ha='center', va='center', fontweight='bold')

plt.show()

print("=" * 70)
print("PODSUMOWANIE SYMULACJI PRÓBKOWANIA PROPORCJI")
print("=" * 70)
print(f"Prawdziwe p = {true_p}")
print(f"Liczba symulacji: {n_simulations} dla każdej wielkości próby")
print()
print("WYNIKI:")
print(f"n=10:  Średnia p̂ = {np.mean(props_n10):.3f}, SE = {se_empirical_n10:.3f}")
print(f"n=30:  Średnia p̂ = {np.mean(props_n30):.3f}, SE = {se_empirical_n30:.3f}")
print(f"n=100: Średnia p̂ = {np.mean(props_n100):.3f}, SE = {se_empirical_n100:.3f}")
print()
print("WERYFIKACJA WZORU SE(p̂) = √[p(1-p)/n]:")
print(f"n=10:  SE teoretyczny = {se_theoretical_n10:.3f}, SE empiryczny = {se_empirical_n10:.3f}")
print(f"n=30:  SE teoretyczny = {se_theoretical_n30:.3f}, SE empiryczny = {se_empirical_n30:.3f}")
print(f"n=100: SE teoretyczny = {se_theoretical_n100:.3f}, SE empiryczny = {se_empirical_n100:.3f}")
print()
print("SPRAWDZENIE REGUŁY 5:")
for n in [10, 30, 100]:
    np_val = n * true_p
    n1p_val = n * (1 - true_p)
    rule5_ok = np_val >= 5 and n1p_val >= 5
    print(f"n={n}: np = {np_val:.1f}, n(1-p) = {n1p_val:.1f} → Reguła 5: {'✓' if rule5_ok else '✗'}")