r"""# github\_inventory
A bit of a meta-project on creating a nicer index of my github repositories. Partially motivated because I'm too greedy to do with only 6 pinned repositories. It's just about stable enough to function. It features several sub-utilities I chain together, including directory-searching and API-json reading. It files my projects under subcategories, and concatenates together readmes under a category heading.
"""

import sys

sys.stdout.write(__doc__)

out = []
toc = []

for line in sys.stdin:
    if line.strip():
        if line.startswith("#"):
            out.append("#{}".format(line))
            toc.append("1. [{}](#{})\n".format(line[2:-1], line[2:-1].lower().replace(" ", "-")))
        else:
            rep_dir, rep_name, rep_url, rep_desc = line.strip().split("\t")
            with open(rep_dir + "README.md", "r") as rep_file:
                for r_line in rep_file:
                    if r_line.startswith("#"):
                        out.append("### [{}]({})\n".format(r_line[2:-1], rep_url))
                        toc.append("    1. [{}](#{})\n".format(r_line[2:-1], r_line[2:-1].lower().replace(" ", "-")))
                    else:
                        out.append(r_line)

sys.stdout.writelines(toc)
sys.stdout.writelines(out)
