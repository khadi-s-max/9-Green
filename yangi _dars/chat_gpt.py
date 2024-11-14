# import sys
# x = sys.maxsize
# result = x + 1  # Bu yerda maksimal raqamdan oshishga urinish mavjud
# try:
#     x = 10
#     y = 0
#     result = x / y
# except ArithmeticError as e:
#     print(f"Xato yuz berdi: {e}")

def hisobla(yil):
    assert yil > 0, "Yil musbat bo'lishi kerak!"  # Shartni tekshirish
    return 2023 - yil

try:
    print(hisobla(-2000))  # Yilni salbiy qiymatga tenglashtirdik
except AssertionError as e:
    print("Xato:", e)  # 'Yil musbat bo'lishi kerak!' xatosini qaytaradi

    
