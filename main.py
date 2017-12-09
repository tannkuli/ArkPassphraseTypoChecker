from arky import api
from arky import core
from itertools import combinations

api.use("ark")

#Your True passphrase
your_passphrase = ""

#Where your ark is unwillingly stored
your_address = "" 

#Characters to check in case of typos.
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÆØÐabcdefghijklmnopqrstuvwxyáæøð\t!"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{|}~'

class PassphraseTypos:
    
    def __init__(self):
        self.alphabet = []
        self.p = []
        
    def characters(self, alphabet):
        self.alphabet = alphabet
        
    def letters(self, letter):
        self.alphabet += letter
        
    def passphrase(self,passphrase):
        self.p = passphrase
        
        
    def change_combination(self):
        #Gets all combinations of words. Note this is not performing permutations.
        return [" ".join(subset) for L in range(1, len(self.p.split())+1) for subset in combinations(self.p.split(), L) ]
    
    def inserted_key(self):
        #Inserts a character from alphabet in each position.
        return ([self.p[:i] + char + self.p[i:] for i in range(0, len(self.p)+1) for char in self.alphabet])
    
    def drop_single_letter(self):
        #Skips one letter at a time
        return [self.p[:i]+self.p[i+1:] for i in range(len(self.p))]

    def double_letter(self):
        #creating a list of phrases using with double letters "hhello world, heello world.."
        return [self.p[:i] + self.p[i-1] + self.p[i:] for i in range(1,len(self.p)+1)]

    def reverse_letter(self):
        #Reversing 2 letters
        return [self.p[:i-1] + self.p[i-1:i+1:1][::-1] + self.p[i+1:] for i in range(len(self.p)) if len(self.p[i-1:i+1:1][::-1]) == 2]
    
    def switch_letter(self):
        #Switches one letter for each letter in the alphabet
        phrases = []
        for i in range(len(self.p)):
            for char in self.alphabet:
                p = list(self.p)
                p[i]=char
                phrases.append("".join(p))
        return phrases

    def all_typos(self):
        #Generating all typos and returning a list
        phrases = []
        phrases += self.change_combination()
        phrases += self.inserted_key()
        phrases += self.drop_single_letter()
        phrases += self.double_letter()
        phrases += self.reverse_letter()
        phrases += self.switch_letter()
        return phrases


class ArkPassphraseTypoChecker:
    def __init__(self):
        self.list_to_check = []
    
    def passphrases_to_check(self, list_of_phrases):
        self.list_of_phrases = list_of_phrases
        
    def private_address(self, address_private):
        self.address_private = address_private
    
    def check_match(self):
        i=0
        print ("Checking {} possible typos.\n".format(len(self.list_of_phrases)))
        for passphrase in self.list_of_phrases:
            address_found = core.getAddress(core.getKeys(secret=passphrase))
            if address_found == self.address_private:
                print ("\nFOUND THE CORRECT PASSPHRASE MATCHING YOUR PRIVATE ADDRESS!!!\n")
                print (passphrase)
                print ("\nYou got lucky this time! Use this address to transfer your ARK")
                print ("\nPlease remember to store your passphrase in a safe place.")
                return passphrase
            i+=1
            if i%100 == 0:
                print ("Checked: {} of {} passphrases so far.".format(i,len(self.list_of_phrases)))
                
if __name__ == "__main__":
    typos = PassphraseTypos()
    typos.characters(alphabet)
    typos.passphrase(your_passphrase)
    all_typos = typos.all_typos()

    checker = ArkPassphraseTypoChecker()
    checker.private_address(your_address)
    checker.passphrases_to_check(all_typos)
    checker.check_match()