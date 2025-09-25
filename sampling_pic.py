# Tworzenie ilustracji koncepcji samplingu
fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Populacja - duży okrąg
population_circle = Circle((3, 4), 2.5, fill=False, linewidth=3, 
                          edgecolor='navy', linestyle='-')
ax.add_patch(population_circle)

# Punkty reprezentujące całą populację
np.random.seed(42)
pop_x = np.random.normal(3, 1.8, 800)
pop_y = np.random.normal(4, 1.8, 800)

# Filtruj punkty żeby były w kole
distances = np.sqrt((pop_x - 3)**2 + (pop_y - 4)**2)
mask = distances <= 2.3
pop_x = pop_x[mask]
pop_y = pop_y[mask]

ax.scatter(pop_x, pop_y, c='lightblue', alpha=0.6, s=15, 
          label='Populacja (N)')

# Próbka - mniejszy okrąg
sample_circle = Circle((8.5, 4), 1.2, fill=False, linewidth=3, 
                      edgecolor='darkred', linestyle='--')
ax.add_patch(sample_circle)

# Punkty reprezentujące próbkę
sample_indices = np.random.choice(len(pop_x), 50, replace=False)
sample_x = pop_x[sample_indices] + 5.5  # przesunięcie
sample_y = pop_y[sample_indices]

ax.scatter(sample_x, sample_y, c='red', alpha=0.8, s=25, 
          label='Próbka (n)')

# Strzałka od populacji do próbki
arrow = patches.FancyArrowPatch((5.2, 4), (7.5, 4),
                               arrowstyle='->', mutation_scale=20,
                               color='darkgreen', linewidth=2)
ax.add_patch(arrow)

# Etykiety
ax.text(3, 1, 'POPULACJA', fontsize=16, fontweight='bold', 
        ha='center', va='center', color='navy')
ax.text(3, 0.5, r'Parametr: $\mu, \sigma$', fontsize=12, 
        ha='center', va='center', color='navy')

ax.text(8.5, 1, 'PRÓBKA', fontsize=16, fontweight='bold', 
        ha='center', va='center', color='darkred')
ax.text(8.5, 0.5, r'Statystyka: $\bar{x}, s$', fontsize=12, 
        ha='center', va='center', color='darkred')

ax.text(6.3, 4.5, 'Losowy\nwybór', fontsize=11, fontweight='bold',
        ha='center', va='center', color='darkgreen')

# Dodanie symboli matematycznych
ax.text(3, 7, r'$N = $ populacja', fontsize=14, ha='center', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
ax.text(8.5, 7, r'$n = $ próbka', fontsize=14, ha='center',
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcoral", alpha=0.7))

# Dodanie wzoru na błąd próby
ax.text(6, 7.5, r'Błąd próby: $\bar{x} \neq \mu$', fontsize=15, 
        ha='center', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))

# Formatowanie wykresu
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 8.5)
ax.set_aspect('equal')
ax.axis('off')

# Tytuł
plt.suptitle('Koncepcja próbkowania (Sampling)', fontsize=20, 
             fontweight='bold', y=0.95)
plt.figtext(0.5, 0.02, 'Od populacji do próbki: podstawy wnioskowania statystycznego', 
            ha='center', fontsize=12, style='italic')

plt.tight_layout()
plt.show()