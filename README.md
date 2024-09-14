Password Manager
This is a simple command-line password manager built using Python. It allows you to securely store and retrieve passwords, encrypted with AES-256 using the cryptography.fernet module. Passwords are stored in a local file (password.txt), and the encryption keys are stored alongside the encrypted passwords (for demonstration purposes, though in a real-world application, keys should be securely stored separately).

Features
Encrypt passwords using AES-256 encryption.
Decrypt passwords for viewing stored credentials.
Add new accounts and passwords securely.
View stored passwords with decryption.
