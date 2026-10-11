def main():
    file_name = input("File name: ").strip().lower().rsplit(".", 1)

    print(determine_mime(file_name))

def determine_mime(name):
    if len(name) < 2:
        return "application/octet-stream"

    match name[1]:
        case "gif":
            return "image/gif"
        case "jpg":
            return "image/jpeg"
        case "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()
