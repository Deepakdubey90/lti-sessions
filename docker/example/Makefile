.PHONY: clean build run

clean:
	docker system prune

build:
	docker build --no-cache --tag akhilputhiry/docker-tutorial:1.0.0 .

run:
	docker run --publish 5000:5000 akhilputhiry/docker-tutorial:1.0.0

all: clean build run
