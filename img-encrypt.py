
def encrypt_image(input_path, output_path, key):
    """
    Encrypt an image by performing pixel manipulation
    """
    try:
        # Open the image
        img = Image.open(input_path)
        pixels = np.array(img)
        
        # Simple encryption: XOR each pixel value with the key and swap channels
        encrypted_pixels = np.bitwise_xor(pixels, key)
        
        # Swap color channels (RGB -> BRG for example)
        encrypted_pixels = encrypted_pixels[:, :, [2, 0, 1]] if encrypted_pixels.shape[2] >= 3 else encrypted_pixels
        
        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_pixels)
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
        
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypt an image by reversing the pixel manipulation
    """
    try:
        # Open the encrypted image
        img = Image.open(input_path)
        pixels = np.array(img)
        
        # Reverse the channel swap first (BRG -> RGB)
        decrypted_pixels = pixels[:, :, [1, 2, 0]] if pixels.shape[2] >= 3 else pixels
        
        # Reverse the XOR operation
        decrypted_pixels = np.bitwise_xor(decrypted_pixels, key)
        
        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_pixels)
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
        
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    print("Simple Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1/2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice")
        return
    
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    
    try:
        key = int(input("Enter encryption key (integer between 0-255): "))
        if key < 0 or key > 255:
            raise ValueError("Key must be between 0-255")
    except ValueError as e:
        print(f"Invalid key: {e}")
        return
    
    if choice == '1':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()