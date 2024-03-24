import pytest
import pandas as pd
from app import load_data

# Testez la fonction load_data
def test_load_data():
    data = load_data()
    assert isinstance(data, pd.DataFrame)
    assert "studytime" in data.columns
    assert "goout" in data.columns
    assert "Dalc" in data.columns
    assert "Walc" in data.columns
    assert "schoolsup" in data.columns
    assert "absences" in data.columns