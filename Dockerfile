FROM python:3.11-bullseye

ARG app_dir=/app

ENV \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PYTHONPATH=$app_dir

RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  build-essential \
  gettext \
  libpq-dev \
  wget && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR $app_dir

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
