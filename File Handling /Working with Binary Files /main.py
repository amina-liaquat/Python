# Copy image using binary mode
with open("image.jpg", "rb") as f1:
    with open("copy.jpg", "wb") as f2:
        f2.write(f1.read())
