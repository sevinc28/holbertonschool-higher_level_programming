#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Liste uzunlukları yetersizse, out of range hatası
            a = my_list_1[i]
            b = my_list_2[i]
            
            # Sayısal olmayan bir tür varsa, wrong type hatası
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
                result.append(0)
            else:
                # Bölme işlemi
                result.append(a / b)

        except ZeroDivisionError:
            # Sıfıra bölme hatası
            print("division by 0")
            result.append(0)

        except IndexError:
            # Liste uzunlukları yetersizse
            print("out of range")
            result.append(0)

        finally:
            #
