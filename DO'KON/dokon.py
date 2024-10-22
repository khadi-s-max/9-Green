"""17|10|2024|"""
o=["olma","apelsin","gilos","non"]
print(f"Assalomu aleykum, Do'komimizga xush kelibsiz!\n bizda quyigadi {len(o)} maxsulotlar bor:",end="")
for mx in o:
    if mx==o[0]:
        print(f"{mx.title()}",end=" ,")
    elif mx==o[-1]:
        print(f"{mx.title()}",end=" ,")
    else:
        print(f"{mx.title()}",end=" ,")
        