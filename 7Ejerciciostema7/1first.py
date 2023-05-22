str = "X-DSPAM-Confidence:0.8475"

search = str.find(":")

extraction = str[search + 1:]

extraction = float(extraction)

print(extraction)