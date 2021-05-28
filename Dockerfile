FROM python:3.8
ADD metrics.py index.html /
CMD [ "python", "./metrics.py" ]
