FROM python:alpine
RUN pip install Flask
COPY rng_service.py /
CMD ["python", "rng_service.py"]
EXPOSE 80
