import pickle

def load_pickle(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def save_pickle(file_path, data):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)
