import random
import time
from person import Person
from move_text import elevator_down_text, elevator_up_text, close_text, open_text

class Elevator:
    def __init__(self):
        self.current_floor = random.randint(1, 10)
        
    def up(self):
        print(elevator_up_text)

    def down(self):
        print(elevator_down_text)

    def open_door(self):
        print(open_text)

    def close_door(self):
        print(close_text)

    def elevator_with_person(self, person: Person):
        print(f"liftin oldugu yer>>{self.current_floor }\nserniwinin oldugu yer>> {person.p_current_floor}\nseerniwin getmey istyediyi yer>>{person.p_target_floor}")
        
        # liftin hereketi
        while self.current_floor != person.p_current_floor:
            if self.current_floor < person.p_current_floor:
                time.sleep(1)
                print(f"[ ]--{self.current_floor}-den {self.current_floor+1}-a qalxir")
                self.current_floor += 1
            elif self.current_floor > person.p_current_floor:
                time.sleep(1)
                print(f"[ ]--{self.current_floor}- mertebden {self.current_floor - 1} enir")
                self.current_floor -= 1
        
        print(f"[ ]--{self.current_floor} mertebeye catdi")

        # lift serniwine catanda
        time.sleep(1)
        self.open_door()
        time.sleep(1)
        person.person_enter()
        time.sleep(1)
        self.close_door()
        
        # serniwin minnenn sora
        while self.current_floor != person.p_target_floor:
            if self.current_floor < person.p_target_floor:
                time.sleep(1)
                print(f"{[person.person_name]}--{self.current_floor + 1} qalxir") 
                self.current_floor += 1 
            elif self.current_floor > person.p_target_floor:
                time.sleep(1)
                print(f"{[person.person_name]}--{self.current_floor - 1} enir")
                self.current_floor -= 1 

        # serniwin gedeceyi yere catanda 
        time.sleep(1)
        self.open_door()
        person.person_exit()
        self.close_door()