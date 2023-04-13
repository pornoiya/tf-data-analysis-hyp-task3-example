import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 146155552 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.01
    pval = mannwhitneyu(x, y, alternative="less").pvalue
    return pval < alpha
