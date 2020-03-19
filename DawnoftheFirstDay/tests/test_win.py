from random import randint


def test_win(method: callable, n=1, sample_list=None):
    error = False
    if sample_list:
        test_list = sample_list
    else:
        test_list = [randint(0, 10) for _ in range(n)]
    results = method(test_list)

    # test skips winning validation if results claim list was unwinnable
    if results == []:
        pass
    else:
        # winning validation
        if results is None:
            error = 'Method didnt return anything'
            results = []
        elif 0 not in results:
            error = 'Did not start from 0 index'
        elif len(test_list) < 2:
            error = 'Paths of <2 are not winnable'
        elif sorted(results) != results:
            error = 'Paths can only move forward'
        elif results[-1] >= len(test_list) - 1:
            error = 'Illegal values exist in results'
        elif results[-1] > len(test_list):
            error = 'Output should contain only index, not values'
        results.append(len(test_list))

        for i, j in zip(results[:-1], results[1:]):
            if test_list[i] < j - i:
                error = f'Jump distance too far between path {i} and {j}'
                break
        results.pop()

    sollution_path = [test_list[i] if i in results else 'x' for i in range(len(test_list))]

    if error:
        return [error, sollution_path, results, test_list]
    else:
        return [True, sollution_path, results, test_list]
