import os

def run():
  files = os.listdir('out/')
  count = 0
  for file in files:
    with open('out/' + file, 'r') as lines:
      for line in lines:
        count += 1
  print('Total Count: ' + str(count))

run()