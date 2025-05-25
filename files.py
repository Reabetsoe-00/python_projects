def read_and_modify_file():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        modified_content = content.upper()
        output_filename = "modified_" + input_filename

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_modify_file()
