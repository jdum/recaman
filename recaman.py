#!/usr/bin/env python
# Copyright 2021 Jérôme Dumonteil
# Licence: MIT
# Authors: jerome.dumonteil@gmail.com
"""Calculate Recaman sequence, with API providing term(), list(), range() methods."""
import sys


class Recaman:
    seen = set()
    sequence = {}

    def __init__(self):
        Recaman.sequence[0] = 0
        Recaman.seen.add(0)

    def _term_recursion(self, n):
        if n in Recaman.sequence:
            return Recaman.sequence[n]
        prior = self._term_recursion(n - 1)
        r = prior - n
        if r > 0 and r not in Recaman.seen:
            Recaman.sequence[n] = r
            Recaman.seen.add(r)
            return r
        r = prior + n
        Recaman.sequence[n] = r
        Recaman.seen.add(r)
        return r

    @staticmethod
    def _feed_until(n):
        for i in range(1, n):
            prior = Recaman.sequence[i - 1]
            r = prior - i
            if r > 0 and r not in Recaman.seen:
                Recaman.sequence[i] = r
                Recaman.seen.add(r)
            r = prior + i
            Recaman.sequence[i] = r
            Recaman.seen.add(r)

    def term(self, n):
        """Return the value of item n of the Recaman sequence."""
        if n > 100 and n - 100 not in Recaman.sequence:
            # avoid recursion problem
            self._feed_until(n - 100)
        return self._term_recursion(n)

    def range(self, start, end=None):
        """Return the Recaman sequence as an iterator."""
        if not end:
            start, end = 0, start
        for i in range(start, end):
            yield self.term(i)

    def list(self, start, end=None):
        """Return the Recaman sequence as a list."""
        if not end:
            start, end = 0, start
        return [self.term(i) for i in range(start, end)]


def test():
    expect = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22]
    reca = Recaman()
    assert reca.term(70) == 155
    assert reca.list(6, 11) == expect[6:11]
    i = 0
    for r in reca.range(10):
        assert r == expect[i]
        i += 1


def print_usage():
    print("Usage: recaman {term|list|range|test} start_index [end_index]")


def main():
    if len(sys.argv) > 2:
        command = sys.argv[1]
        args = [int(a) for a in sys.argv[2:]]
        reca = Recaman()
        if command == "list":
            print(" ".join(str(x) for x in reca.range(*args)))
        elif command == "range":
            for x in reca.range(*args):
                print(x)
        elif command == "term":
            print(reca.term(int(sys.argv[2])))
        else:
            print_usage()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "test":
            test()
        else:
            reca = Recaman()
            print(reca.term(int(sys.argv[1])))
    else:
        print_usage()


if __name__ == "__main__":
    main()
