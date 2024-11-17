grades = {
    "English": 97,
    "Math": 93,
    "Global Studies": 85,
    "Art": 74,
    "Music": 86
}
print(grades["Global Studies"]) # print value of key

grades["Global Studies"] = 87 # assign new value to existing key
grades["Gym"] = 100 # assign value to new key

print(grades["Math"]) # print value of key
print(grades["Global Studies"]) # print value of key

print(grades)