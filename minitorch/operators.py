"""
Collection of the core mathematical operators used throughout the code base.
"""


import math

# ## Task 0.1

# Implementation of a prelude of elementary functions.


def mul(x, y):
    ":math:`f(x, y) = x * y`"
    return x * y
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError("Need to implement for Task 0.1")


def id(x):
    ":math:`f(x) = x`"
    return x
    # TODO: Implement for Task 0.1.
    # raise NotImplementedError("Need to implement for Task 0.1")


def add(x, y):
    ":math:`f(x, y) = x + y`"
    # TODO: Implement for Task 0.1.
    return x + y
    # raise NotImplementedError("Need to implement for Task 0.1")


def neg(x):
    ":math:`f(x) = -x`"
    # TODO: Implement for Task 0.1.
    return -x
    # raise NotImplementedError("Need to implement for Task 0.1")


def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    # TODO: Implement for Task 0.1.
    return 1.0 if x < y else 0.0
    # raise NotImplementedError("Need to implement for Task 0.1")


def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    # TODO: Implement for Task 0.1.
    return 1.0 if x == y else 0.0
    # raise NotImplementedError("Need to implement for Task 0.1")


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    # TODO: Implement for Task 0.1.
    return x if x > y else y
    # raise NotImplementedError("Need to implement for Task 0.1")


def is_close(x, y):
    ":math:`f(x) = |x - y| < 1e-2`"
    # TODO: Implement for Task 0.1.
    return abs(x - y) < 1e-2
    # raise NotImplementedError("Need to implement for Task 0.1")


def sigmoid(x):
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`

    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as

    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >=0 else :math:`\frac{e^x}{(1.0 + e^{x})}`

    for stability.

    Args:
    x (float): input

    Returns:
    float : sigmoid value
    """
    # TODO: Implement for Task 0.1.
    return 1.0 / (1.0 + exp(-x)) if x >= 0.0 else exp(x) / (1.0 + exp(x))
    # raise NotImplementedError("Need to implement for Task 0.1")


def relu(x):
    """
    :math:`f(x) =` x if x is greater than 0, else 0

    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)

    Args:
    x (float): input

    Returns:
    float : relu value
    """
    # TODO: Implement for Task 0.1.
    return max(x, 0)
    # raise NotImplementedError("Need to implement for Task 0.1")


EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(x, d):
    "If :math:`f = log` as above, compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return d * 1.0 / x
    # raise NotImplementedError("Need to implement for Task 0.1")


def inv(x):
    ":math:`f(x) = 1/x`"
    # TODO: Implement for Task 0.1.
    return 1 / x
    # raise NotImplementedError("Need to implement for Task 0.1")


def inv_back(x, d):
    r"If :math:`f(x) = 1/x` compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return d * -1 / x ** 2
    # raise NotImplementedError("Need to implement for Task 0.1")


def relu_back(x, d):
    r"If :math:`f = relu` compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return d if x > 0 else 0
    # raise NotImplementedError("Need to implement for Task 0.1")


# ## Task 0.3

# Small library of elementary higher-order functions for practice.


def map(fn):
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
    fn (one-arg function): Function from one value to one value.

    Returns:
    function : A function that takes a list, applies `fn` to each element, and returns a
    new list
    """

    def f(li):
        return [fn(i) for i in li]

    return f
    # TODO: Implement for Task 0.3.
    # raise NotImplementedError("Need to implement for Task 0.3")


def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    # TODO: Implement for Task 0.3.
    m = map(neg)
    return m(ls)
    # raise NotImplementedError("Need to implement for Task 0.3")


def zipWith(fn):
    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
    fn (two-arg function): combine two values

    Returns:
    function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
    applying fn(x, y) on each pair of elements.

    """
    # TODO: Implement for Task 0.3.
    def f(ls1, ls2):
        return [fn(ls1[i], ls2[i]) for i in range(len(ls1))]

    return f
    # raise NotImplementedError("Need to implement for Task 0.3")


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    # TODO: Implement for Task 0.3.
    f = zipWith(add)
    return f(ls1, ls2)
    # raise NotImplementedError("Need to implement for Task 0.3")


def reduce(fn, start):
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
    fn (two-arg function): combine two values
    start (float): start value :math:`x_0`

    Returns:
    function : function that takes a list `ls` of elements
    :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
    fn(x_1, x_0)))`
    """
    # TODO: Implement for Task 0.3.
    def f(ls):
        a = start
        for i in ls:
            a = fn(i, a)
        return a

    return f
    # raise NotImplementedError("Need to implement for Task 0.3")


def sum(ls):
    "Sum up a list using :func:`reduce` and :func:`add`."
    # TODO: Implement for Task 0.3.
    f = reduce(add, 0)
    return f(ls)
    # raise NotImplementedError("Need to implement for Task 0.3")


def prod(ls):
    "Product of a list using :func:`reduce` and :func:`mul`."
    # TODO: Implement for Task 0.3.
    f = reduce(mul, 1)
    return f(ls)
    # raise NotImplementedError("Need to implement for Task 0.3")
