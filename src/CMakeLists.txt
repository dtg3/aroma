cmake_minimum_required(VERSION 2.8)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin)

find_package (LibXml2 REQUIRED)

if (LIBXML2_FOUND)
  include_directories(${LIBXML2_INCLUDE_DIR})
  add_executable(aroma aroma.cpp)
  target_link_libraries (aroma ${LIBXML2_LIBRARIES})
endif (LIBXML2_FOUND)

install(TARGETS aroma DESTINATION /usr/local/bin/)