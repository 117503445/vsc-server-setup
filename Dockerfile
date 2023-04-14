FROM python:3.10.10 as base
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /root

FROM base as poetry
RUN pip install poetry==1.4.2
COPY poetry.lock pyproject.toml /root/
RUN poetry export -o requirements.txt

FROM base as build
COPY --from=poetry /root/requirements.txt /tmp/requirements.txt
RUN python -m venv .venv && \
    .venv/bin/pip install 'wheel==0.40.0' && \
    .venv/bin/pip install -r /tmp/requirements.txt

FROM python:3.10.10-slim as runtime
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /root
ENV PATH=/root/.venv/bin:$PATH
COPY --from=build /root/.venv /root/.venv
COPY . /root
ENTRYPOINT [ "python" , "main.py"]