def text_to_binary(text):
    binary = ""
    for char in text:
        # Convert each character to its ASCII value
        ascii_value = ord(char)
        
        # Convert the ASCII value to binary and append it to the result
        binary += bin(ascii_value)[2:].zfill(8)
    
    return binary

# Example usage
text = "عاشت ايدك ربي يجازيك ع فعل الخير"
binary_text = text_to_binary(text)
print(binary_text)
