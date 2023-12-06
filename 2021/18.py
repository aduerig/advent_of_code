from functools import partial
from termcolor import colored, cprint
from copy import deepcopy



def do_color(color_str, thing) -> str:
    global blown;
    if id(blown) == id(thing):
        # text = colored(thing, 'red', attrs=['reverse', 'blink'])
        text = colored('[' + ','.join(map(str, thing)) + ']', color_str)
        return text
    elif type(thing) == int:
        return str(thing)
    else:
        return "[" + ','.join(map(partial(do_color, color_str), thing)) + "]"

def good_str(thing):
    if type(thing) == int:
        return str(thing)
    return '[' + ','.join(map(good_str, thing)) + ']'


def magnitude(num):
    if type(num) == int:
        return num
    return magnitude(num[0]) * 3 + magnitude(num[1]) * 2

def copy_add_pair(num1, num2):
    return [deepcopy(num1), deepcopy(num2)]


def explode(num, depth=0):
    global blown; global last_holder; global to_add; global above; global outer;
    if depth > 3 and not blown:    
        blown = above
        if last_holder is not None:
            if type(last_holder[1]) == int:
                last_holder[1] += num[0] 
            else:
                last_holder[0] += num[0]
        to_add = num[1]
        if id(above[0]) == id(num):
            above[0] = 0
        elif id(above[1]) == id(num):
            above[1] = 0
        return

    above = num
    if type(num[0]) == int:
        if blown and to_add is not None:
            num[0] += to_add
            to_add = None
            return
        last_holder = num
    else:
        explode(num[0], depth + 1)
    
    if type(num[1]) == int:
        if blown and to_add is not None:
            num[1] += to_add
            to_add = None
            return
        last_holder = num
    else:
        explode(num[1], depth + 1)

def split(num):
    global blown;
    if type(num) == int:
        return False
    if type(num[0]) == int:
        if num[0] >= 10:
            if num[0] % 2 == 0:
                new = [num[0] // 2, num[0] // 2]
            else:
                new = [num[0] // 2, (num[0] // 2) + 1]
            num[0] = new
            blown = new
            return True 
    if split(num[0]):
        return True
    if type(num[1]) == int:
        if num[1] >= 10:
            if num[1] % 2 == 0:
                new = [num[1] // 2, num[1] // 2]
            else:
                new = [num[1] // 2, (num[1] // 2) + 1]
            num[1] = new
            blown = new
            return True
    if split(num[1]):
        return True

def reducelol(num, break_away=False):
    global blown; global last_holder; global to_add; global above; global outer;
    while True:
        blown = False
        last_holder = None
        to_add = None
        above = None
        outer = num
        explode(num)
        if blown:
            print('curr', "[" + ','.join(map(partial(do_color, 'blue'), num)) + "], EXPLODED")
            if break_away:
                break
            continue
        if split(num):
            print('curr', "[" + ','.join(map(partial(do_color, 'green'), num)) + "], SPLIT")
            continue
        break
    return num

exploders = [
    [[[[[[9,8],1],2],3],4], [[[[0,9],2],3],4]],
    [[7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]]],
    [[[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3]],
    [[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]],
    [[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]]],
]

ok = 0
for k, v in exploders:
    print('testing', ok)
    orig = deepcopy(k)
    print('orig', good_str(orig))
    reducelol(k, True)
    if k != v:
        print('incorrect')
        print('original, mine, correct')
        print(k)
        print(v)
        exit()
    ok += 1

a = [
    [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
    [[[5,[2,8]],4],[5,[[9,9],0]]],
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
    [[[[5,4],[7,7]],8],[[8,3],8]],
    [[9,3],[[9,9],[6,[4,9]]]],
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]],
]


# real input
a = [
    [5,[7,[8,4]]],
[[[4,1],[6,[9,3]]],[[7,4],[5,[7,0]]]],
[[6,2],[[[8,6],[5,5]],0]],
[[[5,9],[3,[4,2]]],[[[1,2],0],2]],
[[[[4,3],2],0],[[[1,7],[1,2]],[[8,2],[6,7]]]],
[[[[0,1],9],3],[[4,7],[7,8]]],
[[[[8,7],4],[5,[9,2]]],[[8,[9,6]],[1,8]]],
[[[2,3],[[9,9],[7,0]]],[6,7]],
[8,[[9,9],[8,6]]],
[[[[5,7],[7,1]],[3,[7,6]]],[2,[[5,5],[8,3]]]],
[[[7,0],2],[[[2,2],7],[6,[2,9]]]],
[[6,2],[[0,8],8]],
[[[[2,9],4],9],[1,[[6,9],[7,5]]]],
[[[9,3],[[5,7],[3,1]]],[5,[6,[7,8]]]],
[0,[[8,9],1]],
[[4,[[4,3],4]],[7,[[4,0],0]]],
[[0,[[1,9],[6,1]]],[[[7,0],[5,2]],[[3,8],[0,4]]]],
[[[2,7],[7,[1,6]]],[6,[[8,7],[8,5]]]],
[[9,5],[[1,[2,5]],[8,[2,0]]]],
[6,[[8,[9,4]],[9,8]]],
[[[[2,0],[4,6]],3],[[8,0],4]],
[[[8,8],[[5,7],[5,6]]],5],
[[5,[[7,9],9]],[1,6]],
[[[[5,2],[4,9]],[[1,9],[2,9]]],[[[6,8],[7,5]],[[0,2],4]]],
[1,[5,[[5,5],[1,2]]]],
[[[1,4],[[0,3],7]],[[[9,1],9],[[2,3],7]]],
[[[[6,4],[4,0]],[[3,4],[7,0]]],[[8,7],[5,[0,6]]]],
[[3,[8,[2,8]]],[9,[0,[5,2]]]],
[[7,[[1,8],1]],[6,[6,6]]],
[[[3,[9,4]],[[3,2],[5,2]]],8],
[3,[[4,[4,3]],[5,[9,2]]]],
[[[1,8],[2,[7,5]]],[[0,[8,1]],[2,0]]],
[1,3],
[7,[[[9,6],[8,4]],9]],
[6,4],
[[[8,9],[[3,7],2]],[4,[[5,0],8]]],
[[[[1,8],[7,9]],0],[[[4,4],3],[4,[1,7]]]],
[[[[2,2],[0,9]],[1,2]],[[[9,1],[0,0]],[[1,6],4]]],
[[[[8,1],6],[[3,3],[6,7]]],[[2,3],5]],
[[[[9,0],7],6],[[[3,6],[6,7]],3]],
[[[[1,0],6],[5,[0,0]]],[[[9,7],7],5]],
[[[[5,1],4],[[7,7],[6,2]]],[[0,[6,0]],2]],
[[[[8,3],[0,4]],[[9,9],[3,7]]],[[[2,7],[2,9]],[[2,0],[4,7]]]],
[6,[[[4,8],0],8]],
[[[6,[5,9]],[[0,3],9]],[[[2,5],[9,5]],0]],
[[1,4],[6,[0,[6,2]]]],
[9,[[[3,7],1],7]],
[[[2,3],[[1,2],1]],[[[2,6],[0,1]],[0,[4,1]]]],
[[[0,1],[[0,3],[7,3]]],[[8,7],3]],
[[0,[[1,5],[5,3]]],4],
[[[5,3],[[5,8],6]],[[[6,0],3],[4,1]]],
[8,3],
[[[[5,5],[3,0]],6],[[7,5],[2,[9,4]]]],
[[[3,[3,3]],[[4,7],4]],[[2,0],1]],
[[[0,[2,8]],[4,[7,9]]],[[[5,4],2],2]],
[[3,[7,[1,8]]],[5,[[8,2],0]]],
[[1,9],[[6,[5,9]],8]],
[[5,[5,2]],5],
[[[1,1],[4,3]],1],
[[[[6,9],[4,1]],0],[[[3,0],6],7]],
[[9,[[7,3],6]],[[[7,2],0],[9,9]]],
[[5,4],[[[6,0],[5,1]],7]],
[[[4,0],0],[[[2,6],[4,4]],[[6,8],2]]],
[[[9,6],8],[[0,[9,5]],9]],
[[6,[2,5]],[[[1,8],[9,0]],[[4,0],[5,7]]]],
[5,[[8,[9,9]],[5,[6,8]]]],
[[[7,[9,0]],5],6],
[[9,[[3,7],[3,0]]],[[[7,2],[5,7]],[[0,5],[7,4]]]],
[[7,3],[[6,5],[9,4]]],
[[4,[4,3]],[9,[[2,6],0]]],
[[[6,[0,1]],9],[[7,[3,2]],[[0,1],[5,2]]]],
[[5,[0,[3,1]]],[[[1,1],[8,9]],[[6,3],[0,9]]]],
[[[[2,8],0],[[8,7],4]],[[[9,6],3],[[7,8],[2,3]]]],
[[[[1,0],1],4],[4,9]],
[[[7,8],5],[[[3,7],[5,7]],6]],
[[[8,[7,4]],[[1,6],[6,7]]],[2,4]],
[[7,8],3],
[[0,[4,[3,8]]],[[[1,0],1],6]],
[[[[6,3],7],2],[[4,5],6]],
[[[5,9],[[1,8],1]],[[[1,8],8],[[6,4],0]]],
[[3,[8,[2,8]]],[[[2,8],[4,4]],9]],
[7,[5,[[3,3],3]]],
[3,[1,[0,[3,0]]]],
[[[1,2],4],[9,[[7,1],[5,4]]]],
[[[5,8],[7,[0,7]]],[0,[[2,9],8]]],
[[[7,[2,0]],[1,[4,3]]],[0,[[1,1],[2,0]]]],
[[[2,[2,5]],[4,1]],[0,[6,0]]],
[[[8,3],9],[[[4,3],[5,8]],[[7,0],9]]],
[2,[1,4]],
[[[3,[2,6]],6],[[[3,2],[0,8]],[[3,5],[6,4]]]],
[[[1,[3,3]],[[0,8],[1,3]]],[8,[[3,8],[0,8]]]],
[[[[1,5],[0,1]],3],[[6,[1,7]],[4,7]]],
[[4,[5,7]],[6,[[6,2],7]]],
[[[[7,4],[3,1]],[5,6]],[0,[6,5]]],
[[[7,[0,0]],6],[5,[[0,0],[3,5]]]],
[[[[8,7],[5,8]],[8,[9,3]]],[[7,0],[[7,2],0]]],
[[[7,[4,2]],0],[[[4,0],1],3]],
[[[6,3],[9,[2,2]]],[[0,8],[1,2]]],
[3,[[3,1],[[7,1],1]]],
[[3,[[4,0],7]],[[[4,6],[2,3]],[[0,2],[1,8]]]],

]



print('==== REAL ===')

# pt 1
# curr = a[0]
# for i in a[1:]:
#     print('new addition')
#     added = copy_add_pair(curr, i)
#     print('curr', good_str(added))
#     curr = reducelol(added)
# print('final', good_str(curr))
# print('magnitude', magnitude(curr))


# pt 2
maxer = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        added = copy_add_pair(a[i], a[j])
        # print('curr', good_str(added))
        curr = reducelol(added)
        maxer = max(maxer, magnitude(curr))

        added = copy_add_pair(a[j], a[i])
        # print('curr', good_str(added))
        curr = reducelol(added)
        maxer = max(maxer, magnitude(curr))


print('max magnitude', maxer)

# not 3873