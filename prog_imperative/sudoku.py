import numpy as np
import random as rd

sudoku = np.loadtxt("")
zeros = np.where(sudoku==0)
trouve=False

def acceptable(sudoku,val,pos):
    if val in sudoku[pos[0],:]: return False
    if val in sudoku[pos[:,pos]]: return False
    return True

def solution(sudoku,ei,zeros):
    global trouve
    if ei==len(zeros[0]):
        trouve=True; return
    for val in [1,2,3,4,5,6,7,8,9]:
        pos = zeros[ei]
        if acceptable(sudoku,val,pos):
            sudoku[pos[0], pos[1]] =val
            solution(sudoku, ei+1, zeros)
            if trouve : return
            sudoku[pos[0], pos[1]] =0