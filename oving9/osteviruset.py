
cheeses = {
    'cheddar':
    ('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
    'mozarella':
    ('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
    'gombost':
    ('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
    'geitost':
    ('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
    'port salut':
    ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
    'camembert':
    ('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
    'ridder':
    ('GOMBOS-4', 'B16-3'),
}

print("a)")

print("Du finner osten port salut på hylleplass: ", cheeses["port salut"])
print("Du finner osten cheddar på hylleplass: ", cheeses["cheddar"])

print("\nb)")

infected_cheeses = []
infected_shelves = ('A234', 'A235', 'B13', 'B14', 'B15', 'C31')

for cheese, shelves in cheeses.items():
    for shelf in shelves:
        prefix = shelf.split('-')[0]
        if prefix in infected_shelves and cheese not in infected_cheeses:
            infected_cheeses.append(cheese)


print("Potentially infected cheeses:", infected_cheeses)

print("\nc)")

healthy_cheeses = []

for cheese in cheeses:
    if cheese not in infected_cheeses:
        healthy_cheeses.append(cheese)

print("Healthy cheeses:", healthy_cheeses)

for cheese, shelves in cheeses.items():
    if cheese in healthy_cheeses:
        for shelf in shelves:
            print(shelf.ljust(10), cheese.rjust(10))

