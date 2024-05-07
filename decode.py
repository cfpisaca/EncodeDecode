import csv

def load_dictionary(file_path):
    char_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2: 
                char_dict[row[1]] = row[0]
    return char_dict

def decode_text(encoded_text, char_dict):
    encoded_chars = encoded_text.split('.')
    decoded_text = ''
    for char in encoded_chars:
        decoded_text += char_dict.get(char, char)
    return decoded_text

def main():
    char_dict = load_dictionary('table.csv')
    with open('output.txt', 'r') as file:
        encoded_text = file.read()
    decoded_text = decode_text(encoded_text, char_dict)
    print('Decoded text:', decoded_text)

if __name__ == '__main__':
    main()
