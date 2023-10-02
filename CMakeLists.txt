cmake_minimum_required(VERSION 3.15)
project(nodejs-wheel)
include(ProcessorCount)
ProcessorCount(N)
include(ExternalProject)
if (UNIX)
    ExternalProject_Add(nodejs
        URL https://github.com/nodejs/node/archive/refs/tags/v18.18.0.tar.gz
        CONFIGURE_COMMAND <SOURCE_DIR>/configure --prefix=${SKBUILD_PLATLIB_DIR}/nodejs_wheel
        BUILD_IN_SOURCE 1
        BUILD_COMMAND make -j${N}
        INSTALL_COMMAND make install
        USES_TERMINAL_DOWNLOAD true
        USES_TERMINAL_UPDATE true
        USES_TERMINAL_PATCH true
        USES_TERMINAL_CONFIGURE true
        USES_TERMINAL_BUILD true
        USES_TERMINAL_INSTALL true
        USES_TERMINAL_TEST true
    )
elseif(WIN32)
    ExternalProject_Add(nodejs
        URL https://github.com/nodejs/node/archive/refs/tags/v18.18.0.tar.gz
        CONFIGURE_COMMAND ""
        BUILD_IN_SOURCE 1
        BUILD_COMMAND <SOURCE_DIR>/vcbuild
        INSTALL_COMMAND ""
        SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/nodejs_source
        USES_TERMINAL_DOWNLOAD true
        USES_TERMINAL_UPDATE true
        USES_TERMINAL_PATCH true
        USES_TERMINAL_CONFIGURE true
        USES_TERMINAL_BUILD true
        USES_TERMINAL_INSTALL true
        USES_TERMINAL_TEST true
    )
    install(
        FILES ${CMAKE_CURRENT_BINARY_DIR}/nodejs_source/out/Release/node.exe
        DESTINATION ${SKBUILD_PLATLIB_DIR}/nodejs_wheel
        USE_SOURCE_PERMISSIONS
    )
    install(
        DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/nodejs_source/deps/npm
        DESTINATION ${SKBUILD_PLATLIB_DIR}/nodejs_wheel/lib/node_modules/
        USE_SOURCE_PERMISSIONS
    )
else()
    message(FATAL_ERROR "Unsupported platform")
endif()
