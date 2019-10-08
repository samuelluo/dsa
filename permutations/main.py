import itertools
import time
from typing import List


def _generate_permutations(chars: List[str], s: str) -> List[str]:
    if len(chars) == 0:
        return [s]
    perms: List[str] = []
    for i, c in enumerate(chars):
        remaining = chars[:i] + chars[i+1:]
        perms_i = _generate_permutations(remaining, s+c)
        perms += perms_i
    return perms


def generate_permutations(chars: List[str]) -> List[str]:
    """
    This version returns List[str].
    """
    perms = _generate_permutations(chars, '')
    return perms


def _perm(chars, elems):
    """
    Parameters
    ----------
    chars : list of str
    elems : list of str

    Returns
    -------
    elems : List[List[str]]
    """
    if len(chars) == 0:
        return [elems]
    perms = []
    for i, c in enumerate(chars):
        remaining = chars[:i] + chars[i+1:]
        perms_i = _perm(remaining, elems+[c])    # perms_i: List[List[str]]
        perms += perms_i
    return perms


def perm(chars):
    """
    This version returns List[List[str]].
    TODO: return List[Tuple[?]]
    """
    return _perm(chars, [])


if __name__ == '__main__':
    test_cases = [
        ['a', 'b', 'c'],
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

        start_time = time.time()
        output = perm(chars)
        end_time = time.time()
        time_elapsed = end_time - start_time
        print([time_elapsed, chars])
        # assert output == expected_raw
