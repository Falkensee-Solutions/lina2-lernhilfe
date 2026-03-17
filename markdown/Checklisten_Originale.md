# Originale Checklisten

## Checkliste: Verstehen und Anwenden

* Zusammenhänge zwischen Determinante / Eigenwerte / Invertierbarkeit / Kern einer Matrix / Lösbarkeit LGS
  <details><summary>💡 Erklärung anzeigen</summary>
  <ul>
  <li><b>Eigenwerte & Determinante:</b> Die Determinante einer Matrix $A$ ist das Produkt aller ihrer Eigenwerte: $\det(A) = \prod \lambda_i$.</li>
  <li><b>Invertierbarkeit & Kern:</b> $A$ ist genau dann invertierbar, wenn ihr Kern trivial ist ($\ker(A) = \{0\}$), was bedeutet, dass der Nullvektor der einzige Vektor ist, der auf den Nullvektor abgebildet wird.</li>
  <li><b>Lösbarkeit LGS & Invertierbar:</b> Das LGS $Ax=b$ ist genau dann für jedes $b$ eindeutig lösbar, wenn $A$ invertierbar ist (also $\det(A) \neq 0$ und alle $\lambda_i \neq 0$). Ist $\det(A) = 0$, hat das homogene LGS $Ax=0$ nichttriviale Lösungen.</li>
  </ul>
  </details>

* geometrische Bedeutung von Eigenvektoren im Bezug auf die lineare Abbildung
  <details><summary>💡 Erklärung anzeigen</summary>
  Ein Eigenvektor einer Matrix $A$ beschreibt eine Richtung im Raum, die durch die Anwendung von $A$ <b>nicht gedreht</b>, sondern höchstens in ihrer Länge (also gestreckt oder gestaucht) verändert wird. Der Eigenwert $\lambda$ ist dieser Streckfaktor ($Av = \lambda v$). Ist $\lambda$ negativ, wandert der Vektor in die entgegengesetzte Richtung (Spiegelung); ist $\lambda=0$, kollabiert die Richtung (Projektion).
  </details>

* Zusammenhänge zwischen Jordan Normalform / Minimalpolynom / Haupträumen / Diagonalisierbarkeit / Linearfaktorzerlegung
  <details><summary>💡 Erklärung anzeigen</summary>
  <ul>
  <li><b>Linearfaktorzerlegung:</b> Damit eine Matrix überhaupt eine JNF hat, muss ihr charakteristisches Polynom vollständig in Linearfaktoren zerfallen (in $\mathbb{C}$ ist dies nach dem Fundamentalsatz der Algebra immer der Fall).</li>
  <li><b>Haupträume:</b> Reichen die Eigenvektoren nicht aus (algebraische Vielfachheit $>$ geometrische Vielfachheit), füllt man den Raum mit Hauptvektoren auf. Die direkte Summe aller Haupträume ergibt den Gesamtraum.</li>
  <li><b>Diagonalisierbarkeit:</b> Eine Matrix ist genau dann diagonalisierbar, wenn alle Jordan-Blöcke die Größe $1 \times 1$ haben. Dies ist der Fall, wenn das Minimalpolynom in einfache Linearfaktoren zerfällt (keine Exponenten $>1$).</li>
  <li><b>Minimalpolynom:</b> Das Minimalpolynom $\mu_A$ bestimmt die Größe des <i>größten</i> möglichen Jordanblocks zu jedem Eigenwert.</li>
  </ul>
  </details>

* Zusammenhang zwischen Reversibilität und Eigenwerten / Eigenvektoren (links und rechts)
  <details><summary>💡 Erklärung anzeigen</summary>
  Bei (markovschen) reversiblen Systemen (die dem "Detailed Balance"-Kriterium gehorchen) besteht eine enge Beziehung zwischen den Links- und Rechtseigenvektoren. Der stationäre Zustand (oder das Gleichgewichtsmaß) agiert als Vermittler: Die Matrix ist symmetrisierbar (über eine Diagonalmatrix der stationären Verteilung), weswegen Linkseigenvektoren simpel in Rechtseigenvektoren umgerechnet werden können und alle Eigenwerte zwangsläufig reell sind.
  </details>

* Zusammenhang zwischen Matrixexponential und Lösung einer Differentialgleichung
  <details><summary>💡 Erklärung anzeigen</summary>
  Das System linearer homogener Differentialgleichungen $\dot{y}(t) = A y(t)$ mit Anfangsbedingung $y(0) = y_0$ wird durch die Matrixexponentialfunktion gelöst: $y(t) = e^{At} y_0$. Es handelt sich um die exakte Verallgemeinerung der eindimensionalen DGL $f'(t) = a f(t) \Rightarrow f(t) = c \cdot e^{at}$. Die Matrix $A$ nimmt dabei den Platz des Skalars $a$ ein.
  </details>

* Zusammenhang zwischen Art der Matrix (z.B. orthogonal, unitär, $\det(A)=1$, $\det(A)<0$) und der linearen Abbildung
  <details><summary>💡 Erklärung anzeigen</summary>
  <ul>
  <li><b>Orthogonal ($\mathbb{R}$) / Unitär ($\mathbb{C}$):</b> Das bedeutet $\det(A)=\pm 1$. Die Matrix beschreibt eine "Isometrie" – Längen und Winkel zwischen Vektoren bleiben nach der Abbildung erhalten (eine starre Transformation).</li>
  <li><b>$\det(A) = 1$:</b> Die Abbildung ist orientierungserhaltend und volumentreu (z.B. eine reine Drehung).</li>
  <li><b>$\det(A) = -1$:</b> Die Abbildung ist volumentreu, aber orientierungs<i>umkehrend</i> (z.B. eine Spiegelung).</li>
  <li><b>$\det(A) < 0$:</b> Das Vorzeichen wechselt (aus einem Rechtssystem wird ein Linkssystem, anschaulich "Links- und Rechtshändigkeit" vertauscht).</li>
  </ul>
  </details>

* Zusammenhang zwischen Symmetrie/Symmetriebrechung und Symmetriegruppe/Untergruppe
  <details><summary>💡 Erklärung anzeigen</summary>
  Die kompletten Symmetrien eines Systems (z.B. eines Quadrats) bilden mathematisch eine <b>Gruppe</b>. Von einer "Symmetriebrechung" spricht man, wenn das System deformiert wird (z.B. vom Quadrat zum Rechteck gezogen). Das neue Objekt verliert einige Symmetrien (z.B. 90°-Drehungen). Die verbliebenen Symmetrien des deformierten Zustandes bilden dabei immer eine <b>Untergruppe</b> der ursprünglichen großen Symmetriegruppe.
  </details>

* Zusammenhang zwischen Skalarprodukten und Längen(=Norm)- und Winkelmessung
  <details><summary>💡 Erklärung anzeigen</summary>
  Das Skalarprodukt $\langle v|w \rangle$ stattet einen abstrakten Vektorraum mit einem Geometriebegriff aus. <br>
  <b>Länge (Norm):</b> $\|v\| = \sqrt{\langle v|v \rangle}$.<br>
  <b>Winkel:</b> Der Winkel $\theta$ zwischen reellen Vektoren ist definiert über $\cos(\theta) = \frac{\langle v|w \rangle}{\|v\| \|w\|}$. Wenn das Skalarprodukt $0$ ist, spricht man von Orthogonalität (Rechter Winkel, 90°).
  </details>

---

## Checkliste: Algorithmen

- allgemeine Lösung eines linearen Gleichungssystems (Bild-Kern-Algorithmus)
  <details><summary>💡 Erklärung anzeigen</summary>
  Mit dem Bild-Kern-Algorithmus (oder Gauß-Verfahren) formt man die erweiterte Koeffizientenmatrix auf reduzierte Zeilenstufenform um. Die Dimension des Lösungsraums (Kern) entspricht der Anzahl an Nullzeilen bzw. Spalten ohne Pivot-Element. Die allgemeine Lösung setzt sich immer zusammen aus: $\vec{x}_{allg} = \vec{x}_{partikulär} + \vec{x}_{homogen}$ ($\vec{x}_{homogen}$ ist die Linearkombination der Basisvektoren des Kerns).
  </details>

- Ausgleichsrechnung (Normalengleichung)
  <details><summary>💡 Erklärung anzeigen</summary>
  Für ein überbestimmtes System $Ax = b$ ohne exakte Lösung sucht man den Parametervektor $x$, der den Fehler minimiert (Methode der kleinsten Quadrate). Man multipliziert mit $A^T$ und löst das neue System (die "Normalengleichung"): $A^T A x = A^T b$. Dieses ist stets lösbar.
  </details>

- Berechnung der Inversen einer Matrix (Bild-Kern-Algorithmus)
  <details><summary>💡 Erklärung anzeigen</summary>
  Man schreibt die Matrix $A$ und die Einheitsmatrix $I$ nebeneinander: $(A | I)$. Durch Zeilenumformungen wandelt man die linke Seite in die Einheitsmatrix um. Die rechte Seite transformiert sich dabei automatisch zur inversen Matrix $A^{-1}$: $(I | A^{-1})$.
  </details>

* Berechnung der Eigenräume einer Matrix (Bild-Kern-Algorithmus)
  <details><summary>💡 Erklärung anzeigen</summary>
  Nachdem man einen Eigenwert $\lambda_i$ gefunden hat, sucht man den Raum aller Vektoren $v$, für die $(A - \lambda_i I)v = 0$ gilt. Das macht man einfach, indem man das homogene LGS zur Matrix $(A-\lambda_i I)$ löst (Gauß-Algorithmus). Der berechnete Kern ist exakt der Eigenraum.
  </details>

* Berechnung der Nullstellen eines Polynoms (pq-Formel, Linearfaktoren abspalten z.B. durch Horner-Schema)
  <details><summary>💡 Erklärung anzeigen</summary>
  Um die Eigenwerte zu erhalten, sucht man Nullstellen des charakteristischen Polynoms: $\chi_A(\lambda) = \det(A-\lambda I) = 0$. <br>
  <b>Bei quadratischen Termen:</b> Nutze $pq$-Formel oder Mitternachtsformel.<br>
  <b>Ab Grad 3:</b> Eine Nullstelle raten (oft 1, 0 oder -1), und danach das Polynom durch $(\lambda - \lambda_{geraten})$ per Polynomdivision abspalten. Das Horner-Schema bietet dafür eine rechenarme Schreibweise ohne $x$'se aufzuschreiben.
  </details>

* Berechnung der Determinante einer Matrix (Spalten/Zeilenumformung, Laplace, Leibniz, Sarrus)
  <details><summary>💡 Erklärung anzeigen</summary>
  <ul>
  <li><b>Sarrus:</b> Nur für $3 \times 3$-Matrizen! Diagonalen mit Plus addieren, Gegendiagonalen mit Minus subtrahieren.</li>
  <li><b>Laplace-Entwicklung:</b> Entwicklung nach einer Spalte oder Zeile mit den meisten Nullen. Das Vorzeichen richtet sich nach dem Schachbrettmuster $(-1)^{i+j}$.</li>
  <li><b>Gauß (Zeilenumformung):</b> Forme die Matrix zur Dreiecksmatrix um. Zeilenvertauschungen drehen das Vorzeichen ($-$). Die Determinante ist am Ende einfach das Produkt der Hauptdiagonalelemente.</li>
  </ul>
  </details>

- Euklidischer Algorithmus (für Polynome)
  <details><summary>💡 Erklärung anzeigen</summary>
  Dient der Bestimmung des größten gemeinsamen Teilers (ggT) zweier Polynome. Man teilt (Polynomdivision) das größere Polynom durch das kleinere und berechnet den Rest. Im nächsten Schritt teilt man das kleinere Polynom durch diesen Rest. Das wiederholt man, bis der Rest $= 0$ ist. Der letzte nicht-verschwindende Rest (normiert) ist der ggT.
  </details>

- Lösung des Distanzgeometrie-Problems (Realisierung einer Gram-Matrix)
  <details><summary>💡 Erklärung anzeigen</summary>
  Ist eine Menge von Distanzen zwischen Knoten gegeben, will man die relativen Koordinaten rekapitulieren. Man wandelt die Abstandsmatrix über Multidimensional Scaling (oder Torgerson-Borg-Verfahren) in eine Skalarproduktmatrix (Gram-Matrix) um. Da eine Gram-Matrix positiv semidefinit ist, kann sie per Eigenwertzerlegung in Koordinaten faktoriert werden (Spektralzerlegung der Gram-Matrix).
  </details>

* Berechnung von $\exp(A)$ mit $A=D+N$ und $DN=ND$ (Taylorreihe für Matrizen)
  <details><summary>💡 Erklärung anzeigen</summary>
  Man spaltet die Matrix $A$ in einen diagonalisierbaren ($D$) und nilpotenten ($N$) Teil auf, die miteinander kommutieren. Dann gilt $e^{D+N} = e^D e^N$. $e^D$ rechnet man direkt auf der Diagonale. Für $e^N$ nutzt man die Taylorreihe ($I + N + N^2 / 2 + \dots$), welche nach endlich vielen Termen abbricht, da $N^k = 0$.
  </details>

* Orthonormalisierung einer gegebenen Vektorraum-Basis (ONS, Gram-Schmidt)
  <details><summary>💡 Erklärung anzeigen</summary>
  Aus einer beliebigen Basis gewinnt man eine Orthonormalbasis. Der erste Vektor wird einfach der Länge nach normiert. Für jeden weiteren Vektor $v_k$ zieht man iterativ seine Projektion(en) auf alle bisherigen neuen Basisvektoren $e_j$ ($j<k$) ab, um einen orthogonalen Restvektor $\tilde{e}_k$ zu erhalten (Orthogonalisierung). Dieser Rest wird dann final durch seine eigene Länge dividiert (Normierung).
  </details>

* Berechnung der/des Projektionsmatrix/operators auf die Basis eines ONS (Summe dyadischer Produkte)
  <details><summary>💡 Erklärung anzeigen</summary>
  Ist eine Orthonormalbasis $e_1, \dots, e_k$ eines Unterraums gegeben, so kann die orthogonale Projektion $P$ auf diesen Raum berechnet werden als die Summe der äußeren ("dyadischen") Produkte der Basisvektoren: $P = \sum_{i=1}^k e_i e_i^T$. Alternativ (als Operator), wandelt man einen Vektor $v$ nach Formel aus: $P(v) = \sum \langle e_i | v \rangle e_i$.
  </details>

* Berechnung einer darstellenden Matrix auf Basis eines ONS (Galerkin)
  <details><summary>💡 Erklärung anzeigen</summary>
  Ist eine lineare Abbildung $T$ und eine Orthonormalbasis $\{e_j\}$ (ONS) gegeben, so stehen die Einträge der darstellenden Matrix $A$ in Zeile $i$ und Spalte $j$ (Galerkin-Einträge). Sie berechnen sich durch Skalarprodukt-Auswertung: $A_{ij} = \langle e_i | T(e_j) \rangle$. Dies nutzt die Eigenschaft der ONS aus.
  </details>

---

## Checkliste: Beweisen

* geometrische Aussagen beweisen über Nutzung komplexer Zahlen (geleitete Klausuraufgaben, sowie im Video „Geometrieaufgaben“ in der ersten Vorlesungswoche)
  <details><summary>💡 Erklärung anzeigen</summary>
  Geometrische Beziehungen (z.B. Orthogonalität, Drehung) lassen sich extrem effizient in Koordinaten der Form $z = a + ib$ formulieren.<br>
  <b>Rotation:</b> Eine Drehung um Winkel $\alpha$ entspricht einer Multiplikation mit $e^{i\alpha}$.<br>
  <b>Orthogonalität/Strecken:</b> Wenn der Vektor (als diff $z_2-z_1$) von der Division zweier Vektoren eine rein imaginäre Zahl liefert, sind sie senkrecht zueinander.
  </details>

* Alle Aussagen im „Ulmer Skript“ beweisen können (9. Woche)
  <details><summary>💡 Erklärung anzeigen</summary>
  (Dies schließt Standardbeweise zur Eigenwerttheorie und Linearen Unabhängigkeit ein. Typischer Ansatz: Setze $c_1 v_1 + \dots = 0$ und wende $A$ darauf an, um Koeffizienten auf Null zu zwingen).
  </details>

* Mit allen in den drei verlinkten Muster-Klausuren (11. bis 13. Woche) bewiesenen Aussagen Fragen des Typs „wahr oder nicht wahr“ beantworten können, jeweils mit einer selbst-formulierten Begründung
  <details><summary>💡 Erklärung anzeigen</summary>
  Bei „Wahr/Falsch“-Aufgaben ist rigorose Genauigkeit gefragt.<br>
  <b>Wahr:</b> Lässt sich oft durch Matrixeigenschaften abkürzen (z.B. Rang, Determinantenregeln wie $\det(AB)=\det(B)\det(A)$).<br>
  <b>Falsch:</b> Ein einziges, kurzes Gegenbeispiel (oft reicht die $2\times 2$ Einheits/Nullmatrix, oder eine simple Projektionsmatrix aus Nullen und Einsen) reicht völlig aus, um die Aussage zu widerlegen.
  </details>

* Zettel 6, Aufgabenpaket 3.1
  <details><summary>💡 Erklärung anzeigen</summary>
  Zieht oft auf formelle Verifikation wie „Unterraum-Kriterium prüfen“, „Nachweise von Gruppenaxiomen“ ab. Immer Schritt für Schritt die Axiome runterbrechen.
  </details>