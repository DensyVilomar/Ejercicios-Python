str = 'X-DSPAM-Confidence:0.8475'

search = str.find(":")

extration = str[search + 1:]

extration = float(extration)

print(extration)