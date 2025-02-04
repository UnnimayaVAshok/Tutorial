f = open("input.txt", "r")
txt = f.read()
words = txt.split()
print(words)

w_count = len(words)
print(w_count)

endings = ['.', '!', '?', ';', ':']
s_count = 0
segment = ""

for char in txt:
    if char in endings:  
        if segment.strip():  
            s_count += 1
        segment = ""  
    else:
        segment += char  

if segment.strip():
    s_count += 1

print("Sentence count:", s_count)

vowels = "aeiou"
syll_count = 0

for w in words:
    w = w.lower()  

    if len(w) <= 3:
        syll_count += 1
        continue

    sylls = 0
    i = 0

    while i < len(w):
        if w[i] in vowels:
            if i + 1 < len(w) and w[i + 1] in vowels:
                sylls += 1
                i += 2  
            else:
                sylls += 1
                i += 1
        else:
            i += 1

    if w.endswith("es") or w.endswith("ed"):
        sylls -= 1
    elif w.endswith("e") and not w.endswith("le"):
        sylls -= 1
    if sylls < 1:
        sylls = 1

    syll_count += sylls

print("Syllable count:", syll_count)

f_index = round(206.835 - 1.1015 * (w_count / s_count) - 84.6 * (syll_count / w_count))
print("Flesch Index:", f_index)

grade_lvl = round(0.39 * (w_count / s_count) + 11.8 * (syll_count / w_count) - 15.59)
print("Grade Level:", grade_lvl)

if grade_lvl >= 0 and grade_lvl <= 30:
    print("College Level")
elif grade_lvl >= 50 and grade_lvl <= 60:
    print("School Level")
elif grade_lvl >= 90 and grade_lvl <= 100:
    print("4th Grade")
