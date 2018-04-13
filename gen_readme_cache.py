import re
import os.path

def get_expected_dirs():
    lookup = {}

    with open("dir_repos.txt", "r") as dir_repos:
        for line in dir_repos:
            if line.strip() and not line.startswith("#"):
                a, b = line.strip().split("\t")
                lookup[b] = a

    return lookup

github_lu = get_expected_dirs()

def parse_readmeline(line):
    return re.match(r"###.*toc.*table-of-contents.*\[(.*)\]\((.*)\).*", line)

def readme_sections(readme_file):
    for line in readme_file:
        re_match = parse_readmeline(line)
        if re_match:
            break

    file_end = False
    while not file_end:
        while not re_match:
            re_match = parse_readmeline(readme_file.readline())

        rp_lines = []
        prevname = re_match.group(1).replace("\\", "")
        url = re_match.group(2)
        for line in readme_file:
            re_match = parse_readmeline(line)
            if re_match:
                break
            elif line.startswith("#"):
                break
            else:
                rp_lines.append(line)
        else:
            file_end = True

        des_file = "{}/README.md".format(github_lu[url])

        print("selected {}".format(des_file))

        os.makedirs(os.path.dirname(des_file), exist_ok=True)

        with open(des_file, "w") as cachefile:
            cachefile.write("# {}\n".format(prevname.replace("_", r"\_")))
            cachefile.write("".join(rp_lines))

with open("README.md", "r") as readme_file:
    readme_sections(readme_file)
