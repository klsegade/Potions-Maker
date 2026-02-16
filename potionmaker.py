import random

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


'''Seed Input'''
def traits_from_serial(serial, plant_type):
    rng = random.Random(serial)  # deterministic seed

    possible_traits = PLANT_TRAIT_POOLS[plant_type]

    return rng.sample(possible_traits, k=2)

'''Data Library'''
alchemicalOutputs = {
    'potion', 'tonic', 'elixir', 'tincture', 'extract', 'infusion', 'salve', 'pills', 'powder', 'vaporous'
}

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
        "traits": ['volatile', 'preservative'],
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
    aqueous, metallic, carbonaceous, combustive, heating, cooling, restorative, 
    luminous, shadowed, transmutative, preservative, catalytic
}
mineralTraits = {
    "salts": ['preservative', 'absorbent', 'crystalline', 'conductive'],
    "alkaline": ['alkaline','crystalline'],
    "oxidizers": ['volatile', 'flammable', 'crystalline', 'conductive'],
    "reactive metals": ['metallic', 'volatile', 'toxic', 'crystalline', 'conductive'],
    "pigments": ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black', 'brown', 'staining', 'light-sensitive']
}

plantTraits = {
    "medicinal": ['soothing', 'cleansing', 'protection', 'restorative', 'stimulant', 'binding', 'numbing'],
    "nutritional": ['caloric', 'stimulant', 'fortifying', 'hydrating', 'restorative', 'acidic', 'alkaline', 'sweet', 'absorbent', 'spicy'],
    "toxic": ['poisonous', 'paralytic', 'acidic', 'necrotic', 'hallucinogenic', 'volatile', 'irritant', 'numbing'],
    "fermentable": ['sweet', 'starchy', 'acidic'],
    "psychoactives": ['hallucinogenic', 'sedative', 'stimulant', 'euphoric', 'dissociative'],
    "aromatics": ['aromatic', 'soothing', 'stimulant', 'preservative', 'repellant'],
    "pigments": ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black', 'brown', 'staining', 'light-sensitive'],
    "industrial" : ['resinous', 'oily', 'fibrous', 'binding', 'flammable', 'alkaline', 'absorbent']
}

animalTraits = {
    "lipids": ['binding', 'oily', 'waxy', 'protection', 'storing'],
    "binders": ['binding'],
    "skeletal": ['alkaline', 'mineral', 'protection', 'fortifying'],
    "venoms": ['paralytic', 'toxic']
}

fungalTraits = {
    "fungi": ['fermentative', 'hallucinogenic', 'sedative', 'stimulant', 'euphoric', 'dissociative']
}

processedTraits = {
    "distillates": ['volatile', 'concentrated', 'cleansing', 'acidic', 'aromatic'],
    "combustibles": ['alkaline', 'carbonaceous'],
    "refined": ['preservative']
}

qualitiesOfCreation = {
    Life, Elemental, Infusion, Mystic, Illusionary, Binding, Echo
}
