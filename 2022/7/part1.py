def main(input):
    folder_tree = get_folder_tree(input)
    import json
    
    print(json.dumps(folder_tree, indent=4))

    possible_folders = {folder:content["folder_size"] for folder, content in folder_tree.items() if content["folder_size"] <= 100000}


    print(json.dumps(possible_folders, indent=4))
    return sum(possible_folders.values())

def get_folder_tree(input):
    current_folder = "/"
    folder_tree = {"/": {"files":{}, "folder_size":0, "folders":[]}}

    size = 0
    if input.startswith("$ "):
        input = input[2:]
    for line in input.split("\n$ "):
        if line == "":
            continue
        command, args = line[:2], line[3:]
        if command == "cd":
            cd = args
            if cd == "..":
                current_folder = "/".join(current_folder.split("/")[:-1])
            elif cd.startswith("/"):
                current_folder = cd
            else:
                if current_folder == "/":
                    current_folder = ""
                current_folder += "/" + cd
                folder_tree[current_folder] = {"files":{}, "folders":[], "folder_size":0}
                print(f"folder_tree: {folder_tree}")

        elif command == "ls":
            folder_content = args.split("\n")
            files, folders = get_files_and_folders_in_folder(folder_content)
            folder_tree[current_folder]["files"] = files
            folder_tree[current_folder]["folders"] = folders
            size = sum(files.values())
            add_content_to_folder(current_folder, size, folder_tree)
            #print(f"folder: {current_folder}, size: {size}, folder_sizes: {folder_sizes}")
        else:
            raise Exception(f"unknown line: '{line}', command: '{command}'")
    
    folder_tree = dict(sorted(folder_tree.items()))
    return folder_tree

def add_content_to_folder(folder_path, size, folder_tree):
    temp_path = folder_path
    # Update all parent directories
    if temp_path not in folder_tree:
        folder_tree[temp_path] = {"files":{}, "folder_size":0}
    while temp_path != "":
        folder_tree[temp_path]["folder_size"] += size
        temp_path = temp_path[:temp_path.rindex("/")]

def get_parent_folders(path):
    return ["/".join(path.split("/")[:i]) 
            if "/".join(path.split("/")[:i]) != "" 
            else "/"
            for i in range(1, len(path.split("/")))]


def get_files_and_folders_in_folder(folder_content):
    files = {}
    folders = []
    for item in folder_content:
        if item == "":
            continue
        file_size, name = item.split(" ")
        if file_size.isnumeric():
            files[name] = int(file_size)
        else:
            folders.append(name)
    return files, folders

if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
