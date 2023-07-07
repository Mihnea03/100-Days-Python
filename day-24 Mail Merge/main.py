# Mail Merge
# Munteanu Mihnea @ Mihnea03

OUT = 'Output/'
TEMPLATE = 'Letter/letter_template.txt'
NAMES = 'Names/names.txt'

def get_names():
    with open(NAMES, 'r') as n:
        aux_names = n.readlines()
    
    names = []
    for name in aux_names:
        names.append(name.replace('\n', ''))
    
    return names

def get_template():
    letter = open(TEMPLATE, 'r')
    letter_template = ''
    for line in letter:
        letter_template += line
    letter.close()

    return letter_template

def main():
    names = get_names()
    letter_template = get_template()

    for name in names:
        with open(OUT + f'letter_for_{name}.txt', 'w') as letter:
            letter.write(letter_template.replace('[name]', name))
    return

if __name__ == '__main__':
    main()
