# Используйте базовый образ Python
FROM python:3

# Установите необходимые зависимости
RUN pip install pymongo

# Скопируйте код в контейнер
COPY your_script.py /usr/src/app/your_script.py

# Запустите код при запуске контейнера
CMD ["python", "/usr/src/app/your_script.py"]
