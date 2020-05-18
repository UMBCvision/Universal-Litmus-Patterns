# Universal Litmus Patterns: Revealing Backdoor Attacks in CNNs

### Tiny-ImageNet

##### Download data

Download data from the [Tiny ImageNet Visual Recognition Challenge](tiny-imagenet.herokuapp.com)
Please replace all occurrences of <tiny-imagenet-root> with the appropriate path.

##### Data cleaning

The organization of Tiny ImageNet differs from standard ImageNet. This scripts cleans the data.
```python
python data_cleaning.py
```

##### Generate poisoned data

To generate the poisoned data to be used in the experiments run
```python
python convert_data.py
python generate_poison.py
```

The first script converts the images into a numpy array and stores them in ./data for faster generation of poisons.
The second script adds the triggers from ./triggers to the images to generate poisoned data. Please generate one set of images for each poisoned model you want to train.
We use poisoned models for Triggers 01-10 for training ULPs and poisoned models for Triggers 11-20 to test. 
This ensures that the train and test poisoned models use a different set of triggers.

##### Train models

We use a modified Resnet architecture for our experiments.
To train clean models use
```python
python train_clean_model.py <partition-num> <logfile>
```

To train poisoned models use
```python
python train_poisoned_model.py <partition-num> <logfile>
```

For training ULPs: Train 1000 clean models and 1000 poisoned models on triggers 01-10.
For evaluating ULPs: Train 100 clean models and 100 poisoned models on triggers 11-20.

Currently each partition trains 50 models. Modify this according to your needs if you have multiple GPUs to train in parallel.

To save time, you can also use our trained models (to be made available soon):
+ extract Clean models train and save in ./clean_models/train
+ extract Poisoned models train and save in ./poisoned_models/Triggers_01_10
+ extract Clean models val and save in ./clean_models/val
+ extract Poisoned models val and save in ./poisoned_models/Triggers_11_20

##### Train ULPs

Once the models are generated, run
```python
python train_ULP.py <logfile> <num_ULPs>
```

Provide appropriate number of ULPs. We run experiments for 1, 5 and 10 patterns.
This will save the results, i.e ULPs and our classifier in ./results

##### Evaluate ULPs and Noise Patterns

To evaluate ULPs run
```python
python evaluate_ULP.py 
```
To evaluate Noise patterns run
```python
python evaluate_noise.py
```

##### Plot ROC curves

```python
python plot_ROC_curves.py
```

<img src="https://github.com/UMBCvision/Universal-Litmus-Patterns/blob/master/tiny-imagenet/ROC_resnetmod_tiny-imagenet.png" width="400" height="300" class="center">


