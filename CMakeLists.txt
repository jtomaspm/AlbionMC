set( CMAKE_CXX_COMPILER "C:\\msys64\\ucrt64\\bin\\g++.exe" )
set( CMAKE_C_COMPILER "C:\\msys64\\ucrt64\\bin\\gcc.exe" )

cmake_minimum_required(VERSION 3.10)
project(AlbionMC)

set(DOCKER_COMPOSE_FILE ${CMAKE_SOURCE_DIR}/apps/docker-compose.yaml)
set(ENV_FILE ${CMAKE_SOURCE_DIR}/apps/.env)


add_custom_target(build
    COMMAND docker-compose -f ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} build
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/apps
    COMMENT "Building all Docker containers using docker-compose"
)

add_custom_target(run
    COMMAND docker-compose -f ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} up -d
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/apps
    COMMENT "Starting all Docker containers using docker-compose"
)

add_custom_target(dev
    COMMAND docker-compose -f ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} up -d --build api frontend
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/apps
    COMMENT "Starting all Docker containers using docker-compose. Rebuilding api and frontend"
)

add_custom_target(kill
    COMMAND docker-compose -f ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} down
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/apps
    COMMENT "Stopping all Docker containers using docker-compose"
)

add_custom_target(clear
    COMMAND docker-compose -f ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} rm -f
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/apps
    COMMENT "Removing all Docker containers using docker-compose"
)

add_custom_target(build-all-targets
    DEPENDS build run dev kill clear
    COMMENT "Build all targets"
)