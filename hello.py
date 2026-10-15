with open ("sample.txt", "r") as file:
    text = file.read()

word = text.split()
word_count = len(word)

print ("word count:", word_count)

def new_func(word_count):
    with open("result.txt","w") as file:
        file.write("Word count:", str(word_count))