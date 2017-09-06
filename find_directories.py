import glob
import sys

for line in sys.stdin:
    name = line.split("\t")[0]
    print(name)
    name_dir, = glob.iglob("/home/izaak/programmeren/**/{}/".format(name), recursive=True)
    sys.stdout.write("{}\t{}".format(name_dir, line))
