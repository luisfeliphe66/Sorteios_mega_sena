SHELL := /bin/bash

export HOST_UID:=$(shell id --user)
export HOST_USER:=$(shell id --user --name)
export HOST_GID:=$(shell id --group)
export HOST_GROUP:=$(shell id --group --name)

COLOR_RESET := $(shell tput sgr0)
COLOR_ITEM := $(shell tput setaf 2)
COLOR_VAL := $(shell tput setaf 4)
COLOR_SESSION := $(shell tput setaf 208)
COLOR_DEFAULT_VAL := $(shell tput setaf 130)

CMAKE := $(MAKE) --no-print-directory
SPACE_CHAR=$(subst ,, )

SERVICE_APP=airflow
PROJECT_DIR := $(CURDIR)
DOCKER_COMPOSE_FILE=$(PROJECT_DIR)/docker/compose/docker-compose.yml

# General targets:
.PHONY: help up down exec log

help:	
	@echo '${COLOR_SESSION}Getting started to use the application:${COLOR_RESET}'
	@echo '  ${COLOR_ITEM}Execute:${COLOR_RESET} make deploy'
	@echo ''
	@echo '${COLOR_SESSION}Using the targets:${COLOR_RESET}'
	@echo '  make TARGET [OPTIONS]'
	@echo ''
	@echo '${COLOR_SESSION}General targets:${COLOR_RESET}'
	@echo '  ${COLOR_ITEM}help${COLOR_RESET}                   Display this help message'
	@echo ''
	@echo '  ${COLOR_ITEM}down${COLOR_RESET}                   Stop the application'
	@echo ''
	@echo '${COLOR_SESSION}Docker targets:${COLOR_RESET}'
	@echo '  ${COLOR_ITEM}prune${COLOR_RESET}                  Remove unused objects'
	@echo ''
	@echo '  ${COLOR_ITEM}prune-container${COLOR_RESET}        Remove unused containers'
	@echo ''
	@echo '  ${COLOR_ITEM}prune-dangling-image${COLOR_RESET}   Remove dangling images'
	@echo ''	
	@echo '  ${COLOR_ITEM}prune-image${COLOR_RESET}            Remove unused images'
	@echo ''
	@echo '  ${COLOR_ITEM}prune-network${COLOR_RESET}          Remove unused networks'
	@echo ''
	@echo '  ${COLOR_ITEM}prune-volume${COLOR_RESET}           Remove unused volumes'
	@echo ''
	@echo '${COLOR_SESSION}Variables:${COLOR_RESET}'
	@echo '  ${COLOR_ITEM}env${COLOR_RESET}                    dev'
	@echo '  ${COLOR_ITEM}user${COLOR_RESET}                   $(HOST_USER)(uid=$(HOST_UID))'
	@echo '  ${COLOR_ITEM}group${COLOR_RESET}                  $(HOST_GROUP)(gid=$(HOST_GID))'

up:
	docker compose --file $(DOCKER_COMPOSE_FILE) up --detach

down:
	docker compose --file $(DOCKER_COMPOSE_FILE) down

deploy:
	$(MAKE) checkOS
# $(MAKE) remove
	$(MAKE) prepare
	$(MAKE) up

	sleep 10

	$(MAKE) show

# remove:
# 	@docker volume rm postgresql_data
# 	@docker volume rm redis_data

prepare:
	@docker network ls | grep public_airflow > /dev/null || docker network create public_airflow
	@docker volume ls | grep postgresql_data > /dev/null || docker volume create postgresql_data
	@docker volume ls | grep redis_data > /dev/null || docker volume create redis_data

show:
	@echo ''
	@echo 'Acesse:' http://$(shell docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' compose-airflow-1):8080/login
	@echo ''

checkOS:
	@if ! cat /etc/os-release | grep -e '^NAME=.*Ubuntu.*' &> /dev/null; then echo "O seu Sistema Operacional precisa ser o Ubuntu!" && exit 1; fi;

# Docker targets:
.PHONY: prune prune-image prune-dangling-image

prune:
	docker system prune --all --force

prune-container:
	docker container prune

prune-dangling-image:
	docker image prune

prune-image:
	docker image prune --all

prune-network:
	docker network prune

prune-volume:
	docker volume prune
