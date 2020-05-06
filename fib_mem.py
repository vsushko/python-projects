import memcache
import time

client = memcache.Client([('127.0.0.1', 11211)])

def memoize(f):
    def helper(x):
        if client.get(str(x)) is None:
            client.set(str(x), f(x))
        return client.get(str(x))

    return helper

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib_mem = memoize(fib)

start = time.time()
print("fib number: ", fib_mem(35))
end = time.time()
print("time: {}".format(end - start))

start = time.time()
print("fib number: " + format(fib(35)))
end = time.time()
print("time: {}".format(end - start))
