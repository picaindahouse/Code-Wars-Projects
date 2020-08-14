class FileNameExtractor:
    def extract_file_name(tom):
        tim = []
        [tim.append(x) for x in tom if tim.count('.') < 2 and x == '_' or '_' in tim and tim.count('.')<2]
        tim.pop(0)
        tim.pop()
        return ''.join(tim)