
input = open('2023/3/input.txt', 'r').read()

isSymbol = lambda c: not str(c).isdigit() and not c == "."


def one():
   schematic = str(input.encode()).removeprefix('b\'').removesuffix('\'').split('\\n')
   sum = 0

   for i in range(len(schematic)):
      j = 0
      lenOfRow = len(schematic[i])
      while j < lenOfRow:
         if not str(schematic[i][j]).isdigit():
            j += 1
            continue
         startOfNumber = j
         while j < lenOfRow and str(schematic[i][j]).isdigit(): j += 1
         endOfNumber = j
         number = schematic[i][startOfNumber:endOfNumber]
         numberIsValid = False
         for row in range(i - 1, i + 2):
            if numberIsValid: break
            if row < 0 or row >= len(schematic): continue
            for col in range(startOfNumber - 1, endOfNumber + 1):
               if col >= lenOfRow: break
               if isSymbol(schematic[row][col]): # shouldn't be checking indexes that belong to the number!
                  sum += int(number)
                  numberIsValid = True
                  break
         j += 1
   print(sum)
   return sum

# one()
# 531561 ✔

def two():
   schematic = str(input.encode()).removeprefix('b\'').removesuffix('\'').split('\\n')
   extractNumber = lambda s, startIdx, endIdx: extractNumber(s, startIdx, endIdx + 1) if endIdx < len(s) and str(s[endIdx]).isdigit() else [s[startIdx:endIdx], endIdx]
   sum = 0
   asteriskIndexes = {}
   endIndexAndNums = {}

   for row in range(len(schematic)):
      col = 0
      while col < len(schematic[row]):
         if schematic[row][col] == "*":
            if asteriskIndexes.get(row) == None:
               asteriskIndexes.setdefault(row, [])
            asteriskIndexes[row].append(col)
         elif str(schematic[row][col]).isdigit():
            [num,col] = extractNumber(schematic[row], col, col + 1)
            if endIndexAndNums.get(row) == None:
               endIndexAndNums.setdefault(row, [])
            endIndexAndNums[row].append((col, num))
            continue
         col += 1

   for row in asteriskIndexes:
      for col in asteriskIndexes[row]:
         upper = [t[1] for t in endIndexAndNums[row - 1] if col in range(int(t[0] - len(t[1]) - 1), int(t[0] + 1))]
         lower = [t[1] for t in endIndexAndNums[row + 1] if col in range(int(t[0] - len(t[1]) - 1), int(t[0] + 1))]
         same = [t[1] for t in endIndexAndNums[row] if t[0] == col or t[0] - len(t[1]) == col + 1]
         list = upper + lower + same
         if len(list) == 2: sum += int(list[0]) * int(list[1])
   print(sum)
   return sum

two()
# 83279367 ✔