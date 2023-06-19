import random

#TODO
# - ist_identisch von yannick fixen lassen
# - GUI ? (kivy)


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
    
    print(p1,p2)
    
    return p1 == p2
    
    
    
def hat_Schnittpunkt(g1: Gerade, g2: Gerade) -> bool:
    """Berechnet ob sich zwei Geraden schneiden"""
    if ist_identisch(g1, g2):
        return True
    if ist_parallel(g1, g2):
        return False
    
    denominator = g1.richtungvec.x * g2.richtungvec.y - g1.richtungvec.y * g2.richtungvec.x
    
    if denominator == 0:
        return False
    
    # calculate the point of intersection
    # t is the parameter for g1, s is the parameter for g2
    # equations from https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    t = ((g2.stützvec.x - g1.stützvec.x) * g2.richtungvec.y - (g2.stützvec.y - g1.stützvec.y) * g2.richtungvec.x) / denominator
    s = ((g2.stützvec.x - g1.stützvec.x) * g1.richtungvec.y - (g2.stützvec.y - g1.stützvec.y) * g1.richtungvec.x) / denominator
    
    # check if the point lies on both lines
    p = Vec(g1.stützvec.x + t * g1.richtungvec.x, g1.stützvec.y + t * g1.richtungvec.y, g1.stützvec.z + t * g1.richtungvec.z)
    q = Vec(g2.stützvec.x + s * g2.richtungvec.x, g2.stützvec.y + s * g2.richtungvec.y, g2.stützvec.z + s * g2.richtungvec.z)
    
    return p == q

def ist_windschief(g1: Gerade, g2: Gerade) -> bool:
    """Berechnet ob zwei Geraden Windschief sind"""
    
    return False if ist_parallel(g1, g2) or ist_identisch(g1, g2) else True


def ascii_table(g1: Gerade, g2: Gerade) -> None:
    
    labels = ["Parallel", "Identisch", "Schnittpunkt", "Windschief"]
    values = [ist_parallel(g1, g2), ist_identisch(g1, g2), hat_Schnittpunkt(g1, g2), ist_windschief(g1, g2)]
    
    #print header
    
    print(f"{'Kategorie':<15} | {'Wert':<15}")
    
    print("-" * 30)
    
    for i in range(len(labels)):
        print(f"{labels[i]:<15} | {values[i]}")


