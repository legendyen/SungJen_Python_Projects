# Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0
for lx in fh:
    if not lx.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        pos = lx.find(":")
        slc = lx[pos+1:].strip()
        f_slc = float(slc)
        total = total + f_slc

print("Average spam confidence:", total/count)