# -*- coding: utf-8 -*-
"""
@author: Nabil Hossain
         nhossain@cs.rochester.edu
         Dept. Computer Science
         University of Rochester, NY
"""

'''
A naive baseline system for task 2

This baseline always predicts the most frequent label in the training set.
'''

import pandas as pd
import numpy as np
import sys
import os

def baseline_task_2(train_loc, test_loc):
    train = pd.read_csv(train_loc)    
    test = pd.read_csv(test_loc)

    pred = np.argmax(train['label'].value_counts())
    test['pred'] = pred
    
    output = test[['id','pred']]    
    out_loc = '../output/task-2-output.csv'
    output.to_csv(out_loc, index=False)
    
    print('Output file created:\n\t- '+os.path.abspath(out_loc))
    
if __name__ == '__main__':
    
    # expect sys.argv[1] = ../data/task-2/train.csv
    # expect sys.argv[2] = ../data/task-2/dev.csv
    baseline_task_2(sys.argv[1], sys.argv[2])

        