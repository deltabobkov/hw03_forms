# Проект Yatube. Продолжение.

![Python](https://img.shields.io/badge/Python-313131?style=flat&logo=Python&logoColor=white&labelColor=306998)
![Django](https://img.shields.io/badge/Django-313131?style=flat&logo=django&labelColor=092e20)
![HTML5](https://img.shields.io/badge/HTML5-313131?style=flat&logo=html5&logoColor=ffffff&labelColor=E34C26)
![СSS3](https://img.shields.io/badge/CSS3-313131?style=flat&logo=CSS3&logoColor=ffffff&labelColor=3C99DC)
![Visual Studio](https://img.shields.io/badge/VS%20Code-313131?style=flat&logo=visualstudiocode&logoColor=ffffff&labelColor=0098FF)

## Проект Yatube — это платформа для публикаций (блог). 
### На данном этапе реализованы формы регистрации пользователей и смены пароля. Формы для создания и редактирования записей пользователями. Профиль пользователя.

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/deltabobkov/hw03_forms.git

cd hw03_forms
```

2. Cоздать и активировать виртуальное окружение:

```
python -m venv env

source env/Scripts/activate
```

3. Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

4. Выполнить миграции:

```
python manage.py migrate
```

5. Создать супер пользователя:

```
python manage.py createsuperuser
```

6. Запустить проект:

```
python manage.py runserver
```
