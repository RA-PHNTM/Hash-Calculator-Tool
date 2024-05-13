import hashlib
import sys

def get_file_hash(file_path, hash_type):
    """Calculate hash of file."""
    hash_obj = hashlib.new(hash_type)
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                hash_obj.update(chunk)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return hash_obj.hexdigest()

def main():
    if len(sys.argv) < 2:
        file_path = input("Please enter file name/directory: ")
    else:
        file_path = sys.argv[1]
    
    md5_hash = get_file_hash(file_path, 'md5')
    sha256_hash = get_file_hash(file_path, 'sha256')
    sha512_hash = get_file_hash(file_path, 'sha512')

    print(f"MD5: {md5_hash}")
    print(f"SHA-256: {sha256_hash}")
    print(f"SHA-512: {sha512_hash}")

if __name__ == "__main__":
    main()
