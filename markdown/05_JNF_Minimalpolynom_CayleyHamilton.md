# 5. Jordan-Normalform, Minimalpolynom & Cayley-Hamilton

> ⚡ **PRIORITÄT 2 – Hier hast du 27/50 Punkte verloren (Aufgaben 1 + 4)!**

> [!INFO] Worum geht es hier? – Einfach erklärt
>
> Nicht jede Matrix lässt sich diagonalisieren – manchmal gibt es einfach nicht genug Eigenvektoren. Für solche Matrizen gibt es die **Jordan-Normalform (JNF)**: eine fast-diagonale Struktur, in der auf der Hauptdiagonale die Eigenwerte stehen und direkt darüber manchmal Einsen. Diese Einsen zeigen an, wo ein Eigenwert „nicht genug" Eigenvektoren hat. Je größer ein Jordan-Block ist, desto weiter entfernt ist die Matrix vom Diagonalisierbaren.
>
> Die JNF ist eine Art Röntgenbild der Matrix. Aus ihr kannst du sofort fast alles ablesen: Eigenwerte (die Diagonaleinträge), algebraische Vielfachheiten (Summe der Blockgrößen pro Eigenwert), geometrische Vielfachheiten (Anzahl der Blöcke pro Eigenwert), das Minimalpolynom, die Determinante und ob die Matrix diagonalisierbar ist. Es lohnt sich enorm, die Tabelle auf dieser Seite sicher zu beherrschen.
>
> Das **Minimalpolynom** ist das kleinste Polynom, das die Matrix zu Null macht – wenn du es in die Matrix einsetzt, kommt die Nullmatrix raus. Es hängt eng mit der JNF zusammen: Der Exponent jedes Eigenwerts im Minimalpolynom entspricht der Größe des größten Jordan-Blocks zu diesem Eigenwert. Der Satz von **Cayley-Hamilton** sagt, dass jede Matrix ihr eigenes charakteristisches Polynom erfüllt – das heißt, wenn du das char. Polynom in die Matrix einsetzt, kommt immer Null raus.
>
> Das **Matrixexponential** $\exp(A)$ ist das Pendant zur Exponentialfunktion für Matrizen und taucht bei Differentialgleichungen auf: Die Lösung von $\dot{x}(t) = Ax(t)$ ist $x(t) = \exp(tA) x_0$. Für die Berechnung hilft es, zu wissen, ob die Matrix idempotent ist ($A^2 = A$), denn dann vereinfacht sich die Reihe drastisch.
>
> **Für die Nachklausur:** Aufgabe 1 (JNF ablesen: 19/30) und Aufgabe 4 (Matrixexponential: 4/20) machten zusammen 50 Punkte aus. In Aufgabe 1 musst du die JNF blitzschnell „lesen" können – char. Polynom, Minimalpolynom, Eigenräume, Determinante, alles direkt ablesen. In Aufgabe 4 war der Schlüssel Cayley-Hamilton: Zeige $A^2 = A$, dann per Induktion $A^m = A$, und damit vereinfacht sich $\exp(A) = I + (e-1)A$. Übe beide Aufgabentypen, bis sie sitzen!

## 5.1 Jordan-Normalform (JNF)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Hier wird's manchmal unübersichtlich. Die JNF ist das Notpflaster der Linearen Algebra, wenn eine Matrix einfach nicht genug Eigenvektoren hat, um sie sauber zu diagonalisieren. Wir retten, was zu retten ist.
</blockquote>
</details>



> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 7, AP 1: Vorbereitungen auf den JNF-Existenzsatz](Uebungszettel_Originale.html#aufgabenpaket-1-vorbereitungen-auf-den-jnf-existenzsatz)
> - [Übungsblatt 7, AP 4: Berechnung einer Jordan-Normalform](Uebungszettel_Originale.html#aufgabenpaket-4-berechnung-einer-jordan-normalform)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Hier wird's manchmal unübersichtlich. Die JNF ist das Notpflaster der Linearen Algebra, wenn eine Matrix einfach nicht genug Eigenvektoren hat, um sie sauber zu diagonalisieren. Wir retten, was zu retten ist.
</blockquote>
</details>


### Jordan-Block

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Warum stehen da Einsen über der Diagonale? Sie bedeuten geometrisch: Die Matrix greift den Vektor, und anstatt ihn nur zu strecken, schubst sie ihn anteilig in die Richtung des vorherigen Vektors. Das erzeugt eine Verkettung (Jordan-Kette).
</blockquote>
</details>

Ein **Jordan-Block** der Größe $k$ zum Eigenwert $\lambda$:

$$J_k(\lambda) = \begin{pmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & & \ddots & \ddots & \vdots \\ 0 & \cdots & & \lambda & 1 \\ 0 & \cdots & & 0 & \lambda \end{pmatrix}$$

### Jordan-Normalform

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein hübscher Block-Baukasten. Wir sortieren die Matrix so um, dass die Blöcke als geschlossene Ketten-Einheiten auf der Diagonale rumhängen.
</blockquote>
</details>

Jede Matrix $A \in \mathbb{C}^{n \times n}$ ist ähnlich zu einer **Blockdiagonalmatrix** aus Jordan-Blöcken:

$$J = \begin{pmatrix} J_{k_1}(\lambda_1) & & \\ & J_{k_2}(\lambda_2) & \\ & & \ddots \end{pmatrix}$$

Es gibt eine invertierbare Matrix $V$ mit $A = VJV^{-1}$.

### Was man aus der JNF ablesen kann

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Anzahl der Blöcke pro Eigenwert = Geometrische Vielfachheit. Summe der Block-Dimensionen = Algebraische Vielfachheit. Det(A) = Alles auf der Diagonale multiplizieren. Spur = Alles addieren.
</blockquote>
</details>


| Information | Wie ablesen |
|-------------|-------------|
| Eigenwerte | Diagonaleinträge von $J$ |
| Algebraische VF von $\lambda$ | Summe der Größen aller Blöcke zu $\lambda$ |
| Geometrische VF von $\lambda$ | **Anzahl** der Blöcke zu $\lambda$ |
| Char. Polynom | $\chi_A(\lambda) = \prod_i (\lambda_i - \lambda)$ aus Diag. |
| Minimalpolynom | Produkt $\prod (\lambda - \lambda_i)^{m_i}$ wobei $m_i$ = Größe des **größten** Blocks zu $\lambda_i$ |
| Diagonalisierbar? | Ja $\iff$ alle Blöcke haben Größe 1 |
| Determinante | Produkt der Diagonaleinträge |

## 5.2 Klausuraufgabe 1 – Analyse der JNF

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Der absolute Klassiker. Ein 2x2 Block und zwei 1x1 Blöcke, alle zu Eigenwert -1. Alles, aber wirklich alles, lässt sich durch Hinsehen lösen.
</blockquote>
</details>


**Gegeben:**
$$J = \begin{pmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & -1 & 1 & 0 \\ 0 & 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0 & -1 \end{pmatrix}$$

**Struktur:**
- Block 1: $J_1(1)$ → Eigenwert 1, Größe 1
- Block 2: $J_1(1)$ → Eigenwert 1, Größe 1
- Block 3: $J_2(-1)$ → Eigenwert -1, Größe 2
- Block 4: $J_1(-1)$ → Eigenwert -1, Größe 1

### 1.1: Charakteristisches Polynom

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Bestimmt sich durch die gesamte Diagonale: Da die -1 dort genau viermal steht, ist das Polynom simpel $(\lambda - (-1))^4$.
</blockquote>
</details>

$$\chi_A(\lambda) = (\lambda - 1)^2 (\lambda + 1)^3$$

(alg. VF von 1 ist 2, alg. VF von -1 ist 3)

### 1.2: Minimalpolynom

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Bestimmt sich nur durch den GRÖSSTEN Block pro Eigenwert. Da der größte Block 2x2 ist, hat die Klammer den Exponenten 2.
</blockquote>
</details>

$$\mu_A(\lambda) = (\lambda - 1)(\lambda + 1)^2$$

**Begründung:** Der größte Jordan-Block zu EW 1 hat Größe 1, der größte zu EW -1 hat Größe 2.

### 1.3: Eigenraum zum Eigenwert -1

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Wie groß ist der Eigenraum (geo. VF)? So viele linear unabhängige Eigenvektoren wie wir Jordan Blöcke haben. Bei 3 Blöcken ist die Dimension 3.
</blockquote>
</details>

Die Eigenvektoren zum EW -1 sind die Spalten von $V$, die dem **Anfang** jedes Jordan-Blocks zu -1 entsprechen.

$E_{-1} = \text{span}(v_3, v_5)$ (Spalte 3 und 5 von $V$, da Block 3 bei Spalte 3 beginnt und Block 4 bei Spalte 5)

**Begründung:** $Av_3 = -v_3$ und $Av_5 = -v_5$ (aus $AV = VJ$ und der Struktur von $J$)

### 1.4: Geometrische Vielfachheiten

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Geo = 3 (wegen 3 Blöcken). Alg = 4 (da die Nullstelle 4-mal auf der Diagonale vorkommt).
</blockquote>
</details>

- geo. VF(1) = 2 (zwei Blöcke der Größe 1)
- geo. VF(-1) = 2 (zwei Blöcke: einer Größe 2, einer Größe 1)

### 1.5: Hauptvektor erster Stufe

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein Vektor der 'zweiten Reihe'. Er wird durch die Matrix erst in den Eigenvektor reingerutscht und braucht zwei Zyklen $(A-\lambda I)^2$, um komplett die Null zu treffen.
</blockquote>
</details>

$v_4$ ist ein **Hauptvektor** erster Stufe zum EW $-1$ (auch verallgemeinerter Eigenvektor).

Er erfüllt: $(A - (-1)I)v_4 = (A + I)v_4 = v_3 \neq 0$, aber $(A + I)^2 v_4 = 0$.

### 1.6: Determinante

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Einfach ALLE Diagonaleinträge multiplizieren: $(-1) \cdot (-1) \cdot (-1) \cdot (-1) = 1$.
</blockquote>
</details>

$$\det(A) = \det(VJV^{-1}) = \det(V)\det(J)\det(V^{-1}) = \det(J)$$
$$\det(J) = 1 \cdot 1 \cdot (-1) \cdot (-1) \cdot (-1) = -1$$

### 1.7: Volumentreu?

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ja! Wenn $|\det(A)| = 1$, bleibt das Volumen im Raum unverändert. Die Matrix quetscht das Volumen in der einen Richtung, dehnt es aber exakt kompensierend in einer anderen aus.
</blockquote>
</details>

$|{\det(A)}| = |-1| = 1$ → **Ja**, die Abbildung ist volumentreu.

### 1.8: Orientierungserhaltend?

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Determinante ist +1, also bleibt das räumliche Koordinatensystem wie es ist ('Rechts bleibt Rechts'). Bei -1 wäre das Volumen gleich geblieben, aber der Raum wäre invertiert / gespiegelt worden.
</blockquote>
</details>

$\det(A) = -1 < 0$ → **Nein**, die Abbildung ist **nicht** orientierungserhaltend.

**Begründung:** Eine lineare Abbildung ist orientierungserhaltend $\iff \det(A) > 0$.

### 1.9: Kann $A$ symmetrisch sein?

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Der Lieblingstrick für Zusatzaufgaben. Gemäß dem Spektralsatz sind symmetrische reelle Matrizen IMMER komplett diagonalisierbar! A hat aber einen 2er Jordanblock (nicht diagonalisierbar), also ist es völlig unmöglich, dass sie ursprünglich symmetrisch war!
</blockquote>
</details>

**Nein.**

**Begründung:** Symmetrische reelle Matrizen sind immer diagonalisierbar (Spektralsatz). Aber $A$ hat einen Jordan-Block der Größe 2 (zu EW -1), ist also **nicht** diagonalisierbar. Widerspruch!

## 5.3 Haupträume und Hauptvektoren

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Wenn dir echte Eigenvektoren fehlen, nimmst du Hauptvektoren als Lückenfüller für deine Basis. Das sind Vektoren, die eine Reaktionskette bilden.
</blockquote>
</details>


### Hauptraum

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Zusammenfassung aller Hauptvektoren, die zu einem Eigenwert gehören. Jeder Eigenraum wohnt im Inneren seines Hauptraumes.
</blockquote>
</details>

$$H_\lambda = \ker(A - \lambda I)^{m_\lambda}$$

wobei $m_\lambda$ = algebraische Vielfachheit von $\lambda$.

### Hauptvektor der Stufe $k$

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Er wird durch die Anwendung von $(A - \lambda I)$ erst auf den k-1'ten Vektor verwandelt, dann auf den k-2'ten... und landet exakt nach der k-ten Anwendung im Nullraum.
</blockquote>
</details>

$v$ ist Hauptvektor der Stufe $k$ zum EW $\lambda$, wenn:
$$(A - \lambda I)^k v = 0 \quad \text{aber} \quad (A - \lambda I)^{k-1} v \neq 0$$

- Stufe 0: Nullvektor
- Stufe 1: Eigenvektor (im eigentlichen Sinn, wenn $k=1$ und $(A-\lambda I)v = 0$)
- Stufe $\geq 2$: verallgemeinerter Eigenvektor

> **Achtung Notation:** Manchmal wird "Hauptvektor erster Stufe" für den verallgemeinerten Eigenvektor mit $(A-\lambda I)v \neq 0$ aber $(A-\lambda I)^2 v = 0$ verwendet. In der Klausur war $v_4$ so einer.

## 5.4 Minimalpolynom

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Das ist das 'effizienteste' Polynom. Wenn du in dieses Polynom deine Matrix A einsetzt, kommt am Ende garantiert die Nullmatrix heraus.
</blockquote>
</details>



> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 8, AP 1: Nullstellen von Polynomen](Uebungszettel_Originale.html#aufgabenpaket-1-nullstellen-von-polynomen)
> - [Übungsblatt 8, AP 2: Begleitmatrix eines Polynoms](Uebungszettel_Originale.html#aufgabenpaket-2-begleitmatrix-eines-polynoms)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Das ist das 'effizienteste' Polynom. Wenn du in dieses Polynom deine Matrix A einsetzt, kommt am Ende garantiert die Nullmatrix heraus.
</blockquote>
</details>


### Definition

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Die klassische Taylorreihe der Schul-e-Funktion, nur eben mit Matrizen. Bei Jordan-Blöcken hat das die geniale Eigenschaft, dass die Taylorreihe durch das 'nilpotente' Verhalten der 1en rasant abbricht!
</blockquote>
</details>

Das **Minimalpolynom** $\mu_A$ ist das normierte Polynom kleinsten Grades mit $\mu_A(A) = 0$.

### Eigenschaften

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Bei einer strikten Diagonalmatrix ist das Minimalpolynom absolut minimal, da jede Nullstelle nur Potenz 1 braucht, um die Matrix zu löschen.
</blockquote>
</details>

- $\mu_A$ teilt $\chi_A$ (d.h. $\chi_A = \mu_A \cdot q$ für ein Polynom $q$)
- $\mu_A$ und $\chi_A$ haben **die gleichen** Nullstellen (= Eigenwerte)
- Aus der JNF: $\mu_A(\lambda) = \prod_i (\lambda - \lambda_i)^{s_i}$, wobei $s_i$ = Größe des **größten** Jordan-Blocks zu $\lambda_i$

### Berechnung ohne JNF

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Man rechnet es meist iterativ aus, indem man Terme hochpotenziert $(A-\lambda I)$, bis tatsächlich die Nullmatrix entsteht.
</blockquote>
</details>

1. Probiere Polynome aufsteigenden Grades, die durch $\chi_A$ teilen
2. Teste ob $p(A) = 0$

## 5.5 Satz von Cayley-Hamilton

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein gigantisch starkes Matrix-Konzept. 'Jede Matrix ist Nullstelle ihres eigenen char. Polynoms'. Heißt: A reingesteckt in $\chi(X)$ ergibt IMMER null.
</blockquote>
</details>



> 🔗 **Zugehörige Übungen:**
> - [Übungsblatt 7, AP 3: Cayley-Hamilton](Uebungszettel_Originale.html#aufgabenpaket-3-cayley-hamilton)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Ein gigantisch starkes Matrix-Konzept. 'Jede Matrix ist Nullstelle ihres eigenen char. Polynoms'. Heißt: A reingesteckt in $\chi(X)$ ergibt IMMER null.
</blockquote>
</details>


> **Satz:** Jede Matrix erfüllt ihr eigenes charakteristisches Polynom:
> $$\chi_A(A) = 0$$

### Wichtige Folgerungen (Wissen für die Theorie/Klausur)

<details>
<summary>🎓 <b>Wikipedia-Ergänzung: Zusammenhänge und Folgerungen</b></summary>
<blockquote>
Nach Wikipedia liefert Cayley-Hamilton sehr nützliche Eigenschaften:
<ul>
<li>Die Potenzen einer quadratischen Matrix spannen einen Untervektorraum auf, der höchstens die Dimension der Zeilenzahl $n$ hat.</li>
<li>Die <strong>Inverse</strong> einer invertierbaren Matrix ist als Linearkombination der Potenzen der Matrix (mit Exponenten kleiner als $n$) darstellbar.</li>
<li>Das <strong>Minimalpolynom</strong> einer Matrix teilt ihr <a href="https://de.wikipedia.org/wiki/Charakteristisches_Polynom">charakteristisches Polynom</a>.</li>
<li>Eine quadratische Matrix mit $n$-fachem Eigenwert Null ist <strong>nilpotent</strong>, da ihr char. Polynom die Form $\lambda^n$ ist.</li>
<li>Man kann höhere Potenzen von Matrizen einfach durch Umstellen des charakteristischen Polynoms berechnen (wie in Aufgabe 4).</li>
</ul>
</blockquote>
</details>

### Anwendung (Klausuraufgabe 4!)

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Extrem nützlich, um Matrixpotenzen zu kürzen! Wenn $A^2 - A = 0$ gilt, wie in der Klausur, dann weiß man, dass unendlich hohe Potenzen wie $A^{100}$ einfach auf A kollabieren. Kein ewiges Multiplizieren!
</blockquote>
</details>


**Gegeben:** $A$ diagonalisierbar mit Eigenwerten $\lambda_1 = 0$ und $\lambda_2 = 1$.

**4.1: Minimalpolynom**
$$\mu_A(\lambda) = \lambda(\lambda - 1) = \lambda^2 - \lambda$$

(Da $A$ diagonalisierbar → alle Jordan-Blöcke Größe 1 → Minimalpolynom hat nur einfache Nullstellen)

**4.2: $A^2 = A$**
Cayley-Hamilton: $\chi_A(A) = 0$. Da $\mu_A | \chi_A$ und $\mu_A(A) = 0$:
$$A^2 - A = 0 \implies A^2 = A$$

(Formal: $\mu_A(\lambda) = \lambda^2 - \lambda$, also $\mu_A(A) = A^2 - A = 0$)

**4.3: $A^m = A$ für $m \geq 1$ (Induktion)**

*Induktionsanfang:* $m = 1$: $A^1 = A$ ✓

*Induktionsschritt:* Angenommen $A^m = A$ für ein $m \geq 1$. Dann:
$$A^{m+1} = A^m \cdot A = A \cdot A = A^2 = A$$

(wobei wir im letzten Schritt $A^2 = A$ aus 4.2 verwenden)

Also gilt $A^{m+1} = A$. $\square$

**4.4: Matrixexponential**
$$\exp(A) = \sum_{k=0}^{\infty} \frac{A^k}{k!} = \frac{A^0}{0!} + \sum_{k=1}^{\infty} \frac{A^k}{k!}$$

$$= I + \sum_{k=1}^{\infty} \frac{A}{k!} \quad \text{(da } A^k = A \text{ für } k \geq 1\text{)}$$

$$= I + A \sum_{k=1}^{\infty} \frac{1}{k!} = I + A\left(\sum_{k=0}^{\infty} \frac{1}{k!} - 1\right) = I + A(e - 1)$$

$$\boxed{\exp(A) = I + (e-1)A}$$

## 5.6 Matrixexponential – Allgemein

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Wofür das alles in der Praxis da ist: Viele Differentialgleichungen von Schwingungen in der Physik hängen an $y' = Ay$. Ein Matrix-Exponential löst diese Naturgesetze auf.
</blockquote>
</details>


### Definition

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Die klassische Taylorreihe der Schul-e-Funktion, nur eben mit Matrizen. Bei Jordan-Blöcken hat das die geniale Eigenschaft, dass die Taylorreihe durch das 'nilpotente' Verhalten der 1en rasant abbricht!
</blockquote>
</details>

$$\exp(A) = \sum_{k=0}^{\infty} \frac{A^k}{k!} = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots$$

### Rechenregeln

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Höchste Vorsicht: $e^{A+B}$ ist NUR dann aufteilbar in $e^A \cdot e^B$, wenn die Matrizen vertauschen ($A \cdot B = B \cdot A$).
</blockquote>
</details>

- $\exp(0) = I$
- Wenn $AB = BA$: $\exp(A+B) = \exp(A)\exp(B)$
- $\exp(A)$ ist **immer** invertierbar mit $\exp(A)^{-1} = \exp(-A)$
- $\det(\exp(A)) = e^{\text{Spur}(A)}$

### Für Diagonalmatrizen

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Zuckerschlecken! Man packt einfach das $e^\lambda$ an jeden Diagonaleintrag. Komplett triviale Berechnung.
</blockquote>
</details>

$$\exp\left(\begin{pmatrix} \lambda_1 & & \\ & \ddots & \\ & & \lambda_n \end{pmatrix}\right) = \begin{pmatrix} e^{\lambda_1} & & \\ & \ddots & \\ & & e^{\lambda_n} \end{pmatrix}$$

### Anwendung: DGL

<details>
<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>
<blockquote>
Löst dir deine linearen DGL-Systeme auf den Punkt durch einfaches Einsetzen von $y(t) = e^{t \cdot A} y(0)$.
</blockquote>
</details>

Die Lösung von $\dot{x}(t) = Ax(t)$ mit $x(0) = x_0$ ist:
$$x(t) = \exp(tA) \cdot x_0$$
