import os
from cryptography.fernet import Fernet
import PySimpleGUI as sg

key = Fernet.generate_key()
cipher_suite = Fernet(key)

layout = [
    [sg.Text('Please enter your password:'), sg.InputText(password_char='*')],
    [sg.Button('Encrypt'), sg.Button('Decode')]]
window = sg.Window('File Encryption', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Encrypt':
        file_path = sg.popup_get_file('Please select the file you want to encrypt.')
        with open(file_path, 'rb') as f:
            data = f.read()
            encrypted_data = cipher_suite.encrypt(data)
        with open(f'{file_path}.encrypted', 'wb') as f:
            f.write(encrypted_data)
        sg.popup(f'{os.path.basename(file_path)} file is encrypted. Encrypted file saved as {os.path.basename(file_path)}.encrypted')
    elif event == 'Decode':
        file_path = sg.popup_get_file('Please select the file you want to decode.')
        with open(file_path, 'rb') as f:
            data = f.read()
            decrypted_data = cipher_suite.decrypt(data)
        with open(f'{os.path.splitext(file_path)[0]}_decrypted{os.path.splitext(file_path)[1]}', 'wb') as f:
            f.write(decrypted_data)
        sg.popup(f'{os.path.basename(file_path)} file has been decoded. Decoded file saved as {os.path.basename(os.path.splitext(file_path)[0])}_decrypted{os.path.splitext(file_path)[1]}')
window.close()
