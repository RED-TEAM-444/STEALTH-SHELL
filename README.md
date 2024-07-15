# Stealth Shell

##  Introduction
The PowerShell Reverse Shell Generator Tool is designed to facilitate the creation of customizable, undetectable PowerShell scripts for establishing reverse shells on Windows systems. This tool allows security professionals and penetration testers to generate scripts that can be used for remote access and management in controlled environments.


##  Features

 - **Dynamic Configuration:**  Users can specify IP addresses and ports to customize generated scripts.

 - **Obfuscation Techniques:** Built-in support for obfuscation to evade antivirus detection.

 - **Integration with ngrok:** Facilitates remote access setup through ngrok tunnels.

 - **Cross-Platform Compatibility:** Python-based tool compatible with various operating systems.


##  Usage
   This project devided into two parts:

- **Local Host:**    Tested between your virtual Machine and get reverse shell of your Virtual Windows, this is only for testing.
   
- **Ngrok Reverse Shell:**    Here You will generate the reverse shell that intergrate with ngrok and get reverse shell over the internet.


##  How To Use

  - Clone the repository
    
     ```
     git clone https://github.com/RED-TEAM-444/STEALTH-SHELL.git
     ```

  - Now go to cloned directory

    ```
    V2-Ngrok
    ```

  - Setup Ngrok
    #### Detailed Implementation
    - Install ngrok
      
        - Download ngrok from ngrok's official website.
        - Unzip and move the binary to a directory included in your system’s PATH (e.g., /usr/local/bin).

    -  Authenticate ngrok
   
       - Sign up for an ngrok account to get an authentication token.
       - Authenticate ngrok on your machine using:
         
        ```
        ngrok authtoken YOUR_AUTH_TOKEN
        ```
- Run the Script

  ```
  python3 main.py -p 4444
  ```

  ![WhatsApp Image 2024-07-14 at 11 55 36 PM](https://github.com/user-attachments/assets/64e6e9b8-2c06-4563-b214-44d56050bfcd)

 
 - Save the output

   ```
   Save the Obfuscated output in .ps1 file.
   Example: reverse_shell.ps1
   ```
 - Transfer the ```.ps1``` file into your Virtual Windows to convert it into executable form ```EXE```.

 - Install PS2EXE Tool in your Virtual Windows
##  Understand Working Structure through diagram



![diagram ](https://github.com/user-attachments/assets/d9334e73-e004-4301-b612-319f7ede06fd)
