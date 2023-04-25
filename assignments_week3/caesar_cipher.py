'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''
def input_checker():
    try:
        data = {}
        mode = input('Do you want to (e)ncrypt or (d)ecrypt?\n')
        assert mode == 'e' or mode == 'd', 'Invalid mode\n'
        
        key = input('Please enter the key (0 to 26) to use.\n')
        try:
            key = int(key)
            assert 0 <= key <= 26, 'Key must be an integer between 0-26'
        except:
            print('Key must be an integer between 0-26')
            return 1
         
        if mode == 'e':
            message = input('Enter the message to encrypt.\n').upper()
        else:
            message = input('Enter the message to decrypt.\n').upper()

        #numbers = [str(i) for i in range(0,10)]

        #for num in numbers:
        #    assert num not in message, "Message should be only letters"


        data['mode'] = mode
        data['key'] = key
        data['message'] = message

        return data
    except AssertionError as e:
        print(f'Error: {e}')
        return 1

def caesar(data):
    mode = data['mode']
    key = data['key']
    message = data['message']
    ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newAlp = ALP[key:] + ALP[:key]

    if mode == 'e':
        key_dict = {letter:newAlp[i] for i, letter in enumerate(ALP)}
    else:
       key_dict = {newAlp[i]:letter for i, letter in enumerate(ALP)} 

    newMessage = ''.join(list(map(lambda x: key_dict[x] if x in ALP else x, message)))
    
    print(newMessage)

    return 0    


def main():
    data = input_checker()
    caesar(data)


main()