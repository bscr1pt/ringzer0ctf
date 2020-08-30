import hashlib


with open("hashes.txt", "a") as fil:
    for i in range(0,100001):
        b = bytes(str(i), "utf-8")
        hex_dig = hashlib.sha1(b).hexdigest()
        fil.write(str(i)+"="+str(hex_dig)+"\n")
