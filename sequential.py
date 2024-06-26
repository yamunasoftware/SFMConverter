import os

def execute_python_file(file_path, input, output):
  try:
    os.system(f'python3 {file_path} {input} {output}')
  except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")

def run():
  files = os.listdir()
  completed = os.listdir('out/')

  for file in files:
    if '.json' in file and file not in completed:
      execute_python_file('sfm_converter.py', file, 'out/' + file)
      execute_python_file('sfm_collection_converter.py', file, 'collections/collection-' + file)

run()