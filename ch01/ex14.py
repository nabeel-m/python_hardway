from sys import argv

script, filename=argv

txt = open(filename)

print(f"Here is a {filename}")
print(txt.read())

print(f"print filename again")
file_again=input('>')

txt_again = open(file_again)
print(txt_again.read())