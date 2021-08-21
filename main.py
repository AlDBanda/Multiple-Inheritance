from app import Resident

resident = Resident(name='Jennifer', age='28', id=23)

#resident.print_name()
#resident.print_age()
#resident.print_id()

resident.title()
print(Resident.__mro__)

#method resolution order


