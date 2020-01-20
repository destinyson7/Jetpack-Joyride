from colorama import Fore, Back, Style

rows = 35
columns = 20000
columnsAtATime = 150
shift = 0.08
beam_length = 7
base_display = Back.BLACK + ' ' + Style.RESET_ALL
border_display = Back.MAGENTA + ' ' + Style.RESET_ALL
mando_display = Back.RED + ' ' + Style.RESET_ALL
angles = [[1, 0], [1, 1], [0, 1], [1, -1]]
beam_end = Back.YELLOW + ' ' + Style.RESET_ALL
boost_display = Back.BLACK + '>' + Style.RESET_ALL
boost_length = 200
shield_length = 100
shield_cooloff = 600
bullet_display = Fore.RED + 'O' + Style.RESET_ALL
