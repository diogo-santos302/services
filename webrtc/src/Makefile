.PHONY: build run stopall push install uninstall

all: build push run

build:
	docker build --network=host -t diogosantosua/webrtc:latest .

run:
	docker run --network=host diogosantosua/webrtc:latest

stopall:
	docker stop $(shell docker ps -q)

push:
	docker push diogosantosua/webrtc:latest

install:
	helm install --generate-name ../nf/webrtc/helm-chart-v3s/demo

uninstall:
	helm uninstall $(shell helm list -q | grep demo-)
