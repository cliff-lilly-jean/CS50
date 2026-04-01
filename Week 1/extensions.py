def main():

    extension = input("File name: ").lower().strip()

    convert_extensions(extension)


def convert_extensions(file_name: str):

    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.endswith("png"):
        print("image/png")
    elif file_name.endswith("pdf"):
        print("application/pdf")
    elif file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".zip"):
        print("application/x-zip-compressed")
    else:
        print("application/octet-stream")

main()