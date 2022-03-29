f=open(input("What file would you like to import?"))
def histogram(str):
    dick = {}

    for word in str:
        if word in dick:
            dick[word] += 1
        else:
            dick[word] = 1
    return dick
    
    
print(histogram(sorted(f.read().split())))