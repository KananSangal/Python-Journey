#My CS50 week 0th problem set 0th, 3rd problem, face converter.
def convert(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    return text

def main():
    text=input("Enter the text: ")
    print(convert(text))

main()
