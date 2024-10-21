# **Week 4 Practical - DES**
## Material:
- ### [Lecture](#)
- ### [Lab](#)
## **Post-sessional work:**
- Change the code through:
   - Making so a file can be handled 
   - Encrypting the file and decrypting it along with printing the results 
   - Export the generated key from DES to a text file 
   - Time how long each process takes  
- 
- _Challenge: Change the code to perform 3DES_ 

## **Examples**
 - [Cryptool2 ver](#)
 - [Python ver wiith random number generated with the python crypto module](#)
## **Code Snippets**
```python
from Cryptodome.Cipher import DES
from Cryptodome import Random

strKey = b'helloall'
obj_des = DES.new(strKey, DES.MODE_ECB)
strPlainText = b'Roses are red. Violets are blue!'

strCipherText = obj_des.encrypt(strPlainText)
print("Ciphertext: ", strCipherText)
strDecrypt = obj_des.decrypt(strCipherText)
print("Plaintext: ", strDecrypt)

```