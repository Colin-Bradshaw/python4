bookshop = [[34597, 'Learning Python, Mark Lutz', 4, 40.95],
            [98762, 'Programming Python, Mark Lutz', 5, 56.80],
            [77226, 'Head First Python, Paul Barry', 3, 32.95],
            [88112, 'Einführung in Python3, Bernd Klein', 3, 24.99]]

bookshop2 = [[34597, (1, 4, 40.95)],
            [98762, (2, 5, 56.80)],
            [77226, (3, 3, 32.95)],
            [88112, (4, 3, 24.99)]]

lam = lambda lst: ((lst[1], lst[3], lst[2]), (lst[1], lst[3] + 10, lst[2])) [lst[2] * lst[3] < 100]

lam2 = lambda lst: [(lst[0], lst[1][1] * lst[1][2])]

print(list(map(lam, bookshop)))
print(list(map(lam2, bookshop2)))
