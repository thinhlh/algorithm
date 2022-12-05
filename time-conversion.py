# Solved
def time_conversion(s: str):
    pm_or_am = s[-2:]
    [h, m, sec] = s[:-2].split(':')

    if pm_or_am == 'PM':
        h = str(int(h) if int(h) >= 12 else int(h) + 12).zfill(2)
        pass
    else:
        h = str(int(h)-12 if int(h) >= 12 else int(h)).zfill(2)

    return ':'.join([h, m, sec])


print(time_conversion('12:45:54PM'))
