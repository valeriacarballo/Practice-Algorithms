# SIMULATING QUANTUM COMPUTER COMPONENTS



# generate random electron spin
import random

def e_spin():
    e = ["up", "down"]
    return random.choice(e)

# assign qubit to e_spin
spin_state = {
    "up" : 0,
    "down" : 1 
}

print(3)