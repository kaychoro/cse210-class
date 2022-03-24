import random
import time
from clown import Clown
from child import Child
from person import Person

def current_time_ms():
    return round(time.time() * 1000)

clown = Clown()
child = Child()
# person = Person()
persons = [Clown(), Person(), Child(), Clown()]

# print(f'The clown says, "{clown.speak()}"')
# print(f'The child says, "{child.speak()}"')
# print(f'The person says, "{person.speak()}"')
clown.sell_item("a shiny button")

for i in range(len(persons)):
    person:Person = persons[i]
    print(f'This one says, "{person.speak()}"')


# print(current_time_ms())
# first_ballon = clown.buy_balloon(3)
# # first_ballon = Clown.buy_balloon(clown, 3)
# second_ballon = clown.buy_balloon(3)
# ballon_list = []
# for i in range(10):
#     ballon_list.append(clown.buy_balloon(random.randint(1,13)))

# print(clown)

# # while game is running:
# first_ballon.update(current_time_ms())
# first_ballon.pop()
# # first_balloon.pop() means Balloon.pop(first_ballon)
# # the self inside of the pop() function refers to whatever object you're using to call
# # the pop() function with
# ballon_list[random.randint(0,len(ballon_list) - 1)].pop()
# for balloon in ballon_list:
#     print(balloon) # print(str(balloon))
#     # print("Second way " + str(balloon))
#     # print(f"Other way: {balloon.color}: {balloon.volume_ml}")