cmake_minimum_required(VERSION 3.10.2)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)



#replace LIB_NAME with your library names
add_library(chesslib_interface
    chesslib_interface.h
    chesslib_interface.cpp
)

add_library(chesslib
    

    core2/attack_tables.h
    core2/attack_tables.cpp    
    core2/chess_board.h
    core2/chess_board.cpp
    core2/attack_tables_handler.h
    core2/attack_tables_handler.cpp
    core2/global_utils.cpp
    
)
