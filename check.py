from colorama import Fore, Back, Style
print(Fore.RED + 'some red text' + Style.RESET_ALL)
print(Back.BLUE + ' ' + Style.RESET_ALL)
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
