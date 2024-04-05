import os

def execute_python_file(file_path, input, output):
  try:
    os.system(f'python {file_path} {input} {output}')
  except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")

def run():
  files = os.listdir()
  for file in files:
    if '.json' in file:
      execute_python_file('sfm_converter.py', file, 'out/' + file)
      execute_python_file('sfm_collection_converter.py', file, 'out/collection-' + file)

run()