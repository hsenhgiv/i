#simple columnar
text=input("enter text : ")
columnkey=input("enter reading column sequence : ")
def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
    order = {int(val): num for num, val in enumerate(key)  }
    ciphertext = ''

    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
          try:
              ciphertext += part[order[index]]
          except IndexError:
              continue
    return ciphertext

print("Encrypted text=",encode(columnkey, text))







