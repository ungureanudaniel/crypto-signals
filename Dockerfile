FROM python:3.8
#variables
ENV VIRTUAL_ENV=/myvenv

WORKDIR /crypto-signals

RUN python3.8 -m venv $VIRTUAL_ENV
# Enable venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .
RUN pip3.8 install --upgrade pip && cd ./main/ && pip3.8 install -r requirements.txt

ENTRYPOINT ["python3.8", "./main/main.py"]
CMD ["btcusdt"]
