from statsmodels.tsa.ar_model import AR

def predict(x, n):
    model = AR(x)
    res = model.fit(maxlag=3)
    return res.predict(len(x), len(x)+n-1)
