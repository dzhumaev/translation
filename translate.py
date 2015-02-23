from io import open

def load_data(text_file):
    sentences = []
    with open(text_file, 'r', encoding='utf-8-sig') as in_file:
        for line in in_file:
            sentences.append(line.strip().encode('utf-8'))
    return sentences

def improve_translation():
    sentences = []

def write_result(text):
    with open('russian', 'w', encoding='utf-8-sig') as out_file:
        for line in text[0:-1]:
            out_file.write(line.decode('utf-8-sig'))
            out_file.write('\n'.decode('utf-8-sig'))
        out_file.write(text[-1].decode('utf-8-sig'))
    
def main():
    english = load_data('english')
    google = load_data('google')
    bing = load_data('bing')
    yandex = load_data('yandex')
    improve_translation()
    write_result(yandex)

if __name__ == '__main__':
    main()
