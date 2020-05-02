class Difference:
    maximumDifference = None

    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maxdiff = []
        for i in range(len(self.__elements)):
            for j in range(i, len(self.__elements)):
                maxdiff.append(abs(self.__elements[i] - self.__elements[j]))

        Difference.maximumDifference = max(maxdiff)
    # maximumDifference = computeDifference()
    # Add your code here


# End of Difference class

# _ = input()
# a = [int(e) for e in input().split(' ')]
a = [1, 2, 5]

d = Difference(a)
d.computeDifference()

# print(d.maximumDifference)
print(d.maximumDifference)
