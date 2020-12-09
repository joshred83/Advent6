
def process_group(g):
  
  yesses = len(group[0].intersection(*group[:]))
  return yesses

with open("customs_declaration_forms") as f:
  group = []
  ttl = 0
  for line in f:
    if line == '\n':
      ttl += process_group(group)
      group = []
    else:
      group.append(set(line.strip()))
      
  ttl += process_group(group)
  print(ttl)
      

    