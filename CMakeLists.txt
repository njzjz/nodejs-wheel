cmake_minimum_required(VERSION 3.15)
file(READ "${CMAKE_SOURCE_DIR}/.nvmrc" _ver)
string(STRIP ${_ver} _ver)
project(nodejs-wheel VERSION ${_ver})
include(ProcessorCount)
ProcessorCount(N)
include(ExternalProject)
if (UNIX)
    ExternalProject_Add(nodejs
        URL https://github.com/nodejs/node/archive/refs/tags/v${CMAKE_PROJECT_VERSION}.tar.gz
        CONFIGURE_COMMAND echo >> <SOURCE_DIR>/deps/cares/config/linux/ares_config.h
        COMMAND echo \#undef HAVE_SYS_RANDOM_H >> <SOURCE_DIR>/deps/cares/config/linux/ares_config.h
        COMMAND echo \#undef HAVE_GETRANDOM >> <SOURCE_DIR>/deps/cares/config/linux/ares_config.h
        COMMAND <SOURCE_DIR>/configure --prefix=${SKBUILD_PLATLIB_DIR}/nodejs_wheel
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
        URL https://github.com/nodejs/node/archive/refs/tags/v${CMAKE_PROJECT_VERSION}.tar.gz
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
        PERMISSIONS
        OWNER_READ
        OWNER_WRITE
        OWNER_EXECUTE
        GROUP_READ
        GROUP_EXECUTE
        WORLD_READ
        WORLD_EXECUTE
    )
    install(
        DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/nodejs_source/deps/npm
        DESTINATION ${SKBUILD_PLATLIB_DIR}/nodejs_wheel/lib/node_modules/
        USE_SOURCE_PERMISSIONS
    )
else()
    message(FATAL_ERROR "Unsupported platform")
endif()
