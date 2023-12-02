
input = open("1/input.txt", "r")


def one():
   sum = 0
   for ln in input:
      val = ""
      n = len(ln)
      for i in range(n):
         if ln[i].isdigit():
            val += str(ln[i])
            break
      for i in range(n):
         if ln[n - i - 1].isdigit():
            val += str(ln[n - i - 1])
            break
      sum += int(val)
   print(sum)
   return sum

# 53194 ✔

numStr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def two():
   sum = 0
   for s in input:
      s = str(s.encode()).split('b\'')[1].split('\\n')[0]
      n = len(s)
      start = 0
      end = int(n - 1)
      while (not(s[start].isdigit())): start += 1
      while (not(s[end].isdigit())): end -= 1
      startVal = s[start]
      endVal = s[end]
      for num in range(len(numStr)):
         if numStr[num] not in s: continue
         lFind = s.find(numStr[num])
         if lFind < start: 
            start = lFind
            startVal = num
         rFind = s.rfind(numStr[num]) + len(numStr[num]) - 1
         if rFind > end: 
            end = rFind
            endVal = num
      # print(s, " | ", "idx", str(start) + str(end), " | ", "val", str(startVal) + str(endVal))
      val = int("{0}{1}".format(startVal, endVal))
      sum += val
   print("sum " + str(sum))
   return sum


# one()
two()

# 54249 ✔