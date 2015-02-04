cmake_minimum_required(VERSION 2.8)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin)

find_package (LibXml2 REQUIRED)
find_package (LibXslt REQUIRED)

if (LIBXML2_FOUND AND LIBXSLT_FOUND)
  include_directories(${LIBXML2_INCLUDE_DIR})
  include_directories(${LIBXSLT_INCLUDE_DIR})
  add_executable(aroma aroma.cpp)
  target_link_libraries (aroma ${LIBXML2_LIBRARIES})
  target_link_libraries (aroma ${LIBXSLT_LIBRARIES})
endif (LIBXML2_FOUND AND LIBXSLT_FOUND)

install(TARGETS aroma DESTINATION /usr/local/bin/)