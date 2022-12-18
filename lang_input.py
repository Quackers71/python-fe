def greet(lang):
    if lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print("Bonjour")
    else:
        print("Hello")

print("Examples: es, fr, gb etc...")
language = input("Enter your language: ")
greet(language)
