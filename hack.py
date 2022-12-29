import logging
from pathlib import Path
from src import (
    args,
    file_manager,
    telnet_manager
)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-4s - %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S"
)


if __name__ == "__main__":
    logins = file_manager.get_logins(Path(args.file_logins))
    passwords = file_manager.get_passwords(Path(args.file_passwords))
    correct_login, correct_password = telnet_manager.enumeration(
        host=args.target_host,
        port=int(args.target_port),
        logins=logins,
        passwords=passwords,
        failed_text=args.failed_text
    )
    if correct_login and correct_password:
        print(f"Успешно!\nЛогин: {correct_login}\nПароль: {correct_password}")
    else:
        print(f"Неуспешно!")





