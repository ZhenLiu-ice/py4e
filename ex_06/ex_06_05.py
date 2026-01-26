text = "X-DSPAM-Confidence:    0.8475"
idx = text.find("0")
number = float(text[idx:])
print(number)
