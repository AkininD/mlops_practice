# lab4

## Отчет

### 1. Настройка git и dvc
Установлены git и dvc. Текущая директория настроена для работы с git и dvc.

```bash
pip install "dvc[gdrive]==2.58.2"

git init
dvc init
```

### 2. Настройка удаленного хранилища файлов на Google Disk

```bash
dvc remote add --default myremote gdrive://1Z953FpJaJguoLI82NkB4uoH-t_IWcwum
```

### Создание и коммит датасета

Создан начальный датасет о пассажирах "Титаника" с использованием функции catboost.titanic().
Датасет сохранен в формате CSV и содержит информацию о классе (Pclass),
поле (Sex) и возрасте (Age) пассажира:

```bash
python create_dataset.py
```
Затем этот файл был добавлен в dvc и git:

```bash
dvc add titanic.csv
git add titanic.csv.dvc .gitignore
git commit -m "Add initial Titanic dataset"
dvc push
```

### Модификация датасета 1: заполнение пропущенных значений

Заполним пропущенные значения в поле "Age" средним значением:
```bash
python modify_dataset.py
```
Снова делаем коммит в git и dvc:
```bash
dvc add titanic.csv
git add titanic.csv.dvc
git commit -m "Fill missing Age values with mean"
dvc push
```

### Модификация датасета 2: cоздание нового признака с использованием one-hot-encoding

```bash
python modify2_dataset.py
```

Коммитим изменения:
```bash
dvc add titanic.csv
git add titanic.csv.dvc
git commit -m "Apply one-hot encoding to Sex column"
dvc push
```

### Переключение между всеми созданными версиями датасета

Переключение на предыдущую версию:

```bash
git checkout HEAD^1 titanic.csv.dvc
dvc checkout
```

Переключение на следующую версию:
```bash
git checkout HEAD^1 titanic.csv.dvc
dvc checkout
```