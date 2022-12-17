def greet(lang):
    if lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print("Bonjour")
    else:
        print("Hello")


language = input("Enter your language: ")
greet(language)
