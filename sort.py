#
# Sort dictionary by value and then key
#
count = {
    "i": 1,
    "love": 2,
    "coding": 3
}
# Ascending sort based on key
count = {v[0]: v[1] for v in sorted(count.items(), key=lambda x:(x[1], x[0]))}

# Descending sort based on value
count = {v[0]: v[1] for v in sorted(count.items(), key=lambda x:(-x[1], x[0]))}

#
# Sort list using value from dictionary
#
count = {
    "i": 1,
    "love": 2,
    "coding": 3
}
keys = list(count.keys())

# Sort the array based on the dictionary value above
keys.sort(key=lambda x:(count[x], x))

# Descending order
keys.sort(key=lambda x:(-count[x], x))
