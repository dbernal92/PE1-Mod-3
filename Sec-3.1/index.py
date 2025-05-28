# 3.1.4 Operators

# Equality: the equal to operator (==)
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

# Inequality: the not equal to operator (!=)
var = 0  # Assigning 0 to var
print(var != 0)
 
var = 1  # Assigning 1 to var
print(var != 0)

# 3.1.7 Conditions and conditional execution
# if statement - Runs code only if a condition is true.
# if sheep_count >= 120:
#     sleep_and_dream()

# if-else statement - Adds a fallback ("Plan B").
# if weather_is_good:
#     go_for_a_walk()
# else:
#     go_to_the_theater()

# Nested if-else statements
# One if inside another, each else connects to the closest matching if at the same indentation level.
# if weather_is_good:
#     if nice_restaurant:
#         have_lunch()
#     else:
#         eat_sandwich()
# else:
#     if theater_tickets:
#         go_to_the_theater()
#     else:
#         go_shopping()

# elif: Else If Chains
# Use elif to check multiple conditions without nesting:
#  - means "otherwise, if..."
#  - else is optional but must be last
#  - Only one block in the chain runs

# if weather_is_good:
#     go_for_a_walk()
# elif theater_tickets:
#     go_to_the_theater()
# elif restaurant_tables:
#     go_for_lunch()
# else:
#     stay_home_and_play_chess()
