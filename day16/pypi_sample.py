# firstly installed prettytable from pypi using terminal. Then, according to the format given by the aurthor of the package. Using it in following.

import prettytable

table = prettytable.PrettyTable()
table.field_names = ["Pokeman name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
print(table)
table.align = "l"
print(table)
