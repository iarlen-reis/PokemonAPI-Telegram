from pathlib import Path


class CreateImage:
    @staticmethod
    def create_image(image):
        file_image = Path('pokemon.png')
        try:
            if file_image.exists:
                file_image.unlink()

        except:
            file_image.touch()

        with open('pokemon.png', 'wb') as file:
            file.write(image)

        return file
