#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as plt
import itertools

lam = 0.2

def sigma(x):
    return 1.0 / (1.0 + math.exp(-x))

def dsigma_dx(x):
    return sigma(x) * (1.0 - sigma(x))

n = 8
a = 100 / math.pi
bs = numpy.arange(n) / n * math.pi / 2
# bs = max(bs) - bs  # !!!!!
# print(bs)
print(n)

def exact(x):
    return math.sin(x)

def approx(x):
    return sum(sigma(a*(x - b)) for b in bs) / n

def dapprox_dbi(x, i):
    return - sum(
        dsigma_dx(a*(x - b)) if j==i else 0
        for b, j in zip(bs, itertools.count())
    ) * a / n


def iterate():
    global bs
    dbs = bs * 0
    for x in numpy.arange(20) / 20 * math.pi / 2:
        for i in range(n):
            dbs[i] = lam * (exact(x) - approx(x)) *  dapprox_dbi(x, i)
        bs += dbs

def plot():
    xs = numpy.arange(500) / 500 * math.pi / 2
    plt.plot(xs, [approx(x) for x in xs])
    plt.plot(xs, [exact(x) for x in xs])


if __name__ == '__main__':
    plt.switch_backend('agg')  # to run headless

    plot()
    plt.savefig("../12.approx_sin_initial.svg")
    plt.clf()

    for _ in range(3):
        plot()
        for __ in range(10):
            iterate()

    plt.savefig("../12.approx_sin.svg")

    plt.clf()
    plot()

    plt.savefig("../12.approx_sin_final.svg")
