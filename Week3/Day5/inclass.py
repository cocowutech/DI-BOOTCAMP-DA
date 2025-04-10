with open('/Users/cocowu/Desktop/nameslist.txt','r') as file:
    for line in file:
        print(line.strip())

with open('/Users/cocowu/Desktop/nameslist.txt','r') as file:
    lines = file.readlines()
    print(lines[4].strip())

with open("/Users/cocowu/Desktop/nameslist.txt", 'r') as f:
    content = f.read(5)
    print("first 5 letters", content)


with open("/Users/cocowu/Desktop/nameslist.txt", 'r') as file:
    words = file.read().split()
    print(words[:10])  

darth_count = words.count("Darth")
luke_count = words.count("Luke")
lea_count = words.count("Lea")

print(f"Darth: {darth_count}, Luke: {luke_count}, Lea: {lea_count}")

with open("/Users/cocowu/Desktop/nameslist.txt", 'a') as file:
    file.write("\nCoco\n")


with open("/Users/cocowu/Desktop/nameslist.txt", 'r') as file:
    content = file.read()

# 替换 Luke 为 Luke SkyWalker
new_content = content.replace("Luke", "Luke SkyWalker")

with open("/Users/cocowu/Desktop/nameslist.txt", 'w') as file:
    file.write(new_content)

