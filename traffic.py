from time import sleep

class traffic_lights:
    def __init__(self):
        self.red = 1
        self.yellow = 0
        self.green = 0
    
#########################################################################################################################################################################

class A(traffic_lights):
    #Print the lights 
    def print_lights(self,B,C,D):
        print("R_A:", self.red, "R_B:", B.red, "R_C:", C.red, "R_D:", D.red)
        print("Y_A:", self.yellow, "Y_B:", B.yellow,"Y_C:", C.yellow,"Y_D:", D.yellow)
        print("G_A:",self.green,"G_B:",B.green,"G_C:",  C.green,"G_D:", D.green)
        
    def run(self, a, b, c):
        #Run the sequence of traffic lights
        self.red = 1
        self.yellow = 1
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        sleep(2)
        self.red = 0
        self.yellow = 0
        self.green = 1
        self.print_lights(a,b,c)
        print("\n")
        sleep(30)
        self.red = 0
        self.yellow = 1
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        sleep(5)
        self.red = 1
        self.yellow = 0
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")

class B(traffic_lights):
    #Print the lights
    def print_lights(self,A,C,D):
        print("R_A:", A.red, "R_B:", self.red, "R_C:", C.red, "R_D:", D.red)
        print("Y_A:", A.yellow, "Y_B:", self.yellow,"Y_C:", C.yellow,"Y_D:", D.yellow)
        print("G_A:",A.green,"G_B:",self.green,"G_C:",  C.green,"G_D:", D.green)
        
    def run(self, a, b, c):
        #Run the sequence of traffic lights
        self.red = 1
        self.yellow = 1
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        sleep(2)
        self.red = 0
        self.yellow = 0
        self.green = 1
        self.print_lights(a,b,c)
        print("\n")
        sleep(30)
        self.red = 0
        self.yellow = 1
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        sleep(5)
        self.red = 1
        self.yellow = 0
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        
class C(traffic_lights):
    #Print the lights
    def print_lights(self,A,B,D):
        print("R_A:", A.red, "R_B:", B.red, "R_C:", self.red, "R_D:", D.red)
        print("Y_A:", A.yellow, "Y_B:", B.yellow,"Y_C:", self.yellow,"Y_D:", D.yellow)
        print("G_A:",A.green,"G_B:",B.green,"G_C:",  self.green,"G_D:", D.green)
    
    def run(self, a, b, c):
        #Run the sequence of traffic lights
        self.red = 1
        self.yellow = 1
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        sleep(2)
        self.red = 0
        self.yellow = 0
        self.green = 1
        self.print_lights(a,b,c)
        print("\n")
        sleep(30)
        self.red = 0
        self.yellow = 1
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        sleep(5)
        self.red = 1
        self.yellow = 0
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")

class D(traffic_lights):
    #Print the lights
    def print_lights(self, A, B, C):
        print("R_A:", A.red, "R_B:", B.red, "R_C:", C.red, "R_D:", self.red)
        print("Y_A:", A.yellow, "Y_B:", B.yellow,"Y_C:", C.yellow,"Y_D:", self.yellow)
        print("G_A:",self.green,"G_B:",B.green,"G_C:",  C.green,"G_D:", self.green)
    
    def run(self, a, b,c):
        #Run the sequence of traffic lights
        self.red = 1
        self.yellow = 1
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        sleep(2)
        self.red = 0
        self.yellow = 0
        self.green = 1
        self.print_lights(a,b,c)
        print("\n")
        sleep(30)
        self.red = 0
        self.yellow = 1
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")
        sleep(5)
        self.red = 1
        self.yellow = 0
        self.green = 0
        self.print_lights(a,b,c)
        print("\n")

a = A()
b = B()
c = C()
d = D()


i = 5
while(i!=0):
    a.run(b,c,d)
    b.run(a,c,d)
    c.run(a,b,d)
    d.run(a,b,c)
    i = i-1
