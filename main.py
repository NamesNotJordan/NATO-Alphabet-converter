import pandas

{"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

def convert_word():
    word = input("enter a word").upper()
    try:
        result = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Only letters please")
        convert_word()
    else:
        print(result)


convert_word()