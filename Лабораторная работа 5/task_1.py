from pprint import pprint


dict_ = [{'bin': bin(num), 'dec': num, 'oct': oct(num), 'hex': hex(num)} for num in range(16)]
pprint(dict_)
