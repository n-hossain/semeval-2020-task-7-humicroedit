# Baseline and Evaluation scripts for SemEval 2020 Task 7
Join our task mailing list: <a href="mailto:funny-headlines-semeval-2020-organizers@googlegroups.com">funny-headlines-semeval-2020-organizers@googlegroups.com</a>

The goal of this <a href="https://competitions.codalab.org/competitions/23212">shared task</a> is to assess humor in news headlines that have been modified using short edits to make them funny. There are two subtasks:

* Sub-task 1 (Regression): Here the goal is to assign a funniness grade to an edited headline on a 0-3 funniness scale.

* Sub-task 2: Given two differently edited versions of the same headline, the goal is to predict which is the funnier of the two.

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