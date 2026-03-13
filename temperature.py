import os,sys

def convert_temp(value,from_unit,to_unit):
    #конвертация температуры
    if from_unit==to_unit:
        return value
    
    # в цельсии
    if from_unit=='C':
        c=value
    elif from_unit=='F':
        c=(value-32)*5/9
    elif from_unit=='K':
        c=value-273.15
    
    # из цельсия
    if to_unit=='C':
        result=c
    elif to_unit=='F':
        result=c*9/5+32
    elif to_unit=='K':
        result=c+273.15
    
    return result

def main():
    print(convert_temp(100,'C','F'))
    print(convert_temp(32,'F','C'))
    print(convert_temp(0,'K','C'))

if __name__=="__main__":
    main()
