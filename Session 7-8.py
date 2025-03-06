s1 = "hello"
s2 = "world"
print(s1 + " "+ s2)
print(s1, "hello")
print(3*s2)
print((10//2)*s1)

print(s1, len(s1))
print(3*s2, len(3*s2))

for c in s2:
    print(c)

for c in s1:
    print(c*4, end="")
print()

s3 = ""
for c in s1:
    s3 += c*4
print(s3)

## in can be used to check if one string is inside another
print("h" in s1) # true
print("d" in s2) # true
print("x" in s1) # false
print("wor" in s2) # true


s = "Hello"
print(s)

s2 = "Hello sir 1234123"
print(s2)

s = 'And she said: "hello!'
print(s)

print(",.'\"\"\"\"")

#Simple String
s = "hello!"
print(s[2], s[2])
print(s[-1])
print(s[-1], s[-5])

#Slices String
s = "abcdefghijklmnop"
print(s)
print(s[1:4], s[6:9])
print(s[:4])
print(s[1:10:2])
print(s[::-1])
print("racecar"[::-1])

s = "cat"
s = "r" + s[1:]
print(s)

s = "seven"
s = s[:2] + "7" + s[3:]
print(s)

#String Methods
from idlelib.replace import replace

print(dir("hello"))

print(help("hi".capitalize))

print("i like to go to school".capitalize())

print("IS THIS SUPPOSED TO WORK?".capitalize())

print("hello".center(50,"x"))

print("gmail.com".find("."))

print("gmail.com".find("john"))

s = "i see a cat who like to cat while i cat on a cat"

poz = 0
while True:
    poz = s.find("cat", poz)
    if poz == -1:
        break
    print("Found cat on position", poz)
    poz += 1

s = "I SEE A LOT OF THINGS!"
print(s.lower())

s= "i see a lot of things"
print(s.upper().capitalize())

s= "i see a cat who likes to eat a rat. what a good cat"
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))
s= "Hello, kind sir! How are you today?"
print(s.replace(",", "").replace("!","").replace("?",""))

s = "i like the mountains"
print(s.title())

s = "i like to go shopping"
print(s.split())

splited = s.split()
print("XX".join(splited))
