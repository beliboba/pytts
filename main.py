from pathlib import Path
from gtts import gTTS
from rich import print
from rich.panel import Panel
import os

supported_exts = ["txt", "pdf"]
supported_langs = ["ru", "en"]


def myprint(text:str):
	print(Panel.fit(text))


def main():
	myprint("[blue]Укажите путь к файлу[/blue]")
	filepath = input().strip()
	if Path(filepath).is_file and Path(filepath).exists():
		pass
	else:
		myprint("[red]Неверный путь. Проверьте правильность ввода[/red]")
		os.abort()
	myprint("[blue]Введите один из следующих языков: \n1. [green]ru[/green] - Русский \n2. [green]en[/green] - English[/blue]")
	langcode = input().strip()
	if langcode not in supported_langs:
		myprint(f"Такой язык в программе не поддерживается. \nПоддерживаются: {supported_langs}")
	if os.path.splitext(filepath)[1][1:] not in supported_exts:
		myprint(f"Файлы с расширением {os.path.splitext(filepath)[1][1:]} не поддерживаются. \nПоддерживаются: {supported_exts}")
		os.abort()
	if os.path.splitext(filepath)[1][1:] == "txt":
		file = open(filepath, 'r+', encoding='utf8').read()
		print(file)
		audio = gTTS(text=file, lang=langcode)
		myprint("Напишите название файла")
		outname = input()
		audio.save(savefile=f"{outname}.mp3")


if __name__ == "__main__":
	main()
