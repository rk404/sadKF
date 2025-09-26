# === ILUSTRACJA 4: Wzory i kluczowe pojęcia ===

fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')

# Główny tekst z wzorami
main_text = """ESTYMACJA WARIANCJI - KLUCZOWE WZORY

Wariancja probkowa (nieobciazona):
s^2 = Σ(x_i - x̄)^2 / (n-1)

Rozklad probkowy wariancji:
(n-1)s^2 / σ^2 ~ chi^2(n-1)

gdzie chi^2(n-1) to rozklad chi-kwadrat z (n-1) stopniami swobody

Przedzial ufnosci dla wariancji (1-alpha):
[(n-1)s^2 / chi^2_alpha/2,n-1  ,  (n-1)s^2 / chi^2_1-alpha/2,n-1]

Wlasnosci estymatora s^2:
• E[s^2] = σ^2 (nieobciazony)
• Var(s^2) = 2σ^4/(n-1) (dla rozkladu normalnego)

ROZKLAD CHI-KWADRAT:
• Gestosc: f(x) = (1/2^(k/2)Γ(k/2)) x^(k/2-1) e^(-x/2)
• E[chi^2] = k (stopnie swobody)
• Var(chi^2] = 2k
• Tylko wartosci nieujemne
"""

# Główne pudełko z wzorami - zmniejszone
main_box = FancyBboxPatch((0.05, 0.25), 0.55, 0.7, boxstyle="round,pad=0.02", 
                         facecolor='lightblue', alpha=0.8, edgecolor='navy', linewidth=2)
ax.add_patch(main_box)
ax.text(0.07, 0.93, main_text, transform=ax.transAxes, fontsize=13,
        verticalalignment='top', fontfamily='monospace')

# Przykład numeryczny - przesunięty wyżej
example_text = f"""PRZYKLAD Z SYMULACJI:

Prawdziwa σ^2 = {true_var}
Probka: n = {sample_size}
Stopnie swobody: df = {df}

WYNIKI:
s^2 = {sample_var:.1f}
95% Przedzial ufnosci:
[{ci_lower:.1f}, {ci_upper:.1f}]

Wartosci krytyczne chi^2:
chi^2_0.025,24 = {chi2_lower:.2f}
chi^2_0.975,24 = {chi2_upper:.2f}

INTERPRETACJA:
Z 95% pewnoscia prawdziwa 
wariancja populacji miesci sie 
w przedziale [{ci_lower:.1f}, {ci_upper:.1f}]

Rzeczywiscie: {ci_lower:.1f} ≤ 100 ≤ {ci_upper:.1f} ✓

ZASTOSOWANIA:
• Kontrola jakosci produkcji
• Ocena ryzyka inwestycyjnego  
• Analiza stabilnosci procesow
• Testy homoskedastycznosci
"""

# Pudełko z przykładem - przesunięte wyżej
example_box = FancyBboxPatch((0.65, 0.25), 0.32, 0.7, boxstyle="round,pad=0.02", 
                           facecolor='lightyellow', alpha=0.8, edgecolor='orange', linewidth=2)
ax.add_patch(example_box)
ax.text(0.67, 0.93, example_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', fontfamily='monospace')

# Tytuł
ax.text(0.5, 0.98, 'Estymacja wariancji i rozklad chi-kwadrat', 
        transform=ax.transAxes, fontsize=18, fontweight='bold', 
        ha='center', va='top')

# Kluczowe wnioski jako lista punktowa - ZMNIEJSZONE I POPRAWIONE
conclusions_title = "KLUCZOWE WNIOSKI:"
conclusions_list = """• s^2 jest nieobciazonym estymatorem σ^2

• (n-1)s^2/σ^2 ma rozklad chi^2(n-1)

• Przedzialy ufnosci sa asymetryczne

• Wymaga normalnosci populacji

• Szerszy przedzial dla mniejszych probek"""

# Zmniejszone pudełko dla wniosków
conclusions_box = FancyBboxPatch((0.05, 0.02), 0.9, 0.2, boxstyle="round,pad=0.02", 
                               facecolor='lightgreen', alpha=0.8, edgecolor='green', linewidth=2)
ax.add_patch(conclusions_box)

# Tytuł wniosków
ax.text(0.07, 0.2, conclusions_title, transform=ax.transAxes, fontsize=12,
        ha='left', va='top', fontweight='bold')

# Lista wniosków - mniejszy font i lepsze pozycjonowanie
ax.text(0.07, 0.17, conclusions_list, transform=ax.transAxes, fontsize=10,
        ha='left', va='top', fontfamily='monospace')

plt.show()