=====================
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
=====================
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
=====================
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
=====================
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
=====================
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
===================== 5
mul x 0
add x z
mod x 26
div z 26
add x -1
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
=====================
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
===================== 7
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
===================== 8
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
=====================
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
===================== 10
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
===================== 11
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
===================== 12
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
===================== 13
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y


trying to prune again:
===== start


=====================
z = w + 6
=====================
z = (z * 26) + w + 11
=====================
z = (z * 26) + w + 5
=====================
z = (z * 26) + w + 6
=====================
z = (z * 26) + w + 8
===================== 5
z /= 26
if (z % 26) - 1 != y:
    z = (z * 26) + w + 14
=====================
z = (z * 26) + w + 9
===================== 7
z /= 26
if (z % 26) - 16 != y:
    z = (z * 26) + w + 4
===================== 8
z /= 26
if (z % 26) - 8 != y:
    z = (z * 26) + w + 7
=====================
z = (z * 26) + w + 13
===================== 10
z /= 26
if (z % 26) - 16 != y:
    z = (z * 26) + w + 11
===================== 11
z /= 26
if (z % 26) - 13 != y:
    z = (z * 26) + w + 11
===================== 12
z /= 26
if (z % 26) - 6 != y:
    z = (z * 26) + w + 6
===================== 13
z /= 26
if (z % 26) - 6 != y:
    z = (z * 26) + w + 1

===== done




working thru 0 - 4
((((in_inputs[0] + 6) * 26 + in_inputs[1] + 11) * 26 + in_inputs[2] + 5) * 26 + in_inputs[3] + 6) * 26 + 8 = -in_inputs[4]



digit 0 ===========
w0
x = 1
y = w + 6
z = w + 6

=====


digit 1 ===========
w1
x = 1
y = w1 + 11
z = (w0 + 6) * 26 + w1 + 11

digit 2 ===========
w2
x = 1
y = w2 + 5
z = ((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5

digit 3===========
x = 1
y = w3 + 6
z = (((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6

digit 4===========
x = 1
y = w4 + 8
z = ((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8

digit 5===========
z = ((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14

digit 6===========
z = (((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9


digit 7===========
z = (((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4

digit 8===========
z = (((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7

digit 9===========
z = ((((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7) * 26 + w9 + 13

digit 10===========
z = ((((((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7) * 26 + w9 + 13) // 26) * 26 + w10 + 11

digit 11===========
z = ((((((((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7) * 26 + w9 + 13) // 26) * 26 + w10 + 11) // 26) * 26 + w11 + 11

digit 12===========
z = ((((((((((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7) * 26 + w9 + 13) // 26) * 26 + w10 + 11) // 26) * 26 + w11 + 11) // 26) * 26 + w12 + 6

digit 13===========
// 26) * 26
y = w13 + 1
add z y






digit 0 ===========
w0
x = 1
y = w + 6
z = w + 6

=====


digit 1 ===========
w1
x = 1
y = w1 + 11
z = (w0 + 6) * 26 + w1 + 11

digit 2 ===========
w2
x = 1
y = w2 + 5
z = ((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5

digit 3===========
x = 1
y = w3 + 6
z = (((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6

digit 4===========
x = 1
y = w4 + 8
z = ((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8

digit 5===========
z = ((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14

digit 6===========
z = (((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9


digit 7===========
z = (((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4

digit 8===========
z = (((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7

digit 9===========
z = ((((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7) * 26 + w9 + 13

digit 10===========
z = ((((((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7) * 26 + w9 + 13) // 26) * 26 + w10 + 11

digit 11===========
z = ((((((((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7) * 26 + w9 + 13) // 26) * 26 + w10 + 11) // 26) * 26 + w11 + 11

digit 12===========
z = ((((((((((((((((((w0 + 6) * 26 + w1 + 11) * 26 + w2 + 5) * 26 + w3 + 6) * 26 + w4 + 8) // 26) * 26 + w5 + 14) * 26 + w6 + 9) // 26) * 26 + w7 + 4) // 26) * 26 + w8 + 7) * 26 + w9 + 13) // 26) * 26 + w10 + 11) // 26) * 26 + w11 + 11) // 26) * 26 + w12 + 6

digit 13===========
// 26) * 26
y = w13 + 1
add z y





concise 

z = w[0] + 6
z = (z * 26) + w[1] + 11
z = (z * 26) + w[2] + 5
z = (z * 26) + w[3] + 6
z = (z * 26) + w[4] + 8

ztmp = (z % 26) - 1
z //= 26
if ztmp != w[5]:
    z = (z * 26) + w[5] + 14

z = (z * 26) + w[6] + 9

ztmp = (z % 26) - 16
z //= 26
if ztmp != w[7]:
    z = (z * 26) + w[7] + 4

ztmp = (z % 26) - 8
z //= 26
if ztmp != w[8]:
    z = (z * 26) + w[8] + 7

z = (z * 26) + w[9] + 13

ztmp = (z % 26) - 16
z //= 26
if ztmp != w[10]:
    z = (z * 26) + w[10] + 11

ztmp = (z % 26) - 13
z //= 26
if ztmp != w[11]:
    z = (z * 26) + w[11] + 11

ztmp = (z % 26) - 6
z //= 26
if ztmp != w[12]:
    z = (z * 26) + w[12] + 6

ztmp = (z % 26) - 6
z //= 26
if ztmp != w[13]:
    z = (z * 26) + w[13] + 1

return z