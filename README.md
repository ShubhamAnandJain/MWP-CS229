Forked from https://github.com/LYH-YF/MWPToolkit

Once you get models, run compare_fail.py to get the failure cases across models. It aggregates the failure cases across models and displays them in order of most failures to least failures.

Remember to change:

1. config.json to add "test_only": true
2. supervised_trainer.py - Polish notation added
3. groupatt.py (or whatever model you use): remember to change model_test to return seq, all_outputs, targets
