# Cristian Costilla Puente
# COSC 3339
# 01/15/2026

"""
ASSIGNMENT: INTRODUCTION TO MERGING
-----------------------------------
This file contains several methods with logical errors, poor style, 
and complex constructs. Your goal is to fix them across multiple 
branches to simulate merge conflicts.
"""

import math

import random

# This method contains a bug. In your commit note, state the bug and how you fixed it
def calculate_hypotenuse(SIDE_A, SIDE_B):
    result = math.sqrt(SIDE_A**2 + SIDE_B**2) 
    return result

# This method contains a bug. In your commit note, state the bug and how you fixed it
def count_words(SENTENCE):
    if len(SENTENCE) == 0:
        return 0
    words = SENTENCE.split()  
    return len(words)


# This method is long to allow for non-overlapping edits.
def calculate_shipping_cost(WEIGHT, DESTINATION):
    cost = None
    
    if WEIGHT < 0:   # change #1 ( check ) 
        print("WEIGHT cant be negative!")
        return None
    
    if DESTINATION == "US":
        base_cost = 5.0
        if WEIGHT < 10: # change 2 ( if WEIGHT is less than 10) 
            cost = base_cost
        else:
            # Over 10 lbs, add $1 per extra lb
            extra_WEIGHT = WEIGHT - 10
            cost = base_cost + (extra_WEIGHT * 1.0)
            
    elif DESTINATION == "International":
        base_cost = 14.0 # change 2
        if WEIGHT <= 5:
            cost = base_cost
        else:
            # Over 5 lbs, add $5 per extra lb
            extra_WEIGHT = WEIGHT - 5
            cost = base_cost + (extra_WEIGHT * 5.0)
            
    else:
        # Unknown DESTINATION
        print(f"Error: Unknown DESTINATION {DESTINATION}")
        return 0.0 # change 1

    return round(cost, 2) # change return


# This method uses funky logic. Rewrite it using different loop structures
def curve_SCORES(SCORES):
    curved = []
    for score in SCORES:
        new_score = min(score * 1.05, 100)
        curved.append(new_score)
    return curved

# For scenario three change the name of this method.
# For scenario five fix the typos
def _validate_input(TEXT_VALUE):

    valud_imput = True 
    
    if TEXT_VALUE is None:
        valud_imput = False
    
    if TEXT_VALUE == "":
        valud_imput = False
        
    return valud_imput

def process_user_data (USER_TEXT):
    return _validate_input(USER_TEXT)



def main():
    print("--- STARTING TESTS ---")

    # TEST A: Hypotenuse
    print(f"Test A1 (0, 5): {calculate_hypotenuse(0, 5)} (Expected: 5.0)") 
    print(f"Test A2 (3, 4): {calculate_hypotenuse(3, 4)} (Expected: 5.0)") 

    print("-" * 20)

    # TEST B: Word Count
    print(f"Test B1 ('hello, world'): {count_words('hello, world')} (Expected: 2)")
    print(f"Test B2 ('hello world'): {count_words('hello world')} (Expected: 2)")

    print("-" * 20)

    # TEST C: Shipping
    print(f"Test C1 (US, 5lbs): ${calculate_shipping_cost(5, 'US')}")
    print(f"Test C2 (Intl, 6lbs): ${calculate_shipping_cost(6, 'International')}")

    print("-" * 20)

    # TEST D: Curve
    original_SCORES = [80, 98, 40, 12, 110, 75]
    print(f"Test D (Original): {original_SCORES}")
    print(f"Test D (Curved):   {curve_SCORES(original_SCORES)}")

    print("-" * 20)

    # SCENARIO 3 TEST BLOCK
    # INSTRUCTIONS: 
    # In 'Change Six', you will uncomment the lines below and write 
    # a new function called 'process_user_data' that uses the helper.
    
    print("--- SCENARIO 3 TEST ---")
    user_input = "This is some fake user data"
    if process_user_data(user_input):
        print("Data processed successfully")
    else:
        print("Data invalid")
    
    print("\n--- END OF TESTS ---")

main()
