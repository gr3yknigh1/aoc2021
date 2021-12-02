import os



BASE_PATH =  os.path.dirname(__file__) 
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")

with open(INPUT_PATH, mode='r') as f:
    buffer = f.read()


class Submarine:

    def __init__(self, horizontal_position=0, depth=0):
        self.horizontal_position = horizontal_position
        self.depth = depth
    
    def exec(self, cmd, amount):
        match cmd:
            case "forward":
                self.horizontal_position += amount
            case "up":
                self.depth -= amount
            case "down":
                self.depth += amount
            case _:
                raise NotImplemented


s = Submarine()

lines = buffer.splitlines()
for line in lines:
    cmd, amount = line.split(" ")
    amount = int(amount)
    s.exec(cmd, amount)

print(s.horizontal_position * s.depth)
