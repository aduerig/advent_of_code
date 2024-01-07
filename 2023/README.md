# 2023## solved 25/25
### retrospective notes 


### 1
string matching 

###### rating: 3/10

### 2
string manipulation and some addition

###### rating: 4/10

### 3
dfs from regex digits found, some fun set stuff to make sure no double count. 

###### rating: 6/10

### 4
dp is def a weak spot for me. from looking at other solutions i don't think theres a non-n^2 solution. 

###### rating: 7/10

### 5
for part 2 this was the first problem I had fun writing a brute force to when it definately wasn't the intended solution. `5_jit_optimized.py`. i got it to run in 42 seconds using numba's JIT and iterating through all the maps. 

Numba seems to demand to compile ALL of the function that you decorate to native code, which makes errors much more hard to work through because typing matters a lot. There's also definately an art to trying to intuit what the JIT will compile your code down to. Definately a case where profiling each change is important if you care about speed.

`5_alternate_part_2.py` implements the range based splitting solution that I read about after solving with the brute force above. I actually really enjoyed this as well. Abstracting the complex range precities into `range_difference` and `range_intersection` and then working with those concepts makes the problem very solvable even though working with ranges has tons of small off by 1 problems and complexities. 

###### rating: 9/10


### 6
I first implemented as a linear search which runs fast enough, but after I coded as a binary search for fun / practice. I read online and chatted with a friend about it and realized I didn't catch that this problem always followes a quadratic curve, which makes sense.

I just solved it mathmatically by finding the critical points and subtracting for fun at the top of 6.py. I like problems with several ways to solve.

###### rating: 6/10

### 7

Implementation challenge problem for part 1. poker, but subtly different. was fun to try to make a concise function to assign the rankings of a hand, though I don't really think I succeeded in making it readable...
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

###### rating: 6.5/10

### 8

binary graph traversal problem. part 2 has multiple start and end points. we want to find the number on when all the starts are on some end. The way I solved it is by taking the LCM of the cycle length of all the starts to the ends.

I later was told by a friend that this isn't nesseccarily true for all inputs though, for multiple reasons. If the graph is more complex and start points can hit multiple ending points, the cycles are much much more confusing. Imagine 3 start nodes which reach an end point at the following indexes:
```
A: (2, 7, 12, 17...) AND (4, 15, 26, 37...)
B: (3, 16, 29, 42...)
```

which also can be written in a fancy math way...
```
t ≡ 2 (mod 5)   [from A]
t ≡ 4 (mod 11)  [from A]
t ≡ 3 (mod 13)  [from B]
```

I spent some time reading some math and I believe when you can solve this LCM whenever the remainders are 0, but not when they are non-zero. Then the Chinese Remainder Theorem (CRT) is used.

##### GCD tangent

CRT relies on calculating GCD's, which lead me to read about euclid's algorithm, which in itself is interesting. It's an quick iterative algorithm, and it relies on the fact that when a > b, GCD(a, b) == GCD(a % b, b). (this is basically the algorithm anyway).

And then to calculate the GCD between many integers we can just run it iteratively on pairs on numbers. But honestly even the fact that GCD(a, b, c) == GCD(GCD(a, b), c) is suprising to me, though after playing around with some numbers it does become clear you can't find an easy counterexample (I don't know the proof).

Both of the properties are interesting and I don't know if I should try to understand them more intrinsically, but I'll try to just memorize them for now.

##### Back to CRT

CRT relies on the fact that all the modulus (number after mod) is coprime with all others. You can calculate coprimeness by taking the GCD of all numbers (using the above method). If it is anything other than 1, it is not coprime. You can do this with arbitrary NON-coprime inputs using prime factorization: 
```
x ≡ 1 (mod 16)
x ≡ 5 (mod 40)

After factoring above because they aren't coprime:

x ≡ 1 (mod 2)
x ≡ 1 (mod 8)
x ≡ 5 (mod 40)

which x ≡ 1 (mod 8) is actually contained WITHIN x ≡ 5 (mod 40), so your final input is:

x ≡ 1 (mod 2)
x ≡ 5 (mod 40)
```

[Maybe there's a more straightforward way to calculate CRT without reducing the inputs to non-coprime inputs](https://math.stackexchange.com/questions/1644677/what-to-do-if-the-modulus-is-not-coprime-in-the-chinese-remainder-theorem), but I don't have the capacity to understand that.

For non-coprime inputs, there's actually MANY ways to find impossibilities. If you ever reduce to the same modulus, but different remainders, it is clear there is no solution. Now, for actually implementing CRT I followed [this video for the concepts](https://www.youtube.com/watch?v=ru7mWZJlRQg), which I implemented to:

```python
def crt(remainders, mods):
    total_prod = functools.reduce(lambda x, y: x * y, mods)

    products_but = [total_prod] * len(remainders)
    for index, mod in enumerate(mods):
        products_but[index] = products_but[index] // mod
    answer = 0
    for product, mod, remainder in zip(products_but, mods, remainders):
        mult = 1
        while True:
            if (mult * product) % mod == (remainder % mod):
                answer += mult * product
                break
            mult += 1
    return answer % total_prod
remainders = [2, 2, 1]
mods       = [3, 4, 5]
print(crt(remainders, mods))
```

Note, to find the modulo inverse (I hardly even know what that is). I implemented a linear search, but a faster method is using euclids EXTENDED algorithm.

I think for any practical usage of CRT you will need to handle the non-coprime case since there's no real world application that would product numbers that are coprime. So any good implementation will have to do all the prime factorization or something fancier, which really gets hairy.

Anyway, all of the above is irrelevant because the problem input has cycles that start at t=0.

###### rating: 2/10 (I don't like math)

### 9

This problem is all about fitting some curve and predicting the next value. The problem has explicit and strange instructions on what seemed to me a very roundabout way of doing exactly that, but when I read them I thought there could be a fancier way to do it in O(n) time. After struggling a bit I thought about it more and realized the instructions given might be the most effeciect way to predict the curve. I'm tempted to believe the instructions given is actually close to an algorithm for polynomial fitting or something. (People were talking about the langrange interpolation formula online?)

I don't feel like doing the deep dive right now, but there's probably some interesting mathematical concept here. Also pascals triangle is probaly related here.

I'm also happy I found the input reversal trick for part 2.

###### rating: 5.5/10

### 10

A bit mind bending to think about. I realized pretty quickly after part 1 that I needed to write a "0.5 index" DFS. This felt familiar to me because I realized this problem is actually just a maze creation algorithm I wrote long ago. It was my first ever personal project I had ever written. (I didn't make the algorithm). You first act as a point following the lines of the maze throughout a 2D grid, then you use the space inbetween the lines as your playing space (the solving), and the lines are your walls.

The only hiccup at the end was determining which space was "inside" and which was "outside", which normally isn't a problem in mazes because they are fully connected. I ended up just printing all spaces and guessing based off this visualization I made during debugging

![small](pictures/10_small.png)
![large](pictures/10_large.png)


###### rating: 9/10

### 11

### 12

### 13

### 14

### 15

### 16

### 17

### 18

### 19

### 20

### 21

### 22

### 23

### 24

### 25

###### rating: 1/10 (I really don't like math)