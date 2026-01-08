# securezip

SecureZip is a lightweight Python utility for creating password-protected ZIP archives.
Encryption passwords are securely managed using environment variables, preventing sensitive credentials from being hardcoded in source code.

This project demonstrates practical Python scripting, secure configuration handling, and basic encryption workflows.




## Features

Password-protected ZIP file creation

Secure password management via environment variables

Separate scripts for zipping and unzipping

Simple and readable Python implementation

Suitable for command-line or script-based use



## Technologies Used

Python

ZIP file handling

AES encryption (via Python ZIP libraries)

Environment variables (os.environ)


## Configuration
Before running SecureZip, set the password as an environment variable.

macOS / Linux

  export SECUREZIP_PASSWORD="your_strong_password"

Windows (PowerShell)

  setx SECUREZIP_PASSWORD "your_strong_password"

Do not store passwords directly in the source code.




## Usage

To create an encrypted Zip archive:

  python zipper.py input_folder output.zip

To Extract an encrypted ZIP archive

python unzipper.py output.zip extract_folder
