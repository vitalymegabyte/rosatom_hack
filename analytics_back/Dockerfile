FROM huggingface/transformers-pytorch-cpu

ENV LANG C.UTF-8
RUN pip3 install --upgrade pip
RUN pip3 install setuptools_rust

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["python3", "analytics.py"]
