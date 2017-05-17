cmake_minimum_required(VERSION 3.5)

set(CMAKE_GENERATOR "Visual Studio 14 Win64")

SET(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake" "${CMAKE_MODULE_PATH}")
FIND_PACKAGE(OpenMP REQUIRED)

SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS} -O3 -fPIC -ffast-math -funroll-loops -static -static-libgcc -static-libstdc++")
SET(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")

FILE(GLOB src *.cpp)

ADD_LIBRARY(tsne_multicore MODULE ${src})
