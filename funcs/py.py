menu_item = {
    "food": "",
    "quantity": "",
    "stars": ""}

items_in_menu = [("food", "pasta"), ("quantity", "2"), ("stars", "5")]


#Put the second value of the touple in the value of the correspondant key of the menu_item dictonary

print(menu_item)

#expected:
#"food": "pasta"
#"quantity": 2
#"stars": 5

contador = 0

while contador < len(items_in_menu):
    item = items_in_menu[contador] 

    menu_item[item] = item[1]

print(menu_item)
