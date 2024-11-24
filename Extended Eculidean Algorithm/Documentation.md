# Extended Euclidean Algorithm for Modular Inverse

This script implements the **Extended Euclidean Algorithm** to calculate the **modular inverse** of a given key relative to a specified domain. It includes a user-defined function `calculateInverse` that performs the modular inverse calculation and a banner function to display program information.

## **File Overview**

### **1. Script Functionality**

- **Banner Display**: Uses the `art` library to print a decorative banner.
- **Modular Inverse Calculation**: Computes the modular inverse using the Extended Euclidean Algorithm.
  - The modular inverse \( a^{-1} \mod m \) satisfies:
    \[
    a \cdot a^{-1} \equiv 1 \mod m
    \]
  - If the modular inverse exists, the function returns it. If it doesn't, it returns `-1`.

## **Code Breakdown**

### **1. Banner Function**

```python
def banner() -> None:
    '''
    Prints the banner for the Extended Euclidean Algorithm for finding Modular Inverse.
    '''
    print(text2art('\nextended euclideam algorithm', font = "usa_flag"))
    print("Developed and maintained by : @syncattacker")
```

- **Purpose**: Displays an ASCII banner using the `art` library.
- **Output Example**:
  ```
  EXTENDED EUCLIDEAN ALGORITHM
  Developed and maintained by : @syncattacker
  ```

### **2. Modular Inverse Function**

```python
def calculateInverse(key: int, domain: int) -> int:
    '''
    Calculates the Modular Inverse of the Key with respect to the domain.
    '''
    copyDomain = domain
    t1, t2 = 0, 1
    while key > 0:
        quotient = domain // key
        remainder = domain % key
        domain, key = key, remainder
        t1, t2 = t2, t1 - quotient * t2

    if domain != 1:
        return -1

    return t1 % copyDomain
```

- **Parameters**:

  - `key` (\( a \)): The number whose modular inverse is being calculated.
  - `domain` (\( m \)): The modulus.

- **Returns**:

  - The modular inverse \( a^{-1} \mod m \), if it exists.
  - `-1` if the modular inverse does not exist.

- **Algorithm Steps**:
  1. Initialize \( t1 = 0 \) and \( t2 = 1 \) to hold coefficients from the Extended Euclidean Algorithm.
  2. Perform repeated division to reduce \( key \) and \( domain \) until the GCD is found.
  3. If the GCD is \( 1 \), the modular inverse exists. Adjust \( t1 \) to be non-negative by taking it modulo \( m \).

### **3. Example Usage**

```python
print(calculateInverse(5, 26))
```

- **Input**:  
   \( a = 5 \), \( m = 26 \).
- **Output**:  
   \( a^{-1} = 21 \), because:
  \[
  5 \cdot 21 \equiv 1 \mod 26
  \]

## **Extended Euclidean Algorithm for Cryptography**

### **What is the Modular Inverse?**

The **modular inverse** of a number \( a \) modulo \( m \) is the number \( x \) such that:
\[
a \cdot x \equiv 1 \mod m
\]
The modular inverse is fundamental in cryptographic systems like RSA and affine ciphers.

### **Why Use the Extended Euclidean Algorithm?**

The **Extended Euclidean Algorithm** extends the classic Euclidean Algorithm to find not just the GCD of two numbers \( a \) and \( m \), but also coefficients \( x \) and \( y \) such that:
\[
a \cdot x + m \cdot y = \text{gcd}(a, m)
\]
If \( \text{gcd}(a, m) = 1 \), then \( x \mod m \) is the modular inverse of \( a \mod m \).

### **Steps of the Extended Euclidean Algorithm**

1. **Initialization**:

   - Start with coefficients: \( t1 = 0, t2 = 1 \).
   - Use the values \( a = \text{key}, m = \text{domain} \).

2. **Iterative Division**:

   - Perform integer division to find \( \text{quotient} = \lfloor m / a \rfloor \) and remainder \( r = m \mod a \).
   - Update \( a, m \) to \( r, a \) respectively, and adjust coefficients \( t1, t2 \) accordingly:
     \[
     t \leftarrow t1 - \text{quotient} \cdot t2
     \]
   - Repeat until \( a = 0 \).

3. **Result**:
   - If the final GCD is \( 1 \), \( t1 \mod m \) is the modular inverse.
   - If GCD \( \neq 1 \), the modular inverse does not exist.

### **Example: Modular Inverse of 5 Modulo 26**

1. **Initial Values**:  
   \( a = 5, m = 26, t1 = 0, t2 = 1 \).

2. **Iterations**:

   - **Step 1**:  
     \( \text{quotient} = 26 \div 5 = 5, \text{remainder} = 26 \mod 5 = 1 \).  
     Update:
     \[
     t1 = 1, t2 = 0 - (5 \cdot 1) = -5
     \]
   - **Step 2**:  
     \( \text{quotient} = 5 \div 1 = 5, \text{remainder} = 5 \mod 1 = 0 \).  
     Update:
     \[
     t1 = -5, t2 = 1 - (5 \cdot -5) = 21
     \]

3. **Final Modular Inverse**:  
   \( t1 = -5 \). Adjust modulo \( m \):  
   \[
   -5 + 26 = 21
   \]

### **Applications in Cryptography**

1. **Affine Cipher**:

   - In decryption:
     \[
     P = a^{-1} \cdot (C - b) \mod m
     \]
     \( a^{-1} \) is computed using the Extended Euclidean Algorithm.

2. **RSA Algorithm**:
   - Finding the private key \( d \):
     \[
     e \cdot d \equiv 1 \mod \phi(n)
     \]

## **Output**

When run, this program computes the modular inverse or informs the user if no inverse exists, aiding in cryptographic implementations.
