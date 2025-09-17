def format_record(rec):
    fio, group, gpa = rec
    if not isinstance(fio, str) or not fio.strip():
        return 'Пустое или нестроковое ФИО'
    if not isinstance(group, str) or not group.strip():
        return 'Пустая или нестроковая группа'
    if not isinstance(gpa, (float, int)):
        return 'GPA должен быть числом'
    
    parts = fio.strip().split()
    parts = [part for part in parts if part]
    if len(parts) < 2:
        return 'ФИО должно содержать хотя бы фамилию и имя'
    LastName = parts[0].capitalize()
    initials = ""
    for i in range(1, min(3, len(parts))):
        initials += parts[i][0].upper() + '.'
    return f'{LastName} {initials}, гр. {group}, GPA {round(float(gpa), 2):.2f}'
tpl = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(tpl))
print(type(format_record(tpl)))