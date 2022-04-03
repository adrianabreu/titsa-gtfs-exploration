FROM jupyter/minimal-notebook:latest

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_PATH=/opt/poetry \
    VENV_PATH=/home/jovyan/venv \
    POETRY_VERSION=1.1
ENV PATH="$POETRY_PATH/bin:$VENV_PATH/bin:$PATH"


WORKDIR /home/jovyan/work
COPY pyproject.toml .
RUN pip install "poetry==$POETRY_VERSION" 
RUN python -m venv $VENV_PATH \
    && poetry config virtualenvs.create false
RUN poetry install

RUN poetry run python3 -m ipykernel install --user
RUN jupyter labextension install jupyterlab-dash@0.4.0
RUN jupyter lab build