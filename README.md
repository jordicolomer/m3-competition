# m3-competition

In this project we evaluate and compare a number of time-series forecasting methods againt the well known m3 competition (https://en.wikipedia.org/wiki/Makridakis_Competitions)

See the paper [1] included in this repository for more details and results about the competition.

Currently we test the following methods:
- last: it just copies the last element of the series
- ar: Univariate Autogressive Processes (statsmodels package implementation)

METHOD MAPE

NAIVE2       10.5

SINGLE       9.5

HOLT         9.0

DAMPEN       8.8

WINTER       9.1

COMB S-H-D   8.9

B-J auto     9.2

AutoBox1     9.8

AutoBox2     9.5

AutoBox3     9.8

ROBUST-Trend 10.5

ARARMA       9.7

Auto-ANN     9.4

Flors-Pearc1 9.2

Flors-Pearc2 10.0

PP-Autocast  9.1

ForecastPro  8.6

SMARTFCS     9.2

THETAsm      9.5

THETA        8.4

RBF          9.9

ForcX        8.7

AAM1         9.8

AAM2         10.0

last         11.6

ar           10.6

[1] Makridakis, Spyros, and Michele Hibon. "The M3-Competition: results, conclusions and implications." International journal of forecasting 16.4 (2000): 451-476.
