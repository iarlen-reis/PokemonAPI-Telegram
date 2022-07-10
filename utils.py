from pathlib import Path


def list_to_string(list):
    ability = ' '.join(map(str, list))
    return ability


def slipt_message(message):
    context = ''.join(message.text).split(' ')
    final_context = context[1]

    return final_context


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
