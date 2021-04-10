# AES-encryptor
Homework for data security class.
File encryption and decryption using Advanced Encryption Standard (AES) with 128 bit key, and integrity check (SHA256) implemented with Python Crypto library. 
Additionaly basic arithmetic and computation of reverse element in prime number field.
In implementation of encryption I used materials and concepts from https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto access: 09-04-2021
For example this:
*For maximal security, the IV should be randomly generated for every new encryption and can be stored together with the ciphertext. Knowledge of the IV won't help the attacker crack your encryption. What can help him, however, is your reusing the same IV with the same encryption key for multiple encryptions.*
I also tried some docker solutions in this project. If you want check them out:
Nawigate to directory cloned from github and build image with `docker build -t aes-encryptor .`. Or change dot to wanted location.
Finally run container with:
```
docker run -v <loaction to run>:/usr/src/app -ti --name aes-encryptor-container aes-encryptor
```
or to run in current directory:
```
docker run -v $(pwd):/usr/src/app -ti --name aes-encryptor-container aes-encryptor
```
Parameter `-v` mounts location from host machine as enviroment of container and `-ti` stands for interactive terminal.

