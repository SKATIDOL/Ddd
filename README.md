# Как открыть мой проект?
1) Сначала вы должны скачать виртуальное окружение.

Для этого вам нужно прописать в терменал следующую команду:

python3 -m venv venv

2) Следом за этим, активируем ее.

Если у вас Windows, вам нужно прописать в терменал следующую команду:

venv\Scripts\activate

Если у вас Linux,  вам нужно прописать в терменал следующую команду:

sourse venv/bin/activate

3) Далее, не зависимо от вашей OC, прописываем данные команды:

pip install -r requirements.txt

cd Ddd

cd lyceum

python manage.py runserver
