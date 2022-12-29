<h1 align="center">
Telnet Bruteforce Script
</h1>

**Скрипт для подбора логина и пароля по протоколу telnet.**

Исполняемый файл: ./hack.py \
Флаги: \
_**--target_host**_ - Target Host (required: True)\
_**--target_port**_ - Target Port (required: True)\
_**--file_logins**_ - File logins (required: True)\
_**--file_passwords**_ - File passwords (required: True)\
_**--failed_text**_ - Text Failure (required: False, default: 'Invalid.')

Example:
```shell
python ./hack.py --target_host localhost --target_port 23 --file_logins ./logins.txt --file_passwords ./passwords.txt
```

_____________________________
## Контакты:
### Username: Baykanurov
### E-mail: vefimov@rvision.ru