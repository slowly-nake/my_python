'''
简单的算法合集：
1. quick_sort()  快速排序

'''


def quick_sort(li, orderly=True):
    '''
    oriderly:顺序或逆序
    '''
    if len(li) < 2:
        return li
    else:
        temp = li[0]
        left = []
        right = []
        for i in range(1, len(li)):
            if li[i] < temp:
                left.append(li[i])
            else:
                right.append(li[i])
        if orderly:
            sort_li = quick_sort(left) + [temp] + quick_sort(right)
        else:
            sort_li = quick_sort(right, orderly=False) + [temp] + quick_sort(left, orderly=False)
        return sort_li
