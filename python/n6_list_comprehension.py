numbers = [1, 2, 3, 4, 5, 6]
doubled = [num * 2 for num in numbers]
print(doubled)

friends = ["Rolf", "Anne", "Ravi", "Ali"]

filteredFriends = [friend for friend in friends if (friend.startswith("A"))]

print(filteredFriends)

# ids or memory address
print(id(friends))
print(id(filteredFriends))
