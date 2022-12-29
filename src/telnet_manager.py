import logging
from typing import Union
from telnetlib import Telnet

logger = logging.getLogger(__name__)


class TelnetManager:

    @staticmethod
    def enumeration(host: str, port: int, logins: list,
                    passwords: list, failed_text: str) -> (Union[str, None], Union[str, None]):
        correct_login = None
        correct_password = None

        logger.info("Start bruteforce")

        for login in logins:
            for password in passwords:
                telnet_client = Telnet(host, port)

                telnet_client.read_until(b"Username")
                telnet_client.write(login.encode('ascii'))
                telnet_client.read_until(b"Password")
                telnet_client.write(password.encode('ascii'))

                index = telnet_client.expect([failed_text.encode('utf-8'), b"#"], 1)[0]

                format_login = login.replace("\n", "")
                format_password = password.replace("\n", "")

                if index != 0:
                    correct_login = format_login
                    correct_password = format_password
                    logger.info(f'Login: [{format_login}] '
                                f'Password: [{format_password}] '
                                f'are successful')
                    break
                else:
                    logger.error(f'Login: [{format_login}] '
                                 f'Password: [{format_password}] '
                                 f'are unsuccessful')

        return correct_login, correct_password
