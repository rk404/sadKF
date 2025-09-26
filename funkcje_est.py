import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# === FUNKCJE DO ESTYMACJI ŚREDNIEJ ===

def estimate_mean(data, confidence_level=0.95):
    """
    Estymacja średniej z przedziałem ufności
    
    Parameters:
    -----------
    data : array-like
        Dane próbkowe
    confidence_level : float
        Poziom ufności (domyślnie 0.95)
    
    Returns:
    --------
    dict : słownik z wynikami estymacji
    """
    data = np.array(data)
    n = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)  # próbkowe odchylenie standardowe
    se = std / np.sqrt(n)  # błąd standardowy średniej
    
    alpha = 1 - confidence_level
    
    # Wybór rozkładu (t-Student dla małych próbek lub nieznana σ)
    if n < 30:
        t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
        margin_error = t_critical * se
        distribution_used = f't({n-1})'
    else:
        z_critical = stats.norm.ppf(1 - alpha/2)
        margin_error = z_critical * se
        distribution_used = 'N(0,1)'
    
    ci_lower = mean - margin_error
    ci_upper = mean + margin_error
    
    return {
        'sample_size': n,
        'mean': mean,
        'std': std,
        'standard_error': se,
        'confidence_level': confidence_level,
        'margin_error': margin_error,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'distribution_used': distribution_used
    }

def sample_size_for_mean(std, margin_error, confidence_level=0.95):
    """
    Oblicza minimalną wielkość próby dla zadanego marginesu błędu średniej
    
    Parameters:
    -----------
    std : float
        Odchylenie standardowe (próbkowe lub oszacowane)
    margin_error : float
        Żądany margines błędu
    confidence_level : float
        Poziom ufności
    
    Returns:
    --------
    int : minimalna wielkość próby
    """
    alpha = 1 - confidence_level
    z_critical = stats.norm.ppf(1 - alpha/2)
    
    n = (z_critical * std / margin_error) ** 2
    return int(np.ceil(n))

def plot_mean_confidence(data, confidence_level=0.95, title="Przedział ufności dla średniej"):
    """
    Wizualizuje średnią z przedziałem ufności
    """
    results = estimate_mean(data, confidence_level)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Histogram danych
    ax1.hist(data, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    ax1.axvline(results['mean'], color='red', linestyle='--', linewidth=2, 
                label=f"Średnia = {results['mean']:.3f}")
    ax1.set_xlabel('Wartości')
    ax1.set_ylabel('Częstość')
    ax1.set_title('Rozkład danych')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Przedział ufności
    ax2.errorbar([1], [results['mean']], 
                yerr=[[results['margin_error']], [results['margin_error']]], 
                fmt='ro', markersize=10, capsize=10, capthick=3, elinewidth=3,
                label=f"Średnia = {results['mean']:.3f}")
    ax2.axhspan(results['ci_lower'], results['ci_upper'], alpha=0.2, color='green',
                label=f"{confidence_level*100}% PU: [{results['ci_lower']:.3f}, {results['ci_upper']:.3f}]")
    ax2.set_ylabel('Wartość')
    ax2.set_xlim(0.5, 1.5)
    ax2.set_xticks([])
    ax2.set_title(f"{confidence_level*100}% Przedział ufności")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return results

# === FUNKCJE DO ESTYMACJI WARIANCJI ===

def estimate_variance(data, confidence_level=0.95):
    """
    Estymacja wariancji z przedziałem ufności (rozkład chi-kwadrat)
    
    Parameters:
    -----------
    data : array-like
        Dane próbkowe
    confidence_level : float
        Poziom ufności
    
    Returns:
    --------
    dict : słownik z wynikami estymacji
    """
    data = np.array(data)
    n = len(data)
    sample_var = np.var(data, ddof=1)  # próbkowa wariancja
    sample_std = np.sqrt(sample_var)
    
    alpha = 1 - confidence_level
    df = n - 1
    
    # Wartości krytyczne chi-kwadrat
    chi2_lower = stats.chi2.ppf(alpha/2, df)
    chi2_upper = stats.chi2.ppf(1 - alpha/2, df)
    
    # Przedział ufności dla wariancji
    ci_var_lower = (df * sample_var) / chi2_upper
    ci_var_upper = (df * sample_var) / chi2_lower
    
    # Przedział ufności dla odchylenia standardowego
    ci_std_lower = np.sqrt(ci_var_lower)
    ci_std_upper = np.sqrt(ci_var_upper)
    
    return {
        'sample_size': n,
        'degrees_freedom': df,
        'sample_variance': sample_var,
        'sample_std': sample_std,
        'confidence_level': confidence_level,
        'chi2_lower': chi2_lower,
        'chi2_upper': chi2_upper,
        'ci_var_lower': ci_var_lower,
        'ci_var_upper': ci_var_upper,
        'ci_std_lower': ci_std_lower,
        'ci_std_upper': ci_std_upper
    }

def plot_variance_confidence(data, confidence_level=0.95):
    """
    Wizualizuje wariancję z przedziałem ufności
    """
    results = estimate_variance(data, confidence_level)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Histogram danych z informacją o wariancji
    ax1.hist(data, bins=20, alpha=0.7, color='lightcoral', edgecolor='black')
    ax1.axvline(np.mean(data), color='blue', linestyle='--', linewidth=2, 
                label=f"Średnia = {np.mean(data):.3f}")
    ax1.set_xlabel('Wartości')
    ax1.set_ylabel('Częstość')
    ax1.set_title(f'Dane (s² = {results["sample_variance"]:.3f})')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Przedział ufności dla wariancji
    ax2.errorbar([1], [results['sample_variance']], 
                yerr=[[results['sample_variance'] - results['ci_var_lower']], 
                      [results['ci_var_upper'] - results['sample_variance']]], 
                fmt='ro', markersize=10, capsize=10, capthick=3, elinewidth=3,
                label=f"s² = {results['sample_variance']:.3f}")
    ax2.axhspan(results['ci_var_lower'], results['ci_var_upper'], alpha=0.2, color='green',
                label=f"{confidence_level*100}% PU: [{results['ci_var_lower']:.3f}, {results['ci_var_upper']:.3f}]")
    ax2.set_ylabel('Wariancja')
    ax2.set_xlim(0.5, 1.5)
    ax2.set_xticks([])
    ax2.set_title(f"{confidence_level*100}% Przedział ufności dla wariancji")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return results

# === FUNKCJE DO ESTYMACJI PROPORCJI ===

def estimate_proportion(data, confidence_level=0.95):
    """
    Estymacja proporcji z przedziałem ufności
    
    Parameters:
    -----------
    data : array-like
        Dane binarne (0/1, True/False) lub kategorialne
    confidence_level : float
        Poziom ufności
    
    Returns:
    --------
    dict : słownik z wynikami estymacji
    """
    data = np.array(data)
    
    # Konwersja na format binarny jeśli potrzeba
    if data.dtype == bool:
        successes = np.sum(data)
    elif np.all(np.isin(data, [0, 1])):
        successes = np.sum(data)
    else:
        # Dla danych kategorialnych - licząc najczęstszą kategorię
        unique_vals = np.unique(data)
        if len(unique_vals) == 2:
            successes = np.sum(data == unique_vals[1])  # druga kategoria jako "sukces"
        else:
            raise ValueError("Dane muszą być binarne lub logiczne")
    
    n = len(data)
    p_hat = successes / n
    
    # Sprawdzenie reguły 5
    rule5_check = (n * p_hat >= 5) and (n * (1 - p_hat) >= 5)
    
    if not rule5_check:
        print(f"UWAGA: Reguła 5 nie jest spełniona (np̂={n*p_hat:.1f}, n(1-p̂)={n*(1-p_hat):.1f})")
        print("Przybliżenie normalne może być niedokładne!")
    
    # Błąd standardowy
    se = np.sqrt(p_hat * (1 - p_hat) / n)
    
    alpha = 1 - confidence_level
    z_critical = stats.norm.ppf(1 - alpha/2)
    margin_error = z_critical * se
    
    ci_lower = max(0, p_hat - margin_error)  # proporcja nie może być ujemna
    ci_upper = min(1, p_hat + margin_error)  # proporcja nie może być > 1
    
    return {
        'sample_size': n,
        'successes': successes,
        'failures': n - successes,
        'proportion': p_hat,
        'standard_error': se,
        'confidence_level': confidence_level,
        'z_critical': z_critical,
        'margin_error': margin_error,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper,
        'rule5_satisfied': rule5_check,
        'np_hat': n * p_hat,
        'n_1minus_p_hat': n * (1 - p_hat)
    }

def sample_size_for_proportion(p_estimate, margin_error, confidence_level=0.95):
    """
    Oblicza minimalną wielkość próby dla proporcji
    
    Parameters:
    -----------
    p_estimate : float
        Wstępne oszacowanie proporcji (użyj 0.5 dla maksymalnej wielkości próby)
    margin_error : float
        Żądany margines błędu
    confidence_level : float
        Poziom ufności
    
    Returns:
    --------
    int : minimalna wielkość próby
    """
    alpha = 1 - confidence_level
    z_critical = stats.norm.ppf(1 - alpha/2)
    
    n = (z_critical**2 * p_estimate * (1 - p_estimate)) / (margin_error**2)
    return int(np.ceil(n))

def plot_proportion_confidence(data, confidence_level=0.95):
    """
    Wizualizuje proporcję z przedziałem ufności
    """
    results = estimate_proportion(data, confidence_level)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Wykres kołowy dla proporcji
    labels = ['Sukcesy', 'Porażki']
    sizes = [results['successes'], results['failures']]
    colors = ['lightgreen', 'lightcoral']
    
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.set_title(f'Proporcja w próbie\np̂ = {results["proportion"]:.3f} ({results["successes"]}/{results["sample_size"]})')
    
    # Przedział ufności
    ax2.errorbar([1], [results['proportion']], 
                yerr=[[results['margin_error']], [results['margin_error']]], 
                fmt='go', markersize=10, capsize=10, capthick=3, elinewidth=3,
                label=f"p̂ = {results['proportion']:.3f}")
    ax2.axhspan(results['ci_lower'], results['ci_upper'], alpha=0.2, color='green',
                label=f"{confidence_level*100}% PU: [{results['ci_lower']:.3f}, {results['ci_upper']:.3f}]")
    ax2.set_ylabel('Proporcja')
    ax2.set_xlim(0.5, 1.5)
    ax2.set_ylim(0, 1)
    ax2.set_xticks([])
    ax2.set_title(f"{confidence_level*100}% Przedział ufności dla proporcji")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return results

# === FUNKCJE UNIWERSALNE ===

def summary_statistics(data):
    """
    Podstawowe statystyki opisowe
    """
    data = np.array(data)
    
    return {
        'count': len(data),
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': stats.mode(data, keepdims=True)[0][0],
        'std': np.std(data, ddof=1),
        'variance': np.var(data, ddof=1),
        'min': np.min(data),
        'max': np.max(data),
        'q25': np.percentile(data, 25),
        'q75': np.percentile(data, 75),
        'iqr': np.percentile(data, 75) - np.percentile(data, 25),
        'skewness': stats.skew(data),
        'kurtosis': stats.kurtosis(data)
    }

def compare_estimators(data, parameter_type='mean'):
    """
    Porównuje różne poziomy ufności dla danego parametru
    """
    confidence_levels = [0.90, 0.95, 0.99]
    results = []
    
    for conf in confidence_levels:
        if parameter_type == 'mean':
            result = estimate_mean(data, conf)
        elif parameter_type == 'variance':
            result = estimate_variance(data, conf)
        elif parameter_type == 'proportion':
            result = estimate_proportion(data, conf)
        else:
            raise ValueError("parameter_type musi być 'mean', 'variance' lub 'proportion'")
        
        results.append({
            'confidence_level': conf,
            'margin_error': result.get('margin_error', 
                                     result.get('ci_var_upper', 0) - result.get('sample_variance', 0) if parameter_type == 'variance' else 0),
            'ci_width': (result.get('ci_upper', result.get('ci_var_upper', 0)) - 
                        result.get('ci_lower', result.get('ci_var_lower', 0)))
        })
    
    return pd.DataFrame(results)

# === PRZYKŁAD UŻYCIA ===

if __name__ == "__main__":
    # Generowanie przykładowych danych
    np.random.seed(42)
    
    # Dane do estymacji średniej
    sleep_data = np.random.normal(7.5, 1.2, 100)  # godziny snu
    
    # Dane do estymacji proporcji
    buy_gadgets = np.random.binomial(1, 0.35, 200)  # chęć kupna gadżetów
    
    print("=== ESTYMACJA ŚREDNIEJ ===")
    mean_results = estimate_mean(sleep_data)
    print(f"Średnia: {mean_results['mean']:.3f}")
    print(f"95% Przedział ufności: [{mean_results['ci_lower']:.3f}, {mean_results['ci_upper']:.3f}]")
    print(f"Margines błędu: ±{mean_results['margin_error']:.3f}")
    
    print("\n=== ESTYMACJA WARIANCJI ===")
    var_results = estimate_variance(sleep_data)
    print(f"Wariancja próbkowa: {var_results['sample_variance']:.3f}")
    print(f"95% PU dla wariancji: [{var_results['ci_var_lower']:.3f}, {var_results['ci_var_upper']:.3f}]")
    
    print("\n=== ESTYMACJA PROPORCJI ===")
    prop_results = estimate_proportion(buy_gadgets)
    print(f"Proporcja: {prop_results['proportion']:.3f}")
    print(f"95% Przedział ufności: [{prop_results['ci_lower']:.3f}, {prop_results['ci_upper']:.3f}]")
    print(f"Reguła 5 spełniona: {prop_results['rule5_satisfied']}")
    
    print("\n=== WIELKOŚĆ PRÓBY ===")
    n_mean = sample_size_for_mean(std=1.2, margin_error=0.2)
    n_prop = sample_size_for_proportion(p_estimate=0.5, margin_error=0.05)
    print(f"Wielkość próby dla średniej (ME=0.2): {n_mean}")
    print(f"Wielkość próby dla proporcji (ME=0.05): {n_prop}")