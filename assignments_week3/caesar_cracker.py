'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''
def input_checker():
    try:
        
        message = input('Entern an encrypted message\n')
        assert message, 'Enter an encrypted message\n'
        return message
    except AssertionError as e:
        print(f'Error: {e}')
        return 1

def caesar_cracker(message):
    ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    keys = [x for x in range(0,26)]

    newAlps = [ALP[key:] + ALP[:key] for key in keys]

    key_dicts = [{newAlp[i]:letter for i, letter in enumerate(ALP)} for newAlp in newAlps]
    
    for key_dict in key_dicts:
        print(''.join(list(map(lambda x: key_dict[x] if x in ALP else x, message))))
    

    return 0    


def main():
    message = input_checker()
    caesar_cracker(message)


main()