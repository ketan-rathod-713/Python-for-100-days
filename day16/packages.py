# TO use the code of the other programmers
# until now we have only seen module

# TO install any package go here and first search
# https://pypi.org/
# https://pypi.org/project/prettytable/
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

# first need to install packages , Go in setting -> project -> python interpreter -> and then install python package by searching it

# here we have installed pretty table so now let's use it

from prettytable import PrettyTable

table = PrettyTable()
print(table)

print(table.align)
table.align='l'

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])

# OR Below one

# table.add_column("Main",["just","great"])
# table.add_column("Main",["just","great"])

print(table)

# For all this things to work and understand properly read the documentation clearly with full understandigs