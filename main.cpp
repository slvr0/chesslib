#include <iostream>

#include <vector>
#include <random>
#include <cstdlib>

#include "src/blowfish/chessboard_generator.h"
#include "src/blowfish/chessboard_extractor.h"
#include "src/blowfish/move_generator.h"
#include "src/blowfish/position_meta_data.h"
#include "src/blowfish/perft_divider_autotraverse.h"
#include "src/blowfish/perft_mg_thread.h"

#include "src/chess_interface/movegen_interface.h"

#include "src/monte_carlo/mc_node.h"
#include "src/monte_carlo/mc_node_structure.h"
#include "src/monte_carlo/mc_mainthread.h"
#include "src/monte_carlo/mc_thread_factory.h"
#include "src/monte_carlo/mc_simulator.h"

#define CREATE(string) ChessboardGenerator::CreateFromFen(string)

int main()
{

    std::string startpos_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";
    std::string kiwipep_fen = "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1";
    std::string promotion_fen = "n1n5/PPPk4/8/8/8/8/4Kppp/5N1N b - - 0 1";

    ChesslibInterface chesslib_io;

    auto startposition = CREATE(startpos_fen);
    auto kiwipep = CREATE(kiwipep_fen);
    auto promoboard = CREATE(promotion_fen);
    /*
        {
            Timer t0;
            const int d = 6;
            //benchmarking
            std::vector<unsigned long long> res = chesslib_io.InitSearch(startposition, SearchType::PERFT, d);

            double t_delta = t0.elapsed();
            std::cout << "search time : " << t_delta << std::endl;

            unsigned long long total = 0;
            for(const auto & dres : res) {
                total += dres;
                print(dres);
            }

            std::cout << "Total nodes : " << total << " NPS : " << (unsigned long long) total/t_delta << std::endl;
        }

        {
            const int maxd = 6;
            MGenThreadManager mg_thread_manager;
            Timer t0;
            unsigned long long result = mg_thread_manager.Enumerate(startposition, maxd);
            double delta_t = t0.elapsed();

            std::cout << "Total nodes (threaded) : " << result << " NPS : " << (unsigned long long) result/delta_t << std::endl;
        }
     */

    /*
        {
            Timer t0;
            //std::unique_ptr<Node> node = std::make_unique<Node> (startposition);

            NodeTreeStructure nodetree(startposition);

            MCTS::MCThreadFactory mc_thread_fac(&nodetree);

            size_t nthreads = 2;

            mc_thread_fac.SpawnThreads(nthreads);


            print(nodetree.GetTreeSize());

            print(t0.elapsed());
        }
         */

    // non threaded test
    /*     {
            NodeTreeStructure nodetree(startposition);
            MCTS::MCExpandSimulateThread mainthread(&nodetree);
            mainthread.Ponder();

            print(nodetree.GetTreeSize());

        }
         */

    Timer t0;
    MCSimulator simulator;
    for(int i = 0 ; i < 1e4; ++i) {
        
        simulator.SimulateGame(startposition);
    }

    print(t0.elapsed());
    print(simulator.generator_time_);
    print(simulator.Moves());
    print(simulator.MoveTime());
    print(simulator.InsertAssert());
    print(simulator.rng_timer);
    print(simulator.n_decisive);


/*     Board b1 (startposition);

    std::unique_ptr<Board> b2 = std::make_unique<Board> ();
    Board b3;

    Timer t0;
    for(int i = 0 ; i<1e6;++i) {
        *b2 = b1;
    }
    print(t0.elapsed());

    Timer t1;
    for(int i = 0 ; i<1e6;++i) {
        b3 = b1;
    }
    print(t1.elapsed());
 */
    return 0;
}
