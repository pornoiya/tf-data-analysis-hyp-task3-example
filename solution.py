import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 146155552 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.01
  
    p = (ztest(x, value = 500,alternative = 'larger')[1])/2
    return p < alpha # Ваш ответ, True или False
