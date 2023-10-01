cmake_minimum_required(VERSION 3.15)
project(nodejs-wheel)
include(ProcessorCount)
ProcessorCount(N)
include(ExternalProject)
ExternalProject_Add(nodejs
    URL https://github.com/nodejs/node/archive/refs/tags/v18.18.0.tar.gz
    CONFIGURE_COMMAND ./configure --prefix=<INSTALL_DIR>
    BUILD_IN_SOURCE 1
    BUILD_COMMAND ${MAKE} -j${N})
