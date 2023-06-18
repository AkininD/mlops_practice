import pandas as pd


def test_data_quality():
    df = pd.read_csv('dataset.csv')

    # Проверка типов данных
    assert df['Pclass'].dtype == 'int64'
    assert df['Sex'].dtype == 'object'
    assert df['Age'].dtype == 'float64'
    assert df['Survived'].dtype == 'int64'

    # Проверка диапазона возраста
    assert df['Age'].min() >= 0
    assert df['Age'].max() <= 100
