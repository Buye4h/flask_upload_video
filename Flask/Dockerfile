FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3" ]
EXPOSE 5000
CMD ["app.py"]