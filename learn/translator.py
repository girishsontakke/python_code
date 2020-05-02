#translating the phrases into language in which vowels are replaced with "g"
def translator(phrase):
        translation =""
        for letter in phrase:
                if letter.lower() in "aeiou":
                        if letter.isupper():
                                translation+="G"
                        else:                                
                                translation+="g"
                else:
                        translation+=letter
        return translation
print(translator(input("Enter a phrase:")))
