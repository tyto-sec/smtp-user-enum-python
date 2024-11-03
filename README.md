# SMTP User Enumeration Script

## Description

This Bash script is used to perform user enumeration on SMTP servers using the `VRFY` command. It checks if the SMTP server supports the `VRFY` command and, if so, attempts to verify the existence of users provided through a user list file.

**Written by**: tyto

## Usage

```bash
./smtp_enum.py <host> <port> <user_list_file> [-v]
```

- `<host>`: IP address or hostname of the target SMTP server.
- `<port>`: SMTP server port (default `25`).
- `<user_list_file>`: Path to the file containing the list of usernames to test, one per line.
- `-v` (optional): Verbose mode, displays additional details during execution.

### Example Usage

```bash
python smtp_enum.py 192.168.0.2 25 wordlists/users.txt -v
```

This command attempts to enumerate users listed in the `wordlists/users.txt` file on the SMTP server located at `192.168.0.2` on port `25`, with verbose output enabled.

## Security Notes

- This script is intended for educational and ethical pentesting purposes. Make sure you have permission to perform this type of test on the target SMTP server.
- Unauthorized use of this script may violate security policies and local laws.

