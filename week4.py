def read_file_safely():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print(f" Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

# Run the function
read_file_safely()