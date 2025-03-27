class Morse_code():
    def __init__(self):
            self.conversion_table = {
                " ": "/",
                "a": ".-",
                "b": "-...",
                "c": "-.-.",
                "d": "-..",
                "e": ".",
                "f": "..-.",
                "g": "--.",
                "h": "....",
                "i": "..",
                "j": ".---",
                "k": "-.-",
                "l": ".-..",
                "m": "--",
                "n": "-.",
                "o": "---",
                "p": ".--.",
                "q": "--.-",
                "r": ".-.",
                "s": "...",
                "t": "-",
                "u": "..-",
                "v": "...-",
                "w": ".--",
                "x": "-..-",
                "y": "-.--",
                "z": "--..",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "10": "-----",
                ".": ".-.-.-",
                ",": "--..--",
                "?": "..--..",
                "'": ".----.",
                "!": "-.-.--",
                "(": "-.--.",
                ")": "-.--.-",
                "&": ".-...",
                ":": "---...",
                ";": "-.-.-.",
                "=": "-...-"
            }

    def text_to_Morse(self,s):

        conversion = []
        str_lower = s.lower()
        i = 0
        for i in range(len(s)):
            print(str_lower[i])
            if str_lower[i] in self.conversion_table:
                morse_value = self.conversion_table.get(str_lower[i])
                print(morse_value)
                conversion.append(morse_value + ' ')
        return "".join(conversion)

    def Morse_to_text(self,s):
        message = s + ' '
        print(s)
        decipher = ''
        citext =''
        for letter in message:
            if (letter == '/'):
                decipher +=' '
            elif (letter != ' '):
                    citext += letter
                    print(citext)
            else:
                print('converting text')
                decipher += list(self.conversion_table.keys())[list(self.conversion_table.values()).index(citext)]
                citext =''
        return decipher







