# Encryption Project
A pair of programs that work with file handling in Python to both encrypt and decrypt text based on the available encryption algorithms selected by the user.
(still a slight work in progress)

# encrypt.py
encrypt.py allows the user to either provide an existing file to encrypt or enter text to encrypt. If the former option is selected, the user will be prompted to enter the name of the file to encrypt given it's in the same repository/directory. If the latter chosen, the user will first be asked to name a file to save the original text to before encrypting it.
After specifying the name of the output file - which will publically store the ciphertext and corresponding decryption key - the user is granted the option to choose the number of levels by which to encryt the text. Each level (3 maximum) indicates how many times the text will be encrypted upon itself.
Then, the user is prompted to specify which of the 4 ciphers they would like to be used for each of the levels they chose previously.
Should the Caesar or Backshift cipher be selected, the user will have to provide an integer (within a specified range) as the shift for each of these algorithms.
Should the Vigenere cipher be selected, the user will be asked to provide a 3-letter keyword to be used for this type of cipher.
Once equipped with all of this information, encrypt.py will encrypt the text and save the output to the file named by the user.
The decryption key it creates (and also writes to the output file) details which of the 4 algorithms were used at each level of encryption, if applicable. It also details the relevant numerical or ASCII values in the event that the user provided an integer shift and/or a 3-letter keyword for the corresponding cipher.

# decrypt.py
decrypt.py similarly allows the user to decrypt the text of an existing file or to enter text to decrypt. Since this program works in conjunction with encrypt.py, it will only accept files or text that have a valid decryption key at the beginning. Then, it will prompt the user for the name of a file to save the output decrypted text to.
Finally, the decryption algorithm decrypts the text following the decryption key based on the information about each cipher used to encrypt it that it interprets from this key. It writes the decrypted output to the file specified by the user and concludes execution.
