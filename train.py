mediaType = [
    {"name": ".cpp", "file": "C++/programming"},
    {"name": ".html", "file": "html/markupText"},
    {"name": ".css", "file": "css/markupText"},
    {"name": ".java", "file": "java/programming"},
    {"name": ".rb", "file": "ruby/programming"},
    {"name": ".js", "file": "javaScript/programming"},
    {"name": ".py", "file": "python/programming"}
]

userInput = input("Search_File: ")

existingType = False

for type in mediaType:
    if userInput.endswith(type['name']):
        print(f"medeaType:$ {type['file']}")
        existingType = True
        break

if not existingType:
    print("invalid input!")
