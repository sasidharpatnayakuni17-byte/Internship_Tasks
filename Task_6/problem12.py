# Problem: Set .discard(), .remove() & .pop()
# HackerRank: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        command = input().split()

        if command[0] == 'pop':
            if s:
                s.remove(min(s))
        elif command[0] == 'remove':
            s.remove(int(command[1]))
        elif command[0] == 'discard':
            s.discard(int(command[1]))

    print(sum(s))
