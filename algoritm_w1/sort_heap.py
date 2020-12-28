from typing import MutableSequence
"""
힙 정렬 절차:
    1. 힙으로 만들기
    2. 최대 루트 꺼내서 배열 마지막으로 보내고 남은 부분 다시 힙으로 만들기(모든 원소에 대해서 적용)
"""


def heap_sort(a: MutableSequence) -> None:

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        temp = a[left]

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n-1) // 2, -1, -1):  # 밑에서부터 위로 (자식이 있는 노드에 대해서만)
        down_heap(a, i, n-1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)


if __name__ = "__main__":
    print("힙 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    print("오름차 순으로 정렬했습니다.")
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
