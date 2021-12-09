#!/bin/bash

set -e

. .env
docker-compose -f docker-compose.yml down --volumes
docker-compose -f docker-compose.yml build 
docker-compose -f docker-compose.yml up
