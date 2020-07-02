def biggest_slice(angles) -> int:
    sorted_angles = sorted(angles)
    largest_slice = 0
    for i in range(len(sorted_angles) - 1):
        current_slice = sorted_angles[i + 1] - sorted_angles[i]
        largest_slice = current_slice if current_slice > largest_slice else largest_slice
    first_angle = 360 + sorted_angles[0]
    current_slice = first_angle - sorted_angles[-1]
    largest_slice = current_slice if current_slice > largest_slice else largest_slice
    return largest_slice


def test_suite(tests):
    passes = 0
    fails = 0
    num_tests = len(tests)
    result = ('FAILED :(', 'PASSED :)',)
    for count, test in enumerate(tests):
        print(f'Running test {count + 1} {40 * "."}')
        outcome = biggest_slice(test[0])
        passed = test[1] == outcome
        if passed:
            passes += 1
        else:
            fails += 1
        print(f'{test[2]} -> {test[0]}')
        print(f'[{result[passed]}]: Expected - {test[1]} | Outcome - {outcome}')
        print(f'{70 * "+"}')

    print('\nTest Summary')
    print(70 * '-')
    print(f'Run {num_tests} test cases')
    print(f'{passes}/{num_tests} cases passed' * (passes > 0))
    print(f'{fails}/{num_tests} cases failed' * (fails > 0))


if __name__ == '__main__':
    test_cases = [([20, 50], 330, 'Testing largest slice between last and first'),
                  ([13, 45, 68, 100, 300, 330], 200, '')]
    test_suite(test_cases)
