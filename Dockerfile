FROM python:3.9.13-buster
RUN mkdir build
WORKDIR /build
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
WORKDIR /build/app
CMD python -m uvicorn server.main:app --host 0.0.0.0 --port 5000
