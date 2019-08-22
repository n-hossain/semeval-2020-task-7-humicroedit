# Baseline and Evaluation scripts for SemEval 2020 Task 7
Join our task mailing list <a href="https://groups.google.com/forum/#!forum/semeval-2020-task-7-all">here.</a>

The goal of this <a href="https://competitions.codalab.org/competitions/20970">shared task</a> is to assess humor in news headlines that have been modified using short edits to make them funny. There are two subtasks:

* Sub-task 1 (Funniness Estimation): Here the goal is to assign a funniness grade to an edited headline in the [0,3] interval. Systems will be ranked by Root Mean Squared Error.

* Sub-task 2 (Funnier of the Two): Given two differently edited versions of the same headline, the goal is to predict which is the funnier of the two. Systems will be ranked by prediction accuracy.

This repository provides python code to run baseline experiments and evaluation scripts for the two sub-tasks.

## Pre-requisites:
* Python 2 or 3

* Libraries: Pandas, Numpy

## Quickstart
* Clone this repository: ```git clone https://github.com/n-hossain/semeval-2020-task-7-humicroedit```

* ```cd semeval-2020-task-7-humicroedit```

* Download the dataset from <a href="https://www.cs.rochester.edu/u/nhossain/humicroedit/semeval-2020-task-7-data.zip">here</a>.

* Unzip: ```unzip semeval-2020-task-7-data.zip```

* Create directory to save predictions: ```mkdir output```

* ```cd code/```

#### Sub-task 1:
Run the baseline (always predicts the overall mean funniness grade in the training set):

```
 python baseline_task_1.py ../data/task-1/train.csv ../data/task-1/dev.csv
```

#### Sub-task 2:
Run the baseline (always predicts the most-frequent label in the training set, i.e., headline 2):

```
python baseline_task_2.py ../data/task-2/train.csv ../data/task-2/dev.csv
```
