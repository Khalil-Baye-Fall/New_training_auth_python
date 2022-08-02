FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
WORKDIR /code
COPY requirements.txt /code
RUN python -m venv env
COPY . .
RUN  . env/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/