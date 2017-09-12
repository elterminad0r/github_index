r"""# github\_inventory
A bit of a meta-project on creating a nicer index of my github repositories. Partially motivated because I'm too greedy to do with only 6 pinned repositories. It's just about stable enough to function (on my personal convention for my repositories). It features several sub-utilities I chain together, including directory-searching and API-json reading. It files my projects under subcategories, and concatenates together readmes under a category heading. It was also about familiarising myself with Markdown (generating headers, normalising header names in links to contents, tables etc). It features just about the right combination of absolute and relative links that the readme source is in-place stable. Now featuring disgusting links at the start of each header to jump back to the table of contents - I'm not a web designer leave me alone.
"""

import sys
import re

sys.stdout.write(__doc__)

out = []
toc = ["## Table of Contents\n"]

toclink = r"[\[toc\]](#table-of-contents)"

for line in sys.stdin:
    if line.strip():
        if line.startswith("#"):
            out.append(re.sub(r"^(#*) (.*)$", r"\1 {} \2".format(toclink), line))
            toc.append("- [{}](#toc-{})\n".format(line[2:-1], line[2:-1].lower().replace(" ", "-")))
        else:
            rep_dir, rep_name, rep_url, rep_desc = line.strip().split("\t")
            with open(rep_dir + "README.md", "r") as rep_file:
                for r_line in rep_file:
                    if r_line.startswith("#"):
                        out.append("### {} [{}]({})\n".format(toclink, r_line[2:-1], rep_url))
                        toc.append("    - [{}](#toc-{})\n".format(r_line[2:-1], r_line[2:-1].lower().replace(" ", "-")))
                    else:
                        out.append(r_line)

sys.stdout.writelines(toc)
sys.stdout.writelines(out)
