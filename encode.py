import csv

def load_dictionary(file_path):
    char_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                char_dict[row[0]] = row[1]
    return char_dict

def encode_text(input_text, char_dict):
    encoded_text = ''
    for char in input_text:
        encoded_text += char_dict.get(char, char) + '.'  
    return encoded_text

def main():
    char_dict = load_dictionary('table.csv')
    with open('input.txt', 'r') as file:
        input_text = file.read()
    encoded_text = encode_text(input_text, char_dict)
    with open('output.txt', 'w') as file:
        file.write(encoded_text)

if __name__ == '__main__':
    main()
