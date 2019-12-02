#part 2.1
#start = (lambda l: l[:1] + [12, 2] + l[3:])([int(x) for x in open("input.txt").readline().split(',')])
#add p i = p[:p[i+3]] + [p[p[i+1]]+p[p[i+2]]] + p[:p[i+3]+1]
#mul p i = p[:p[i+3]] + [p[p[i+1]]*p[p[i+2]]] + p[:p[i+3]+1]
#halt p = p[0]
#action p i = 
    #(p[i] == 1 and (action (add p i) i+4)) or
    #(p[i] == 2 and (action (mul p i) i+4)) or
    #(p[i] == 99 and halt p)

print((lambda a: lambda v,i: a(a,v,i))(lambda rec,p,i: (p[i] == 1 and rec(rec, p[:p[i+3]] + [p[p[i+1]]+p[p[i+2]]] + p[p[i+3]+1:], i + 4)) or (p[i] == 2 and rec(rec,p[:p[i+3]] + [p[p[i+1]]*p[p[i+2]]] + p[p[i+3]+1:], i+4)) or (p[i] == 99 and p[0]))((lambda l: l[:1] + [12, 2] + l[3:])([int(x) for x in open("input.txt").readline().split(',')]),0))

#part 2.2
# [noun * 100 + verb for noun in [0,99] for verb in [0,99] if #part1(noun, verb) == 19690720][0]
print([noun * 100 + verb for noun in range(100) for verb in range(100) if (lambda noun, verb: (lambda a: lambda v,i: a(a,v,i))(lambda rec,p,i: (p[i] == 1 and rec(rec, p[:p[i+3]] + [p[p[i+1]]+p[p[i+2]]] + p[p[i+3]+1:], i + 4)) or (p[i] == 2 and rec(rec,p[:p[i+3]] + [p[p[i+1]]*p[p[i+2]]] + p[p[i+3]+1:], i+4)) or (p[i] == 99 and p[0]))((lambda l: l[:1] + [noun, verb] + l[3:])([int(x) for x in open("input.txt").readline().split(',')]),0))(noun, verb) == 19690720][0])
