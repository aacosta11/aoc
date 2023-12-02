
input = open("2023/2/input.txt", "r")

# Find the sum of all games that satisfy the given limits:
# A game has at most 12 red cubes, 13 green cubes, and 14 blue cubes
# What is the sum of the IDs of those games?

limits = {
   'red': 12,
   'green': 13,
   'blue': 14
}

def hasValidSets(sets):
   for set in sets:
      cubes = set.split(",")
      for cube in cubes:
         i = 0
         while cube[i].isdigit(): i += 1
         color = cube[i:]
         val = int(cube[:i])
         if val > limits[color]:
            return False
   return True


def one():
   sum = 0
   for game in input:
      game = str(game.encode()).removeprefix('b\'').removesuffix('\\n\'').replace(" ", "")
      [id, sets] = game.split("Game")[1].split(":")
      sets = sets.split(";")
      # print(id, sets)
      if hasValidSets(sets): sum += int(id)
   print(sum)
   return sum

# one()
# 2447 ✔


# For each game, find the fewest number of cubes needed for each color.
# What is the sum of the power of these sets? ( the minimum #'s needed for each game )
# power = numbers of red, green, and blue cubes multiplied together

def two():
   getFirstAlphaCharIdx = lambda s, i: getFirstAlphaCharIdx(s,i + 1) if s[i].isdigit() else i
   sum = 0
   for game in input:
      game = str(game.encode()).removeprefix('b\'').removesuffix('\\n\'').split(":")[1].replace(" ", "").replace(";", ",").split(",")
      leastNeeded = { "blue": 0, "green": 0, "red": 0 }
      for cube in game:
         i = getFirstAlphaCharIdx(cube, 0)
         color = cube[i:]
         val = int(cube[:i])
         leastNeeded[color] = max(val, leastNeeded[color])

      power = leastNeeded["blue"] * leastNeeded["green"] * leastNeeded["red"]
      sum += power

   print(sum)
   return sum

two()
# 56322 ✔