FROM python:3.8.1

RUN ln -sf /usr/share/zoneinfo/Asia/Manila /etc/localtime && echo Asia/Manila > /etc/timezone

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -U flask-cors

COPY . .

CMD [ "python", "./app.py" ]
