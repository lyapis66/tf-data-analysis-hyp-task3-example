import pandas as pd
import numpy as np


chat_id = 1882360450 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    from statsmodels.stats.weightstats import ztest as ztest
    a,p=ztest(x, value= 500, alternative="smaller")
    if p<=0.02: 
        answer=True
    else:
        answer=False

    return answer
