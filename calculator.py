# calculator توابع اصلی ماشین حساب

"""جمع دو عدد"""
def add(a, b):
    return a + b

"""تفریق دو عدد"""
def subtract(a, b):
    return a - b

"""ضرب دو عدد"""
def multiply(a, b):
    return a * b

"""تقسیم دو عدد"""
def divide(a, b):
    if b == 0:
        return "خطا: تقسیم بر صفر ممکن نیست!"
    return a / b

"""توان: a به توان b"""
def power(a, b):
    return a ** b

"""باقیمانده"""
def modulus(a, b):
    if b == 0:
        return "خطا: مقسوم‌علیه نمی‌تواند صفر باشد!"
    return a % b