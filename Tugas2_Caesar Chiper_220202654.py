def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97  
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  
    return result

def decrypt(cipher_text, shift):
    return encrypt(cipher_text, -shift) 

message = input("Masukkan pesan: ")
shift = int(input("Masukkan nilai shift (pergeseran): "))

encrypted_message = encrypt(message, shift)
print(f"Hasil enkripsi: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift)
print(f"Hasil dekripsi: {decrypted_message}")
