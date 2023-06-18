# Итоговый проект

## Описание приложения

Построить образ Docker FastAPI приложения для предсказания класса Survived из Titanic и запустить его:
```bash
docker build -t myapp .
docker run --rm -d -p 81:81 myapp
```

Можно использовать следующую команду curl для отправки POST-запроса на ваш FastAPI сервер:
```bash
curl -X POST 'http://localhost:81/predict' -H  'Content-Type: application/json' -d '{"Pclass":3,"Sex":"male","Age":22.0}'
```

## Описание DVC хранилища

Адрес DVC хранилища на Google Disk: [ссылка](https://drive.google.com/drive/folders/1Z953FpJaJguoLI82NkB4uoH-t_IWcwum)

Переключение между датасетами:

```bash
# Вариант 1
#################################
git checkout akinin828_final_main
dvc checkout
#################################

# Вариант 2
#################################
git checkout akinin828_final_alt
dvc checkout
#################################
```

## Описание Pytest

* Модульный тест проверки работы модели через FastAPI сервер: `test_app.py`
* Проверка качества датасета: `test_app.py`

## Описание Jenkins pipeline

Происходит сборка образа приложения и запуск тестов Pytest.