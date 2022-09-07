def make_juice(fruit):
    return f"{fruit}+★"

def make_ice(juice):
    return f"{juice}+§"

def input_sugar(su):
    return f"{make_ice}+＠"

juice = make_juice("♥")

iced_juice = make_ice(juice)

perfact_juice = input_sugar(make_ice)

print(perfact_juice)
