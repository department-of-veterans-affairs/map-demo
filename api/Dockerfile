FROM python:alpine
RUN pip install redis
RUN pip install requests
COPY api_service.py /
CMD ["python", "api_service.py"]
