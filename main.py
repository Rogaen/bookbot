def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count = len(file_contents.split())
    # print(count)
    # print(character_count(file_contents))
    x = report(character_count(file_contents))

def character_count(text):
    char_count_dict = {}
    for char in text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def report(charcount):
    for entry in charcount:
        if entry.isalpha():
            count = charcount[entry]
            print(f"the'{entry}' character was found {count} times")

main()
