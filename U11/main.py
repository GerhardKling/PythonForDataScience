"""
U11 OOP
@author: Gerhard Kling
"""

from staff import Staff
from firm import Firm

#==================================================================================
#Main
#==================================================================================


#Instance
staff1 = Staff('Amy', 40)
staff2 = Staff('Tom', 35)
print(f'{staff1.name} works for {staff1.hours} hours.')

#Start firm
my_firm = Firm()
print(my_firm.staff)

#Add staff to list
my_firm.add_staff(staff1)
my_firm.add_staff(staff2)

#Show our list
print(my_firm.staff)
