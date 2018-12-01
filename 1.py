import sys

sum=reduce(lambda a, b: int(a) + int(b), sys.stdin.readlines())
print(sum)