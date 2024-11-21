# Caesar Cipher

The Caesar Cipher is one of the simplest and oldest encryption techniques. It is a type of substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet. The cipher is named after Julius Caesar, who reportedly used it to communicate with his generals.

---

## How It Works

1. **Encryption**:  
   Each letter in the plaintext is replaced with a letter that is a fixed number of positions down the alphabet.  
   For example, with a shift of **3**:

   - `A` becomes `D`
   - `B` becomes `E`
   - `C` becomes `F`  
     This is applied to all letters in the plaintext.

2. **Decryption**:  
   To decrypt, the reverse process is applied. The letters are shifted back by the same number of positions.

---

## Example

Let's take the plaintext: `HELLO`  
With a shift of **3**, the encrypted text is:

- `H` → `K`
- `E` → `H`
- `L` → `O`
- `L` → `O`
- `O` → `R`

Encrypted text: `KHOOR`

To decrypt `KHOOR` with a shift of **3**:

- `K` → `H`
- `H` → `E`
- `O` → `L`
- `O` → `L`
- `R` → `O`

Decrypted text: `HELLO`

---

## Caesar Cipher Formula

For a letter `x`:

- **Encryption**: `E(x) = (x + n) % 26`
- **Decryption**: `D(x) = (x - n) % 26`

Where:

- `n` is the shift amount (key).
- `% 26` ensures the calculation wraps around the alphabet.

---

## Strengths

- Simple to implement.
- Easy to understand.

---

## Weaknesses

- **Low Security**: Since there are only 25 possible shifts, it is vulnerable to brute-force attacks.
- **Letter Frequency Analysis**: The cipher does not alter the frequency of letters, making it susceptible to statistical attacks.

---

## Applications

Although the Caesar Cipher is not used in modern cryptography due to its simplicity and vulnerability, it is still used in:

- Educational tools to teach the basics of encryption.
- Simple puzzles or games.
