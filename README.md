# AI-PM-Team-4

## Installation

### 1. Git Clone
```
git clone https://github.com/Xungerrrr/AI-PM-Team-4
```

### 2. Install all requirements
Python environments: 3.8.9
```
pip install -r requirement.txt
```

### 3. Run Project
If you want to train the model from scratch, use jupyter notebook to run `train_model.ipynb` line by line. After running the code, the vectorizer will be stored as `vectorizer` and the trained model will be stored as `svc.model`.

If you want to use our prediction service, you can run `predict.py` according to the [usage](#Usage) below.

## Usage
1. Predict a title
```
python predict.py -t [title]
```
e.g.
```
python predict.py -t Why does velocity affect time? Does velocity affect space geometry?
```

2. Predict multiple titles

```
python predict.py -f [file_path]
```

First, we should save all titles as a file, then use the above command.

e.g. We save all titles in `test.txt`

```
python predict.py -f test.txt
```
