#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Elemanları alıyoruz
            a = my_list_1[i]
            b = my_list_2[i]
            
            # Sayısal olmayan bir tür varsa
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
                result.append(0)
            else:
                # Bölme işlemi
                result.append(a / b)
        
        except ZeroDivisionError:
            # Bölme sıfıra yapılırsa
            print("division by 0")
            result.append(0)
        
        except IndexError:
            # Liste uzunluğu yetersizse
            print("out of range")
            result.append(0)
        
        finally:
            # Her durumda işlemi bitiririz
            continue
    
    return result
