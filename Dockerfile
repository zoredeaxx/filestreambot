FROM python

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENV PORT = 8080

EXPOSE 8080

CMD [ "python3", "-m", "Code_X_Mania" ]
