from pretty_tables import PrettyTables
from prettytable import PrettyTable

headers = ['ID', 'Name', 'Occupation', 'Employed']
rows = [
    [1, 'Justin', 'Software Engineer', True],
    [2, 'Misty', 'Receptionist', False],
    [3, 'John', None, False],
]

round_table = PrettyTables.generate_table(
    headers=headers,
    rows=rows,
    empty_cell_placeholder='No data'
)
print(round_table)

square_table = PrettyTable()
square_table.add_column("Pokemon name", ["Pikachu", "Charizard", "Squirtle"])
square_table.add_column("Type", ["Electric", "Fire", "Water"])
square_table.align = "l"


print(square_table)