
# Social Media Friendship Network

users = ["Aarav", "Diya", "Rohan", "Sara"]
n = len(users)

# Create adjacency matrix
matrix = [[0] * n for _ in range(n)]

# Add friendships
friendships = [
    ("Aarav", "Diya"),
    ("Aarav", "Rohan"),
    ("Diya", "Sara"),
    ("Rohan", "Sara")
]

for u1, u2 in friendships:
    i = users.index(u1)
    j = users.index(u2)

    matrix[i][j] = 1
    matrix[j][i] = 1

# Display matrix
print("Friendship Adjacency Matrix")
print("     ", users)

for i in range(n):
    print(users[i], matrix[i])

# Check friendship
u1 = "Aarav"
u2 = "Diya"

i = users.index(u1)
j = users.index(u2)

if matrix[i][j] == 1:
    print(u1, "and", u2, "are friends")
else:
    print(u1, "and", u2, "are not friends")

# Count friends
print("\nNumber of Friends:")
for i in range(n):
    print(users[i], ":", sum(matrix[i]))
