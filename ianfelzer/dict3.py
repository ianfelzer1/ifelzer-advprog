dict = {}
dict['1']='1'
dict['2']='2'
dict['3'] = '3'

for key in sorted(dict.keys()):
    print "%s: %s" % (key, dict[key])
