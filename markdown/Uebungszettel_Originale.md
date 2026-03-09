# Originale Übungszettel 1-10
Hier findest du alle originalen Übungsaufgaben (Zettel 1 bis 10) direkt zum Aufklappen, ohne die PDFs öffnen zu müssen.

<details>
<summary>📖 <b>Übungsblatt 01 anzeigen</b></summary>

# Übungsblatt 1: Komplexe Zahlen
**Lineare Algebra II**

## Lernziel
Ziel dieses Übungsblatts ist es, den sicheren Umgang mit komplexen Zahlen zu vertiefen. Studierende sollen insbesondere die Darstellung in kartesischer und polarer Form beherrschen, n-te Wurzeln berechnen, transzendente und trigonometrische Funktionen auf komplexe Argumente anwenden sowie geometrische Interpretationen komplexer Zahlen verstehen und anwenden können.

---

## Aufgabenpaket 1: Grundoperationen und Darstellungen
**1.1** Berechnen Sie die folgenden Ausdrücke und geben Sie das Ergebnis in kartesischer Form an, wobei Sie Realteil und Imaginärteil der Zahl benennen:
(a) $(2 + 3i)$ multipliziert mit der komplexen Zahl, die den Betrag $2$ und das Argument $-45^\circ$ hat.
(b) $\frac{1+i}{2-i}$
(c) $|3 - 4i|$

**1.2** Wandeln Sie die folgenden komplexen Zahlen in die Polarform $r \cdot \exp(i\theta)$ um:
(a) $z_1 = -1 + i$
(b) $z_2 = 2 - 2i$

**1.3** Berechnen Sie die Potenz $z^5$ in kartesischer Darstellung, wobei $z = \sqrt{2} \cdot e^{i \frac{\pi}{4}}$.

---

## Aufgabenpaket 2: n-te Wurzeln und komplexe Gleichungen
**2.1** Bestimmen Sie alle dritten Wurzeln von $8 \cdot e^{i\pi}$ und zeichnen Sie diese in der komplexen Ebene.
**2.2** Lösen Sie die Gleichung $z^4 = 16$ in der Menge der komplexen Zahlen.
**2.3** Zeigen Sie, dass die Menge aller n-ten Einheitswurzeln ein regelmäßiges n-Eck auf dem Einheitskreis bildet.

---

## Aufgabenpaket 3: Transzendente und trigonometrische Funktionen
**3.1** Berechnen Sie $\exp\left(i \frac{\pi}{3} + 2\right)$ und interpretieren Sie das Ergebnis geometrisch. Berechnen Sie alle Lösungen der Gleichung $4z = 3i - 4$.

**3.2** Zeigen Sie, dass für alle $z \in \mathbb{C}$ gilt: 
$$ \cos(z) = \frac{e^{iz} + e^{-iz}}{2} \quad \text{und} \quad \sin(z) = \frac{e^{iz} - e^{-iz}}{2i} $$

**3.3** Berechnen Sie $\sin(1 + i)$ und $\cos(1 + i)$.

---

## Aufgabenpaket 4: Geometrie und komplexe Zahlen
**4.1** Drehung in der komplexen Ebene: Zeigen Sie, dass eine Drehung um den Ursprung um den Winkel $\phi$ durch Multiplikation mit $e^{i\phi}$ beschrieben wird. Interpretieren Sie diese Operation geometrisch und wenden Sie sie auf den Punkt $z = 2+i$ mit $\phi = \frac{\pi}{2}$ an. Wie könnte man eine solche Drehung um einen anderen Punkt als den Ursprung arithmetisch formulieren?

**4.2** Abstand und Winkel: Gegeben seien die komplexen Zahlen $z_1 = 1+i$, $z_2 = 3+2i$, $z_3 = 2 - i$.
(a) Berechnen Sie die Seitenlängen des Dreiecks mit den Eckpunkten $z_1, z_2, z_3$.
(b) Berechnen Sie den Winkel bei $z_1$ ohne Zuhilfenahme des Skalarprodukts nur mit komplexen Operationen.
(c) Spiegeln Sie das Dreieck an der “x-Achse”.

**4.3** Konstruktion eines gleichseitigen Dreiecks: Gegeben seien zwei Punkte $z_1 = 0$, $z_2 = 1$. Konstruieren Sie einen dritten Punkt $z_3$, sodass das Dreieck $z_1, z_2, z_3$ gleichseitig ist und $z_3$ oberhalb der Verbindungslinie liegt. Nutzen Sie komplexe Zahlen zur Konstruktion und begründen Sie Ihre Wahl.

**4.4** Napoleon-Dreieck (anspruchsvoll): Gegeben sei ein beliebiges Dreieck mit komplexen Eckpunkten $z_1, z_2, z_3$. Errichten Sie auf jeder Seite ein äußeres gleichseitiges Dreieck und bestimmen Sie die Mittelpunkte dieser drei Dreiecke. Zeigen Sie, dass diese Mittelpunkte ein gleichseitiges Dreieck bilden. Nutzen Sie komplexe Zahlen zur Beweisführung und argumentieren Sie geometrisch.
</details>

<details>
<summary>📖 <b>Übungsblatt 02 anzeigen</b></summary>

# Übungsblatt 2: Erzeugendensysteme algebraischer Strukturen und algorithmische Anwendung
**Lineare Algebra II**

## Lernziele
Nach Bearbeitung dieses Übungsblatts sollen Sie in der Lage sein, die Unterschiede zwischen algebraischen Strukturen (mit zwei Verknüpfungen, d.h. mit Addition und mit Multiplikation) zu sehen und zu wissen, wie sich diese Unterschiede auf die Verwendbarkeit des Begriffes “Dimension” auswirken. Sie sollen anhand des Euklidischen Algorithmus und der Konstruktion von Abbildungsmatrizen lernen, wie sich die Definition algebraischer Strukturen algorithmisch verwenden lässt.

---

## Aufgabenpaket 1: Verschiedene Algebraische Strukturen
**1.1** Schreiben Sie auf, wie die folgenden algebraischen Strukturen definiert sind: Körper, Vektorraum, Schiefkörper, Ring, Algebra, Modul, Ideal. Gehen Sie insbesondere auf die algebraischen Eigenschaften von Addition und Multiplikation ein und wie diese Operationen jeweils als “abgeschlossen” zu sehen sind in den entsprechenden algebraischen Strukturen. Welche Form von “Distributivgesetzen” gibt es?

**1.2** Versuchen Sie eine “Hierarchie” der algebraischen Strukturen zu finden. Im Sinne von “Jeder Körper ist auch ein Vektorraum, aber nicht jeder Vektorraum ist auch ein Körper”.

---

## Aufgabenpaket 2: Basis und Dimension
Sie haben gelernt, dass man einen Vektorraum erhält indem man alle Linearkombinationen (die sogenannte “lineare Hülle” oder den “Spann”) von gegebenen erzeugenden Elementen bestimmt. Eine Basis ist dabei ein minimales Erzeugendensystem. Man kann eine Auswahl unter den Erzeugenden treffen, die dann eine Basis bilden. Die verschiedenen Basen eines gegebenen Vektorraumes haben immer die gleiche Anzahl an Elementen. Daraus leitet sich der Begriff der “Dimension” ab. Auch andere algebraische Strukturen lassen sich mit Hilfe des “Spanns” von einzelnen Elementen erzeugen, z.B. der Modul oder das Ideal. Haben diese Strukturen auch eine “Dimension”? Recherchieren Sie in der Literatur.

---

## Aufgabenpaket 3: Euklidischer Algorithmus
**3.1** Welche zusätzlichen Eigenschaften hat der “Euklidische Ring” gegenüber einem Ring? Zeigen Sie, dass die Menge der ganzen Zahlen und dass die Menge der Polynome mit komplexen Koeffizienten jeweils einen Euklidischen Ring bilden.

**3.2** Nutzen Sie den Euklidischen Algorithmus, um die folgenden Brüche zu kürzen:
$$ \frac{105}{147} \quad \text{und} \quad \frac{x^3 - 2x^2 - x + 2}{x^3 + x^2 - x - 1} $$

**3.3** Primfaktorzerlegungen in Euklidischen Ringen sind immer eindeutig bis auf Reihenfolge der Faktoren und bis auf Multiplikation mit “Einheiten”. Die Einheiten sind diejenigen Elemente des Rings, die ein multiplikatives Inverses besitzen. Welche Einheiten besitzen die ganzen Zahlen? Welche Einheiten besitzt der Ring der Polynome mit komplexen Koeffizienten?

---

## Aufgabenpaket 4: Abbildungsmatrix erzeugen
**4.1** Gegeben seien die Basen
$$ B = \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\} \quad \text{und} \quad B' = \left\{ \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \end{pmatrix} \right\} $$
und die lineare Abbildung $h : \mathbb{R}^2 \to \mathbb{R}^2$ mit
$$ h \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x + y \\ x - y \end{pmatrix} $$
Bestimmen Sie die Abbildungsmatrix von $h$ bezüglich der Basen $B$ und $B'$.

**4.2** Gegeben seien zwei verschiedene Punkte $A$ und $B$ in der Ebene. Eine affine Abbildung bestehe darin, zunächst eine Figur um den Punkt $A$ um $180^\circ$ zu drehen und dann eine zentrische Streckung an $B$ mit dem Faktor $1/3$ auszuführen. Bestimmen Sie den Fixpunkt dieser Abbildung und setzen Sie so den Ursprung des Koordinatensystems fest. Bestimmen Sie die Abbildungsmatrix, die diese affine (jetzt lineare) Abbildung darstellt.

**4.3** Die Elemente $\{1, i, j, k\}$ bilden die Basis des 4-dimensionalen reellen Vektorraumes der Quaternionen. Die Quaternion-Multiplikation von rechts mit $i, j$ beziehungsweise $k$ stellt jeweils eine bestimme Form von Rotation in diesem Vektorraum dar. Zeigen Sie, dass diese Multiplikationen lineare Abbildungen sind und finden Sie die zugehörigen darstellenden ($4\times 4$)-Abbildungsmatrizen dieser linearen Abbildungen.
</details>

<details>
<summary>📖 <b>Übungsblatt 03 anzeigen</b></summary>

# Übungsblatt 3: Bild und Kern Linearer Abbildungen, Zusammenhang mit Determinanten
**Lineare Algebra II**

## Lernziele
Nach Bearbeitung dieses Übungsblatts sollen Sie in der Lage sein, Bild und Kern einer Matrix bestimmen zu können. Sie kennen Zusammenhänge zwischen Bild, Kern, Rang, Defekt, Dimension des Definitionsraumes, Invertierbarkeit und “Determinante = 0” und können diese Zusammenhänge auf die Lösung linearer Gleichungssysteme und auf Volumenberechnungen anwenden.

---

## Aufgabenpaket 1: Homomorphiesatz und Dimensionsformel
**1.1** Der Homomorphiesatz in Vektorräumen lautet: Seien $V$ und $W$ Vektorräume über einem Körper $K$ und $f : V \to W$ ein linearer Homomorphismus. Dann gilt:
$$ V / \ker(f) \cong \text{Im}(f) $$
Das heißt, der Quotientenraum von $V$ modulo dem Kern von $f$ ist isomorph zum Bild von $f$. Wie lässt sich dieser Satz und aus diesem Satz die Dimensionsformel
$$ \dim(\ker(f)) + \dim(\text{Im}(f)) = \dim(V) $$
beweisen (also Rang + Defekt = Dimension Definitionsraum)?

**1.2** Der Homomorphiesatz gilt auch für andere algebraische Strukturen. Recherchieren Sie!

---

## Aufgabenpaket 2: Bild und Kern einer Linearen Abbildung berechnen
**2.1** Bestimmen Sie eine Basis für das Bild und den Kern der folgenden Matrix:
$$ A = \begin{pmatrix} -1 & 2 & 1 \\ 1 & 2 & 7 \\ 0 & 3 & 6 \end{pmatrix} $$

**2.2** Gibt es eine eindeutige/mehrdeutige Lösung für die folgenden linearen Gleichungssysteme? Begründen Sie!
$$ A \cdot \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \quad , \quad A \cdot \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} -1 \\ 5 \\ 3 \end{pmatrix} $$

**2.3** Zeigen Sie, dass die Ableitung einer Funktion eine lineare Abbildung auf dem Vektorraum der differenzierbaren Funktionen ist. Was ist der Kern dieser Abbildung? Wie lässt sich das Bild dieser linearen Abbildung beschreiben? Wie lautet die allgemeine Lösung der linearen Gleichung $\frac{d}{dx} f(x) = 3x^2$?

---

## Aufgabenpaket 3: Bedeutung von “Determinante = 0”
Nehmen wir an, eine quadratische Matrix $A$ habe die Determinante $= 0$. Welche der folgenden Aussagen trifft dann zu bzw. nicht zu? Finden Sie jeweils Begründungen für Ihre Ansicht!
**3.1** Aussage: Der Kern der Matrix $A$ enthält einen Vektor $v$, der nicht der Nullvektor ist. (Mathematisch gesprochen: Die Matrix hat einen nicht-trivialen Kern.)
**3.2** Aussage: Die Spalten von $A$ sind linear abhängig.
**3.3** Aussage: Die Matrix besitzt eine inverse Matrix.
**3.4** Aussage: Ein lineares Gleichungssystem der Form $Ax = b$ ist eindeutig lösbar.

---

## Aufgabenpaket 4: Invertierbare Matrizen
Zeigen Sie, dass folgende Aussagen für eine quadratische $n \times n$-Matrix $A$ äquivalent sind! Gegebenenfalls schauen Sie die Definitionen der benutzten Begriffe nach!
**4.1** $A$ ist invertierbar.
**4.2** $Ax = 0$ hat nur die triviale Lösung $\{0\}$.
**4.3** $A$ lässt sich durch Spaltenumformungen auf die Einheitsmatrix bringen.
**4.4** $A$ lässt sich als Produkt von Elementarmatrizen darstellen.
**4.5** Die Spalten von $A$ bilden ein Parallelepiped mit Volumen $\neq 0$.
**4.6** Der Wertebereich der durch $A$ dargestellten linearen Abbildung ist $\mathbb{R}^n$.
**4.7** Die durch $A$ dargestellte lineare Abbildung ist injektiv.
**4.8** Die Spalten von $A$ sind linear unabhängig.
**4.9** $\text{rang}(A) = n$.
**4.10** $\text{def}(A) = 0$.
**4.11** Das orthogonale Komplement des Kerns von $A$ ist $\mathbb{R}^n$.
</details>

<details>
<summary>📖 <b>Übungsblatt 04 anzeigen</b></summary>

# Übungsblatt 4: Determinanten berechnen und Eigenräume bestimmen
**Lineare Algebra II**

## Lernziele
Mit diesem Übungsblatt sollen Sie lernen, die Determinante von Matrizen rechnen zu können, deren spezielle Struktur vorgegeben ist. Sie sollen mit Hilfe des Bild-Kern-Algorithmus Eigenräume von Matrizen ausrechnen können. Sie sollen eine mögliche Nutzung von Eigenvektoren kennenlernen.

---

## Aufgabenpaket 1: Determinante der Vandermonde-Matrix
Gegeben seien $n$ paarweise verschiedene Zahlen $x_1, x_2, \dots, x_n \in \mathbb{R}$. Betrachte die $n \times n$ Vandermonde-Matrix
$$ V = \begin{pmatrix}
1 & x_1 & x_1^2 & \dots & x_1^{n-1} \\
1 & x_2 & x_2^2 & \dots & x_2^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \dots & x_n^{n-1}
\end{pmatrix} $$

**1.1** Berechne die Determinante der Matrix $V$ für $n = 3$ explizit.
**1.2** Zeige, dass die Determinante der allgemeinen Vandermonde-Matrix durch folgende Formel gegeben ist:
$$ \det(V) = \prod_{1 \leq i &lt; j \leq n} (x_j - x_i) $$
**1.3** Begründe, warum die Vandermonde-Matrix invertierbar ist, wenn die $x_i$ paarweise verschieden sind.

---

## Aufgabenpaket 2: Eigenschaften einer Linearen Abbildung aus der Matrix ablesen
Sie wissen, dass eine lineare Abbildung eindeutig durch die Bilder der Basisvektoren bestimmt ist. Nehmen wir an, die folgende Matrix $A$ enthalte die Bilder der drei Einheitsvektoren des kartesischen Koordinatensystems:
$$ A = \begin{pmatrix}
1 & 0 & 0 \\
0 & \frac{1}{3} & -\frac{\sqrt{8}}{3} \\
0 & -\frac{\sqrt{8}}{3} & -\frac{1}{3}
\end{pmatrix} $$

**2.1** Wie können Sie testen, ob die Abbildung längen- und winkeltreu, volumenerhaltend und/oder orientierungstreu ist?
**2.2** (a) Nennen Sie Beispiele für lineare Abbildungen, die zusätzlich zum Ursprung noch Fixgeraden und/oder Fixebenen besitzen. (b) Kennen Sie eine lineare Abbildung, bei der alle Ursprungsgeraden Fixgeraden sind? (c) Kennen Sie eine lineare Abbildung, die keine Fixgerade besitzt?
**2.3** Welche geometrische lineare Abbildung wird durch die Matrix $A$ dargestellt? Beschreiben Sie die Wirkung der Abbildung möglichst anschaulich und genau.

---

## Aufgabenpaket 3: Berechnung von Eigenräumen
Betrachten Sie die folgenden drei Matrizen $A_1, A_2$ und $A_3$:
$$ A_1 = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix}, \quad A_2 = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 5 & 1 \\ 0 & -1 & 3 \end{pmatrix}, \quad A_3 = \begin{pmatrix} 4 & 4 & 0 \\ 3 & 4 & 6 \\ 0 & -2 & 4 \end{pmatrix} $$

**3.1** Zeigen Sie, dass alle drei Matrizen dasselbe charakteristische Polynom $(\lambda - 4)^3$ besitzen.
**3.2** Bestimmen Sie für jede der drei Matrizen die Eigenvektoren zum Eigenwert $\lambda = 4$.
**3.3** Vergleichen Sie die algebraischen und geometrischen Vielfachheiten der Eigenwerte bei den drei gegebenen Matrizen.

---

## Aufgabenpaket 4: Distanzgeometrieproblem lösen
Mit Hilfe von NMR-Experimenten ist es oft möglich, Informationen über die Distanzen zwischen bestimmten Atomen in dem zu untersuchenden Molekül zu gewinnen (NOEs). Die Aufgabe, aus diesen Distanzen auf die 3D-Koordinaten der Atome zurück zu rechnen, bezeichnet man als Distanzgeometrie-Problem. Im Allgemeinen sind solche Probleme mathematisch schwer zu lösen. Anders ist es jedoch, wenn alle paarweisen Distanzen der beteiligten Atome bekannt sind. Nehmen wir an, die folgende Matrix enthält die paarweisen Distanzen von einem Molekül aus vier Atomen:
$$ D = \begin{pmatrix}
0 & 2 & \sqrt{3} & \sqrt{5} \\
2 & 0 & \sqrt{11} & \sqrt{17} \\
\sqrt{3} & \sqrt{11} & 0 & \sqrt{6} \\
\sqrt{5} & \sqrt{17} & \sqrt{6} & 0
\end{pmatrix} $$

Distanzmatrizen sind auf jeden Fall nicht-negativ und symmetrisch. Die Diagonalelemente sind Null. Zunächst quadriert man alle Elemente dieser Matrix und kommt so zu der Matrix $\tilde{D}$. Aus dieser Matrix gewinnt man eine andere Matrix $M$ auf folgende Weise:
$$ M_{ij} = \frac{\tilde{D}_{1j} + \tilde{D}_{i1} - \tilde{D}_{ij}}{2} $$
Von dieser Matrix $M$ berechnet man alle positiven Eigenwerte (es sind drei, einer ist “0”) und die dazugehörigen (drei) Eigenvektoren. Das Eigenwert-Problem hat bei dieser Methode immer drei positive Eigenwerte, egal wie viele Atome es sind. Jetzt bedarf es noch einer Skalierung: Multiplizieren Sie jeden Eigenvektor mit der Wurzel aus dem zugehörigen Eigenwert. Sie erhalten so eine Matrix von drei skalierten vier-dimensionalen Spalten-Eigenvektoren. Die (vier) Zeilen dieser Matrix sind die gesuchten 3-dimensionalen Koordinaten der Atome.

**4.1** Machen Sie sich zunächst klar, dass die $M$-Matrix gemäß der obigen Formel so aussieht:
$$ M = \begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 4 & -2 & -4 \\
0 & -2 & 3 & 1 \\
0 & -4 & 1 & 5
\end{pmatrix} $$
**4.2** Suchen Sie eine Möglichkeit, das Eigenwert-Problem mit dem Rechner zu lösen.
**4.3** Beachten Sie, dass Ihre Lösung auch die Eigenschaft hat, dass die Eigenvektoren ein Orthonormalsystem bilden und die Eigenwerte reell sind (evtl. müssen Sie die Eigenvektoren auf Länge 1 normieren).
**4.4** Machen Sie die Probe, ob die vorgegebenen Distanzen eingehalten werden!
</details>

<details>
<summary>📖 <b>Übungsblatt 05 anzeigen</b></summary>

# Übungsblatt 5: Eigenraumbasen erweitern und Projektion auf Orthonormalsysteme
**Lineare Algebra II**

## Lernziele
Manche ($n \times n$)-Matrizen sind nicht diagonalisierbar. Sie sollen verstehen, wie man dann Eigenraumbasen erweitern kann, um eine n-dimensionale Basis zu erhalten (zum Lösen von linearen Differentialgleichungen). Orthonormalbasen spielen eine große Rolle. Sie sollen die Galerkin-Projektion durchführen können.

---

## Aufgabenpaket 1: Ergänzung einer Eigenraumbasis
Betrachten Sie die folgende Matrix, die Sie schon aus einer vorangehenden Aufgabe kennengelernt haben:
$$ A = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 5 & 1 \\ 0 & -1 & 3 \end{pmatrix} $$

**1.1** Zeigen Sie, dass diese Matrix nicht diagonalisierbar ist.
**1.2** Es soll jetzt eine invertierbare ($3\times3$)-Matrix $V$ erzeugt werden, die zu einer möglichst einfachen Gestalt $\Lambda = V^{-1} A V$ führt ($\Lambda$ kann nicht Diagonalgestalt haben). Zeigen Sie, dass der 2-dimensionale Eigenraum, den Sie gefunden haben, von zwei orthogonal zueinander stehenden Eigenvektoren aufgespannt wird. Finden Sie auf einfache Weise einen weiteren Vektor, der diese Basis zu einer Orthogonalbasis von $\mathbb{R}^3$ ergänzt (Stichwort: Kreuzprodukt). Zeigen Sie, dass $V^\top V$ eine Diagonalmatrix $D$ ist. Schlussfolgern Sie, dass in diesem Falle $V^{-1} = D^{-1} V^\top$ ist. Berechnen Sie $V^{-1} A V$.
**1.3** Alternativer Weg zu 1.2 (Idee der Jordan-Kette): Bestimmen Sie einen Vektor $v \in \mathbb{R}^3$, so dass $(A - 4I)v$ im Kern von $(A - 4I)$ liegt, wobei $v$ aber nicht im Kern von $(A - 4I)$ liegen darf. Bauen Sie auf diese Weise eine ($3 \times 3$)-Matrix $V$ auf und rechnen Sie $V^{-1} A V$.

---

## Aufgabenpaket 2: Lösen einer linearen Differentialgleichung
In beiden Fällen in Aufgabe 1 kann man sich jeweils die Matrix $\Lambda$ als eine Summe einer Diagonalmatrix $\tilde{D}$ und einer nilpotenten Matrix $N$ denken. Zeigen Sie, dass jeweils gilt $\tilde{D}N = N\tilde{D}$. Geben Sie alle Lösungen des linearen Differentialgleichungssystems $\frac{d}{dt} f = A f$ mit der Matrix $A$ aus Aufgabe 1 an.

---

## Aufgabenpaket 3: Darstellung der Ableitung
**3.1** Zeigen Sie, dass die Funktionen $f_1 = 1$, $f_2 = \sqrt{3}(2x - 1)$ und $f_3 = \sqrt{5}(6x^2 - 6x + 1)$ bezüglich des Skalarproduktes
$$ \langle f, g \rangle = \int_0^1 f(x) \cdot g(x) dx $$
eine Orthonormalbasis eines Untervektorraumes der differenzierbaren Funktionen $f : \mathbb{R} \to \mathbb{R}$ bilden.

**3.2** Berechnen Sie die darstellende Matrix des Ableitungsoperators (das ist eine lineare Abbildung) in dieser Basis.

---

## Aufgabenpaket 4: Galerkin-Projektion
**4.1** Zeigen Sie, dass das Integrieren (Integrationskonstante = 0) als lineare Abbildung aus dem Raum hinaus führt, der durch die drei in Aufgabe 3 gegebenen Basisfunktionen aufgespannt wird.
**4.2** Bestimmen Sie mit Hilfe der Galerkin-Projektion auf die gegebene Orthonormalbasis eine lineare Abbildung, die innerhalb des dreidimensionalen Raums abbildet und eine Approximation des Integraloperators darstellt.
</details>

<details>
<summary>📖 <b>Übungsblatt 06 anzeigen</b></summary>

# Übungsblatt 6: Orthonormalprojektion, Gram-Schmidt-Verfahren und Konstruktion von Matrizen
**Lineare Algebra II**

## Lernziele
Sie sollen in der Lage sein, bei gegebenem Skalarprodukt und gegebener Basis eines Vektorraumes diese mittels Gram-Schmidt-Verfahren in eine Orthonormalbasis zu überführen. Sie sollen in der Lage sein, für ein gegebenes Orthonormalsystem (ONS) die Orthogonalprojektion auf dieses ONS als Matrix bzw. als linearer Operator (Dualraum) schreiben zu können. Sie sollen Verfahren kennen lernen, wie man Matrizen konstruieren kann, die vorbestimmte Eigenschaften hinsichtlich ihrer Diagonalisierbarkeit haben. Sie dürfen für diesen Übungszettel Computerprogramme verwenden!

---

## Aufgabenpaket 1: Gram-Schmidt-Verfahren
Verwenden Sie das Gram-Schmidt-Orthonormalisierungsverfahren, um die gegebene Monom-Basis $u_1 = 1$, $u_2 = x$, $u_3 = x^2$ des Vektorraums der Polynome bis zum Grad 2 bezüglich des Skalarproduktes
$$ \langle f, g \rangle = \int_0^1 f(x) \cdot g(x) dx $$
zu orthonormalisieren.

---

## Aufgabenpaket 2: Projektionsabbildung
**2.1** Sie wissen bereits, dass $f_1 = 1$, $f_2 = \sqrt{3}(2x - 1)$, $f_3 = \sqrt{5}(6x^2 - 6x + 1)$ bezüglich des Skalarproduktes aus Aufgabe 1 ein Orthonormalsystem bilden. Wie lautet die lineare Abbildungsvorschrift, die eine gegebene Funktion $f$ auf dieses ONS projiziert? Diskutieren Sie in diesem Zusammenhang die Bedeutung des Begriffes “Dualraum”.
**2.2** Gegeben sei folgendes Skalarprodukt (zeigen Sie, dass es eines ist!):
$$ \langle x, y \rangle_A = x^\top Ay \quad \text{mit} \quad A = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 3 & 0 \\ 0 & 0 & 2 \end{pmatrix} $$
**2.3** Orthonormalisieren Sie die Vektoren
$$ u_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad u_2 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} $$
bezüglich $\langle \cdot, \cdot \rangle_A$. Schreiben Sie die Projektionsmatrix auf, die die Orthogonalprojektion $\Pi : \mathbb{R}^3 \to \mathbb{R}^3$ auf den von $u_1$ und $u_2$ aufgespannten Unterraum (auf Basis der Einheitsvektoren) darstellt.

---

## Aufgabenpaket 3: Quaternionen als Vektoren in $\mathbb{R}^4$
In Aufgabe 4.3 auf dem 2. Übungszettel haben Sie die reellwertigen ($4 \times 4$)-Matrizen ausgerechnet, die jeweils die Multiplikation mit Quaternionen darstellen.
**3.1** Durch diese Matrizen werden verschiedene Rotationen innerhalb des $\mathbb{R}^4$ gegeben. Liegen deren Rotationsachsen jeweils in $\mathbb{R}^4$? Kann es Rotationen in $\mathbb{R}^2$ bzw. in $\mathbb{R}^3$ geben, deren Rotationsachsen nicht in $\mathbb{R}^2$ bzw. in $\mathbb{R}^3$ liegen?
**3.2** Berechnen Sie die (komplexe und reelle) Schur-Zerlegung dieser ($4 \times 4$)-Matrizen.

---

## Aufgabenpaket 4: Konstruktion von Matrizen
Lesen Sie noch einmal die Fallbeispiele von Übergangsmatrizen nach, die wir in der Vorlesung besprochen haben. Bestimmen Sie eine nicht-negative ($5 \times 5$)-Matrix $P$ mit Zeilensumme 1, die nicht-diagonalisierbar ist, nur reelle Eigenwerte hat und für die $P^\top \pi = \pi$ gilt mit dem Vektor
$$ \pi = \begin{pmatrix} 1 \\ 3 \\ 3 \\ 2 \\ 2 \end{pmatrix} $$
</details>

<details>
<summary>📖 <b>Übungsblatt 07 anzeigen</b></summary>

# Übungsblatt 7: Jordan Normalform von Matrizen
**Lineare Algebra II**

## Lernziele
Sie sollen in der Lage sein zu verstehen, warum jede Matrix, die ein charakteristisches Polynom besitzt, das vollständig in Linearfaktoren zerfällt, eine Jordan Normalform (JNF) besitzt. Sie sollen den theoretischen Hintergrund von Rechenschritten verstehen, die zur JNF führen.

---

## Aufgabenpaket 1: Vorbereitungen auf den JNF-Existenzsatz
Zeigen Sie folgende Aussagen:
**1.1** Seien $M$ eine Menge, $f : M \to M$ eine Selbstabbildung von $M$ und $U$ eine $f$-invariante Teilmenge von $M$. Dann gilt: (i) $U$ ist in $f^{-1}(U)$ enthalten. (ii) Jede Teilmenge $W$ von $f^{-1}(U)$, die $U$ enthält, ist $f$-invariant.
**1.2** Ist $f$ eine lineare Selbstabbildung eines Vektorraums $V$ so gilt: (i) Jeder Untervektorraum von $\ker(f)$ ist $f$-invariant. (ii) Jeder $\text{Im}(f)$ enthaltende Untervektorraum von $V$ ist $f$-invariant.

---

## Aufgabenpaket 2: Ein weiterer Hilfssatz
Ist $f$ eine lineare Selbstabbildung eines Vektorraumes $V$ über einem Körper $K$ und $\lambda$ ein Element von $K$ sowie $e : V \to V$ die Identitätsabbildung, so gilt für jeden Untervektorraum $U$ von $V$: $U$ ist $f$-invariant genau dann, wenn $U$ invariant unter $(f - \lambda e)$ ist.

---

## Aufgabenpaket 3: Cayley-Hamilton
Gegeben sei die Matrix
$$ A = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 5 & 1 \\ 0 & -1 & 3 \end{pmatrix} $$
**3.1** Bestimmen Sie das charakteristische Polynom von $A$.
**3.2** Formulieren Sie den Satz von Cayley-Hamilton für diese Matrix.
**3.3** Überprüfen Sie, dass die Matrix $A$ ihr eigenes charakteristisches Polynom erfüllt, d.h. setzen Sie $A$ in das Polynom ein und zeigen Sie, dass das Ergebnis die Nullmatrix ist.
**3.4** Bestimmen Sie das Minimalpolynom von $A$.

---

## Aufgabenpaket 4: Berechnung einer Jordan-Normalform
Gegeben sei die Matrix
$$ A = \begin{pmatrix} 1 & 1 & 0 & 0 \\ -1 & 3 & 0 & 0 \\ -1 & 1 & 1 & 1 \\ -1 & 1 & -1 & 3 \end{pmatrix} $$
**4.1** Zeigen Sie, dass das charakteristische Polynom von $A$ lautet $(2 - \lambda)^4$.
**4.2** Bestimmen Sie die geometrische Vielfachheit von $\lambda = 2$.
**4.3** Bestimmen Sie den Kern von $(A - 2I)^2$.
**4.4** Nutzen Sie 4.3, um die Matrix $V$ zu bestimmen, die $A$ mittels $J = V^{-1} A V$ in eine Jordan-Normalform überführt.
</details>

<details>
<summary>📖 <b>Übungsblatt 08 anzeigen</b></summary>

# Übungsblatt 8: Polynome und Symmetriegruppen, endliche Körper
**Lineare Algebra – 2. Semester**

## Lernziele
Sie sollen eine Methode kennen lernen, wie man die Nullstellen eines Polynoms bestimmen kann (durch Abspalten von Linearfaktoren). Die Begriffe “Symmetriegruppen” und “endliche Körper” werden eingeführt. Sie können Symmetriegruppen aufstellen und in endlichen Körpern Additionen und Multiplikationen rechnen, sowie inverse Elemente bestimmen.

---

## Aufgabenpaket 1: Nullstellen von Polynomen
Bestimmen Sie alle Nullstellen $\lambda_i \in \mathbb{C}, i = 1, \dots, 4$, des Polynoms:
$$ \lambda^4 + \lambda^3 - \lambda^2 + \lambda - 2 $$
Finden Sie dabei einzelne Nullstellen (durch Ausprobieren) und spalten Sie diese mit Hilfe des Horner-Schemas ab. Schreiben Sie das Polynom, das als Summe von Monomen $\sum_{i=0}^n c_i \lambda^i$ gegeben war, nun als Produkt von Linearfaktoren $c_n \prod_{i=1}^n (\lambda - \lambda_i)$.

---

## Aufgabenpaket 2: Begleitmatrix eines Polynoms
Gegeben sei das Polynom
$$ p(\lambda) = \lambda^4 - 2\lambda^3 + 3\lambda^2 - \lambda + 5 $$
**2.1** Konstruieren Sie die Begleitmatrix $C$ zu $p(\lambda)$, d.h. die Matrix der Form
$$ C = \begin{pmatrix}
0 & 0 & 0 & \dots & 0 & -c_0 \\
1 & 0 & 0 & \dots & 0 & -c_1 \\
0 & 1 & 0 & \dots & 0 & -c_2 \\
0 & 0 & 1 & \dots & 0 & -c_3 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & \dots & 1 & -c_{n-1}
\end{pmatrix} $$
wobei das Polynom die Gestalt $p(\lambda) = \lambda^n + c_{n-1}\lambda^{n-1} + \dots + c_1\lambda + c_0$ hat.
**2.2** Überprüfen Sie, dass die Eigenwerte von $C$ genau die Nullstellen von $p(\lambda)$ sind.

---

## Aufgabenpaket 3: Symmetriegruppe aufstellen
Zu einem gleichseitigen Dreieck in einem dreidimensionalen Raum mit Schwerpunkt im Ursprung gehören bestimmte lineare Abbildungen (Isometrien in $\mathbb{R}^3$), die nach Anwendung auf das Dreieck wieder als Resultat dasselbe Dreieck ergeben.
**3.1** Schreiben Sie alle diese linearen Abbildungen auf, indem Sie sie geometrisch beschreiben.
**3.2** Zeigen Sie, dass diese Abbildungen eine Gruppe bezüglich der “Hintereinanderausführung” als Gruppenoperation bilden, indem Sie die Verknüpfungstafel aufstellen.
**3.3** Welche Untergruppen gibt es?
**3.4** Zeigen Sie zu jeder Untergruppe, wie Sie das Dreieck verändern müssten, damit diese Untergruppe die Symmetriegruppe der veränderten Figur ist.

---

## Aufgabenpaket 4: Eigenwerte in endlichen Körpern
Gegeben sei die Matrix
$$ A = \begin{pmatrix} 0 & 0 & 2 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix} \in GF(3)^{3\times 3} $$
**4.1** Bestimmen Sie das charakteristische Polynom mit Koeffizienten in $GF(3)$. (Hinweis: $-1 = 2$ und $-2 = 1$ in $GF(3)$. Nutzen Sie Aufgabe 2.)
**4.2** Versuchen Sie durch Einsetzen aller Elemente aus $GF(3)$, die Nullstellen des charakteristischen Polynoms zu bestimmen.
**4.3** Kann man das charakteristische Polynom als Produkt von Linearfaktoren schreiben?
</details>

<details>
<summary>📖 <b>Übungsblatt 09 anzeigen</b></summary>

# Übungsblatt 9: Euklid, Banach und Hilbert Vektorräume mit Norm bzw. Skalarprodukt; Unitäre Vektorräume
**Lineare Algebra – 2. Semester**

## Lernziele
Viele der hier gefragten Aufgaben haben Sie schon auf den vorangehenden Zetteln behandelt oder behandeln können. Hier werden die Aufgaben jedoch mit einer mathematisch strengeren und moderneren Notation gegeben. Zudem lernen Sie, dass es verschiedene Arten von Vektorräumen gibt, die Sie vorher auch schon kennen gelernt haben, aber die hier explizit unterschieden werden. Einige Begriffe wie “vollständig” müssen Sie durch Literaturrecherche ergründen.

---

## Aufgabenpaket 1: Euklidische Räume
Sei $V = \mathbb{R}^3$ mit dem Standardskalarprodukt $\langle x, y \rangle = x_1 y_1 + x_2 y_2 + x_3 y_3$.
**1.1** Zeigen Sie, dass $\langle \cdot, \cdot \rangle$ ein Skalarprodukt ist.
**1.2** Bestimmen Sie die Norm $\|x\| = \sqrt{\langle x, x \rangle}$ für $x = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$.
**1.3** Finden Sie ein Orthonormalsystem, das den Vektor $v = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$ enthält.

---

## Aufgabenpaket 2: Hilberträume
Sei $H = L^2([0, 1])$ mit dem Skalarprodukt
$$ \langle f, g \rangle = \int_0^1 f(t)g(t) dt $$
**2.1** Bestimmen Sie die Norm von $f(t) = t$.
**2.2** Überprüfen Sie, ob die Funktionen $f_1(t) = 1$, $f_2(t) = \sqrt{2} \sin(\pi t)$ orthogonal sind.
**2.3** Zeigen Sie, dass $H$ vollständig ist.

---

## Aufgabenpaket 3: Banachräume
**3.1** Zeigen Sie, dass $(C([0, 1]), \|\cdot\|_\infty)$ ein Banachraum ist.
**3.2** Geben Sie ein Beispiel für eine Cauchy-Folge in $C([0, 1])$, die gleichmäßig konvergiert.
**3.3** Diskutieren Sie, ob $(\mathbb{Q}, |\cdot|)$ ein Banachraum ist.

---

## Aufgabenpaket 4: Unitäre Vektorräume
Sei $U = \mathbb{C}^2$ mit dem Standardskalarprodukt $\langle x, y \rangle = \bar{x}_1 y_1 + \bar{x}_2 y_2$.
**4.1** Zeigen Sie, dass $\langle \cdot, \cdot \rangle$ hermitesch und positiv definit ist.
**4.2** Bestimmen Sie die Norm von $x = \begin{pmatrix} 1+i \\ 2 \end{pmatrix}$.
**4.3** Finden Sie eine unitäre Matrix $U \in \mathbb{C}^{2\times 2}$, die $x$ auf einen Vektor der Länge $1$ abbildet.
</details>

<details>
<summary>📖 <b>Übungsblatt 10 anzeigen</b></summary>

# Übungsblatt 10: Untergruppen von Automorphismen
**Lineare Algebra II**

## Lernziel
Lineare Algebra beschäftigt sich auch mit linearen, bijektiven Selbstabbildungen (Automorphismen), die durch quadratische, invertierbare ($n \times n$)-Matrizen dargestellt werden können. Für fest gewähltes $n$ bilden diese Matrizen eine Gruppe (bezüglich der Matrixmultiplikation bzw. Hintereinanderausführung der Automorphismen). Diese Gruppen haben Untergruppen und Sie sollen lernen, welche theoretischen Arbeiten es dazu gibt und wie linear-algebraische Beweise in der modernen Mathematik funktionieren.

---

## Aufgabe
Suchen Sie sich zwei von den neun Aufgaben aus dem auf der Homepage verlinkten Skript der Vorlesung aus. Ergründen Sie die Lösung dieser Aufgaben, indem Sie LLMs verwenden und befragen.
</details>
