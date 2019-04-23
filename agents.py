import random
from heuristic import Heuristic

class SearchTimeout(Exception):
    """Subclass base exception for code clarity."""
    pass

class MinimaxPlayer:
    def __init__(self, search_depth=3, score_cls=Heuristic(), timeout=10.):
        '''
        Game-playing agent that chooses a move using minimax search. 
        You must finish and test this player to make sure it properly uses
        minimax to return a good move before the search time limit expires.

        Params
        ----------
        search_depth : int (optional)
            A strictly positive integer (i.e., 1, 2, 3,...) for the number of
            layers in the game tree to explore for fixed-depth search. (i.e., a
            depth of one (1) would only explore the immediate sucessors of the
            current state.)

        score_fn : callable (optional)
            A function to use for heuristic evaluation of game states.

        timeout : float (optional)
            Time remaining (in milliseconds) when search is aborted. Should be a
            positive value large enough to allow the function to return before the
            timer expires.
        '''

        self.search_depth = search_depth
        self.score = score_cls.get_score
        self.TIMER_THRESHOLD = timeout

    def search(self, game, time_left):
        '''
        Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        int
            Board row corresponding to a legal move; may return
            -1 if there are no available legal moves.
        '''

        self.time_left = time_left
        best_move = -1

        try:
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            print('timeout')
            pass

        return best_move

    def minimax(self, game, depth):
        '''
        Implement minimax search algorithm as described in the workshop.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

            Parameters
            ----------
            game : `connect4.Connect4`
                An instance of `connect4.Connect4` encoding the current state of the game.

            depth : int
                Depth is an integer representing the maximum number of plies to
                search in the game tree before aborting

            Returns
             -------
            int
                The board row of the best move found in the current search;
                -1 if there no legal move is found

            Notes
            -----
            (1) You MUST use the `self.score()` method for board evaluation
                to participate in the tournament; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA pseudocode) 
                then you must copy the timer check into the top of each helper function 
                or else your agent will timeout while playing.
        '''

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        '''
        TODO
        ----
        Return the optimal move from the given game state.
        '''
        raise NotImplementedError

    def terminal_state(self, game):
        '''
        Checks if the game has ended

        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.
        '''

        return not game.available_moves

    def min_value(self, game, depth):
        '''
        Finds the lowest utility among all the posible actions from the given board

        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        float
            The lowest utility value found among all the actions for the given board state.
        '''

        '''
        TODO
        ----
        check if there is time left.
        if depth == 0 return the utility of the current board.
        if a terminal state is reached return the score.
        Otherwise for each available action calculate the maximun utility value.
        then return the lowest utility value found.
        '''
        raise NotImplementedError

    def max_value(self, game, depth):
        '''
        Finds the highest utility among all the posible actions from the given board

        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        float
            The highest utility value found among all the actions for the given board state.
        '''

        '''
        TODO
        ----
        check if there is time left.
        if depth == 0 return the utility of the current board.
        if a terminal state is reached return the score.
        Otherwise for each available action calculate the minimum utility value.
        then return the highest utility value found.
        '''

        raise NotImplementedError

    def minimax_search(self, game, depth):
        '''
        Finds the best action among all the posible actions from the given board

        Parameters
        ----------
        game : `connect4.Connect4`
            An instance of `connect4.Connect4` encoding the current state of the game.

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        int
            Board row corresponding to a legal move.
        '''

        '''
        TODO
        ----
        check if there is time left.
        for each available action calculate the minimum utility value.
        then return the highest utility value found.
        '''
        return -1