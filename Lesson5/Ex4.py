def decrypt_the_secret_message(message: str) -> str:
    """
    Decrypts the secret message in capital letters
    """
    secret_message = ''
    for letter in message:
        if letter.isupper():
            secret_message += letter
    return secret_message


# Test case
assert decrypt_the_secret_message("How are you? Eh, ok. Low or Lower? Ohhh.") == 'HELLO'
assert decrypt_the_secret_message("This is a tEst of the function'S abiliTy to find seCret phrAses "
                                  "in messageS by parsing capital lEtters in sentences.") == 'TESTCASE'
