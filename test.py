from answers import answers_from

otvet = answers_from(['Да'])

print(otvet[17:otvet.find('\n')])
otvet = otvet[otvet.find('\n'):]
otvet = otvet.replace('\n', '')
print(otvet[16:])