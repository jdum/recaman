## Recamán's sequence

Calculate Recamán's sequence, with API providing term(), list(), range() methods.

First terms are:

0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, ...

For information on this sequence, see:
https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence


### Usage from command line:

- term of sequence at some position:

    ```
    $ ./recaman.py term 10
    11
    ```

- sequence, space separator:

    ```
    $ ./recaman.py list 10
    0 1 3 6 2 7 13 20 12 21
    ```

    ```
    $ ./recaman.py list 10 12
    11 22
    ```

- sequence, newline separator:

    ```
    $ ./recaman.py range 4
    0
    1
    3
    6
    ```

    ```
    $ ./recaman.py range 8 12
    12
    21
    11
    22
    ```

    ```
    $ ./recaman.py range 1000000 1000005
    499798510100
    499797510099
    499796510097
    499795510094
    499794510090
    ```

### Usage from python:

    >>> from recaman import Recaman
    >>> reca = Recaman()
    >>> reca.term(10)
    11
    >>> reca.list(11)
    [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11]
    >>> for r in reca.range(1000000, 1000005): print(r)
    ...
    499798510100
    499797510099
    499796510097
    499795510094
    499794510090
