import math
with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_11.txt', 'r') as f:
    inp = f.read()

monkeys = {}
for i in inp.split('\n\n'):
    monkey = i.split('\n')[0][:-1]
    starting_items = [int(f) for f in i.split('\n')[1].split(': ')[1].split(',')]
    operation = i.split('\n')[2].split(': ')[1].split('= ')[1]
    test = int(i.split('\n')[3].split('by')[1])
    true = i.split('\n')[4].split('to ')[1]
    false = i.split('\n')[5].split('to ')[1]
    times_of_inspections = 0
    monkeys[monkey] = {'starting_items': starting_items, 'operation': operation, 'test': test,
                       'true': true, 'false': false, 'times of inspections': times_of_inspections}

for t in range(20):
    for num in range(0, 8):
        m = monkeys['Monkey ' + str(num)]
        if m['starting_items'] == []:
            pass
        else:
            for item in m['starting_items']:
                old = item
                new_item = math.floor(eval(m['operation'])/3)
                if new_item % m['test'] == 0:
                    monkeys['Monkey ' + str(m['true'][-1])]['starting_items'].append(new_item)
                else:
                    monkeys['Monkey ' + str(m['false'][-1])]['starting_items'].append(new_item)
            m['times of inspections'] += len(m['starting_items'])
            m['starting_items'] = []

insp_times = []
for monkey in monkeys:
    insp_times.append(monkeys[monkey]['times of inspections'])

print(sorted(insp_times)[-1]*sorted(insp_times)[-2])