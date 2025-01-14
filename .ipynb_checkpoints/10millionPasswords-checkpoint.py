import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Open Passwords Txt")

openPassFile = open('10-million-password-list-top-100000.txt')
readFile = openPassFile.read()
print(readFile)
