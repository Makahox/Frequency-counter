# Max Senior
# 06/05/2020
# Frequency thingy

word = input("What word do you want to count?")
test_str = word

all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("The number of all characters in", word, "is :\n" + str(all_freq))
