pythons = ["ali", "hamid", "zahra", "farzad"]
icdls = ["ali", "pedram", "tara", "mina", "zahra"]
common = [i for i in icdls if i in pythons]
print(common)
