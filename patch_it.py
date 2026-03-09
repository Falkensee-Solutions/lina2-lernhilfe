import re

def clean_old_explanations(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
         content = f.read()
    # Entferne die alten Quote-Blöcke komplett. Regex sucht nach allen eLehrer Blockquotes.
    content = re.sub(r'> \*\*🎓 eLehrer-Erklärung.*?\*\*\n(?:> .*\n)*\n?', '', content)
    with open(file_path, 'w', encoding='utf-8') as f:
         f.write(content)

def inject_tips(file_path, tips):
    clean_old_explanations(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        header_key = line.strip()
        
        if header_key in tips:
            # Check for existing details to avoid dup
            if i + 1 < len(lines) and '<details>' in lines[i+1] + (lines[i+2] if i+2 < len(lines) else ""):
                pass
            else:
                tip_content = tips[header_key]
                details_html = f"<details>\n<summary>🎓 <b>eLehrer-Erklärung einblenden</b></summary>\n<blockquote>\n{tip_content}\n</blockquote>\n</details>\n\n"
                if not out[-1].endswith('\n\n'):
                    if not out[-1].endswith('\n'):
                        out.append('\n')
                    else:
                        out.append('\n')
                out.append(details_html)
        i += 1
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(out)

tips_01 = {
    "## 1.1 Komplexe Zahlen": "Komplexe Zahlen sprengen den eindimensionalen Zahlenstrahl. Das 'i' ist im Grunde geometrisch eine 90-Grad-Drehung auf eine neue Achse (den Imaginärteil). Zweimal 90 Grad = 180 Grad, was exakt drehen auf die negative X-Achse und somit der Multiplikation mit -1 entspricht!",
    "### Definition": "Ein Vektorraum kann alles sein: Polynome, Matrizen, sogar Audiosignale. Solange du Objekte addieren und skalieren (strecken) kannst, bist du in einem Vektorraum.",
    "### Rechenregeln": "Plus/Minus ist einfaches Vektor-Schieben (wie im R²). Mal und Geteilt sind immer Kombinationen aus Streckung (Längen verändern) und Drehung (Winkel addieren).",
    "### Wichtige Eigenschaften": "Der Trick z * z-quer rettet uns in Klausuren oft aus der Patsche, um aus etwas Komplexem wieder eine handfeste reelle Zahl (den Radius im Quadrat) zu machen.",
    "### Polarform": "Merk dir: Die Polarform ist der Cheat-Code für Multiplikation! Statt ewig Klammern auszumultiplizieren, addierst du hier einfach die Winkel und nimmst die Radien absolut mal. Es visualisiert das Drehen im Raum direkt.",
    "### Geometrische Interpretation": "Prof. Weber liebt Geometrie! Merk dir: Konjugieren ist immer eine Spiegelung an der reellen Achse. Multiplizieren mit $e^{i\varphi}$ ist die exakte Drehung um den Ursprung.",
    "## 1.2 Quaternionen (kurz)": "Damit haben Hamilton und Grassmann den 3D-Raum verknüpft (das baut direkt auf komplexe Zahlen auf). Wichtigstes Detail: Das Kommutativgesetz bricht! a*b ist nicht mehr b*a, denn in 3D kommt es massiv darauf an, ob du erst um X oder erst um Y drehst.",
    "## 1.3 Vektorräume": "Verlasse gedanklich den Schul-Vektor (xyz-Pfeil). Abstraktion ist gefragt: Eine Lösungsmenge eines LGS, eine Menge von Differentialgleichungen – das sind alles abstrakte Vektoren.",
    "### Unterräume": "Ein Unterraum ist eine stabile, 'brave' Teilwelt. Wenn du auf einer 2D-Ebene im 3D-Raum bleibst und durch den Ursprung gehst, hast du so eine Welt. Wichtig: Die Null (Ursprung) MUSS immer drin sein!",
    "### Basis & Dimension": "Basis = Absolutes Raster. Nimmst du einen Vektor weg, erreichst du nicht mehr jeden Punkt (Erzeugendensystem kaputt). Tust du einen dazu, gibt es Redundanzen (Lineare Abhängigkeit). Die Dimension ist exakt die Mindest-Baustein-Zahl.",
    "### Lineare Abbildungen": "Lineare Abbildungen sind Transformationen, die das Gitter des Raumes nicht verbiegen, sondern nur gleichmäßig drehen/strecken/scheren. Jede lineare Abbildung kann man in eine Matrix übersetzen.",
    "### Dimensionsformel (Rangsatz)": "Die wohl wichtigste Intuition der Vorlesung! Du hast einen 3D-Raum (n=3). Die Matrix projiziert/quetscht ihn auf ein 2D-Blatt (Bild hat Dim 2). Wo ist die dritte Dimension hin? Sie wurde zu Null zerquetscht! Das ist der Kern (Dim 1)."
}

tips_02 = {
    "## 2.1 Bild-Kern-Algorithmus": "Dieser Algorithmus ist die praktische Umsetzung des Homomorphiesatzes. Du schaust, was nach der Abbildung real 'übrig bleibt' (Bild) und was durch die Skalierung 'getötet' wird (Kern).",
    "### Kern (Nullraum)": "Der Kern ist das 'Schwarze Loch' der Matrix. Alle Vektoren, die im LGS auf den Nullvektor abgebildet werden. Ein großer Kern bedeutet meistens massiven Informationsverlust bei der Abbildung.",
    "### Bild (Spaltenraum)": "Das Bild ist der komplette Raum, den du nach der Transformation noch erreichen kannst. Wenn die Matrix aus 3 Vektoren (Spalten) besteht, ist das Bild einfach der Schatten oder das Volumen, das diese drei Vektoren aufspannen.",
    "### Rang einer Matrix": "Die Dimension des Bildes. Wenn der Rang gleich der Anzahl der Spalten ist, hast du vollen Informationserhalt (Kern ist 0, die Abbildung ist injektiv).",
    "### Zusammenfassung der Zusammenhänge": "Injektiv = Keine zwei Werte crashen auf dasselbe Bild (Kern = 0). Surjektiv = Du triffst wirklich jeden Punkt im Zielraum (Bild füllt alles aus).",
    "## 2.2 Determinanten": "Die Determinante ist der Volumen-Faktor! Eine Det=2 bedeutet: Jedes Quadrat wird nach Transformation doppelt so groß. Det=0 bedeutet: Der Raum wurde so flachgedrückt, dass kein Volumen mehr bleibt (nicht umkehrbar).",
    "### Definition (Leibniz-Formel)": "Eher theoretisch wichtig. Praktisch zeigt sie, dass die Determinante sich aus allen Permutationen/Vertauschungen der Dimensionen errechnet. Vorzeichen prüfen nicht vergessen!",
    "### Rechenregeln (AUSWENDIG LERNEN!)": "Klassische Fehlerquelle: Eine Matrix skaliert man in JEDER Dimension. Also ist $det(\lambda \cdot A) = \lambda^n \cdot det(A)$ und NICHT nur $\lambda$. Stell dir vor, du verdoppelst einen 3D-Würfel in Länge, Breite und Höhe: Das Volumen wächst um $2^3 = 8$.",
    "### Laplace-Entwicklung": "Der rechenintensive Weg. Achte auf das Schachbrettmuster aus Plus/Minus bei den Vorzeichen, und nimm IMMER die Zeile/Spalte, wo die meisten Nullen stehen. Zeit ist wertvoll in der Klausur!",
    "### Geometrische Bedeutung": "Prof. Weber stellt hier seine Det=1 vs Det=-1 Fallen! Eine Spiegelung dreht den Raum komplett 'auf links' (Orientierung umgekehrt = negatives Volumen = Det -1). Eine Drehung hält die Orientierung aufrecht (Det +1).",
    "## 2.3 LGS-Theorie": "Hier fließen Analysis und Algebra zusammen. Wie löst man Probleme, die eigentlich nicht perfekt lösbar sind? Mit partikulärer Lösung plus Freiheitsgraden (dem Kern).",
    "### Lösungsstruktur von $Ax = b$": "Erinner dich an DGLs: Die Gesamtlösung ist IMMER = EINE richtige Speziellösung (partikulär) + die Gesamtheit aller Nullstellen (homogen, also der Kern).",
    "### Gauß-Algorithmus": "Er verändert den Lösungsraum nicht essentiell. Achtung: Durch die Umformungen bleibt der Kern zwar identisch, aber der Original-Spaltenraum (das Bild) kann visuell kippen. Deswegen muss man für die Basis des Bildes immer die SPALTEN DER ORIGINALMATRIX ablesen."
}

tips_03 = {
    "## 3.1 Grundbegriffe": "Beim Konzept Eigenwert gehen wir auf die Suche nach dem Einfachen: Welche Vektoren werden von der Matrix nicht aus der Bahn geworfen, sondern behalten stoisch ihre Richtung und werden lediglich skaliert?",
    "### Eigenwert & Eigenvektor": "Eigenvektoren sind die grundlegenden 'Rotations- oder Streckachsen' der Matrix. Wenn du einen Vektor auf diese Linien legst, tut die Matrix nichts anderes, als simple Vergrößerung / Verkleinerung.",
    "### Eigenraum": "Das ist einfach die komplette Menge aller Eigenvektoren zu der gleichen Skalierung (die auf derselben Geraden oder Ebene liegen), PLUS dem Nullvektor.",
    "### Charakteristisches Polynom": "Der Trick hier: Wir wollen, dass $(A - \lambda I)x = 0$ eine Lösung ungleich dem 0-Vektor hat. Das geht nur, wenn die Matrix nicht den vollen Rang hat und selbst einen Kern besitzt. Also muss ihre Determinante Null sein!",
    "## 3.2 Algebraische vs. Geometrische Vielfachheit": "Ein klassisches Prüfung-Stolperbeispiel. Algebraisch = 'Wie oft taucht die Lösung rechnerisch im Term auf?'. Geometrisch = 'Wie viele echte linear unabhängige Vektoren bekomme ich dafür tatsächlich raus?'.",
    "### Algebraische Vielfachheit (alg. VF)": "Sagt einfach, welchen Exponenten eine Nullstelle im Polynom hat. Wenn $\lambda=2$ eine dreifache Nullstelle ist, hat sie algebraische VF 3.",
    "### Geometrische Vielfachheit (geo. VF)": "Die Anzahl der linear unabhängigen Vektoren, die wir im Eigenraum finden. Die Dimension dieses Raums kann nie größer werden, als die algebraische Vielfachheit uns an Platz erlaubt.",
    "### Fundamentale Ungleichung": "Diese Ungleichung entscheidet über Leben (Diagonalisierbarkeit) und Tod (Krampf mit Jordan-Normalform). Wenn $geo < alg$, dann 'fehlen' uns Vektoren, die Matrix ist defekt.",
    "## 3.3 Diagonalisierbarkeit": "Das Wunsch-Szenario: Eine Diagonalmatrix lässt sich exponentiell super einfach ausrechnen (z.B. für DGLs!), weil man nur die Diagonale potenzieren muss. Keine überkreuzten Abhängigkeiten mehr.",
    "### Diagonalisieren: Algorithmus": "Man sucht die 'Zauber-Basis' S. Wendet man den Basiswechsel an: $S^{-1} A S$, dann verschwinden alle Nebendiagonalen und zurück bleiben nur saubere Streckfaktoren (die Eigenwerte) auf der Diagonalen.",
    "## 3.4 Defekt einer Matrix": "Defekt ist nur ein anderes Wort für 'Dimension des Kerns'. Wenn 0 ein Eigenwert ist, dann meint $Ax = 0x$ exakt den Kern, ergo ist die Dimension des Kerns gleich der geometrischen Vielfachheit des Eigenwerts 0.",
    "## 3.5 Beweis zu ONS und Eigenwerten (Klausuraufgabe 2.1!)": "Genau das kam in der Nachklausur! Der Trick ist die Assoziativität: $(v_1^T)v_1 = v_1^T v_1$, was das Skalarprodukt formt und bei einem ONS exakt 1 ergibt. Andere Kreuzprodukte $v_2^T v_1$ sind 0, weil sie senkrecht aufeinander stehen. Damit löst sich die eklige Summe sofort in Rauch auf.",
    "## 3.6 Zusammenhang: Eigenwerte und Matrixeigenschaften": "Hier kann man Prof. Webers True/False-Aufgaben in Sekunden knacken: Orthogonal heißt alle EW haben Betrag 1. Symmetrisch heißt alle EW sind reell. Nilpotent heißt, die Matrix zerschießt sich selbst, also ist jeder EW zwingend 0."
}

tips_04 = {
    "## 4.1 Skalarprodukte – Axiome": "Das Skalarprodukt ist letztlich nur das Mathe-Wort für ein Werkzeug, das universell Längen messen und Winkel (Orthogonalität) zwischen zwei Elementen berechnen kann.",
    "### Reelles Skalarprodukt": "Das simple Punktprodukt aus der Schule. $x_1 y_1 + x_2 y_2$. Es ist zu sich selbst immer komplett symmetrisch.",
    "### Komplexes Skalarprodukt (hermitesch) ← **KLAUSURRELEVANT!**": "Im Komplexen droht ein Problem: Multipliziert man i mit sich selbst, ergäbe das eine negative Länge (-1). Darum muss im Skalarprodukt das erste Argument IMMER konjugiert werden! Dabei gilt: $\langle u|v\rangle = \overline{\langle v|u\rangle}$.",
    "### Standard-Skalarprodukte": "Denk daran: Integrale sind das absolute Äquivalent zur Vektor-Summe, wenn du von diskreten Spaltenvektoren zu kontinuierlichen Funktionen wechselst. Ein Integral über $f(x)g(x)$ IST ein Skalarprodukt.",
    "### Norm (durch Skalarprodukt induziert)": "Jedes Skalarprodukt eines Vektors mit sich selbst ergibt die quadrierte Länge. Wenn du am Ende die Wurzel ziehst, ist dein Vektor 'genormt' (Länge 1).",
    "## 4.2 Orthogonalität": "Zwei Vektoren (oder Funktionen!) haben absolut keine Berührungspunkte, keine gemeinsame Richtung. Sie spannen den Raum maximal breit auf.",
    "### Definitionen": "Orthogonal = Senkrecht (Skalarprodukt = 0). Orthonormal = Senkrecht UND auf Länge 1 normiert. Ein ONS ist wahnsinnig bequem zu rechnen, da fast jede Multiplikation in 0 oder 1 zerfällt.",
    "### Orthogonales Komplement": "Das ist genau die Menge aller Vektoren im Raum, die auf deinem Unterraum senkrecht stehen. Wenn du auf dem flachen Fußboden deines Zimmers stehst, ist das Komplement genau die Achse, die zur Decke zeigt.",
    "## 4.3 Gram-Schmidt-Verfahren – Schritt für Schritt": "Der systematische 'Schatten-Auslöscher'-Algorithmus. Wir wollen saubere Orthogonalachsen formen, indem wir iterativ immer das abziehen, was nicht senkrecht ist.",
    "### Algorithmus": "Wenn du von $v_2$ den Term $\langle u_1|v_2\rangle u_1$ subtrahierst, schneidest du genau den Schatten ab, den $v_2$ auf $u_1$ wirft. Zurück bleibt genau der Teil, der strikt senkrecht absteht. Das klappt exakt so auch mit Polynomen!",
    "## 4.4 Klausuraufgabe 3 – Komplette Musterlösung": "Hier haben fast alle Punkte verloren! Beim komplexen Integral wird die Konjugation vergessen. Wenn du $ix$ in den linken Slot des Skalarprodukts knallst, MUSS das Integral mit $-ix$ (konjugiert) weiterrechnen sonst wird das Ergebnis falsch.",
    "## 4.5 Projektionsoperatoren": "Wenn man eine zu schwere Gleichung lösen will, projiziert man sie mit $P_U$ auf einen einfacheren Unterraum. Das stutzt die Gleichung auf das Wesentliche zurück.",
    "### Orthogonalprojektion auf einen Unterraum": "Hast du eine ONS-Basis, baust du dir deine Projektion direkt aus Summen zusammen. Alles, was nicht reinpasst, fällt atomar zu Null ab.",
    "### Eigenschaften": "$P^2 = P$ (idempotent) heißt: Wenn ich einmal einen Taschenlampenschatten auf den Boden geworfen habe, bleibt es der exakt selbe Schatten, wenn ich die Lampe nochmal von oben drauf scheinen lasse."
}

tips_05 = {
    "## 5.1 Jordan-Normalform (JNF)": "Hier wird's manchmal unübersichtlich. Die JNF ist das Notpflaster der Linearen Algebra, wenn eine Matrix einfach nicht genug Eigenvektoren hat, um sie sauber zu diagonalisieren. Wir retten, was zu retten ist.",
    "### Jordan-Block": "Warum stehen da Einsen über der Diagonale? Sie bedeuten geometrisch: Die Matrix greift den Vektor, und anstatt ihn nur zu strecken, schubst sie ihn anteilig in die Richtung des vorherigen Vektors. Das erzeugt eine Verkettung (Jordan-Kette).",
    "### Jordan-Normalform": "Ein hübscher Block-Baukasten. Wir sortieren die Matrix so um, dass die Blöcke als geschlossene Ketten-Einheiten auf der Diagonale rumhängen.",
    "### Was man aus der JNF ablesen kann": "Anzahl der Blöcke pro Eigenwert = Geometrische Vielfachheit. Summe der Block-Dimensionen = Algebraische Vielfachheit. Det(A) = Alles auf der Diagonale multiplizieren. Spur = Alles addieren.",
    "## 5.2 Klausuraufgabe 1 – Analyse der JNF": "Der absolute Klassiker. Ein 2x2 Block und zwei 1x1 Blöcke, alle zu Eigenwert -1. Alles, aber wirklich alles, lässt sich durch Hinsehen lösen.",
    "### 1.1: Charakteristisches Polynom": "Bestimmt sich durch die gesamte Diagonale: Da die -1 dort genau viermal steht, ist das Polynom simpel $(\lambda - (-1))^4$.",
    "### 1.2: Minimalpolynom": "Bestimmt sich nur durch den GRÖSSTEN Block pro Eigenwert. Da der größte Block 2x2 ist, hat die Klammer den Exponenten 2.",
    "### 1.3: Eigenraum zum Eigenwert -1": "Wie groß ist der Eigenraum (geo. VF)? So viele linear unabhängige Eigenvektoren wie wir Jordan Blöcke haben. Bei 3 Blöcken ist die Dimension 3.",
    "### 1.4: Geometrische Vielfachheiten": "Geo = 3 (wegen 3 Blöcken). Alg = 4 (da die Nullstelle 4-mal auf der Diagonale vorkommt).",
    "### 1.5: Hauptvektor erster Stufe": "Ein Vektor der 'zweiten Reihe'. Er wird durch die Matrix erst in den Eigenvektor reingerutscht und braucht zwei Zyklen $(A-\lambda I)^2$, um komplett die Null zu treffen.",
    "### 1.6: Determinante": "Einfach ALLE Diagonaleinträge multiplizieren: $(-1) \cdot (-1) \cdot (-1) \cdot (-1) = 1$.",
    "### 1.7: Volumentreu?": "Ja! Wenn $|\det(A)| = 1$, bleibt das Volumen im Raum unverändert. Die Matrix quetscht das Volumen in der einen Richtung, dehnt es aber exakt kompensierend in einer anderen aus.",
    "### 1.8: Orientierungserhaltend?": "Determinante ist +1, also bleibt das räumliche Koordinatensystem wie es ist ('Rechts bleibt Rechts'). Bei -1 wäre das Volumen gleich geblieben, aber der Raum wäre invertiert / gespiegelt worden.",
    "### 1.9: Kann $A$ symmetrisch sein?": "Der Lieblingstrick für Zusatzaufgaben. Gemäß dem Spektralsatz sind symmetrische reelle Matrizen IMMER komplett diagonalisierbar! A hat aber einen 2er Jordanblock (nicht diagonalisierbar), also ist es völlig unmöglich, dass sie ursprünglich symmetrisch war!",
    "## 5.3 Haupträume und Hauptvektoren": "Wenn dir echte Eigenvektoren fehlen, nimmst du Hauptvektoren als Lückenfüller für deine Basis. Das sind Vektoren, die eine Reaktionskette bilden.",
    "### Hauptraum": "Zusammenfassung aller Hauptvektoren, die zu einem Eigenwert gehören. Jeder Eigenraum wohnt im Inneren seines Hauptraumes.",
    "### Hauptvektor der Stufe $k$": "Er wird durch die Anwendung von $(A - \lambda I)$ erst auf den k-1'ten Vektor verwandelt, dann auf den k-2'ten... und landet exakt nach der k-ten Anwendung im Nullraum.",
    "## 5.4 Minimalpolynom": "Das ist das 'effizienteste' Polynom. Wenn du in dieses Polynom deine Matrix A einsetzt, kommt am Ende garantiert die Nullmatrix heraus.",
    "### Definition": "Es hat dieselben Nullstellen wie das Charakteristische Polynom, macht die Exponenten aber nur so hoch wie unbedingt nötig (Länge des größten Jordan-Blocks für den EW).",
    "### Eigenschaften": "Bei einer strikten Diagonalmatrix ist das Minimalpolynom absolut minimal, da jede Nullstelle nur Potenz 1 braucht, um die Matrix zu löschen.",
    "### Berechnung ohne JNF": "Man rechnet es meist iterativ aus, indem man Terme hochpotenziert $(A-\lambda I)$, bis tatsächlich die Nullmatrix entsteht.",
    "## 5.5 Satz von Cayley-Hamilton": "Ein gigantisch starkes Matrix-Konzept. 'Jede Matrix ist Nullstelle ihres eigenen char. Polynoms'. Heißt: A reingesteckt in $\chi(X)$ ergibt IMMER null.",
    "### Anwendung (Klausuraufgabe 4!)": "Extrem nützlich, um Matrixpotenzen zu kürzen! Wenn $A^2 - A = 0$ gilt, wie in der Klausur, dann weiß man, dass unendlich hohe Potenzen wie $A^{100}$ einfach auf A kollabieren. Kein ewiges Multiplizieren!",
    "## 5.6 Matrixexponential – Allgemein": "Wofür das alles in der Praxis da ist: Viele Differentialgleichungen von Schwingungen in der Physik hängen an $y' = Ay$. Ein Matrix-Exponential löst diese Naturgesetze auf.",
    "### Definition": "Die klassische Taylorreihe der Schul-e-Funktion, nur eben mit Matrizen. Bei Jordan-Blöcken hat das die geniale Eigenschaft, dass die Taylorreihe durch das 'nilpotente' Verhalten der 1en rasant abbricht!",
    "### Rechenregeln": "Höchste Vorsicht: $e^{A+B}$ ist NUR dann aufteilbar in $e^A \cdot e^B$, wenn die Matrizen vertauschen ($A \cdot B = B \cdot A$).",
    "### Für Diagonalmatrizen": "Zuckerschlecken! Man packt einfach das $e^\lambda$ an jeden Diagonaleintrag. Komplett triviale Berechnung.",
    "### Anwendung: DGL": "Löst dir deine linearen DGL-Systeme auf den Punkt durch einfaches Einsetzen von $y(t) = e^{t \cdot A} y(0)$."
}

tips_06 = {
    "## 6.1 Bilinearformen": "Denk an Bilinearformen als ein verallgemeinertes Skalarprodukt. Eine Maschine, die zwei Vektoren als Input frisst und dir dazu passend genau einen reellen Wert/Skalar ausspuckt.",
    "### Definition": "Es ist in extremem Maß linear: Streckst du Vektor $u$ ums Dreifache, wächst das Endergebnis um x3. Addierst du Vektoren im Argument, addiert sich das Ergebnis. Exakt wie Flächengeometrie.",
    "### Sesquilinearform (Halbilinearform)": "WICHTIG in Klausuren! Das komplexe Integral ist im 1. Argument stets 'antilinear'. Zieht man dort ein $i$ aus der Klammer, wandert es als komplex konjugiertes $-i$ nach draußen.",
    "### Darstellungsmatrix": "Jede Bilinearform kann durch schlichte Matrizen-Multiplikation formuliert werden: $v^T A w$. Das $A$ ist das Herzstück der Maschine.",
    "### Symmetrie/Antisymmetrie": "Ist die Matrix $A=A^T$ (symmetrisch), dürfen links und rechts die Inputs getauscht werden. Antisymmetrie begegnet dir ständig als Kreuzprodukt in der Physik.",
    "## 6.2 Quadratische Formen": "Du steckst zwei mal den GLEICHEN Vektor v in die Formel hinein: $Q(v) = v^T A v$. Grafisch im Raum erzeugt das z.B. Parabolstäbe oder Schüsseln (wie $x^2 + y^2$).",
    "### Signatur": "Sylvester sagt: Auch wenn du dein Koordinatensystem brutal verbiegst, die Anzahl der '+', '-', und '0' Vorzeichen bleibt gleich. $(+,+)$ formt eine Schale nach oben, $(+,-)$ einen Pringles-artigen Sattel.",
    "## 6.3 Adjungiertheit": "Adjungiert = Das große Gegenstück. Wie bei komplexen Zahlen das Konjugieren, nur eben für Matrizen. Bei reellen Matrizen ist es einfach nur Matrix transponieren $\rightarrow A^T$.",
    "### Definition": "Wenn du im Skalarprodukt die Matrix von der linken auf die rechte Seite der Gleichung schubsen willst, musst du sie adjungieren. $\langle Ax | y\rangle = \langle x | A^* y\rangle$.",
    "### Konkret": "Der Standard-Move im Komplexen: Diagonale spiegeln (transponieren) UND sofort noch jedes 'i' zu einem '-i' machen.",
    "### Spezialmatrizen": "Selbstadjungiert heißt Matrix = Matrix*. In der Quantenphysik garantiert das z.B., dass Messwerte der Schwingungen absolut reell bleiben.",
    "## 6.4 Trigonalisierbarkeit": "Wenn Diagonalisieren scheitert (wie z.B. bei reinen Rotationsmatrizen, die keine reellen EW haben), formen wir in den komplexen Zahlen wenigstens eine hübsche obere Dreiecksmatrix.",
    "### Satz": "Über den komplexen Zahlen $\mathbb{C}$ hat wirklich jedes Polynom eine Wurzel. Deswegen ist das dort immer garantiert machbar. Im Reellen versuchen uns Rotationen das Leben schwerzumachen.",
    "### Schur-Zerlegung": "Der Beweis, dass wir diese Dreiecksstruktur durch eine absolut ordentliche Transformationsmatrix U erreichen, die selbst Isometrien (Basiswinkel) erhält.",
    "## 6.5 Isometrien": "Transformationen absoluter Unveränderlichkeit! Weder stauchen noch strecken sie den Raum. Abstände zwischen Objektpunkten bleiben beim Bewegen erhalten.",
    "### Definition": "Längentreu bedeutet: $\Vert f(v) \Vert = \Vert v \Vert$. Der komplette Zielraum wird als starrer Block gedreht oder an einer Achse geklappt.",
    "### Orthogonale Matrizen ($\mathbb{R}^n$)": "Bestehen in Spalten und Reihen aus ONS-Einheitsvektoren. Orthogonal-Fehlerfalle für Klausuren beachten: Es kann auch eine negative Determinante haben, dann ist es keine reine Drehung, sondern eine Spiegelung!",
    "### Unitäre Matrizen ($\mathbb{C}^n$)": "Das komplexe Bruder-Gegenstück zur Isometrie. Da $A^* A = I$ gilt, liegen alle komplexen Eigenwerte genau auf einem Kreisring mit dem Maß-Betrag 1.",
    "## 6.6 Grundlagen der Gruppentheorie": "Muss man für die Klausur einordnen können! Gruppen sind abgeschottete Welten (Mengen) mit einer Verknüpfung, aus der man nie zufällig 'herausrechnen' kann (Abgeschlossenheit).",
    "### Gruppe": "Die 3 Grundsäulen: Du hast ein Element, das nichts tut (Nullvektor/Identität). Du kannst Aktionen rückgängig machen (Inverses/Subtraktion). Und die Ausführung bleibt in der Menge.",
    "### Wichtige Beispiele": "$O(n)$ = Komplettes Set von Rotationen und spiegelnden Umklappungen. $SO(n)$ = 'Spezielle' Orthogonalgruppe, die Determinante ist strickt +1 (also absolute reine Drehung im Raum).",
    "### Untergruppen": "Ein elitärer Zirkel innerhalb der Gruppe. So bilden Drehungen stets eine Untergruppe, reine Spiegelungen aber z.B. nicht (da Spiegelung hinter Spiegelung sofort in Drehung verfällt – du fällst aus dem Club raus!).",
    "### Körper": "Sämtliche Regeln unserer Schulmathematik komprimiert. Plus, mal, minus, geteilt – es geht alles (außer geteilt durch 0). Ob reelle Zahlen, komplexe, oder kleine Restklassenkörper – hier klappen alle Vektorraum-Skalaraxiome vollumfänglich.",
    "## 6.7 Reversibilität": "Ein Zusatzkonzept. Wenn Operatoren die Vorzeichen in der Matrix unter bestimmten Spiegelungs-Strukturen komplett invertieren. (Gibt es z.B. für Systeme mit vertauschter Zeitrichtung)."
}

inject_tips("lina2-lernhilfe/markdown/01_Komplexe_Zahlen_Vektorraeume.md", tips_01)
inject_tips("lina2-lernhilfe/markdown/02_Bild_Kern_Determinanten.md", tips_02)
inject_tips("lina2-lernhilfe/markdown/03_Eigenwerte_Diagonalisierung.md", tips_03)
inject_tips("lina2-lernhilfe/markdown/04_Skalarprodukte_GramSchmidt.md", tips_04)
inject_tips("lina2-lernhilfe/markdown/05_JNF_Minimalpolynom_CayleyHamilton.md", tips_05)
inject_tips("lina2-lernhilfe/markdown/06_Bilinearformen_Isometrien_Gruppen.md", tips_06)

print("Patching completed!")
