class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name= name
    self.items= items
    self.start_time= start_time
    self.end_time= end_time

  def __repr__(self):
    return "{} menu available from {} to {}.".format(self.name,self.start_time,self.end_time)
  def calculate_bill(self,purchased_items):
    bill=0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill+=self.items[purchased_item]
    return bill

class Franchise:
  def __init__(self,address,menus):
    self.address= address
    self.menus= menus
  def __repr__(self):
    return "Address of the Restaurant: {}.".format(self.address)
  def available_menus(self,time):
    available_menus=[]
    for menu in self.menus:
#IMPORTANTEEEEEEEEEEEEEEEEEEEEE AQUI SE ASOCIA CON LA OTRA CLASE
      if time>= menu.start_time and time<=menu.end_time:
        available_menus.append(menu)
    return available_menus

class Business:
  def __init__(self,name,franchises):
    self.name= name
    self.franchices = franchises

#DICCIONARIO
brunch_items={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
# ASOCIANDO Y EJECUTANDO IMPRIMIENDO UNA CLASE CON PARAMETROS DADOS SE EJECUTARA EL INIT Y EL REPR
brunch_menu=Menu('Brunch',brunch_items,1100,1600)
print(brunch_menu)
#IMPRIMIENDO UN METODO FUNCION QUE SE EJECUTA CON UNA VARIABLE ASOCIADA  A UNA CLASE
print(brunch_menu.calculate_bill(['pancakes','fries','coffee']))
print("\t")

#DICCIONARIO
early_bird_items={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
# ASOCIANDO Y EJECUTANDO IMPRIMIENDO UNA CLASE CON PARAMETROS DADOS SE EJECUTARA EL INIT Y EL REPR
early_bird_menu=Menu('Early Bird',early_bird_items,1500,1800)
print(early_bird_menu)
#IMPRIMIENDO UN METODO FUNCION QUE SE EJECUTA CON UNA VARIABLE ASOCIADA  A UNA CLASE
print(early_bird_menu.calculate_bill(['mushroom ravioli (vegan)','salumeria plate']))
print("\t")

#DICCIONARIO
dinner_items={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
# ASOCIANDO Y EJECUTANDO IMPRIMIENDO UNA CLASE CON PARAMETROS DADOS SE EJECUTARA EL INIT Y EL REPR
dinner_menu=Menu('Dinner',dinner_items,1700,2300)
print(dinner_menu)

#DICCIONARIO
kids_items={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
# ASOCIANDO Y EJECUTANDO IMPRIMIENDO UNA CLASE CON PARAMETROS DADOS SE EJECUTARA EL INIT Y EL REPR
kids_menu=Menu('Kids',kids_items,1100,2100)
print(kids_menu)

print("\t")
#LISTA CON UN CONJUNTO DE ELEMENTOS ASOCIADOS A UNA CLASE. MENUS_LIST ES UNA LISTA QUE ASOCIA A ELEMENTOS DE LA CLASE MENU
menus_rest=[brunch_menu,early_bird_menu,dinner_menu,kids_menu]
#ASOCIANDO UNA VARIABLE A LA CLASE FRANCHISE, RECORDAR QUE MENUS_REST ESTA ASOCIADO A CLASE MENU
flagship_store= Franchise("1232 West End Road",menus_rest)
new_installment=Franchise("12 East Mulberry Street",menus_rest)
# IMPRIMIRA EL CONSTRUCTOR INIT DEL FRANCHISE
print(flagship_store)
# IMPRIMIRA EL METODO AVAILABLE MENUS DONDE HAY CLASES ASOCIADAS CON LA CLASE MENU YA QUE LA VARIABLE MENUS_REST ASOCIA AL LA CLASE FRANCHISE CON LOS MENUS
print(flagship_store.available_menus(1800))

basta=Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])
#Arepa
arepas_items={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu=Menu('Take a’ Arepa',arepas_items,1000,2000)

arepas_place=Franchise("189 Fitzgerald Avenue",[arepas_menu])

arepa=Business('Take a’ Arepa',[arepas_place])

print(arepa.franchices[0])