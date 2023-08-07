# 0x01. Python - Async
```Python``` ```Back-end```

### Learning Objectives
- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

```
0-basic_async_syntax.py

"""
an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) that
waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
```
```
1-concurrent_coroutines.py

"""
an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified
max_delay.
"""
```
```
2-measure_runtime.py

"""
function with integers n and max_delay as arguments
that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n.
"""
```
```
3-tasks.py

"""
a function task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""
```
```
4-tasks.py

"""
a new function task_wait_n.
task_wait_random is being called.
"""
```