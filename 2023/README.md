# 2023## solved 25/25
### retrospective notes 


#### 1
string matching 

###### rating: 3/10

#### 2
string manipulation and some addition

###### rating: 4/10

#### 3
dfs from regex digits found, some fun set stuff to make sure no double count. 

###### rating: 6/10

#### 4
dp is def a weak spot for me. from looking at other solutions i don't think theres a non-n^2 solution. 

###### rating: 7/10

#### 5
for part 2 this was the first problem I had fun writing a brute force to when it definately wasn't the intended solution. `5_jit_optimized.py`. i got it to run in 42 seconds using numba's JIT and iterating through all the maps. 

Numba seems to demand to compile ALL of the function that you decorate to native code, which makes errors much more hard to work through because typing matters a lot. There's also definately an art to trying to intuit what the JIT will compile your code down to. Definately a case where profiling each change is important if you care about speed.

`5_alternate_part_2.py` implements the range based splitting solution that I read about after solving with the brute force above. I actually really enjoyed this as well. Abstracting the complex range precities into `range_difference` and `range_intersection` and then working with those concepts makes the problem very solvable even though working with ranges has tons of small off by 1 problems and complexities. 

###### rating: 9/10


#### 6
I first implemented as a linear search which runs fast enough, but after I coded as a binary search for fun / practice. I read online and chatted with a friend about it and realized I didn't catch that this problem always followes a quadratic curve, which makes sense.

I just solved it mathmatically by finding the critical points and subtracting for fun at the top of 6.py. I really like problems with several ways to solve.

###### rating: 7/10

#### 7

Implementation challenge problem for part 1. very subtly different poker rules. was fun to try to make a concise function to assign the rankings of a hand, though I don't really think I succeeded in making it readable...
```python
def get_type(a, b, c, d, e):
    if a != b:
        return 1
    if a == b == c == d == e:
        return 7
    if a == b == c == d:
        return 6
    if a == b == c:
        if d == e:
            return 5
        return 4
    if c == d:
        return 3
    return 2
```


#### 8

#### 9

#### 10

#### 11

#### 12

#### 13

#### 14

#### 15

#### 16

#### 17

#### 18

#### 19

#### 20

#### 21

#### 22

#### 23

#### 24

#### 25

