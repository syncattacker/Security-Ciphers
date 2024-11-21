# **Caesar Cipher Documentation**

## **Overview**

The Caesar Cipher program is a Python-based tool that provides a simple encryption and decryption mechanism by shifting alphabetic characters by a user-defined key. It also supports brute-forcing to determine the encryption key. The program is menu-driven, making it user-friendly and interactive.

## **Features**

- **Encryption**: Converts plaintext to ciphertext using a shift key.
- **Decryption**: Converts ciphertext back to plaintext using the same key.
- **Brute-Force**: Determines the encryption key by comparing plaintext and ciphertext.
- **Interactive Menu**: A user-friendly interface for easy operation.

## **Requirements**

- Python 3.x
- `art` library (for the banner)
  ```bash
  pip install art
  ```

## **Usage**

### **Running the Program**

1. Save the program file (`caesar_cipher.py`) in your working directory.
2. Run the program using:
   ```bash
   python caesar_cipher.py
   ```

### **Menu Options**

Upon running the program, you will see the following menu:

1. **Encrypt**: Encrypt a plaintext message using a shift key.
2. **Decrypt**: Decrypt a ciphertext message using a shift key.
3. **Brute-Force**: Find the key by comparing plaintext and ciphertext.
4. **Exit**: Exit the program.

## **Functions**

### **1. `banner()`**

- **Description**: Displays a decorative banner using the `art` library.
- **Parameters**: None
- **Returns**: None

### **2. `clearTerminal()`**

- **Description**: Clears the terminal for better readability.
- **Parameters**: None
- **Returns**: None

### **3. `userChoice()`**

- **Description**: Displays the menu and prompts the user to select an option.
- **Parameters**: None
- **Returns**: Integer representing the user's choice.

### **4. `encrypt(plainText, encryptionKey)`**

- **Description**: Encrypts plaintext by shifting alphabetic characters using the given key.
- **Parameters**:
  - `plainText` (str): The text to be encrypted.
  - `encryptionKey` (int): The shift key (0–25).
- **Returns**: Encrypted ciphertext (str).

### **5. `decrypt(cipherText, decryptionKey)`**

- **Description**: Decrypts ciphertext by reversing the shift applied during encryption.
- **Parameters**:
  - `cipherText` (str): The text to be decrypted.
  - `decryptionKey` (int): The shift key (0–25).
- **Returns**: Decrypted plaintext (str).

### **6. `bruteForce(plainText, cipherText, verbose=False)`**

- **Description**: Tries all possible keys to match the ciphertext with the plaintext.
- **Parameters**:
  - `plainText` (str): The original plaintext.
  - `cipherText` (str): The ciphertext to match.
  - `verbose` (bool): Enables detailed output during brute force.
- **Returns**: The encryption key (int) if found, otherwise `None`.

### **7. `validateMessage(message)`**

- **Description**: Ensures the input message contains only alphabetic characters.
- **Parameters**:
  - `message` (str): The text to validate.
- **Returns**: `True` if valid, otherwise `False`.

### **8. `validateKey(userKey)`**

- **Description**: Validates the shift key to ensure it is within the range 0–25.
- **Parameters**:
  - `userKey` (int): The key to validate.
- **Returns**: `True` if valid, otherwise `False`.

### **9. `handleUserInput(inputType, keyType)`**

- **Description**: Handles user input for encryption or decryption tasks.
- **Parameters**:
  - `inputType` (str): Specifies if the input is plaintext or ciphertext.
  - `keyType` (str): Specifies if the input is an encryption or decryption key.
- **Returns**: List containing the validated message and key.

### **10. `handleBruteForceInput(plainPrompt, cipherPrompt)`**

- **Description**: Handles user input for brute-forcing a key.
- **Parameters**:
  - `plainPrompt` (str): Prompt text for plaintext input.
  - `cipherPrompt` (str): Prompt text for ciphertext input.
- **Returns**: List containing the plaintext and ciphertext.

### **11. `isVerbose(plainText, cipherText, key)`**

- **Description**: Displays detailed output for each key during brute force.
- **Parameters**:
  - `plainText` (str): The plaintext being tested.
  - `cipherText` (str): The target ciphertext.
  - `key` (int): The key being tested.
- **Returns**: None

### **12. `entryPoint()`**

- **Description**: The main function that drives the program. Handles the user interface and function calls.
- **Parameters**: None
- **Returns**: None

## **Example Usage**

### **Encryption**

Input:

```
Enter Your Plain Text: hello
Enter The Encryption Key: 3
```

Output:

```
Your Cipher Text is: khoor
```

### **Decryption**

Input:

```
Enter Your Cipher Text: khoor
Enter The Decryption Key: 3
```

Output:

```
Your Plain Text is: hello
```

### **Brute-Force**

Input:

```
Enter The Plain Text: hello
Enter The Cipher Text: khoor
Do you want verbose for brute force [yes / no]: no
```

Output:

```
Key Found: 3
```

## **Author**

Developed and maintained by **@syncattacker**.

## **License**

This program is open-source and free to use. Contributions are welcome!
