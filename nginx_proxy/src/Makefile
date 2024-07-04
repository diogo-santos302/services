.PHONY: all build run push

all: build run

build: 
	docker build --network=host -t diogosantosua/python-nginx-cron:latest  .

run: 
	docker run --network=host diogosantosua/python-nginx-cron:latest 

push: 
	docker push diogosantosua/python-nginx-cron:latest 

install:
	helm install --generate-name ../nf/nginx_proxy/helm-chart-v3s/nginx-proxy

uninstallall:
	helm uninstall $(shell helm list -q)
