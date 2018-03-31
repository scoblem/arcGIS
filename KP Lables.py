#1km KP markers (1:100,000 - <none>)
def FindLabel ( [KP] ):
  return ("KP "+ [KP])

#10km KP markers (1:500,000 - 1:125,000)
def FindLabel ( [KP] ):
    if int(([KP])) % 10 == 0: return ("KP " + [KP])

#50km KP markers (1:2,000,000 - 1:600,000)
def FindLabel ( [KP] ):
    if int(([KP])) % 50 == 0: return ("KP " + [KP])

#100km KP markers inc sol / eol (<none> - 1:2,500,000)
def FindLabel ( [KP] ):
    if int(([KP])) % 100 == 0 or int(([KP])) in [0, 622]: return ("KP " + [KP])
