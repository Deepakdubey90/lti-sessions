.PHONY: clean docker

VERSION=1.2.1

clean:
	docker system prune

docker:
	docker build -t akhilputhiry/flask-app:${VERSION} .
	docker push akhilputhiry/flask-app:${VERSION}

deploy:
	kubectl apply -f k8-manifests/secret.yaml
	kubectl apply -f k8-manifests/service.yaml
	kubectl apply -f k8-manifests/deployment.yaml
