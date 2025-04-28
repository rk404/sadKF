# Latex - ściąga

===========

Cheatsheet dla LaTexa, używający Markdown jako język znaczników dla wszystkich, których Latex trochę przeraża :-) a potrzebują wzorków w swoich dokumentach technicznych z analizy danych.

Więcej opisu znajdziecie tutaj: [https://tug.ctan.org/info/short-math-guide/short-math-guide.pdf](https://tug.ctan.org/info/short-math-guide/short-math-guide.pdf).

Dodatkowo, na repo załączam ściągawkę w wersji do wydruku A4 w PDF tutaj: [latexsheet-a4.pdf](https://github.com/kflisikowsky/sad/blob/main/latexsheet-a4.pdf)

## Przykładowe wyrażenia / funkcje

============================

Ty wprowadzasz             | Zrenderowane będzie wyglądało tak        |
-----------------:|----------------:|
`$a = b + c − d$` | $a = b + c − d$ |
`$\sqrt{?\frac{\pi}{2}}$` | $\sqrt{\frac{\pi}{2}}$ |
`$y = a x_1^2 + b x_2 + c$` | $y = a x_1^2 + b x_2 + c$ |

## Znaki specjalne / Symbole

============================

### Łacińskie - bez kropek:

`\imath` $\rightarrow$ $\imath$,
`\jmath` $\rightarrow$ $\jmath$

##### Daszek:  

`\hat{\imath}`  $\rightarrow$ $\hat{\imath}$,
`\hat{\jmath}`  $\rightarrow$ $\hat{\jmath}$

### Alfabet grecki

##### Wielkie litery:

LaTex      |   | LaTex    |   |
----------:|--:|---------:|--:|
`\Gamma`   | Γ | `\Delta` | ∆ |
`\Lambda`  | Λ | `\Phi`   | Φ |
`\Pi`      | Π | `\Psi`   | Ψ |
`\Sigma`   | Σ | `\Theta` | Θ |
`\Upsilon` | Υ | `\Xi`    | Ξ |
`\Omega`   | Ω |          |   |

##### Małe litery:

LaTex      |   | LaTex     |   |
----------:|--:|----------:|--:|
`\alpha`   | α | `\nu`     | ν |
`\beta`    | β | `\kappa`  | κ |
`\gamma`   | γ | `\lambda` | λ |
`\delta`   | δ |  `\mu`    | µ |    
`\epsilon` | ϵ | `\zeta`   | ζ |
`\eta`     | η | `\theta`  | θ |
`\iota`    | ι | `\xi`     | ξ |
`\pi`      | π | `\rho`    | ρ |
`\sigma`   | σ | `\tau`    | τ |
`\upsilon` | υ | `\phi`    | φ |
`\chi`     | χ | `\psi`    | ψ |
`\omega`   | ω |           |   |

##### Inne

LaTex       |   | LaTex       |   |
-----------:|---|------------:|--:|
`\digamma`  | ϝ | `varepsilon`| ε       |
`\varkappa` | ϰ | `\varphi`   | ϕ       |
`\varpi`    | ϖ | `\varrho`   | ϱ       |
`\varsigma` | ς | `\vartheta` | ϑ       |
`\eth`      | ð | `\hbar`     | $\hbar$ |


### Inne

#### Inne symbole

LaTex         |   | LaTex            |   |
-------------:|---|-----------------:|--:|
`\partial`    | ∂ | `\infty`         | ∞ |
`\wedge`      | ∧ | `\vee`           | ∨ |
`\neg` `\not` | ¬ |                  |   |
`\bot`        | ⊥ | `\top`           | ⊤ |
`\nabla`      | ∇ | `\varnothing`    | ∅ |
`\angle`      | ∠ | `\measuredangle` | ∡ |
`\surd`       | √ | `\forall`        | ∀ |
`\exists`     | ∃ | `\nexists`       | ∄ |

#### Wyrażenia logiczne

LaTex             |   | LaTex              |          |
-----------------:|---|-------------------:|---------:|
`\hookrightarrow` | ↪      | `\Rightarrow`     | ⇒         |
`\rightarrow`     | →      | `\Leftrightarrow` | ⇔         |
`\nrightarrow`    | ↛      | `\mapsto`         | $\mapsto$ |
`\geq`            | ≥      | `\leq`            | ≤         |
`\equiv`          | ≡      | `\sim`            | ∼         |
`\gg`             | ≫      | `\ll`            | ≪          |
`\subset`          | ⊂     | `\subseteq`     | ⊆           |
`\in`             | ∈      | `\notin`         | ∉          |
`\mid`            | $\mid$ | `\propto`        | ∝          |
`\perp`            | ⊥     | ` \parallel`     | ∥          |
`\vartriangle`     | $\vartriangle$

#### Operatory binarne

LaTex        |   | LaTex  |   |
------------:|---|-------:|--:|
`\wedge`     | ∧ | `\vee` | ∨ |
`\neg``\not` | ¬ |        |   |

#### Operatory kumulacji

LaTex     |           | LaTex       |             |
---------:|-----------|------------:|------------:|
`\int`    | ∫         | `\iint`     | $\iint$     |
`\iiint`  | $\iiint$  | `\idotsint` | $\idotsint$ |
`\prod`   | $\prod$   | `\sum`      | $\sum$      |
`\bigcup` | $\bigcup$ | `\bigcap`   | $\bigcap$   |

#### Operatory nazwane (matematyczne)

- $\arccos$,
- $\arcsin$, 
- $\arctan$, 
- $\arg$, 
- $\cos$, 
- $\cosh$, 
- $\cot$, 
- $\coth$, 
- $\deg$, 
- $\det$, 
- $\dim$, 
- $\exp$, 
- $\gcd$, 
- $\hom$, 
- $\inf$, 
- $\injlim$, 
- $\lg$, 
- $\lim$, 
- $\liminf$, 
- $\limsup$, 
- $\ln$, 
- $\log$, 
- $\max$, 
- $\min$, 
- $\Pr$, 
- $\projlim$, 
- $\sec$,  
- $\sin$, 
- $\sinh$, 
- $\sup$ 

