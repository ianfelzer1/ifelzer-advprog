i = 0
permission_granted = False

first = raw_input("Do you want to continue y/n: ")
if first == "y":
    i -= 1
    permission_granted = True
else:
    raise SystemExit

if (permission_granted == True):
    get_address = raw_input("What is your address ;) ")
