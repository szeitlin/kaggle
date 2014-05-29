import pandas

def add_full_name(path_to_csv, path_to_new_csv):

    baseball_data = pandas.read_csv("Master.csv")

    baseball_data['nameFull'] = baseball_data['nameFirst'] + " " + baseball_data['nameLast']

#    baseball_new = baseball_data + nameFull
#apparently don't need this, it seems to overwrite the original

    baseball_new.to_csv("test_sz.csv")

#apparently don't need to call pandas again explicitly
