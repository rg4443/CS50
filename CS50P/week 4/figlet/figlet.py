import pyfiglet
import random
import sys

figlet = pyfiglet.Figlet()

if len(sys.argv) == 1:
    font = random.choice(pyfiglet.Figlet().getFonts())
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    font = sys.argv[2]
    if font not in pyfiglet.Figlet().getFonts():
        sys.exit("Error: Invalid font")
else:
    sys.exit("Error: Invalid usage")

word = input("Input: ")
figlet.setFont(font=font)
print(figlet.renderText(word))
