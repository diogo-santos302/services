FROM python:3.8.10-slim

RUN apt-get update && \
    apt-get install -y nginx cron && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/nginx/ssl

# Install any Python dependencies if needed
# RUN pip install -r requirements.txt

EXPOSE 80
EXPOSE 443

CMD ["sh", "-c", "service cron start && nginx -g 'daemon off;'"]
