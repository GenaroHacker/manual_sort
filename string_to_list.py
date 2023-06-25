
def string_to_list(string):
    string = string.split('\n')
    string = [line.strip() for line in string if line.strip()]
    return string
