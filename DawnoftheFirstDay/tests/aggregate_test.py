from random import randint
from DawnoftheFirstDay.tests.test_win import test_win
from timeout import timeout
import multiprocessing.pool
import numpy as np
from tempfile import mkdtemp
import os.path as path

@timeout(5)
def timed_test(m, sample_list):
    return test_win(m, sample_list=sample_list)

def aggregate_test(method_callables: callable):
    methods = {x: [True, [], []] for x in method_callables}
    print('starting')
    round_no = 0
    while True:
        test_pool = [x for x in methods if methods[x][0] is True]

        # continue until a winner exists
        if len(test_pool) < 2:
            if len(test_pool) == 1:
                print(f'{test_pool[0].__name__} wins')
            else:
                print('Everyone lost.  Congrats!')
                for t in test_pool:
                    print(t.__name__)
            break

        # generate a random test list
        if round_no > 16: #if the array size is larger than the computer can handle, write to a temporary file
            l_file = path.join(mkdtemp(), 'game_data.dat')
            game_memory = np.memmap(l_file, dtype='int', mode='w+', shape=(len(methods), 2 ** round_no))
            #initialize the memory space
            random_board = np.random.randint(0, 5 + round_no, 2 ** round_no)
            random_board.resize((len(methods), 2 ** round_no))

            #this part creates the 1-D array with random numbers
            for chunk in range(int((2 ** round_no) / (2**(round_no/10)))):  # writing to mem space in chunk size 2^10
                game_memory[0][chunk: chunk + 2**10] = random_board[chunk:chunk + 2**10]
                #we probably want a smaller chunk size for big compoots
        else:
            test_list = [randint(0, 5 + round_no) for _ in range(2 ** round_no)]



        # test that method solutions are valid
        for m in methods:
            try:
                #and then here, run the methods chunk by chunk
                #prob need to save [prev_value, curr_value] so that the compoots can continue chunk to chunk
                methods[m] = timed_test(m, sample_list=test_list)
            except multiprocessing.context.TimeoutError:
                methods[m] = 'Process exceeded 5 seconds', [], [], []

        # test claims of impossible configurations against other solutions
        validation = {x for x in methods if methods[x][0] is True and len(methods[x][2]) > 0}
        if len(validation) > 0:
            for m in set(methods.keys()).difference(validation):
                if methods[m][0] is True:
                    methods[m][0] = 'Could not find a valid path'
        round_no += 1
        print(f'*Round {round_no}*')
        print('results:')
        for m in methods:
            print(f'\t{m.__name__}: {"Passed" if methods[m][0] is True else "Failed: " + methods[m][0]}')
            print(f'\t\tpath: {methods[m][1][:100]}')
            print(f'\t\tindex: {methods[m][2][:100]}')
            print(f'\t\tproblem set: {methods[m][3][:100]}')
