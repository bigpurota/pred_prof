def first_file_read(file):
    """
    возвращает список списков в которыз лежат данные о ноутбуку
    file :анализируемый файл
    """
    devices = []
    with open(file) as f:
        for i in f.readlines():
            e = tuple(i[:-2].split("*"))
            devices.append(e)
        devices = devices[1:]
        return tuple(devices)
def ram_counter(file : str):
    """
    взвращаеаеь словарей словарей где ключев перого словаря является тип ноутбука а второго количество оперативной памяти а значение кол-во таких ноутбуков
    file :анализируемый файл
    """
    notebook_ram= {}
    devices = []
    for e in first_file_read(file):
        devices.append((e[2], e[5]))
    for i in devices:
        e = i[0]
        notebook_ram[e] = {}
    for i in devices:
        notebook_ram[i[0]][i[1]] = 0
    for i in devices:
        notebook_ram[i[0]][i[1]] += 1
    return notebook_ram
def output_notebook(out ,need, out_file_name):

    with open(out_file_name, "w") as f:
        for i in out.keys():
            if i in need:
                f.write(f'{i}\n')
                for j in out[i].keys():
                    f.write(f"{j} {out[i][j]}\n")


output_notebook(ram_counter("devices.txt"),("Ultrabook", "Notebook", "Netbook"), "count_company.txt")