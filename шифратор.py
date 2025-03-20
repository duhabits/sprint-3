class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def process_text(self, text: str, shift: int, is_encrypt: bool):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
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


cipher_master = CipherMaster()
print(
    cipher_master.process_text(
        text="Саня, сосал ?",
        shift=2,
        is_encrypt=True,
    )
)
print(
    cipher_master.process_text(
        text="Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ",
        shift=-3,
        is_encrypt=False,
    )
)
