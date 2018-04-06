# Ark Passphrase Typo Checker
Python script which generates > 20.000 possible typos from your original passphrase. It then uses bruteforce to check if a missspelled passphrase matches a known Ark address. This problem can occur if you mistakenly send Ark to an address while using the wrong passphrase.

Requires that you know the passphrase you used to transfer Ark and the "only" mistake you made was a typo (e.g. missing word or spelling mistake).

### Generated typos include:

* Forgot words
* Missclicked a random key somewhere in the phrase
* Missed letter or a space
* Double letters
* Reversed two letters
* Switched one letter with another from alphabet (including capital letters)

Just edit the script, type in your original passphrase and Ark address where your ark is stored by mistake and run main.py. 

Requires: Python, Arky and itertools

Hopefully this can help you restore your lost Ark.

Feel free to donate if this helped you.

ARK: AJDh1uUUQdPqzznN3SyyHvjCR81o7j3DL5

BTC: 1N3xrh4vHTdFtSL7konsYrC6iWmnCGgzkd
