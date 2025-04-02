import os, marshal

file_path = input('Enter Python file path (e.g., src/file.py): ')
if not file_path.endswith('.py'):
    print('Error: Please enter a .py file!')
    exit()

try:
    with open(file_path, 'r') as f:
        file_content = f.read()
except FileNotFoundError:
    print('Error: No such file or directory')
    exit()

encoded_code = marshal.dumps(compile(file_content, '', 'exec'))
output_file = f"{file_path[:-3]}_enc.py"

with open(output_file, 'w') as ofile:
    ofile.write(f'#Telegram: @MrEsfelurm\n\n\nimport marshal\nexec(marshal.loads({repr(encoded_code)}))')

print(f'Success! Encoded file saved as {output_file}')
