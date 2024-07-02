user_input = input("File Name: ")

splitted = user_input.split('.')[-1]

lower = splitted.lower().strip()

if lower == "gif":
    print("image/gif")

elif lower == "jpg":
    print("image/jpeg")

elif lower == "jpeg":
    print("image/jpeg")

elif lower == "png":
    print("image/png")

elif lower == "pdf":
    print("application/pdf")

elif lower == "txt":
    print("text/plain")

elif lower == "zip":
    print("application/zip")

else:
    print("application/octet-stream")



