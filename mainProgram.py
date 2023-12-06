 # Draw a hexagon around Target 1
from robolink import *    # RoboDK's API
from robodk import *      # Math toolbox for robots
 
# Start the RoboDK API:
RDK = Robolink()
 
# Get the robot (first robot found):
robot = RDK.Item('KUKA KR 6 R900 sixx', ITEM_TYPE_ROBOT)
 
# Get the reference target by name:
home = RDK.Item('Home')
target = RDK.Item('Target 1')
target_pose = target.Pose()
xyz_ref = target_pose.Pos()
 
# Move the robot to the reference point:
robot.MoveJ(home)
robot.MoveJ(target)

def semi_circulo(valorx, valory ,angulo_inicial, angulo_final, raio, direcao):
    xyz_ref[0] += valorx #valor x do Centro do Circulo
    xyz_ref[1] += valory #valor y do Centro do Circulo
      # Raio do semicírculo
    num_pontos = 50

    if(direcao=="inversa"):
        for i in range(num_pontos +1):
            angulo = angulo_inicial + (angulo_final - angulo_inicial) * i / num_pontos
            x = xyz_ref[0] - raio * cos(angulo * pi / 180) # new X coordinate
            y = xyz_ref[1] - raio * sin(angulo * pi / 180) # new Y coordinate
            z = xyz_ref[2] # new Z coordinate
            target_pose.setPos([x,y,z])
            if(i):
                robot.MoveJ(target_pose)


    if(direcao=="correta"):
        for i in range(num_pontos +1):
            angulo = angulo_inicial + (angulo_final - angulo_inicial) * i / num_pontos
            x = xyz_ref[0] + raio * cos(angulo * pi / 180) # new X coordinate
            y = xyz_ref[1] + raio * sin(angulo * pi / 180) # new Y coordinate
            z = xyz_ref[2] # new Z coordinate
            target_pose.setPos([x,y,z])
            if(i):
                robot.MoveJ(target_pose)

            
    xyz_ref[1] += -valory
    xyz_ref[0] += -valorx

def desenha_b():
    m=0
    for ponto in pontos_letra_b:
        m+=1
        if(m==3):
            semi_circulo(50, 30 , 90, 270, 30, "inversa")
    
        if(m==4):
            semi_circulo(50, 80, 90, 270, 20, "inversa")

        if(m==11):
            semi_circulo(50, 32.5, 90, 270, 17.5, "inversa")

        if(m==18):
            semi_circulo(50, 80, 90, 270, 10, "inversa")
        
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
    
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_c():
    m=0
    for ponto in pontos_letra_c:
        m+=1
        if(m==6):
            semi_circulo(50, 50 , 270, 90, 25, "correta")
        if(m==10):
            semi_circulo(50, 50 , 90, 270, 50, "correta")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_d():
    m=0
    for ponto in pontos_letra_d:
        m+=1
        if(m==3):
            semi_circulo(50, 50 , 90, 270, 50, "inversa")
        if(m==10):
            semi_circulo(50, 50 , 90, 270, 25, "inversa")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_g():
    m=0
    for ponto in pontos_letra_g:
        m+=1
        if(m==4):
            semi_circulo(50, 50, 270, 50, 50, "correta")
        if(m==6):
            semi_circulo(50, 50, 50, 360, 25, "correta")
        if(m==8):
            semi_circulo(50, 50, 360, 270, 50, "correta")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_j():
    m=0
    for ponto in pontos_letra_j:
        m+=1
        if(m==5):
            semi_circulo(50, 40, 360, 180, 40, "correta")
        if(m==8):
            semi_circulo(50, 35, 180, 360, 10, "correta")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_o():
    m=0
    for ponto in pontos_letra_o:
        m+=1
        if(m==3):
            semi_circulo(50, 50, 270, 630, 50, "correta")
        if(m==5):
            semi_circulo(50, 50, 270, 630, 20, "correta")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_p():
    m=0
    for ponto in pontos_letra_p:
        m+=1
        if(m==4):
            semi_circulo(30, 70, 270, 90, 30, "inversa")
        if(m==11):
            semi_circulo(25, 70, 90, 270, 15, "inversa")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_q():
    m=0
    for ponto in pontos_letra_q:
        m+=1
        if(m==3):
            semi_circulo(50, 50, 270, 630, 50, "correta")
        if(m==5):
            semi_circulo(50, 50, 270, 630, 30, "correta")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_r():
    m=0
    for ponto in pontos_letra_r:
        m+=1
        if(m==7):
            semi_circulo(40, 75, 90, 270, 25, "inversa")
        if(m==13):
            semi_circulo(35, 75, 90, 270, 15, "inversa")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_s():
    m=0
    for ponto in pontos_letra_s:
        m+=1
        if(m==4):
            semi_circulo(75, 30, 90, 270, 30, "inversa")
            semi_circulo(75, 70, 270, 90, 10, "correta")
        if(m==6):
            semi_circulo(75, 70, 90, 270, 30, "correta")
            semi_circulo(75, 30, 270, 90, 10, "inversa")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

def desenha_u():
    m=0
    for ponto in pontos_letra_u:
        m+=1
        if(m==4):
            semi_circulo(50, 25, 360, 180, 35, "correta")
        if(m==6):
            semi_circulo(50, 25, 180, 360, 15, "correta")
        x, y, z = ponto
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
         #Move to the new target:
        robot.MoveJ(target_pose)

        
def proxima_letra():
    x = xyz_ref[0] 
    y = xyz_ref[1] 
    z = xyz_ref[2] +50
    target_pose.setPos([x,y,z])
    robot.MoveL(target_pose)
    x = xyz_ref[0] +110
    y = xyz_ref[1] 
    z = xyz_ref[2] +50
    target_pose.setPos([x,y,z])
    robot.MoveL(target_pose)
    xyz_ref[0] += 110


def desenhar_letra(letra):
    for ponto in letra:
        # Polygon radius
        x, y, z = ponto
        # Calculate the new position:
        x = xyz_ref[0] + x # new X coordinate
        y = xyz_ref[1] + y # new Y coordinate
        z = xyz_ref[2] + z # new Z coordinate
        target_pose.setPos([x,y,z])
        # Move to the new target:
        robot.MoveL(target_pose)



a = [
    [100, 0, 0],
    [75, 100, 0],
    [25, 100, 0],
    [0, 0, 0],
    [20, 0, 0],
    [32.5 ,45, 0],
    [67.5, 45, 0],
    [80, 0, 0],
    [100, 0, 0],
    [100, 0, 50],
    [33.75, 55, 50],
    [33.75, 55, 0],
    [42.5, 90, 0],
    [57.5, 90, 0],
    [66.25, 55, 0],
    [33.75, 55, 0],
    
    
]

pontos_letra_b = [
    [0, 0, 0],
    [50, 0, 0],
    [50, 60, 0],
    [50, 100, 0],
    [0, 100, 0],
    [0, 0, 0],
    [0, 0, 50],
    [25, 15, 50],
    [25, 15, 0],
    [50, 15, 0],
    [50, 50, 0],
    [25, 50, 0],
    [25, 15, 0],
    [25, 15, 50],
    [25, 70, 50],
    [25, 70, 0],
    [50, 70, 0],
    [50, 90,0],
    [25, 90,0],
    [25, 70,0],
]

pontos_letra_c = [
    [50, 0, 50],
    [50, 0, 0],
    [100, 0, 0],
    [100, 25, 0],
    [50, 25, 0],
    [50, 75, 0],
    [100, 75, 0],
    [100, 100, 0],
    [50, 100, 0],
    [50 , 0, 0]
]

pontos_letra_d = [
    [0, 0, 0],
    [50,0, 0],
    [50,100, 0],
    [0, 100, 0],
    [0,0,0],
    [0, 0, 50],
    [25,25,50],
    [25,25,0],
    [50, 25, 0],
    [50, 75, 0],
    [25, 75,0],
    [25, 25,0] 
]

e = [
    [0, 0, 0],
    [100, 0, 0],
    [100, 20, 0],
    [20, 20, 0],
    [20, 40, 0],
    [80, 40, 0],
    [80, 60, 0],
    [20, 60, 0],
    [20, 80, 0],
    [100, 80, 0],
    [100, 100, 0],
    [0, 100, 0],
    [0, 0, 0]
]

f = [
    [0, 0, 0],
    [20, 0, 0],
    [20, 40, 0],
    [80, 40, 0],
    [80, 60, 0],
    [20, 60, 0],
    [20, 80, 0],
    [100, 80, 0],
    [100, 100, 0],
    [0, 100, 0],
    [0, 0, 0]
]

pontos_letra_g = [
    [0, 0, 50],
    [50, 0,50],
    [50, 0, 0],
    [82.15, 88.28, 0],
    [63.99, 70.71, 0],
    [75, 50, 0],
    [100, 50, 0],
    [50, 0, 0],
    [50, 0, 50],
    [50, 30, 50],
    [50, 30, 0],
    [50, 30, 0],
    [50, 50, 0],
    [100, 50, 0],
    [100, 0, 0],
    [80, 0, 0],
    [80, 30, 0],
    [50, 30, 0]
    
]

h = [
    [0, 0, 0],
    [30, 0, 0],
    [30, 40, 0],
    [70, 40, 0],
    [70, 0, 0],
    [100, 0, 0],
    [100, 100, 0],
    [70, 100, 0],
    [70, 60, 0],
    [30, 60, 0],
    [30, 100, 0],
    [0, 100, 0],
    [0, 0, 0]
]

i = [
    [0, 0, 0],
    [30, 0, 0],
    [30, 100, 0],
    [0, 100, 0],
    [0, 0, 0],
    [0, 0, 50],
    [0, 120, 50],
    [0, 120, 0],
    [30, 120, 0],
    [30, 140, 0],
    [0, 140, 0],
    [0, 120, 0],
    [0, 120, 50],
    [0, 0, 50],
    [0, 0, 0]
]
pontos_letra_j = [
    [60, 100, 50],
    [60, 100, 0],
    [90, 100, 0],
    [90, 40, 0],
    [10, 40, 0],
    [40, 40, 0],
    [40, 35, 0],
    [60, 35, 0],
    [60, 100, 0]
]

k = [
    [0, 0, 0],
    [25, 0, 0],
    [25, 30, 0],
    [60, 0, 0],
    [100, 0, 0],
    [35, 55, 0],
    [100, 100, 0],
    [60, 100, 0],
    [25, 80, 0],
    [25, 100, 0],
    [0, 100, 0],
    [0, 0, 0]
]

l = [
    [0, 0, 0],
    [100, 0, 0],
    [100, 20, 0],
    [25, 20, 0],
    [25, 100, 0],
    [0, 100, 0],
    [0, 0, 0]
]

m = [
    [0, 0, 0],
    [20, 0, 0],
    [20, 80, 0],
    [40, 0, 0],
    [60, 0, 0],
    [80, 80, 0],
    [80, 0, 0],
    [100, 0, 0],
    [100, 100, 0],
    [70, 100, 0],
    [50, 20, 0],
    [30, 100, 0],
    [0, 100, 0],
    [0, 0, 0]
]

n = [
    [0, 0, 0],
    [30, 0, 0],
    [30, 60, 0],
    [55, 0, 0],
    [100, 0, 0],
    [100, 100, 0],
    [70, 100, 0],
    [70, 35, 0],
    [40, 100, 0],
    [0, 100, 0],
    [0, 0, 0]
]
pontos_letra_o = [
    [50, 0, 50],
    [50, 0, 0],
    [50, 0, 50],
    [50, 30, 50],
    [50, 30, 0],
    [50, 30, 0],
    [50, 30, 50],
]

pontos_letra_p = [
    [0, 0, 0],
    [0, 100, 0],
    [30, 100, 0],
    [30, 40, 0],
    [30, 0, 0],
    [0, 0, 0],
    [0, 0, 50],
    [15, 55, 50],
    [15, 55, 0],
    [25, 55, 0],
    [25, 85, 0],
    [15, 85, 0],
    [15, 55, 0]
]

pontos_letra_q = [
    [50, 0, 50],
    [50, 0, 0],
    [50, 0, 50],
    [50, 20, 50],
    [50, 20, 0],
    [50, 20, 0],
    [50, 20, 50],
    [60, 35, 50],
    [60, 35, 0],
    [70, 55, 0],
    [95, 15, 0],
    [85, -5, 0],
    [60, 35, 0],
]

pontos_letra_r = [
    [0, 0, 0],
    [20, 0, 0],
    [20, 40, 0],
    [40, 0, 0],
    [60, 0, 0],
    [35, 50, 0],
    [30, 100, 0],
    [0, 100, 0],
    [0, 0, 0],
    [0, 0, 50],
    [20, 60, 50],
    [20, 60, 0],
    [20, 90, 0],
    [20, 60, 0]
]

pontos_letra_s = [
    [0, 0, 50],
    [45, 0, 50],
    [45, 0, 0],
    [100, 80, 0],
    [100, 100, 0],
    [45, 20, 0],
    [45, 0, 0]
]

t = [
    [35, 0, 50],
    [35, 0, 0],
    [65, 0, 0],
    [60, 70, 0],
    [100, 70, 0],
    [100, 100, 0],
    [0, 100, 0],
    [0, 70, 0],
    [35, 70, 0],
    [35, 0, 0]
]

pontos_letra_u = [
    [0, 0, 50],
    [85, 25, 50],
    [85, 25, 0],
    [15, 100, 0],
    [35, 100, 0],
    [65, 100, 0],
    [85, 100, 0],
    [85, 25, 0]
]

v = [
    [35, 0, 50],
    [35, 0, 0],
    [65, 0, 0],
    [100, 100, 0],
    [70, 100, 0],
    [50, 30, 0],
    [30, 100, 0],
    [0, 100, 0],
    [35, 0, 0],
]

w = [
    [10, 0, 50],
    [10, 0, 0],
    [40, 0, 0],
    [50, 70, 0],
    [60, 0, 0],
    [90, 0, 0],
    [100, 100, 0],
    [80, 100, 0],
    [75, 30, 0],
    [65, 95, 0],
    [35, 95, 0],
    [25, 30, 0],
    [20, 100, 0],
    [0, 100 ,0],
    [10, 0, 0]
]

x = [
    [0, 0, 0],
    [30, 0, 0],
    [50, 30, 0],
    [70, 0, 0],
    [100, 0, 0],
    [70, 50, 0],
    [100, 100, 0],
    [70, 100, 0],
    [50, 70, 0],
    [30, 100, 0],
    [0, 100, 0],
    [30, 50, 0],
    [0, 0, 0]
    
]

y = [
    [42.5, 0, 50],
    [42.5, 0, 0],
    [65, 0, 0],
    [100, 100, 0],
    [80, 100, 0],
    [65, 60, 0],
    [50, 100, 0],
    [30, 100, 0],
    [55, 33.33, 0],
    [42.5, 0, 0]
]

z = [
    [0, 0, 0],
    [100, 0, 0],
    [100, 30, 0],
    [40, 30, 0],
    [100, 70, 0],
    [100, 100, 0],
    [0, 100, 0],
    [0, 70, 0],
    [60, 70, 0],
    [0, 30, 0],
    [0, 0, 0]
]
    



palavra=InputDialog("digita", "")
while(len(palavra)>9 or len(palavra)==0):
    palavra=InputDialog("digite uma palavra com 9 letras ou menos", "")

switch = {
    'a': a,
    'b': desenha_b,
    'c': desenha_c,
    'd': desenha_d,
    'e': e,
    'f': f,
    'g': desenha_g,
    'h': h,
    'i': i,
    'j': desenha_j,
    'k': k,
    'l': l,
    'm': m,
    'n': n,
    'o': desenha_o,
    'p': desenha_p,
    'q': desenha_q,
    'r': desenha_r,
    's': desenha_s,
    't': t,
    'u': desenha_u,
    'v': v,
    'w': w,
    'x': x,
    'y': y,
    'z': z,
}

for caracter in palavra:
    if(    caracter == 'a'
        or caracter == 'e'
        or caracter == 'f'
        or caracter == 'h'
        or caracter == 'i'
        or caracter == 'k'
        or caracter == 'l'
        or caracter == 'm'
        or caracter == 'n'
        or caracter == 't'
        or caracter == 'v'
        or caracter == 'w'
        or caracter == 'x'
        or caracter == 'y'
        or caracter == 'z'
        ):
        desenhar_letra(switch.get(caracter))
    else:
        if(caracter == ' '):
            t1=0 
        else:
            switch.get(caracter)()
    proxima_letra()
 
# Trigger a program call at the end of the movement
robot.RunInstruction('Program_Done')


# Move back to the reference target:
robot.MoveL(target)
robot.MoveJ(home)
