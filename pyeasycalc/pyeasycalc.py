import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_even(n):
    return n % 2 == 0
    # code by aadidev11 on github
    
def is_odd(n):
    return n % 2 != 0

def is_str_palindrome(s):
    # checks if the string is the same backwords (case sensitive)
    return s == s[::-1]

def is_int_palindrome(n):
    # checks if a integer is the same backwards
    s = str(n)
    return s == s[::-1]

def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_f(c):
    return (c * 9 / 5) + 32

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

def sum_list(lst):  # sum of a list
    return sum(lst)

def avg_list(lst):  # average of a list
    return sum(lst) / len(lst) if lst else 0

def fact(n):  # factorial
    return math.factorial(n)

def sqr(n):  # square
    return n * n

def sqrt_num(n):  # square root
    return math.sqrt(n)

def cube(n):  # cube
    return n ** 3

def min_list(lst):  # smallest value in list
    return min(lst) if lst else None

def max_list(lst):  # largest value in list
    return max(lst) if lst else None

def med_list(lst):  # median of list
    s = sorted(lst)
    l = len(s)
    if l == 0:
        return None
    mid = l // 2
    if l % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    else:
        return s[mid]

def rng_list(lst):  # range (max - min)
    return max(lst) - min(lst) if lst else None

def pow_num(base, exp):  # power
    return base ** exp

def abs_num(n):  # absolute value
    return abs(n)

def gcd_num(a, b):  # greatest common divisor
    return math.gcd(a, b)

def lcm_num(a, b):  # least common multiple
    return abs(a * b) // math.gcd(a, b) if a and b else 0

def pct(part, whole):  # percentage
    return (part / whole) * 100 if whole else 0

def deg_to_rad(deg):  # degrees → radians
    return math.radians(deg)

def rad_to_deg(rad):  # radians → degrees
    return math.degrees(rad)





    

        
