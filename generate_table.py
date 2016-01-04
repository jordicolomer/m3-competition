import pandas as pd

test = {}
train = {}
M3C = pd.ExcelFile('M3C.xls')
for sheet in 'M3Year M3Quart M3Month M3Other'.split():
    M3Year = M3C.parse(sheet).as_matrix()
    for row in M3Year:
        series = row[0]
        N = row[1]
        NF = row[2]
        train[series] = row[6:6+N-NF]
        test[series] = row[6+N-NF:6+N]

print 'method,MAPE'
M3Forecast = pd.ExcelFile('M3Forecast.xls')
for sheet in M3Forecast.sheet_names:
    m = M3Forecast.parse(sheet, header=None).as_matrix()
    MAPE = 0
    n = 0
    for row in m:
        series = row[0]
        NF = row[1]
        pred = row[2:2+NF]
        true = test[series]
        MAPE += abs(pred[0]-true[0])/((pred[0]+true[0])/2)*100
        n += 1
    print sheet, "%.1f" % (MAPE/n)

for module_name in 'last ar'.split():
    predictor = __import__(module_name)
    MAPE = 0
    n = 0
    for series in train:
        true = test[series]
        pred = predictor.predict(train[series], len(true))
        MAPE += abs(pred[0]-true[0])/((pred[0]+true[0])/2)*100
        n += 1
    print module_name, "%.1f" % (MAPE/n)
