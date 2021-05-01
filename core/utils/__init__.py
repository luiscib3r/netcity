import base64


def load_image(file_path: str) -> str:
    with open(file_path, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read())

        return base64_string
