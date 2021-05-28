FROM python:3.8
ADD metrics.py index.html /
RUN [ "python", "./metrics.py" ]
