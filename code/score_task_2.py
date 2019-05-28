# -*- coding: utf-8 -*-
"""
@author: Nabil Hossain
         nhossain@cs.rochester.edu
         Dept. Computer Science
         University of Rochester, NY
"""

'''
An evaluation script for task-2. 
'''

import sys
import pandas as pd
import numpy as np

def score_task_2(truth_loc, prediction_loc):
    truth = pd.read_csv(truth_loc, usecols=['id','label'])
    pred = pd.read_csv(prediction_loc, usecols=['id','pred'])
    
    assert(sorted(truth.id) == sorted(pred.id)),"ID mismatch between ground truth and prediction!"
    
    data = pd.merge(truth,pred)
    data = data[data.label != 0]
    accuracy = np.sum(data.label == data.pred)*1.0/len(data)
    
    print("Accuracy = %.3f" % accuracy)
    
    
if __name__ == '__main__':
    # expect sys.argv[1] = ../data/task-2/dev.csv
    # expect sys.argv[2] = ../output/task-2-output.csv

    score_task_2(sys.argv[1], sys.argv[2])