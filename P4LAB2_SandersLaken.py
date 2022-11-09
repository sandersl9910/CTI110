user1 = int(input())
user2 = int(input())

if user1 <= user2:
    for i in range(user1, user2 + 1, 5):
        print(i, end=' ')
    print()
else:
    print("Second integer can't be less than the first.")