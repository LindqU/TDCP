"""abc277_a"""
from sys import stdin


def main():
    N, X = map(int, stdin.readline().split())
    P_line = list(map(int, stdin.readline().split()))

    for idx, p in enumerate(P_line):
        if X == p:
            return idx + 1


if __name__ == "__main__":
    res = main()
    print(res)
