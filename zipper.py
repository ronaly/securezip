#!/usr/bin/env python3


import pyzipper
import os
import argparse


def create_secure_zip(input_path, output_zip, password):
    """
    Create a password-protected ZIP file using AES encryption.
    
    input_file: file or folder path you want to compress
    output_zip: name of the resulting zip file
    password:   password string
    """


    with pyzipper.AESZipFile(output_zip,
                             'w',
                             compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode())  # password must be bytes

        if os.path.isfile(input_path):
            # Single file -> store only filename ; arcname includes only the file itself
            zf.write(input_path, arcname=os.path.basename(input_path))
        elif os.path.isdir(input_path):
            # folder walk through all files and preserve structure
            for root, _, files in os.walk(input_path):
                for file in files:
                    full_path = os.path.join(root, file)
                    #preserve folder hierarchy relative to input_path
                    arcname = os.path.relpath(full_path, start=input_path)
                    zf.write(full_path, arcname=arcname)




def main():

    parser = argparse.ArgumentParser(description="Secure ZIP Tool (AES encrypted)")
    parser.add_argument("--zip", required=True, help="File or Folder to zip")
    parser.add_argument("--out", required=True, help="Output zip file name")

    args = parser.parse_args()

    password = os.getenv("ZIPPER_PASS")
   
    if not password:
        raise ValueError("Password in environment variable is not set!")    

    create_secure_zip(args.zip, args.out, password)
    print(f"Created {args.out} with AES encryption")
   


# Entry Point
if __name__ == "__main__":
    main()
