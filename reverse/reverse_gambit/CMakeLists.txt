cmake_minimum_required(VERSION 3.10)
project(reverse_gambit)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Werror -mno-mmx -fcf-protection=none")

add_executable(challenge challenge.c)
add_executable(flag_generator flag_print.c)

add_custom_target(generate_flag
    COMMAND flag_generator challenge.h
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Generate challenge.h with flag_ciphertext variable\n"
    SOURCES flag_print.c
)

if(CMAKE_BUILD_TYPE MATCHES Release)
    add_custom_command(
            TARGET challenge
            POST_BUILD
            COMMAND ${CMAKE_STRIP} challenge
            COMMENT "Stripping executable of symbols"
    )
endif()
add_dependencies(challenge generate_flag)