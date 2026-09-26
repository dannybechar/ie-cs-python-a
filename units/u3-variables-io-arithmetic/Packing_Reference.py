# Packing calculator
items = int(input("How many items? "))
per_pack = int(input("How many items per pack? "))

full_packs = items // per_pack
left_over = items % per_pack

print("Full packs:", full_packs)
print("Left over:", left_over)
