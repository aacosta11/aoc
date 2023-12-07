input = open('2023/4/input.txt', 'r').read()


def one():
   scratchCards = str(input.encode()).removeprefix('b\'').removesuffix('\'').split('\\n')
   sum = 0
   for row in scratchCards:
      if not row: continue
      row = row.split(':')[1].split('|')
      winning = row[0].split(None)
      numbers = row[1].split(None)
      matches = [num for num in numbers if num in winning]
      if matches: sum += 2 ** int(len(matches) - 1)

   print(sum)
   return sum

# one()
# 26426 ✔

def two():
   scratchCards = str(input.encode()).removeprefix('b\'').removesuffix('\'').split('\\n')
   sum = 0
   matches = [len([num for num in card[1] if num in card[0]]) for card in [[numbers.split(None) for numbers in card] for card in [row.split(':')[1].split('|') for row in scratchCards if row]]]
   nCopiesHash = list([1 for i in range(len(matches))])
   
   for i in range(len(matches)):
      for x in range(matches[i]):
         nCopiesHash[int(i + x + 1)] += nCopiesHash[i]
      sum += nCopiesHash[i]

   print(sum)
   
two()
# 6227972 ✔