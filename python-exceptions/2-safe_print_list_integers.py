#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):  # Dövrümüzü x qədər dönmək üçün yazırıq.
        try:
            if isinstance(my_list[i], int):  # Elementin tam ədəd olub olmadığını yoxlayırıq
                print("{:d}".format(my_list[i]), end="")  # Tam ədəd isə onu çap edirik.
                count += 1  # Çap edilmiş tam ədədin sayını artırırıq.
        except IndexError:
            break  # Əgər x, my_list uzunluğundan böyükdürsə, dövrü dayandırırıq.
    print()  # Növbəti sətir üçün bir boşluq əlavə edirik.
    return count  # Çap edilmiş tam ədədlərin sayını qaytarırıq.
