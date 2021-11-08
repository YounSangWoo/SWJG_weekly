def solve(a: list) -> int:
    sum = 0
    for i in a:
        sum += i
    return sum
if __name__ == "__main__":
    print(solve([1, 2, 3, 4, 5]))
