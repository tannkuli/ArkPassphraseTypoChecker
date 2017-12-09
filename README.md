# Ark Passphrase Typo Checker
Python script which generates > 20.000 possible typos from your original passphrase and checks if an Ark address matches the one where you sent the Ark by mistake.
Requires that you know the passphrase you used and the "only" mistake you made was a typo.

### Generated typos include:

* Forgot words
* Missclicked a random key somewhere in the phrase
* Missed letter or a space
* Double letters
* Reversed two letters
* Switched one letter with another from alphabet (including capital letters)

Edit the script, type in your passphrase and Ark address where your ark is stored by mistake and run main.py. Hopefully this can help you restore your Ark.

Requires python, arky and itertools
