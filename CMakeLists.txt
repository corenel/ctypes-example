cmake_minimum_required(VERSION 3.10)

project(ctypes_example)

# set compilation for c++
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
add_definitions(-Wall -Wextra -Wno-unused-parameter -O2)

# common include directories
include_directories(cpp/include)

# find all source files
file(GLOB_RECURSE src_files ${PROJECT_SOURCE_DIR}/cpp/src/*.cc)

# add library add_library(foo MODULE ${SOURCE})
add_library(${PROJECT_NAME} MODULE ${src_files})
target_link_libraries(${PROJECT_NAME})
