from time import sleep
import os

class traffic_lights:
    def __init__(self):
        self.red = 1
        self.yellow = 0
        self.green = 0
        self.delay_1 = 2
        self.delay_2 = 30
        self.delay_3 = 5
        
#######################################################################################

    #Initiate the traffic light run    
    def run(self, a, b, c, d):
        
        
        #Print the lights
        def print_lights(A,B,C,D):
            print("R_A:", A.red, "R_B:", B.red, "R_C:", C.red, "R_D:", D.red)
            print("Y_A:", A.yellow, "Y_B:", B.yellow,"Y_C:", C.yellow,"Y_D:", D.yellow)
            print("G_A:",A.green,"G_B:",B.green,"G_C:",  C.green,"G_D:", D.green)
            
        #Run the sequence of traffic lights
        self.red = 1
        self.yellow = 1
        self.green = 0
        print_lights(a,b,c,d)
        print("\n")
        sleep(self.delay_1)
        self.red = 0
        self.yellow = 0
        self.green = 1
        print_lights(a,b,c,d)
        print("\n")
        sleep(self.delay_2)
        self.red = 0
        self.yellow = 1
        self.green = 0
        print_lights(a,b,c,d)
        print("\n")
        sleep(self.delay_3)
        os.system('cls')
        self.red = 1
        self.yellow = 0
        self.green = 0
        print_lights(a,b,c,d)
        print("\n")
        
a = traffic_lights()
b = traffic_lights()
c = traffic_lights()
d = traffic_lights()


i = 5
while(i!=0):
    a.run(a,b,c,d)
    b.run(a,b,c,d)
    c.run(a,b,c,d)
    d.run(a,b,c,d)
    i = i-1
