pythonScriptPath = "C:\Absolute\Path\To\coviPing\coviPing.py"
command = "cmd.exe /c cd """ & pythonScriptPath & """ && pythonw.exe """ & pythonScriptPath & "coviPing.py"""

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run command, 0, False
Set WshShell = Nothing
