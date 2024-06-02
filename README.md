Для запуска локально:
1. Введите в консоли https://github.com/Alexandr-eng/IT_Fox.git
2. Создайте и войдите в виртуальное окружение
3. Введите в консоли pip install -r requirements.txt
4. Далее введите в консоли python manage.py makemigrations
5. После создания миграций введите в консоли python manage.py migrate
6. Запустите локальный сервер python manage.py runserver
7. Перейдите по адресу http://127.0.0.1:8000/api/swagger/ и пользуйтесь всеми ручками приложения
