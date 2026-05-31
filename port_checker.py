import socket

def check_port(host, port):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  # timeout for faster response

            # Try connecting to the host and port
            result = s.connect_ex((host, port))

            if result == 0:
                print(f"[OPEN] Port {port} is OPEN on {host}")
            else:
                print(f"[CLOSED] Port {port} is CLOSED on {host}")

    except socket.gaierror:
        print("Error: Invalid host address.")
    except ValueError:
        print("Error: Invalid port number.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    print("=== Port Status Checker ===")

    host = input("Enter host (e.g., 127.0.0.1 or google.com): ").strip()

    try:
        port = int(input("Enter port number: ").strip())

        if port < 1 or port > 65535:
            print("Port must be between 1 and 65535.")
            return

        check_port(host, port)

    except ValueError:
        print("Please enter a valid numeric port number.")


if __name__ == "__main__":
    main()
