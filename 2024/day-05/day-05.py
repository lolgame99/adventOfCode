import random
def get_input(filename):
    rules = {}
    updates = []
    isRules = True
    with open(filename, 'r') as file:
        for line in file:
            if line == '\n':
                isRules = False
                continue
            if isRules:
                key, value = line.strip().split('|')
                if int(key) not in rules:
                    rules[int(key)] = [int(value)]
                else:
                    rules[int(key)] = [*rules[int(key)], int(value)]
            else:
                updates.append([int(x) for x in line.strip().split(",")])
    return rules, updates

def part1(rules,updates):
    sum = 0
    for update in updates:
        valid = True  
        for value in update:
            if value in rules.keys():
                if not all(update.index(value) < update.index(subset) for subset in set(rules[value]) & set(update)):
                    valid = False
                    break
        if valid:
            sum  += update[len(update)//2]
            #print("Valid Update: ",update)
            #print("Middle Element: ",update[len(update)//2])
            #print("Update: ",update)
            #print("Rules for page",value, ":",rules[value])
            #print("Subset: ",set(rules[value]) & set(update))
            
            #print("--------------------")
        
    print("Part 1 Solution: ",sum)

def part2(rules,updates):   
    def isValid(cur_update):
        valid = True  
        for value in cur_update:
            if value in rules.keys():
                if not all(update.index(value) < update.index(subset) for subset in set(rules[value]) & set(update)):
                    valid = False
                    break
        return valid
    
    def makeValid(cur_update):
        print("Not Valid: ",cur_update)
        for value in cur_update:
            if value in rules.keys():
                    for subset in set(rules[value]) & set(cur_update):
                        if cur_update.index(value) < cur_update.index(subset):
                            print("swapping: ",value, "and",subset)
                            new = cur_update.copy()
                            new[cur_update.index(value)] = subset
                            new[cur_update.index(subset)] = value
                            cur_update = makeValid(new)
        return cur_update
            

    
    sum = 0
    for update in updates:
        update_copy = update.copy()
        valid = isValid(update_copy)
        if not valid:
            update_copy = makeValid(update_copy)
            print("Changed: ",update_copy, "Original: ",update, "Valid: ",isValid(update_copy))
            valid = isValid(update_copy)
            if valid:
                sum  += update[len(update_copy)//2]
        
    print("Part 2 Solution: ",sum)



#print(get_input('test.txt'))
part1(*get_input('input.txt'))
part2(*get_input('test.txt'))