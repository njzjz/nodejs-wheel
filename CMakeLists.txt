cmake_minimum_required(VERSION 3.15)
project(nodejs-wheel)
include(ProcessorCount)
ProcessorCount(N)
include(ExternalProject)
ExternalProject_Add(nodejs
    URL https://github.com/nodejs/node/archive/refs/tags/v18.18.0.tar.gz
    CONFIGURE_COMMAND ./configure --prefix=<INSTALL_DIR>
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j${N}
    USES_TERMINAL_DOWNLOAD true
    USES_TERMINAL_UPDATE true
    USES_TERMINAL_PATCH true
    USES_TERMINAL_CONFIGURE true
    USES_TERMINAL_BUILD true
    USES_TERMINAL_INSTALL true
    USES_TERMINAL_TEST true
)
