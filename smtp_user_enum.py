#!/usr/bin/python3

import socket
import sys
import argparse

def check_vrfy_support(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((host, port))
            server.recv(1024) 
            
            server.sendall(b"EHLO scanner.localdomain\r\n")
            response = server.recv(1024).decode()
            
            server.sendall(b"QUIT\r\n")

        return "VRFY" in response
    
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        sys.exit(1)

def enumerate_users(host, user_list, port=25, verbose=False):
    try:
        for user in user_list:
            if verbose:
                print(f"Testing user: {user}")

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.connect((host, port))
                server.recv(1024) 
                
                server.sendall(f"VRFY {user}\r\n".encode())
                response = server.recv(1024).decode()
                
                server.sendall(b"QUIT\r\n")

                if response.startswith("252"):
                    print(f" - User found: {user}")

    except Exception as e:
        print(f"Error during enumeration: {e}")

def main():
    parser = argparse.ArgumentParser(description="SMTP User Enumeration Script")
    parser.add_argument("host", type=str, help="IP address or hostname of the SMTP server")
    parser.add_argument("port", type=int, default=25, help="Port number of the SMTP server (default 25)")
    parser.add_argument("user_list_file", type=str, help="File containing a list of usernames")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    try:

        with open(args.user_list_file, 'r') as f:
            user_list = [line.strip() for line in f.readlines()]

        if check_vrfy_support(args.host, args.port):
            enumerate_users(host=args.host, port=args.port, user_list=user_list, verbose=args.verbose)
        else:
            print("VRFY command is not supported")

    except FileNotFoundError:
        print(f"User list file '{args.user_list_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()