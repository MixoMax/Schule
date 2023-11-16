
## Buch S. 287
1,2,3,5

1) Nehmen sie Stellung zu der Aussage "ultraviolettes Licht ist energiereicher als infrarot"

	Aufgrund der Definition der Energie eines Photons:
	$E=h \cdot f$ 
	ist die Energie direkt abhängig von der Frequenz $f$ des Photons. je höher die Frequenz, desto höher ist die Energie des Photons. Ultraviolettes Licht hat eine signifikant höhere Frequenz als infrarotes Licht. Somit ist die Aussage, dass ultraviolettes Licht energiereicher als infrarotes Licht sei, korrekt.

2) Beschreiben sie ein Experiment, bei dem die Grenzen des Wellenmodels für das Licht deutlich werden

	die Grenzen des Wellenmodells werden bei solchen Experimenten erreicht, die nur Erfolgreich sind, wenn Licht eine Teilchen ("Photon") ist. Dies ist zum Beispiel bei dem Experiment zur Feststellung der Austrittsenergie der Fall. Der Versuchsaufbau schickt Photonen entgegen der Richtung eines Elektromagnetischen Feldes. Auf der anderen Seite des Elektromagnetischen Feldes ist ein Sensor, der erkennt, ob Photonen Ankommt. Wenn nun die Feldstärke des Elektromagnetischen erhöht wird, gibt es eine Feldstärke, wo die Photonen nicht mehr genug Energie haben, um den Sensor zu erreichen, weil sie von dem Elektromagnetischen Feld aufgehalten werden. Wenn Licht eine Welle sei, würde es trotzdem ankommen, aber mit linear weniger Energie. Wenn Licht ein Teilchen ist, kommt es entweder an, oder nicht.
	Aus dem Experiment hat sich ergeben, dass Licht entweder ankommt, oder nicht.

3) Erläutern sie den Begriff Austrittsenergie und beschreiben sie, wie sich die Austrittsenergie eines Materials experimentell ermitteln lässt.

	Die Austrittsenergie ist die Energie, die ein Photon beim Austritt 
	!TODO

5) Eine Metallplatte wird mit UV-Licht ($\lambda = 230$ nm) bestrahlt. Aus dem Metall werden Elektronen mit einer Maximalenergie von 1,8eV ausgelöst. Bestimmen sie die Austrittsenergie

Gegeben:
$\lambda = 0.000000230$ m
Maximalenergie = $1.8eV$
$f = {c \over \lambda} = 1303445469565217.5$ hz


Gesucht:
$E_A$

Rechnung:
$E_{Max} = E_Phot - E_A$

$E_A = E_{phot} - E_{Max}$

$E_A = h*f - E_{Max}$
$E_A = 6.626*10^{-34} * 1303445469565217.5 - 1.8$
$E_A = 8.636629681339131*10^{-19}J - 2.88*10^{-19}$
$E_A = 5.756629681339132*10^{-19}$


## Photonenimpuls

pass

## Strahlungsdruck

Buch S. 289)

1) Entscheiden sie, ob Sonnensegel reflektierend oder schwarz ausgeführt werden sollten
	Schwarz
2) Begründen sie, dass kleine Partikel stärker vom Strahlungsdruck beeinflusst werden als große
	Die Energie, die Strahlungsdruck auf ein Objekt übertragen kann ist proportional zu der Oberfläche des Objektes. 
	In Relation zu dem Durchmesser steigt die Oberfläche zum Quadrat ($A=d^2$).
	Die Beschleunigung hängt aber auch von der Masse des Teilchens ab. Diese wächst im Verhältnis zum Durchmesser mit dem Kubik ($m=d^3$). Dies bedeutet, dass die Masse signifikant mit der Größe wächst als die Oberfläche. Um so größer das Teilchen, je weniger Oberfläche pro Masse.
3) Ein kleiner Meteorit (d=1) wird von der Sonne mit einer Leistung von 500W bestrahlt. Schätzen sie ab, nach welcher Zeit sich seine Geschwindigkeit dadurch um 1m/s ändert. Treffen sie dazu ggf. vereinfachende Annahmen über die Energie der Photonen.

gegeben:
d = 1m
m = 2500kg
P = 500w
v = 1m/s
$\lambda = 580nm = 580e-9$m



gesucht:
t


### Lösungsansatz 1: E_kin

$E_kin = 0.5*m*v^2$
$v = 2*{E_kin \over m}$

$v(t) = 2*((P*t)/m)$


v(t) = 1

$v(2.5) = 2*((500*2.5)/2500)$

$v(2.5) = 2*(1250/2500)$
$v(2.5) = 2*0.5 = 1$


### Lösungsansatz 2: Photonenanzahl

$E_phot = h*c/\lambda$
$E_phot = 6.626e-34 * 299792458 / 580e-9$
$E_Phot = 3.4248703908758624*10^{-19} J$

$500 J/S = n * 3.425*10^{-19}$
$500/3.425*10^{-19} = n$
$n = 1.46*10^{21}$ p/s

$1250 = 3.36e-19 * n$
$n = 3.72e21$

$t = 3.72e21/1.46e21$

$t \approx 2.5$s


### Lösungsansatz 3:

Anzahl Photonen pro sekunde:
$n = 1.46*10^{21}$ p/s

$E_Phot =3.425*10^{-19} J$
$E_Phot = 5.5 * 10^{-38} eV$


