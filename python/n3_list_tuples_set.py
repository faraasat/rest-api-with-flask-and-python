# order will remaing same, tuples cannot be modified
l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")

# can't have duplicates, order can be changed
s = {"Bob", "Rolf", "Anne"}


l.append("Smith")
l.remove("Bob")
print(l[0])

print(t[1])

s.add("Julie")
# print(s[0])

print(l, t, s)

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local_friends_1 = friends.difference(abroad)
local_friends_2 = abroad.difference(friends)
print(local_friends_1)
print(local_friends_2)
