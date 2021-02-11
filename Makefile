IMG_NAME = jvanderaa/ci_demo
IMG_VERSION = 0.1.0

.DEFAULT_GOAL := test

build:
	docker build -t $(IMG_NAME):$(IMG_VERSION) .

cli:
	docker run -it \
		-v $(shell pwd):/local \
		-w /local \
		$(IMG_NAME):$(IMG_VERSION) bash

.PHONY: test
test:	lint unit

.PHONY: lint
lint:
	@echo "Starting  lint"
# Verify all YAML files
	docker run -t -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) yamllint -s .
# Verify all python files pass the Bandit security scanner
	docker run -t -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) bandit -r ./ -c .bandit
# # Verify all Python files pass pylint
	docker run -t -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) make pylint
# # Verify all Python files meet Black code style
	docker run -t -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) black --check ./
	@echo "Completed lint"

.PHONY: pylint
pylint:
	find ./ -name "*.py" | xargs pylint

.PHONY: unit
unit:
	@echo "Starting Unit Tests"
	docker run -t -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) pytest -vvvv
	@echo "Completed Unit Tests"