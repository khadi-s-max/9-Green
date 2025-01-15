"""matnlar"""
print("bu matn edi")
matn="O'zbekiston respublikasi"
python="python the best programming language"
print(matn)
print(python)

""" "" va '' """
print("o'g'il")
print('o\'g\'il')

# atributlar \ metodlar
shaxar="             NamangaN shaXar uychi Tuman    "
print(shaxar.title()) #birinchi xarfini katta qilib chiqaradi
print(shaxar.upper()) #barcha xarfini katta qilib chiqaradi
print(shaxar.capitalize()) #matndagi 1-harfini 1-so'zini  xarfini katta qilib chiqaradi
print(shaxar.lower()) #barcha xarfini kichik qilib chiqaradi


"""strip()"""
print(shaxar) 
print(shaxar.strip())                               
print(shaxar.lstrip())                               
print(shaxar.rstrip())