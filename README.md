# sloth-cli

![logo](docs/sloth.jpg)

A library to speed the profile (cProfile) analyses of code performance on a per
line basis. This library allow the user to call a python script file with 
arguments and analyse what lines of code are taking longer to process.

An example output of the `sloth-cli`:

```shell
Sat Jun  8 11:56:40 2019    profileOutput.profile

         5400 function calls (5340 primitive calls) in 3.017 seconds

   Ordered by: cumulative time
   List reduced from 352 to 100 due to restriction <100>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      4/1    0.000    0.000    3.017    3.017 {built-in method builtins.exec}
        1    0.000    0.000    3.017    3.017 tester.py:1(<module>)
        1    0.000    0.000    3.014    3.014 tester.py:21(run)
        3    3.012    1.004    3.012    1.004 {built-in method time.sleep}
``` 

## Install

```
pip install sloth-cli
```

## CLI Usage

Using a `tester.py` cli script (argsparse):

### To run `tester.py` with arguments:

```bash
sloth -f tester.py --cmd fake --fake-arg test
```

### To get the `tester.py` help:

```bash
sloth -f tester.py -l 100 --cmd --help
```

## Decorator Usage

The `sloth.profile` allows you to gather the profile data by adding it as
a decorator. The decorator can be enabled or disabled whenever needed. It 
can also be turned on by setting the environment variable `SLOTH_PROFILE` 
to `True` (`SLOTH_PROFILE='True'`) so you can set add it to your code and 
leave it; then just turn it on when you need to validate the code performance.

### To use the decorator do the following

```python
import time

from sloth_cli import profile


def _loop_sleep():
    """Loops and sleeps"""
    for i in range(3):
        print(i)
        time.sleep(1)


def _loop():
    """Loops 1000 times"""
    ints = []
    for i in range(1000):
        ints.append(i)


@profile(enable=True, lines=50, builtins=False)
def run():
    """Run loops"""
    _loop()
    _loop()
    _loop_sleep()


if __name__ == '__main__':
    run()
```

```bash
         10 function calls in 3.006 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.006    3.006 test_profiler.py:20(run)
        1    3.005    3.005    3.005    3.005 test_profiler.py:6(_loop_sleep)
        6    0.000    0.000    0.000    0.000 capture.py:413(write)
        2    0.000    0.000    0.000    0.000 test_profiler.py:13(_loop)
```
