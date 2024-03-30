from ex1 import first_file_read
def predic(a, b):
    """
    принимает два кортежа и возвращает истину если 1 элемнт первого кортежа больше первого элемента второго кортежа
    :param a: 1 кортеж
    :param b: 2 кортеж
    :return кто большше
    """
    return a[0] > b[0]

def merge(a, b):
    """
    принимает 2 отсортированных кортежа и возвращает их отсортированное обьединение
    :param a: кортеж 1
    :param b: кортеж 2
    :return: слитый кортеж
    """
    ans = []
    n = 0
    m = 0
    while(n < len(a) and m < len(b)):
        if(predic(a[n], b[m])):
            ans.append(a[n])
            n += 1
        else:
            ans.append(b[m])
            m += 1
    if(n < len(a)):
        for i in range(n, len(a)):
                ans.append(a[i])
    if (m < len(b)):
        for i in range(m, len(b)):
            ans.append(b[i])
    return ans
def merge_sort(a):
    """
    рекурсивно сортирует кортеж
    :param a: кортеж который надо отсортировать
    :return: отсортированный кортеж
    """
    mid = int((len(a) / 2))
    if len(a) == 1:
        return  a
    return  merge(merge_sort(a[0 : mid]), merge_sort(a[mid : len(a)]))
sorted_ = merge_sort(first_file_read(("devices.txt")))
for i in range(0, 5):
    e = sorted_[i]
    print(f"{e[0]}-e{e[1]}-{e[8]}")
with open("devices.txt", "w") as f:
    for i in sorted_:
        f.write("*".join(i) + "\n")

