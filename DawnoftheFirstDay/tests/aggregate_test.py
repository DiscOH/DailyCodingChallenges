from random import randint
from DawnoftheFirstDay.tests.test_win import test_win
from timeout import timeout
import multiprocessing.pool


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
        test_list = [randint(0, 5 + round_no) for _ in range(2 ** round_no)]

        # test that method solutions are valid
        for m in methods:
            print(f'testing {m.__name__}')
            try:

                methods[m] = timed_test(m, sample_list=test_list)
            except multiprocessing.context.TimeoutError:
                methods[m] = 'Process exceeded 5 seconds', [], []
            except:
                raise
                methods[m] = 'Unexpected error encountered', [], []

        # test claims of impossible configurations against other solutions
        validation = {x for x in methods if methods[x][0] is True and len(methods[x][1]) > 0}
        if len(validation) > 0:
            for m in set(methods.keys()).difference(validation):
                methods[m][0] = False
        round_no += 1
        print(f'end of round {round_no}')
        print('results:')
        for m in methods:
            print(f'{m.__name__}:')
            print(f'{"Passed" if methods[m][0] else "Failed"}, {methods[m][1][:100]}, {methods[m][2][:100]}')
