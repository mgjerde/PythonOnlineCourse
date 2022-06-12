import argparse

parser = argparse.ArgumentParser()
parser.add_argument("firstinput")
parser.add_argument("secondinput")
parser.add_argument("thirdinput")

args = parser.parse_args()

print(args.firstinput, args.secondinput,args.thirdinput)