FROM python:3.10-alpine
WORKDIR /app
COPY requirements.txt /app
# NOTE: This repos are required for chronium to run in Alpine
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
# Install dependencies
RUN apk update && \
    apk add --no-cache gcc libc-dev linux-headers libpq-dev chromium chromium-chromedriver && \
    rm -rf /var/cache/apk/* && \    
    pip3 install -r requirements.txt --no-cache-dir

COPY . /app
RUN chmod +rw /app/results
CMD ["python3", "script.py"]