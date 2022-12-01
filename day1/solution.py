class Solution():

    def __init__(self):
        with open("input.txt", "r") as f:
            self.input = f.readlines()

    def part1(self):
        elfs = []
        curr_cal = 0
        for line in self.input:
            line = line.strip()
            if line == "":
                elfs.append(curr_cal)
                curr_cal = 0
            else:
                curr_cal += int(line)

        if curr_cal != 0:
            elfs.append(curr_cal)
        
        return max(elfs)

    def part2(self):
        elfs = []
        curr_cal = 0
        for line in self.input:
            line = line.strip()
            if line == "":
                elfs.append(curr_cal)
                curr_cal = 0
            else:
                curr_cal += int(line)

        if curr_cal != 0:
            elfs.append(curr_cal)
        
        return sum(sorted(elfs, reverse=True)[0:3])


if __name__ == "__main__":
    sol = Solution()
    print(sol.part1())
    print(sol.part2())
