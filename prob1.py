def sleep_in(weekday,vacation):
	return not weekday or vacation
x = sleep_in(False, True)
print(x)