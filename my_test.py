# import my_algorithm.simple_algorithm as algorithm
#
# li = [1, 34, 78, 16, 9, 1]
# a = algorithm.quick_sort(li, orderly=False)
# print(a)

# class Li():
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# l3 = Li(3)
# l2 = Li(2, l3)
# l1 = Li(1, l2)
#
# print(l1.val)
# print(l1.next.val)
# print(l1.next.next.val)


# def cou(a):
#     n = 0
#     if a < 1:
#         return n
#     elif a < 10:
#         n += 1
#         return n
#     else:
#         a = a/10
#         n = cou(a) + 1
#         return n
#
# print(cou(float(input())))


# a = [123,345,555,666]
#
# print(a.pop())
#
# print(a)


def num_ways(steps: int, arr_len: int) -> int:
    # write your code here
    return dig(steps, arr_len, 0)


def dig(steps, arr_len, pos):
    if pos < 0 or pos >= arr_len or steps < pos:
        return 0
    if steps == 0:
        return 1 if pos == 0 else 0
    return dig(steps - 1, arr_len, pos - 1) + dig(steps - 1, arr_len, pos) + dig(steps - 1, arr_len, pos + 1)

print(num_ways(4, 2))


a =