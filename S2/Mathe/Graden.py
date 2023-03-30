
#TODO
# - ist_identisch von yannick fixen lassen
# - hat_Schnittpunkt schreiben lassen von chatgpt

class Vec():
    def __init__(self, x: float, y: float, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

class Gerade():
    def __init__(self, stützvec: Vec, richtungvec:Vec) -> None:
        self.stützvec = stützvec
        self.richtungvec = richtungvec
    

def ist_parallel(g1: Gerade, g2: Gerade) -> bool:
    
    if g1.richtungvec.x == 0 or g2.richtungvec.x == 0:
        if g1.richtungvec.y == 0 or g2.richtungvec.y == 0:
            mult = g1.richtungvec.z / g2.richtungvec.z
        else:
            mult = g1.richtungvec.y / g2.richtungvec.y
    else:
        mult = g1.richtungvec.x / g2.richtungvec.x
    
    return g1.richtungvec.y == g2.richtungvec.y * mult and g1.richtungvec.z == g2.richtungvec.z * mult

def ist_identisch(g1: Gerade, g2: Gerade) -> bool:
    if not ist_parallel(g1, g2):
        return False
    
    r = 17
    
    # check if g1.stützvec + r * g1.richtungvec == g2.stützvec + r * g2.richtungvec
    
    p1 = (g1.stützvec.x + r * g1.richtungvec.x, g1.stützvec.y + r * g1.richtungvec.y, g1.stützvec.z + r * g1.richtungvec.z)
    
    mult = g1.richtungvec.x / g2.richtungvec.x
    
    p2 = (g2.stützvec.x + r * g2.richtungvec.x * mult, g2.stützvec.y + r * g2.richtungvec.y * mult, g2.stützvec.z + r * g2.richtungvec.z * mult)
    
    print(p1, p2)
    
    return p1 == p2
    
def hat_Schnittpunkt(g1: Gerade, g2: Gerade) -> bool:
    """Berechnet ob sich zwei Geraden schneiden"""
    if ist_identisch(g1, g2):
        return True
    if ist_parallel(g1, g2):
        return False if not ist_identisch(g1, g2) else True
    
    pass

def ist_windschief(g1: Gerade, g2: Gerade) -> bool:
    """Berechnet ob zwei Geraden Windschief sind"""
    
    return False if hat_Schnittpunkt(g1, g2) and not ist_parallel(g1, g2) else True



g1 = Gerade(Vec(0, 0, 0), Vec(-1, -1, 0))

g2 = Gerade(Vec(0, 0, 0), Vec(0, 0, 1))

print("parallel", ist_parallel(g1, g2))
print("identisch", ist_identisch(g1, g2))
print("schnittpunkt", hat_Schnittpunkt(g1, g2))
print("windschief", ist_windschief(g1, g2))