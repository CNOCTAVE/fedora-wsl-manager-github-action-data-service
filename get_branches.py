import subprocess
import os
import fnmatch
import json

def find_first_tar_file(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if fnmatch.fnmatch(filename, '*.tar'):
                return os.path.join(root, filename)
    return None

def main():
    try:
        output = subprocess.check_output(['git', 'branch', '-a'], stderr=subprocess.STDOUT, text=True)
        print(f"Git branches:\n{output}\n")
        output_list = output.replace('-> origin/master', '').strip().split('\n')
        print(f"Git branch list:\n{output_list}\n")
        branch_list = list()
        for line in output_list:
            branch_list.append(line.split('/')[-1])
        with open('../branch_list.txt', 'w', encoding='utf-8') as f:
            f.writelines(branch_list)
        print(f"Git branch list:\n{branch_list}\n")
        docker_brew_fedora_list = list()
        for branch in branch_list:
            try:
                output = subprocess.check_output(['git', 'checkout', branch], stderr=subprocess.STDOUT, text=True)
                docker_brew_fedora = find_first_tar_file('./x86_64')
                docker_brew_fedora_list.append({'branch': branch, 'docker_brew_fedora': docker_brew_fedora})
            except subprocess.CalledProcessError as e:
                print(f"Cannot get docker_brew_fedora, skip: {e.output}")
        print(f"Docker brew fedora list:\n{docker_brew_fedora_list}\n")
        json.dump(docker_brew_fedora_list, open('../docker_brew_fedora_list.json', 'w'), indent=4)
            
    except subprocess.CalledProcessError as e:
        print(f"Cannot get git branch: {e.output}")

if __name__ == '__main__':
    main()