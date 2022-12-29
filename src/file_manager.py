from typing import Union
from pathlib import Path


class FileManager:
    @staticmethod
    def get_logins(file_logins: Union[str, Path]) -> list:
        with open(Path(file_logins), 'r') as file:
            logins = [f'{login.strip()}\n' for login in file.readlines()]

        return logins

    @staticmethod
    def get_passwords(file_passwords: Union[str, Path]) -> list:
        with open(Path(file_passwords), 'r') as file:
            passwords = [f'{password.strip()}\n' for password in file.readlines()]

        return passwords
