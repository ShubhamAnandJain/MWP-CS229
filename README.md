Forked from https://github.com/LYH-YF/MWPToolkit

How to use this code:

1. Train a model using 

```
python3 run_mwptoolkit.py --model=GroupATT --dataset=SVAMP --task_type=single_equation --equation_fix=prefix --k_fold=5 --test_step=5 --gpu_id=0
```

2. If you already have a trained model and wish to test, use the flag
```
--test_only=True
```

3. If you want question debug output (both for training & testing) to see the kind of testcases the model fails on, the equations the model creates and the targets, use the flag
```
--question_output=True
```

4. You can add your own dataset that is similar to mawps in format by adding a test, train and validation file in the "dataset" folder with the name of the dataset as the folder name, and add a file in mwptoolkit/properties/dataset as well.

Once you get models, run compare_fail.py to get the failure cases across models. It aggregates the failure cases across models and displays them in order of most failures to least failures.

You can also run deep_analyze.py to check the kinds of failures different datasets have on testcases.

Finally, you can use our code to generate your own datasets.

We have tested that GroupATT, MathEN, GTS, Graph2Tree work with the current changes. Changes you might need if you are running models we have not tested/datasets not in the form of mawps:

1. Whatever trainer file you use - You might need to add a Polish notation converter or equivalent, and write the debug output logic here.
2. groupatt.py (or whatever model you use): remember to change model_test to return seq, all_outputs, targets (so that questions are returned)
3. Datasets require special preprocessing - there is no general guideline. You will have to go through the code to figure out how your dataset will work.
