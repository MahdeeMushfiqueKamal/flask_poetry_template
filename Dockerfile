# Dockerfile 
FROM python:3.10-slim
WORKDIR /app
COPY . /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 5000
ENV PORT=5000

# CMD ["poetry", "run", "python", "flask_app/app.py"]
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "-w", "1", "--timeout", "120", "flask_app.app:app"]


