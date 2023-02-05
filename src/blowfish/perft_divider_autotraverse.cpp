#include "perft_divider_autotraverse.h"

bool PerftDividerAutotraverse::EnumerateDivide(const Board & board, const int & divide_depth) {
    PerftDividerFactory divider_fac;

    int     current_depth = divide_depth;
    Board   current_board = board;

    while(current_depth >= 1) {
        //we start search from a position, we enter divider map depth
        PerftNodeMap node_map = divider_fac.Enumerate(current_board, current_depth);

        auto board_fen = BoardAsFen(current_board);     

        std::cout << "Depth : " << current_depth << " Position : " << board_fen << " ";    
        
        InitFileRead();
        
        //we update our stockfish command file with search query
        UpdateStockfishSearchQuery(board_fen, current_depth);

        //Stockfish search command is being executed and the result is parsed into a PerftResultMap
        std::string search_result = ExecuteStockfishCommand();    

        command_fstream_.close();

        PerftResultMap search_result_map = ConvertStockfishResult(search_result);

        if(current_depth == 1) {
            return CompareAny(node_map, search_result_map);            
        }
        else {
            //we retrieve the issue and iterate the search
            std::pair<SearchErrorType, std::string> res = CompareReturnFirstError(node_map, search_result_map);

            if(res.first == SearchErrorType::kMoveNotAllowed || res.first == SearchErrorType::kMoveNotFound) {
                std::cout << "Final result from position : " << board_fen << std::endl;
                return CompareAny(node_map, search_result_map);             
            }
            else if (res.first == SearchErrorType::kNoError) {
                print("The generator fully supports the position depth search");
                std::cout << "concluded from position : " << board_fen << std::endl;
                return true;
            }
            else { 
                current_board = (*node_map[res.second]).board_;
                std::cout << "Make move : " << res.second << std::endl;
            }
        }

        --current_depth; 
    }

      
}