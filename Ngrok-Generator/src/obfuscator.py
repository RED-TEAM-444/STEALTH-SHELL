import base64

def obfuscate_script(script):
    # Step 1: Base64 encode the script
    encoded_script = base64.b64encode(script.encode('utf-16le')).decode('utf-8')

    # Step 2: Introduce simple string manipulations for added obfuscation
    shifted_script = ''.join(chr(ord(char) + 1) for char in encoded_script)

    # Step 3: Base64 encode the shifted script
    final_encoded_script = base64.b64encode(shifted_script.encode('utf-8')).decode('utf-8')

    # Return the final obfuscated PowerShell command with de-obfuscation logic
    deobfuscation_script = f'''
$encoded_command = "{final_encoded_script}"
$decoded_command = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded_command))
$shifted_command = ""
foreach ($char in $decoded_command.ToCharArray()) {{
    $shifted_command += [char]([int][char]$char - 1)
}}
$final_command = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($shifted_command))
iex $final_command
'''
    return deobfuscation_script.strip()
