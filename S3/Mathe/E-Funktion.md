
Asymptotisches Verhalten -> eine funktion schneidet fast aber gerade so nicht

## Aufgabe 1

Eine Mikrobenpopulation wächst täglich 1,6x
zum beobachtungsbegin sind 200 Mikroben vorhanden

$N(t) = 1,6^t * 200$


$f(t) = 0,7^t * 2$


# logarithmen

Ein Logarithmus wird benutzt, wenn man rausfinden möchte, wie häufig man etwas mit sich selbst multiplizieren muss, damit ein Ergebnis rauskommt:

$Startwert * Basis ^{exponent}= Potenzwert$
$2^x = 8$

kann umgeschrieben werden zu:

$\log_{Basis}({Potenzwert\over Startwert}) = Exponent$
$\log_2(8)=x$

Der Logarithmus ist nur für Positive Zahlen definiert, also muss gelten:
$Basis > 0$  ; $Potenzwert > 0$

Außerdem ist die Basis 1 nicht definiert:
$Basis \neq 1$

### Natürlicher Logarithmus

der Natürliche Logarithmus ist eine normaler Logarithmus mit einer bestimmten Basis. Beim Natürlichen Logarithmus ist die Basis immer Eulers Zahl $e$ , ohne das es spezifiziert wird.

daher gilt:

$\ln(Potenzwert) = \log_e(Potenzwert)$

### Logarithmusgesetze

1. $\log_b(u*v) = \log_b(u)+\log_b(v)$
2. $\log_b({u \over v}) = \log_b(u) - \log_b(b)$
3. $\log_b(u^a) = a*\log_b(u)$
4. $log_u(v) = {log_b(v) \over log_b(u)}$ für irgendeine positive reele b != 0 und b != 1


## Aufgabe 2

$N(t) = 200 * 1,6^t$

N(t) = 1000
$1000 = 200*1,6^t$
$\log_{1,6}(1000/200)$
$\log_{1,6}(5) \approx 3,424$


### Buch s. 270 / 271

### Übung 2

Müller:
$m(t) = 10000*1,05^t$
m(t) = 20000

$\log_{1,05}({20000 \over 10000}) = t$
$\log_{1,05}(2) = t$
$t = 14,2$



Dorn
$d(t) = 8000*1,07^t$
d(t) = 20000

$t = \log_{1,07}(20000/8000)$
$t = 13,55$


d(t) + m(t) = 30000

$t = \log_{1,05}(30000/10000)+\log_{1,07}(30000/8000)$



### Übung 3
Usa:
1998 = $274*10^6$
2050 = $350*10^6$
Kumulatives Prozentuales Wachstum:  27,7%

Bangladesch:
1998 = $106*10^6$
2050 = $213*10^6$
Kumulatives Prozentuales Wachstum: 100,9%

Bangladesch hat ein signifikant höheres Bevölkerungswachstum.



## Aufbau einer Exponentialfunktion

$f(x) = c*a^{m*x+b} + d$

| Variable | Sinn | Einschränkung |
|---|---|---|
| c | Startwert -> Streckt bzw. Staucht | - |
| a | Basis -> Wachstumsrate | > 0; != 1 |
| m | Steigungsshit | - |
| x | Fortlaufende Variable | - |#
| b | idk lol | - | 
| d | Verschiebung auf der Y Achse | - |


## Ableitung von Exponentiallfunktionen

$f(x) = b^x$
$f´(x) = b^x*\ln(b)$
