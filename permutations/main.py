import itertools
import time
from typing import List


def _generate_permutations(s: str, chars: List[str]) -> List[str]:
    if len(chars) == 0:
        return [s]
    perms: List[str] = []
    for i, c in enumerate(chars):
        remaining = chars[:i] + chars[i+1:]
        perms_i = _generate_permutations(s+c, remaining)
        perms += perms_i
    return perms


def generate_permutations(chars: List[str]) -> List[str]:
    perms = _generate_permutations('', chars)
    return perms


if __name__ == '__main__':
    test_cases = [
        ["a", "b", "c"],
        ['a', 'b', 'c', 'd'],
    ]

    for chars in test_cases:
        expected_raw = list(itertools.permutations(chars))
        expected = [''.join(t) for t in expected_raw]
        start_time = time.time()
        output = generate_permutations(chars)
        end_time = time.time()
        time_elapsed = end_time - start_time
        print([time_elapsed, chars])
        assert output == expected
