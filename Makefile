VERSION := v0.0.3-dev
IMAGE_NAME_BASE=llama2-fastapi
IMAGE_BASE=simon3458/${IMAGE_NAME_BASE}

build:
	docker build . -t ${IMAGE_BASE}:${VERSION}

push:
	docker push ${IMAGE_BASE}:${VERSION}

run:
	docker run --rm -d -p 8000:8000 --name llama-cpp-fastapi-service ${IMAGE_BASE}:${VERSION}

log:
	docker logs -f llama-cpp-fastapi-service

remove:
	docker rm -f llama-cpp-fastapi-service