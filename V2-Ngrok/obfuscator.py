import base64
import random
import string

def obfuscate_script(script):
    # Step 1: Base64 encode the script in UTF-16LE format
    encoded_script = base64.b64encode(script.encode('utf-16le')).decode('utf-8')

    # Step 2: Introduce character shift for added obfuscation
    shifted_script = ''.join(chr(ord(char) + 1) for char in encoded_script)

    # Step 3: Base64 encode the shifted script again
    final_encoded_script = base64.b64encode(shifted_script.encode('utf-8')).decode('utf-8')

    # Step 4: Split the script into parts and concatenate at runtime
    parts = [final_encoded_script[i:i+50] for i in range(0, len(final_encoded_script), 50)]
    concatenated_script = ' + '.join(f'"{part}"' for part in parts)

    # Step 5: Use aliases for common PowerShell commands
    ps_aliases = {
        'New-Object': 'New-Obj',
        'System.Text.Encoding': '[Text.Encoding]',
        'System.Convert': '[Convert]',
        'Get-String': 'Get-Str',
        'iex': 'Invoke-Expression'
    }

    deobfuscation_script = f'''
$encoded_command = {concatenated_script}
$decoded_command = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($encoded_command))
$shifted_command = ""
foreach ($char in $decoded_command.ToCharArray()) {{
    $shifted_command += [char]([int][char]$char - 1)
}}
$final_command = [Text.Encoding]::Unicode.GetString([Convert]::FromBase64String($shifted_command))
Invoke-Expression $final_command
'''

    # Step 6: Replace common PowerShell commands with aliases
    for original, alias in ps_aliases.items():
        deobfuscation_script = deobfuscation_script.replace(original, alias)

    return deobfuscation_script.strip()
