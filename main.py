morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',   ' ': '/',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.'
              }

user_input = input("What phrase (letters and numbers) would you like to translate?\n").upper()
translated_list = [morse_dict[item] for item in user_input if item in morse_dict]

translated_message = " ".join(translated_list)
print(f"Your coded message is:\n {translated_message}")
