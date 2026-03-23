import ml.model as mlm
import os
import pandas as pd
import pickle
import pytest
from sklearn.ensemble import RandomForestClassifier

def test_train_model_output_type():
    """
    Checks that model.train_model() returns an
    instance of a sklearn.ensemble.RandomForestClassifier()
    """

    # Create dummy data for X & y
    X = pd.DataFrame( data={
        'c1': [1, 2, 3],
        'c2': [0, 0, 1],
        'c3': [5, 2, 7]
    })
    y = [0, 1, 0]

    # Test train_model()
    m = mlm.train_model(X, y)

    assert type(m).__name__ == "RandomForestClassifier", (
        "Incorrect model type for ml/model.py train_model()\n"
        "Expected \"RandomForestClassifier\",\n"
        f"returned {type(m).__name__}"
    )    


def test_compute_model_metrics_recall():
    """
    Checks that model.compute_model_metrics() computes the correct
    recall metric
    """

    # Create dummy values
    y = [0, 1, 1, 0, 1]
    preds = [0, 0, 1, 0, 1]

    # Compute recall
    TP = 2
    FN = 1
    r_man = (TP) / (TP + FN)


    _, r_func, _ = mlm.compute_model_metrics(y, preds)
    assert r_func == r_man, (
        "Incorrect recall calculation for ml/model.py compute_model_metrics()\n"
        f"Expected {r_man:.4f} but returned {r_func:.4f}"
    )


def test_save_model():
    """
    Checks that the model is saved in pickle format successfully by
    attempting to load the model .pkl file using pickle.load()
    """
    
    # Create dummy model
    model = RandomForestClassifier()

    # Create temporary file path
    # NOTE: File location must not change
    proj_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(proj_path, "model", "temp_model.pkl")
    
    # Save model
    mlm.save_model(model, path)

    # Attempt to load file
    try: 
        with open(path, 'rb') as f:
            model = pickle.load(f)
            result = True
    except:
        result = False

    # Delete temp file
    os.remove(path)

    assert result == True, (
        "Model fails to save via ml/model.py save_model()"
)
