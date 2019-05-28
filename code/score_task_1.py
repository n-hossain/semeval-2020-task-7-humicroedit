# -*- coding: utf-8 -*-
"""
@author: Nabil Hossain
         nhossain@cs.rochester.edu
         Dept. Computer Science
         University of Rochester, NY
"""

'''
An evaluation script for task-1. 
'''

import sys
import pandas as pd
import numpy as np

def score_task_1(truth_loc, prediction_loc):
    truth = pd.read_csv(truth_loc, usecols=['id','meanGrade'])
    pred = pd.read_csv(prediction_loc, usecols=['id','pred'])
    
    assert(sorted(truth.id) == sorted(pred.id)),"ID mismatch between ground truth and prediction!"
    
    data = pd.merge(truth,pred)
    rmse = np.sqrt(np.mean((data['meanGrade'] - data['pred'])**2))
    
    print("RMSE = %.3f" % rmse)
    
    
if __name__ == '__main__':
    # expect sys.argv[1] = ../data/task-1/dev.csv
    # expect sys.argv[2] = ../output/task-1-output.csv

    score_task_1(sys.argv[1], sys.argv[2])