from colorama import Fore, Back, Style

rows = 35
columns = 20000
columnsAtATime = 150
shift = 0.15
beam_length = 7
base_display_background = Back.BLACK
base_display = base_display_background + ' ' + Style.RESET_ALL
border_display = Back.MAGENTA + ' ' + Style.RESET_ALL
mando_display = Back.RED + ' ' + Style.RESET_ALL

angles = [[1, 0], [1, 1], [0, 1], [-1, 1]]
