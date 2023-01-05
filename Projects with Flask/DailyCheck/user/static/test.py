seq = {'id': '101', 'name': 'Adam', 'department': 'IT'}

print(sorted(seq.items(), key=lambda x: (x[1])))

