def encrypt(text, key):
    encrypted_text = ""

    for char in text:
        if ord(char) >= 97 and ord(char) <= 122:
            encrypted_text += chr( (ord(char)-97 + key)%26 + 97)
        elif ord(char) >= 65 and ord(char) <= 90:
            encrypted_text += chr( (ord(char)-65 + key)%26 + 65)
        else:
            encrypted_text += char

    return encrypted_text

def main():
    key = 3
    with open("data.txt", "r") as file, open("result.txt", "w") as result:
        for line in file:
            result.write(encrypt(line, key))

if __name__ == '__main__':
    main()