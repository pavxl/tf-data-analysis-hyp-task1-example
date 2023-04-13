import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 362844815

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    alpha = 0.1
    cnt, nb = np.array([x_success, y_success]), np.array([x_cnt, y_cnt])
    z, p = proportions_ztest(cnt, nb, alternative = 'larger')
    
    return p < alpha
