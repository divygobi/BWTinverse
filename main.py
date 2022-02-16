# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def inverse(name):
    withCount = ""
    list_with_count = []
    result=""
    for i in name:
        withCount += i + str(withCount.count(i)+1)
    for j in range(0, len(withCount), 2):
        list_with_count.append(withCount[j:j+2])
    sorted_list_with_count=sorted(list_with_count)
    start = sorted_list_with_count[list_with_count.index("$1")]
    for i in range(len(name)):
        result = result + start
        index = list_with_count.index(start)
        start = sorted_list_with_count[index]

    result = ''.join([i for i in result if not i.isdigit()])
    print(f'{result}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inverse('ABB$AILA')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
