# Password Analyzer

A Python-based password strength analyzer that combines entropy calculation, dictionary checks, pattern detection, and brute-force estimations to evaluate password security.

## Features

- Entropy calculation

- Dictionary (wordlist) lookup

- Case-sensitive or case-insensitive analysis

- Common word detection

- Repetition detection

- Character repetition detection

- Palindrome detection

- Password strength evaluation

- Brute-force attack time estimation

- Support for custom wordlists

- Colored terminal output

---

## How It Works

The analyzer evaluates passwords using several criteria:

### 1. Entropy Estimation

The program estimates theoretical password entropy based on:

- Lowercase letters
- Uppercase letters
- Digits
- Special characters
- Password length

Entropy is displayed in bits.

### 2. Dictionary Check

The password is checked against a wordlist.

If the password appears in the selected wordlist, it is considered significantly weaker because it may be vulnerable to dictionary attacks.

### 3. Pattern Detection

The analyzer detects several common weaknesses:

- Repeated strings

- Repeated characters

- Common words

- Weak palindromes

- Very short passwords

### 4. Brute-Force Estimation

The program estimates the time required to crack a password under several attack scenarios:

- Online website attacks

- Weak server attacks

- Modern GPU attacks

- GPU cluster attacks

The estimation are theoretical as the entropy and the penalisation. Then the measure can be imprecise.

---

## Project Structure

```text
password-analyzer/
|
|--- main.py
|--- README.md
|--- LICENSE
|
|--- src/
|    |--- analyzer/
|    |    |--- __init__.py
|    |    |--- analyze_psswd.py
|    |    |--- bruteforce.py
|    |    |--- checker.py
|    |    |--- entropy.py
|    |    |--- patterns.py
|    |    |--- penalties.py
|    |
|    |--- ui/
|    |    |--- __init__.py
|    |    |--- display.py
|    |    |--- progress_bar.py
|    |
|    |--- wordlists/
|         |--- __init__.py
|         |--- formatter.py
|         |--- loader.py
|
|--- Screenchot/
|    |--- Screenshot-1.png
|    |--- Screenshot-2.png
|    |--- Screenshot-3.png
|    |--- Screenshot-4.png
|    |--- Screenshot-5.png
|
|--- Licenses/
|    |--- derkc0de_LICENSE.txt
|
|--- data/
     |--- common_words.txt
     |--- darkc0de.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Maheva-Christan/password-analyzer.git
```

Move to the directory

```bash
cd password-analyzer
```

Run the program:

```bash
python main.py
```

No external dependencies are required.

---

## Usage

Launch the program:

```bash
python main.py
```

Choose:

1. Built-in wordlist
2. Custom wordlist

Then enter passwords to analyze.

Type:

```text
\exit
```

to quit the program.

Type:

```text
\clear
```

to clear the terminal.

---

## Wordlist Attribution

The bundled `darkc0de.txt` wordlist was not created by this project's author.

It is included under its original MIT License

All rights and credits remain with the original author(s).

---

## Included Wordlist Notice

The repository includes a small example wordlist (`darkc0de.txt`) to allow the project to work immediately after download.

This file is provided for educational and demonstration purposes only.

It is significantly smaller than the datasets commonly used in real-world password cracking attacks.

Professional security assessments often use much larger collections containing millions or billions of entries, including:

- Leaked password databases

- Custom dictionaries

- Rule-based transformations

- Hybrid attacks

Large password datasets are intentionally not distributed with this repository.

Users who want more realistic testing can provide their own wordlists through the custom wordlist feature.

---

## Responsible Use

This project is intended for educational and defensive security purposes only.

Users are responsible for complying with applicable laws and regulations.

The authors does not encourage unauthorized access, password cracking, or any illegal activity.

---

## Limitations

This project is intended as an educational tool.

The reported values should be considered estimates rather than exact measurements.

Important limitations include:

- Entropy calculations are theoretical.

- Real attackers use smarter techniques than pure brute force.

- Dictionary attacks can be much faster than entropy-based estimates suggest.

- The included wordlist is intentionally limited.

- Attack speeds vary depending on hardware and hashing algorithms.

Examples:

- SHA-256
- NTLM
- bcrypt
- Argon2

can produce vastly different cracking times.

---

## Educational Purpose

This project was created for learning purposes:

- Python programming

- Password security concepts

- Entropy estimation

- Dictionary attacks

- Brute-force attacks

- Regular expressions

It is not intended to replace professional password auditing tools.

---

## Future Improvements

Planned features:

- Keyboard pattern detection

- Sequential character detection

- Date/year detection

- Additional password rules

- Improved attack modeling

- Unit tests

- Better reporting

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
