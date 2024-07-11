import base64

def obfuscate_script(script):
    encoded_script = script.encode('utf-16le')
    base64_script = base64.b64encode(encoded_script).decode('utf-8')
    return f'powershell -EncodedCommand {base64_script}'

