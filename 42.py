import re


nc = ord('A') -1

def find_tri(maxt):
    return [int(0.5 * e * (e+1)) for e in range(1,maxt)]

tri = find_tri(30)
biggest_t = max(tri)
tri_c = 0

print( tri,biggest_t)


with open("p042_words.txt") as f:
    for line in f:
        for word in line.split(","):
            word = re.sub(r'^"|"$','', word)
            cur = sum([ord(r) - nc  for r in word])
            # print("word:cur", word, cur)
            if biggest_t < cur:
                exit("BIGGGGGGEST T TO SMALL!!")
            if cur in tri:
                tri_c +=1

print("Found triangle words:",tri_c)


