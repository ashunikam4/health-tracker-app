def input_positive(x):
    """ Keep asking till positive numeric input. """
    res = 0
    while res <= 0:
        try:
            res = float(input('Enter your {}: '.format(x)))
        except ValueError:
            print('Please enter a valid {}'.format(x))
    return res

def parse_to_hours(time_str):
    """ 'HH:MM:SS' ->  hours(float) """
    time = time_str.split(':')
    return int(time[0]) + \
            int(time[1]) / 60 + \
            int(time[2]) / 3600

def parse_record(rec):
    """ Parse a workout record from stdin. """
    try:
        rec = rec.split(',')
        return int(rec[0]), float(rec[1]), parse_to_hours(rec[2])
    except Exception as e:
        print('Error encoutered while parsing record : {}'.format(e))
        print('Please refer to docs for record input format')