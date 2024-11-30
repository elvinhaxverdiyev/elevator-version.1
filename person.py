import random
from move_text import person_text_in, person_text_out

class Person:
    def __init__(self):
        self.p_current_floor = random.randint(1, 10)      
        self.p_target_floor = random.randint(1, 10) 
        self.person_name = random.choice(["leyla", "nigar"])  
        
    def person_enter(self):
        print(f"{self.person_name} {person_text_in}")

    def person_exit(self):
        print(f"{self.person_name} {person_text_out}")