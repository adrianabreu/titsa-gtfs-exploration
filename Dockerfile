FROM jupyter/pyspark-notebook:spark-3.2.1

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_PATH=/opt/poetry \
    VENV_PATH=/home/jovyan/venv \
    POETRY_VERSION=1.1
ENV PATH="$POETRY_PATH/bin:$VENV_PATH/bin:$PATH"


WORKDIR /home/jovyan/work
RUN pip install "poetry==$POETRY_VERSION" 
RUN python -m venv $VENV_PATH \
    && poetry config virtualenvs.create false