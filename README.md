## A CLI for Quickly Connecting to Your Saved Servers

## Список команд
- ls - Отображает все сохраненные сервера
- add - Добавляет новый сервер. После добавления применяет к нему `ssh-copy-id`
- del - Удаляет сервер
- {server_name} - Подключает к серверу. Можно использовать, в качестве аргумента, во времяя запуска скрипта, в таком случае автоматически сработает эта команда, например `memhost main`

![image](https://github.com/user-attachments/assets/7c81eb31-646a-4c85-91a9-775454ee3983)


### Requirements:
- `bash.exe` added to your environment variables
- Generated SSH keys. If you don't have them, run: `ssh-keygen`
