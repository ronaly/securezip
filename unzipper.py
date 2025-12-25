#!/usr/bin/env python3


import pyzipper
import os
import argparse


def extract_the_zipped_file(zip_path, password):
    """Extract the AES-encrypted ZIP file"""

    folder = os.path.splitext(os.path.basename(zip_path))[0]
    
    #create the folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    try:

        with pyzipper.AESZipFile(zip_path) as zf:
            zf.setpassword(password.encode())
            zf.extractall(folder) 
    except RuntimeError as e:
        print("AES extraction failed: ", e)
        print("Trying ZipCrypto fallback ...")
        
        try: 
            with pyzipper.ZipFile(zip_path) as zf:
                zf.setpassword(password.encode())
                zf.extractall(".")
            print("Extracted using ZipCrypto")
        except Exception as e2:
            print("Extraction failed both AES and Crypto", e2)    
        


def main():
    parser = argparse.ArgumentParser(description="Secure Unzip Tool (AES encrypted)")
    parser.add_argument("--unzip", required=True, help="Zip file to extract")   

    args = parser.parse_args()

    #Read the password from environment variable
    password = os.getenv("ZIPPER_PASS")

 
    if not password:
        raise ValueError("Password in environment variable is not set!")    


    extract_the_zipped_file(args.unzip, password)
    print(f"Extracted {args.unzip} successfully")


# Entry Point
if __name__ == "__main__":
    main()
