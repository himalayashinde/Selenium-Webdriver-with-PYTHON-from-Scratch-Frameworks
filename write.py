#Write the list reversed list back to the file

with open("test.txt","r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("test.txt","w") as writer:
        for line in reversed(content):
            writer.write(line)
