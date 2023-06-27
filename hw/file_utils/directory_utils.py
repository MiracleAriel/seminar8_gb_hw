import os
import json
import csv
import pickle

def save_directory_contents(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        parent_dir = os.path.basename(root)
        for filename in files:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            results.append({
                'name': filename,
                'path': file_path,
                'type': 'file',
                'parent': parent_dir,
                'size': file_size
            })

        dir_size = sum(os.path.getsize(os.path.join(root, f)) for f in files)
        for dirname in dirs:
            dir_path = os.path.join(root, dirname)
            dir_size += sum(
                os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, f))
            )
            results.append({
                'name': dirname,
                'path': dir_path,
                'type': 'directory',
                'parent': parent_dir,
                'size': dir_size
            })


    json_file = os.path.join(directory, 'results.json')
    with open(json_file, 'w') as f:
        json.dump(results, f, indent=4)


    csv_file = os.path.join(directory, 'results.csv')
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'path', 'type', 'parent', 'size'])
        writer.writeheader()
        writer.writerows(results)

    pickle_file = os.path.join(directory, 'results.pickle')
    with open(pickle_file, 'wb') as f:
        pickle.dump(results, f)

    print("Results saved successfully!")
