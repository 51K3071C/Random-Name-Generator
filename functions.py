from random import randint
def names_only(file, new_file, index, gender = "none"):
  """Reads from a csv file, finds the names at a specific indexl, and creates a text file with one name per line."""
  with open(file, "r") as names:
    info_dump = list(names)
    names_only_list = []
    for i in range(1, len(info_dump)):
      line = info_dump[i].split(",")
      name = line[index]
      g = line[3][1:-2]
      if gender == "none": 
        if name[0] == "\"":
          name = name[1:-1]
          if name not in names_only_list:
            names_only_list.append(name)
        else:
          names_only_list.append(name)
      elif gender == "boy" and g == "boy":
        if name[0] == "\"":
          name = name[1:-1]
          if name not in names_only_list:
            names_only_list.append(name)
        else:
          names_only_list.append(name)
      elif gender == "girl" and g == "girl":
        if name[0] == "\"":
          name = name[1:-1]
          if name not in names_only_list:
            names_only_list.append(name)
        else:
          names_only_list.append(name)
  with open(new_file, "w+") as names:
    for name in names_only_list:
      if name != names_only_list[-1]:
        names.write(f"{name}")
      else:
        names.write(name)
    print("Names copied to file")


def random_name_generator(names):
  boy_list = []
  girl_list = []
  last_list = []
  random_names = [["gender", "first_name", "last_name", "full_name"]]
  for i in range(len(names)):
    with open(names[i], "r") as bn:
      info_dump = list(bn)
    for name in info_dump:
      if "\n" in name:
        name = name[:-1]
        if i == 0:
          boy_list.append(name)
        elif i == 1:
          girl_list.append(name)
        else:
          last_list.append(name)
  b_max, g_max, l_max = len(boy_list), len(girl_list), len(last_list)
  gender = ["male", "female"]
  for i in range(1000):
    
    b_name = boy_list[randint(0, b_max-1)].upper()
    g_name = girl_list[randint(0, g_max-1)].upper()
    l_name = last_list[randint(0, l_max-1)]
   
    if i % 2 == 0:
      f_name = b_name + " " + l_name
      boy = [gender[0], b_name, l_name, f_name]
      random_names.append(boy)
    else:
      f_name = g_name + " " + l_name
      girl = [gender[1], g_name, l_name, f_name]
      random_names.append(girl)
  random_names_str = [", ".join(ele) for ele in random_names]
  # create random_names.csv' and add random_names to the file
  with open("random_names.csv", "w+") as b:
    for i in random_names_str:
      b.write(f"{i}\n")
    print("File Created")