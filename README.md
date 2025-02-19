## A CLI for Quickly Connecting to Your Saved Servers

## List of Commands
- `ls` — Displays all saved servers
- `add` — Adds a new server and applies ssh-copy-id to it
- `del` — Removes a server
- `copyid` —  Applies ssh-copy-id to server
- `help` — Get all commands
- `exit` — Stop program
- {server_name} — Connects to the specified server. You can also use this command as an argument when launching the script (e.g., `memhost main`), in which case it will be executed automatically.

![image](https://github.com/user-attachments/assets/7c81eb31-646a-4c85-91a9-775454ee3983)


### Requirements:
- `bash.exe` added to your environment variables
- Generated SSH keys. If you don't have them, run: `ssh-keygen`
