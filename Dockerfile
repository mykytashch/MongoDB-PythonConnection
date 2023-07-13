# Используйте базовый образ Python
FROM python:3

# Установите драйвер MongoDB
RUN pip install pymongo

# Скопируйте код в контейнер
COPY your_python_script.py /app/your_python_script.py

# Установите рабочую директорию
WORKDIR /app

# Запустите код при запуске контейнера
CMD [ "python", "your_python_script.py" ]
