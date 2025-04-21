input_packets = ["S Mary", "P Dee", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee", "E Vicky", "E George",
                 "P Dee", "P Joe", "E Sally", "P Joe", "S Pete", "P Dee", "S Bill", "S Chase", "E Price", "P Dee",
                 "E Sue"]
pq = []
sq = []
eq = []
for i in input_packets:
    match i[0]:
        case "P":
            pq.append(i)
        case "S":
            sq.append(i)
        case "E":
            eq.append(i)
        case _:
            print("There is a problem in the sorter.")
            exit(-621)

while pq != [] or sq != [] or eq != []:
    if len(pq) > 2:
        for i in range(3):
            print(pq.pop())
    else:
        for i in pq:
            print(pq.pop())
    if len(sq) > 1:
        for i in range(2):
            print(sq.pop())
    else:
        for i in sq:
            print(sq.pop())
    if eq != []:
        print(eq.pop())
#ran on Python ver 3.10