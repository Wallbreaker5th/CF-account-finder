from typing import *
import numpy as np


def norm(vec: Mapping[str, int]):
    sum = 0
    for i in vec.values():
        sum += i**2
    return sum**0.5


def similarity(a: List[str], b: List[str], n_gram: Union[int, Iterable[int]] = [3, 4]) -> float:
    # Return the similarity (in [0, 1]) between two list of codes.
    # The more similar, the larger the return value is.

    if type(n_gram) == int:
        n_gram = [n_gram]

    vec_a = {}
    vec_b = {}
    for codes, vec in [(a, vec_a), (b, vec_b)]:
        for s in codes:
            t = s

            # It can be faster.
            for i in range(40, 0, -1):
                t = t.replace(' '*i, chr(0xe000+i))
            for i in range(10, 0, -1):
                t = t.replace('\t'*i, chr(0xf000+i))

            for n in n_gram:
                for i in range(len(s)-n+1):
                    substr = t[i:i+n]
                    if substr not in vec:
                        vec[substr] = 0
                    vec[substr] += 1
    for vec in [vec_a, vec_b]:
        for i in vec:
            vec[i] = np.log(vec[i]+1)
    norm_a = norm(vec_a)
    norm_b = norm(vec_b)
    if norm_a == 0 or norm_b == 0:
        return 0
    dot = 0
    for i in vec_a:
        if i in vec_b:
            dot += vec_a[i]*vec_b[i]
    return dot/norm_a/norm_b
