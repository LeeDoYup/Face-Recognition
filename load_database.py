def load_database(path_list, model)
  name_list = []
  for path in path_list:
    name_list.append(path.split('.')[0].split('/')[-1])

  database = {}

  for name, name_path in name_list, path_list:
    database[name] = img_to_encoding(name_path, model)

  return database