import random

'''Component Classes'''
class Component:
    def __init__(self, name, traits, modifiers):
        self.name = name
        self.traits = traits
        self.modifiers = modifiers

'''Seed Input'''
def traits_from_serial(serial, plant_type):
    rng = random.Random(serial)  # deterministic seed

    possible_traits = PLANT_TRAIT_POOLS[plant_type]

    return rng.sample(possible_traits, k=2)

'''Data Library'''
alchemicalOutputs = {
    'potion', 'tonic', 'elixir', 'tincture', 'extract', 'infusion', 'salve', 'unguent', 'cream', 'pills', 'powder', 'vaporous'
}

components = {
    "water" : {
        "category": "base",
        "traits": ['hydrating'],
        "modifiers": {"stability":20, 'potency': 10}
    },
    "oil" : {
        "category": "base",
        "traits": ['oily'],
        "modifiers": {"stability":15, 'potency': 15}
    },
    "alcohol" : {
        "category": "base",
        "traits": ['volatile', 'preservative'],
        "modifiers": {"stability":10, 'potency': 20}
    },
    "acid" : {
        "category": "base",
        "traits": ['acidic'],
        "modifiers": {"stability":10, 'potency': 20}
    },
    "preservative" : {
        "category": "stabilizer",
        "traits": [],
        "modifiers": {"stability":10, 'potency': 20}
    },
    "binder" : {
        "category": "stabilizer",
        "traits": ['binding'],
        "modifiers": {"stability":10, 'potency': 10}
    },
    "alkaline buffer" : {
        "category": "stabilizer",
        "traits": ['mineral', 'alkaline'],
        "modifiers": {"stability":10, 'potency': 10}
    },
    "caustic" : {
        "category": "booster",
        "traits": ['mineral', 'alkaline'],
        "modifiers": {"stability":10}
    },
    "oxidizer" : {
        "category": "booster",
        "traits": ['flammable', 'crystalline'],
        "modifiers": {"stability":10}
    },
    "combustive" : {
        "category": "booster",
        "traits": ['volatile', 'flammable'],
        "modifiers": {"stability":10}
    },
    "metallic reactive" : {
        "category": "booster",
        "traits": ['volatile'],
        "modifiers": {"stability":10}
    },
    "organic stimulant" : {
        "category": "booster",
        "traits": ['spicy'],
        "modifiers": {"stability":10}
    },
    "ferment catalyst" : {
        "category": "booster",
        "traits": ['fermentative'],
        "modifiers": {"stability":10}
    },
    "aromatic" : {
        "category": "finisher",
        "traits": ['aromatic'],
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
        "traits": ['sweet'],
        "modifiers": {"stability":10}
    },
    "absorbent" : {
        "category": "finisher",
        "traits": ['absorbent'],
        "modifiers": {"stability":10}
    },
    "mineral reactive" : {
        "category": "finisher",
        "traits": ['volatile'],
        "modifiers": {"stability":10}
    },
    "essence" : {
        "category": "finisher",
        "traits": ['concentrated'],
        "modifiers": {"stability":10}
    },
}

modifiers = {
    stability, volatility, shelf-life, potency, duration, intensity, absortion, diffusion, 
    penetration, toxicity, corruption, purity, clarity, aroma, resonance, viscosity, reactivity
}

traits = {
    aqueous, metallic, carbonaceous, combustive, heating, cooling, restorative, 
    luminous, shadowed, transmutative, catalytic
}
mineralTraits = {
    "salts": ['preservative', 'absorbent', 'crystalline', 'conductive'],
    "alkaline": ['alkaline','crystalline'],
    "oxidizers": ['volatile', 'flammable', 'crystalline'],
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
