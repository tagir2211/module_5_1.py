class House:
  def __init__(self, name, number_of_floors):
    self.name = name
    self.number_of_floors = number_of_floors
  def go_to(self, new_floor):
    if new_floor < 1 or new_floor > self.number_of_floors:
      print(f'В доме "{self.name}" нет этажа {new_floor}')
    else:
      for i in range(0, new_floor):
          print(i+1)
          
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

  

