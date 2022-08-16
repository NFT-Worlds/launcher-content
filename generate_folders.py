import os

def cmd(command: str):
    os.system(command)

def left_pad(num: int) -> str:
    s = str(num)
    while len(s) < 5:
        s = "0" + s
    return s

def initialize_folder(num: int):
    content = '''# Index for NFT World #{}
Posts will be displayed in the order below:

- [Your first post](./001-first.md)

'''.format(num)
    first_post = 'Hello NFT Worlds!'
    cmd('mkdir worlds/' + left_pad(num))
    f = open("./worlds/" + left_pad(num) + "/_index.md", "w")
    f.write(content)
    f.close()
    f = open("./worlds/" + left_pad(num) + "/001-first.md", "w")
    f.write(first_post)
    f.close()

c = 1
end = 10000

while c <= 10000:
    initialize_folder(c)
    print(c)
    c += 1