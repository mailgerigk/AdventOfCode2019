#part 1
print(sum([int(x) // 3 - 2 for x in open("input.txt").readlines()]))

#part 2
print(sum([(lambda a: lambda v:a(a,v))(lambda rec,x: 0 if x // 3 - 2 <= 0 else x // 3 - 2 + rec(rec, x // 3 - 2))(int(x)) for x in open("input.txt").readlines()]))