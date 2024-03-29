def isprime(n) -> bool:
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    if n < 2:
        return False #return False해서 끝낸다/2이상일 때 약수발생하면 return False해서 끝낸다
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

def fahrenheit_to_celcius(fahrenheit) -> float :
    return (fahrenheit - 32.0)*5.0/9.0

def celcius_to_fahrenheit(celcius) -> float :
    return (celcius * 9.0/5.0)+32.0