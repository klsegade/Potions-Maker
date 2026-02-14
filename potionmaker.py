'''Component Classes'''
class Base:
    def __init__(self, name, modifiers, traits=None):
        self.name = name
        self.modifiers = modifiers
        self.traits = traits or []

class Stabilizer:
    def __init__(self, name, modifiers, traits=None):
        self.name = name
        self.modifiers = modifiers
        self.traits = traits or []

class Booster:
    def __init__(self, name, modifiers, traits=None):
        self.name = name
        self.modifiers = modifiers
        self.traits = traits or []

class Finisher:
    def __init__(self, name, modifiers, traits=None):
        self.name = name
        self.modifiers = modifiers
        self.traits = traits or []


'''Data Library'''
components = {
    "water" : {
        "category": "base",
        "traits": [],
        "modifiers": {"stability":20, 'potency': 10}
    },
    "oil" : {
        "category": "base",
        "traits": [],
        "modifiers": {"stability":15, 'potency': 15}
    },
    "alcohol" : {
        "category": "base",
        "traits": [],
        "modifiers": {"stability":10, 'potency': 20}
    },
    "acid" : {
        "category": "base",
        "traits": [],
        "modifiers": {"stability":10, 'potency': 20}
    },
    "preservative" : {
        "category": "stabilizer",
        "traits": [],
        "modifiers": {"stability":10, 'potency': 20}
    },
    "binder" : {
        "category": "stabilizer",
        "traits": [],
        "modifiers": {"stability":10, 'potency': 10}
    },
    "alkaline buffer" : {
        "category": "stabilizer",
        "traits": [],
        "modifiers": {"stability":10, 'potency': 10}
    },
    "caustic" : {
        "category": "booster",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "oxidizer" : {
        "category": "booster",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "combustive" : {
        "category": "booster",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "metallic reactive" : {
        "category": "booster",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "organic stimulant" : {
        "category": "booster",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "ferment catalyst" : {
        "category": "booster",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "aromatic" : {
        "category": "finisher",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "pigment" : {
        "category": "finisher",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "prestige" : {
        "category": "finisher",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "sweetener" : {
        "category": "finisher",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "absorbent" : {
        "category": "finisher",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "mineral reactive" : {
        "category": "finisher",
        "traits": [],
        "modifiers": {"stability":10}
    },
    "essence" : {
        "category": "finisher",
        "traits": [],
        "modifiers": {"stability":10}
    },
}

modifiers = {
    stability, volatility, shelf-life, potency, duration, intensity, absortion, diffusion, 
    penetration, toxicity, corruption, purity, clarity, aroma, resonance, viscosity, reactivity
}

traits = {
    aqueous, oleaginous, volatile, acidic, alkaline, mineral, organic, metallic, carbonaceous, 
    combustive, stimulant, soothing, heating, cooling, drying, moistening, restorative, toxic, 
    luminous, shadowed, transmutative, fermentative, preservative, binding, catalytic
}