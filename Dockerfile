FROM python
RUN pip install flask
RUN mkdir /test
COPY app.py /test/
EXPOSE 5000
CMD ["python", "/app/app.py"]
