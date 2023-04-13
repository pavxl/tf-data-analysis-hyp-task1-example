import pandas as pd
import numpy as np


chat_id = 362844815

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.1
    _, p_value = proportions_ztest(
        [x_success, y_success], [x_cnt, y_cnt], alternative="smaller"
    )
    
    return p_value <= alpha
