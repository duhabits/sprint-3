class CipherMaster:

    def __init__(self, alp):
        self.alphabet = alp

    def process_text(self, text: str, shift: int, is_encrypt: bool):
        """Метод шифратора

        Args:
            text (str): начавльная строка
            shift (int): код
            is_encrypt (bool): шиф/дешиф

        Returns:
            _type_: None
        """
        if is_encrypt is False:
            shift = -shift
        alfavit = self.alphabet
        text = text.lower()
        result = []
        for letter in text:
            if letter not in alfavit:
                result.append(letter)
            else:
                nummber_bukvs = alfavit.find(letter)
                if (len(alfavit[:nummber_bukvs]) + shift) < len(alfavit):
                    result.append(alfavit[nummber_bukvs + shift])
                else:
                    defect_num = len(alfavit[:nummber_bukvs]) + shift
                    while defect_num > len(alfavit) - 1:
                        defect_num -= len(alfavit)

                    result.append(alfavit[defect_num])
        return "".join(result)


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

cipher_master = CipherMaster(alp=alphabet)
print(
    cipher_master.process_text(
        text="Саня, сосал ?",
        shift=2,
        is_encrypt=True,
    )
)
print(
    cipher_master.process_text(
        text="увпб, урувн ?",
        shift=2,
        is_encrypt=False,
    )
)
