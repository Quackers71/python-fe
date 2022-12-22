def greet(lang):
    if lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print("Examples: es, fr, gb etc...")
language = input("Enter your language: ")
name = input("Enter your name: ")

print(greet(language), name)
