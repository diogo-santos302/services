#!/bin/sh
NODE_PORT=$(kubectl get --namespace {{ .Values.namespace }} -o jsonpath="{.spec.ports[1].nodePort}" services {{ include "nginx_proxy.fullname" . }})

cat > /mnt/shared/nginx.conf << EOF 
worker_processes 1;

events { 
    worker_connections 1024; 
}

http {
    server {
        listen 80;
        server_name _;
        return 301 https://\$host:${NODE_PORT}\$request_uri;
    }

    server {
        listen 443 ssl;
        server_name _;

        ssl_certificate     /etc/nginx/ssl/localhost.crt;
        ssl_certificate_key /etc/nginx/ssl/localhost.key;
        ssl_protocols       TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
        ssl_ciphers         HIGH:!aNULL:!MD5;

        location / {
            proxy_pass {{ $.Values.backend_url }};
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto \$scheme;
        }
    }
}
EOF
