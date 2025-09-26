import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from scipy import stats
import matplotlib.patches as mpatches

# Ustawienie stylu
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# === ILUSTRACJA 1: Koncepcja estymacji proporcji ===

fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Symulacja populacji z określoną proporcją
np.random.seed(42)
population_p = 0.3  # prawdziwa proporcja sukcesu w populacji
population_size = 2000

# Tworzenie wizualnej reprezentacji populacji
# Sukces = zielone kółka, porażka = czerwone krzyżyki
successes_pop = int(population_size * population_p)
failures_pop = population_size - successes_pop

# Pozycje dla populacji
x_pop_success = np.random.uniform(1, 5, successes_pop)
y_pop_success = np.random.uniform(20, 80, successes_pop)
x_pop_failure = np.random.uniform(1, 5, failures_pop)
y_pop_failure = np.random.uniform(20, 80, failures_pop)

# Rysowanie populacji
ax.scatter(x_pop_success, y_pop_success, c='green', alpha=0.4, s=8, 
          marker='o', label='Sukcesy w populacji')
ax.scatter(x_pop_failure, y_pop_failure, c='red', alpha=0.4, s=8, 
          marker='x', label='Porazki w populacji')

# Dodanie pudełka dla populacji
pop_box = FancyBboxPatch((0.5, 15), 4.5, 70, boxstyle="round,pad=0.5", 
                        facecolor='lightblue', alpha=0.2, edgecolor='navy', linewidth=2)
ax.add_patch(pop_box)

# Etykiety dla populacji
ax.text(2.75, 90, 'POPULACJA', fontsize=16, fontweight='bold', 
        ha='center', va='center', color='navy')
ax.text(2.75, 85, f'Prawdziwa p = {population_p}', fontsize=12, 
        ha='center', va='center', color='navy')
ax.text(2.75, 80, f'Sukcesy: {successes_pop}, Porazki: {failures_pop}', fontsize=10, 
        ha='center', va='center', color='navy')

# Symulacja próbek i ich proporcji
sample_size = 50
n_samples = 5

# Pozycje dla próbek
sample_positions = [(7, 70), (9, 70), (11, 70), (9, 45), (9, 20)]
sample_proportions = []

for i, (x_pos, y_pos) in enumerate(sample_positions):
    # Symulacja próbki - losowe wybieranie sukces/porażka
    sample_successes = np.random.binomial(sample_size, population_p, 1)[0]
    sample_failures = sample_size - sample_successes
    sample_prop = sample_successes / sample_size
    sample_proportions.append(sample_prop)
    
    # Pozycjonowanie punktów w próbce
    if sample_successes > 0:
        x_sample_success = np.random.uniform(x_pos-0.4, x_pos+0.4, sample_successes)
        y_sample_success = np.random.uniform(y_pos-8, y_pos+8, sample_successes)
        ax.scatter(x_sample_success, y_sample_success, c='darkgreen', alpha=0.8, s=25, marker='o')
    
    if sample_failures > 0:
        x_sample_failure = np.random.uniform(x_pos-0.4, x_pos+0.4, sample_failures)
        y_sample_failure = np.random.uniform(y_pos-8, y_pos+8, sample_failures)
        ax.scatter(x_sample_failure, y_sample_failure, c='darkred', alpha=0.8, s=25, marker='x')
    
    # Pudełko dla próbki
    sample_box = FancyBboxPatch((x_pos-0.5, y_pos-10), 1, 20, boxstyle="round,pad=0.2", 
                              facecolor='lightcoral', alpha=0.3, edgecolor='darkred', linewidth=1)
    ax.add_patch(sample_box)
    
    # Etykieta próbki
    ax.text(x_pos, y_pos-15, f'p^ = {sample_prop:.2f}', fontsize=10, fontweight='bold',
            ha='center', va='center', color='darkred')
    ax.text(x_pos, y_pos-18, f'({sample_successes}/{sample_size})', fontsize=8,
            ha='center', va='center', color='darkred')

# Główne pudełko dla próbek
samples_box = FancyBboxPatch((6.2, 8), 5.6, 75, boxstyle="round,pad=0.5", 
                           facecolor='lightcoral', alpha=0.1, edgecolor='darkred', linewidth=2)
ax.add_patch(samples_box)

# Etykiety dla próbek
ax.text(9, 88, 'PROBKI', fontsize=16, fontweight='bold', 
        ha='center', va='center', color='darkred')
ax.text(9, 83, f'n = {sample_size} kazda', fontsize=12, 
        ha='center', va='center', color='darkred')

# Strzałka
arrow = FancyArrowPatch((5.2, 50), (6.8, 50), arrowstyle='->', 
                       mutation_scale=20, color='darkgreen', linewidth=3)
ax.add_patch(arrow)
ax.text(6, 55, 'Losowe\nprobkowanie', fontsize=11, ha='center', color='darkgreen', fontweight='bold')

# Obszar z wynikami
results_text = "Proporcje z probek:\n" + "\n".join([f"p^_{i+1} = {prop:.2f}" for i, prop in enumerate(sample_proportions)])
results_text += f"\n\nSrednia p^ = {np.mean(sample_proportions):.2f}"
results_text += f"\nPrawdziwa p = {population_p}"
results_text += f"\n\nBlad standardowy:"
results_text += f"\nSE = √(p(1-p)/n)"
results_text += f"\nSE = {np.sqrt(population_p * (1-population_p) / sample_size):.3f}"
ax.text(13.5, 50, results_text, fontsize=10, ha='left', va='center',
        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))

# Formatowanie
ax.set_xlim(0, 16)
ax.set_ylim(10, 95)
ax.set_xlabel('', fontsize=14)
ax.set_ylabel('Rozklad w populacji/probach', fontsize=14)
ax.set_title('Koncepcja estymacji proporcji', fontsize=18, fontweight='bold', pad=20)

# Legenda
success_patch = mpatches.Patch(color='green', label='Sukcesy')
failure_patch = mpatches.Patch(color='red', label='Porazki')
ax.legend(handles=[success_patch, failure_patch], loc='upper left')

plt.tight_layout()
plt.show()

# === ILUSTRACJA 2: Rozkład próbkowy proporcji ===

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Parametry symulacji
true_p = 0.3
sample_sizes = [20, 50, 100, 200]
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
    # Sprawdź warunek normalnego przybliżenia
    if n * p >= 5 and n * (1-p) >= 5:
        y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
        ax.plot(x, y, color=color, linewidth=3, alpha=0.8, linestyle='--', 
                label=f'Teoretyczny N({mean:.2f}, {std:.3f})')
    return mean, std

axes = [ax1, ax2, ax3, ax4]
colors = ['red', 'blue', 'green', 'orange']

for i, n in enumerate(sample_sizes):
    ax = axes[i]
    
    # Symulacja proporcji próbkowych
    props = simulate_proportions(n, true_p, n_simulations)
    se_theoretical = np.sqrt(true_p * (1-true_p) / n)
    se_empirical = np.std(props)
    
    # Histogram symulowanych proporcji
    ax.hist(props, bins=30, alpha=0.7, density=True, color=colors[i], 
            edgecolor='black', label=f'Symulowane p^')
    
    # Średnie
    ax.axvline(np.mean(props), color='darkgreen', linestyle='-', linewidth=3, 
               label=f'Srednia = {np.mean(props):.3f}')
    ax.axvline(true_p, color='red', linestyle='--', linewidth=2, 
               label=f'Prawdziwa p = {true_p}')
    
    # Teoretyczny rozkład normalny (jeśli spełnia warunki)
    plot_theoretical_normal(ax, n, true_p, 'red', 0.5)
    
    # Sprawdź regułę 5
    rule5_ok = n * true_p >= 5 and n * (1-true_p) >= 5
    rule5_text = f'np = {n * true_p:.1f}, n(1-p) = {n * (1-true_p):.1f}'
    rule5_status = 'OK' if rule5_ok else 'NIE'
    
    ax.set_title(f'n = {n}, SE = {se_empirical:.3f}\nRegula 5: {rule5_text} {rule5_status}', 
                fontsize=10, fontweight='bold')
    ax.set_xlabel('Proporcja probki p^')
    ax.set_ylabel('Gestosc')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 0.6)

plt.suptitle('Rozklad probkowy proporcji dla roznych wielkosci proby', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# === ILUSTRACJA 3: Przedziały ufności dla proporcji ===

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Przykład obliczenia przedziału ufności dla proporcji
sample_size = 100
confidence_level = 0.95
alpha = 1 - confidence_level
z_alpha = stats.norm.ppf(1 - alpha/2)

# Symulacja jednej próbki
np.random.seed(123)
sample_successes = np.random.binomial(sample_size, true_p, 1)[0]
sample_prop = sample_successes / sample_size
se_prop = np.sqrt(sample_prop * (1 - sample_prop) / sample_size)

# Przedział ufności dla proporcji
margin_error = z_alpha * se_prop
ci_lower = sample_prop - margin_error
ci_upper = sample_prop + margin_error

# Wykres rozkładu normalnego
x_norm = np.linspace(-4, 4, 1000)
y_norm = stats.norm.pdf(x_norm, 0, 1)

ax1.plot(x_norm, y_norm, 'b-', linewidth=2, label='N(0,1)')
ax1.fill_between(x_norm[x_norm <= -z_alpha], y_norm[x_norm <= -z_alpha], 
                alpha=0.3, color='red', label=f'alpha/2 = {alpha/2}')
ax1.fill_between(x_norm[x_norm >= z_alpha], y_norm[x_norm >= z_alpha], 
                alpha=0.3, color='red')
ax1.fill_between(x_norm[(x_norm >= -z_alpha) & (x_norm <= z_alpha)], 
                y_norm[(x_norm >= -z_alpha) & (x_norm <= z_alpha)], 
                alpha=0.3, color='green', label=f'1-alpha = {confidence_level}')

ax1.axvline(-z_alpha, color='red', linestyle='--', linewidth=2, 
           label=f'z_0.025 = {-z_alpha:.2f}')
ax1.axvline(z_alpha, color='red', linestyle='--', linewidth=2, 
           label=f'z_0.975 = {z_alpha:.2f}')

ax1.set_title('Rozklad N(0,1) dla przedzialu ufnosci proporcji', fontsize=12, fontweight='bold')
ax1.set_xlabel('Wartosc z')
ax1.set_ylabel('Gestosc prawdopodobienstwa')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Wizualizacja przedziału ufności
ax2.errorbar([1], [sample_prop], yerr=[[margin_error], [margin_error]], 
            fmt='ro', markersize=10, capsize=10, capthick=3, elinewidth=3,
            label=f'Probka: p^ = {sample_prop:.2f}')
ax2.axhline(true_p, color='blue', linestyle='--', linewidth=2, 
           label=f'Prawdziwa p = {true_p}')
ax2.axhspan(ci_lower, ci_upper, alpha=0.2, color='green', 
           label=f'95% PU: [{ci_lower:.2f}, {ci_upper:.2f}]')

ax2.set_title('95% Przedzial ufnosci dla proporcji', fontsize=12, fontweight='bold')
ax2.set_ylabel('Proporcja')
ax2.set_xlim(0.5, 1.5)
ax2.set_ylim(0, 0.6)
ax2.set_xticks([])
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# === ILUSTRACJA 4: Wzory i kluczowe pojęcia dla proporcji ===

fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')

# Główny tekst z wzorami
main_text = """ESTYMACJA PROPORCJI - KLUCZOWE WZORY

Proporcja z proby:
p^ = X/n  (gdzie X = liczba sukcesow)

Blad standardowy proporcji:
SE(p^) = √[p(1-p)/n]
W praktyce: SE(p^) = √[p^(1-p^)/n]

Rozklad probkowy proporcji (CTG):
p^ ~ N(p, p(1-p)/n)  dla duzych n

Standaryzacja proporcji z proby:
Z = (p^ - p) / SE(p^) = (p^ - p) / √[p(1-p)/n]

Przedzial ufnosci dla proporcji:
p^ ± z_alpha/2 × √[p^(1-p^)/n]

WARUNKI STOSOWANIA PRZYBLIZENIA NORMALNEGO:
• np ≥ 5  oraz  n(1-p) ≥ 5
• Lub np^ ≥ 5  oraz  n(1-p^) ≥ 5
"""

# Główne pudełko z wzorami
main_box = FancyBboxPatch((0.05, 0.25), 0.55, 0.7, boxstyle="round,pad=0.02", 
                         facecolor='lightblue', alpha=0.8, edgecolor='navy', linewidth=2)
ax.add_patch(main_box)
ax.text(0.07, 0.93, main_text, transform=ax.transAxes, fontsize=13,
        verticalalignment='top', fontfamily='monospace')

# Przykład numeryczny
example_text = f"""PRZYKLAD Z SYMULACJI:

Prawdziwa p = {true_p}
Probka: n = {sample_size}

WYNIKI:
Sukcesy: {sample_successes}
p^ = {sample_successes}/{sample_size} = {sample_prop:.3f}
SE(p^) = √[p^(1-p^)/n] = {se_prop:.3f}

95% Przedzial ufnosci:
[{ci_lower:.3f}, {ci_upper:.3f}]

Margines bledu: ±{margin_error:.3f}

SPRAWDZENIE REGULY 5:
np^ = {sample_size * sample_prop:.1f} ≥ 5 OK
n(1-p^) = {sample_size * (1-sample_prop):.1f} ≥ 5 OK

ZASTOSOWANIA:
• Sondaze opinii publicznej
• Kontrola jakosci produkcji  
• Badania kliniczne (skutecznosc leku)
• Marketing (click-through rate)
• Wybory (poparcie kandydatow)
"""

# Pudełko z przykładem
example_box = FancyBboxPatch((0.65, 0.25), 0.32, 0.7, boxstyle="round,pad=0.02", 
                           facecolor='lightyellow', alpha=0.8, edgecolor='orange', linewidth=2)
ax.add_patch(example_box)
ax.text(0.67, 0.93, example_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', fontfamily='monospace')

# Tytuł
ax.text(0.5, 0.98, 'Estymacja proporcji - matematyczne podstawy', 
        transform=ax.transAxes, fontsize=18, fontweight='bold', 
        ha='center', va='top')

# Kluczowe wnioski jako lista punktowa
conclusions_title = "KLUCZOWE WNIOSKI:"
conclusions_list = """• p^ jest nieobciazonym estymatorem p

• SE(p^) = √[p(1-p)/n] maleje z √n

• Przyblizenie normalne wymaga reguly 5

• Przedzialy ufnosci sa symetryczne

• Wieksze n → mniejszy SE → dokladniejszy szacunek"""

# Pudełko dla wniosków
conclusions_box = FancyBboxPatch((0.05, 0.02), 0.9, 0.2, boxstyle="round,pad=0.02", 
                               facecolor='lightgreen', alpha=0.8, edgecolor='green', linewidth=2)
ax.add_patch(conclusions_box)

# Tytuł wniosków
ax.text(0.07, 0.2, conclusions_title, transform=ax.transAxes, fontsize=12,
        ha='left', va='top', fontweight='bold')

# Lista wniosków
ax.text(0.07, 0.17, conclusions_list, transform=ax.transAxes, fontsize=10,
        ha='left', va='top', fontfamily='monospace')

plt.show()

print("=" * 70)
print("PODSUMOWANIE ESTYMACJI PROPORCJI")
print("=" * 70)
print(f"Prawdziwa proporcja populacji: p = {true_p}")
print(f"Wielkosc probki: n = {sample_size}")
print()
print("WYNIKI ESTYMACJI:")
print(f"Liczba sukcesow: {sample_successes}")
print(f"Proporcja probkowa: p^ = {sample_prop:.3f}")
print(f"Blad standardowy: SE(p^) = {se_prop:.3f}")
print(f"95% Przedzial ufnosci: [{ci_lower:.3f}, {ci_upper:.3f}]")
print(f"Margines bledu: ±{margin_error:.3f}")
print()
print("SPRAWDZENIE REGULY 5:")
print(f"np^ = {sample_size * sample_prop:.1f} ≥ 5: {'TAK' if sample_size * sample_prop >= 5 else 'NIE'}")
print(f"n(1-p^) = {sample_size * (1-sample_prop):.1f} ≥ 5: {'TAK' if sample_size * (1-sample_prop) >= 5 else 'NIE'}")
print()
print("WERYFIKACJA:")
czy_zawiera = ci_lower <= true_p <= ci_upper
print(f"Czy przedzial zawiera prawdziwa wartosc? {'TAK' if czy_zawiera else 'NIE'}")
print(f"Szerokosc przedzialu: {ci_upper - ci_lower:.3f}")