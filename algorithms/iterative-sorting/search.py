def name_in_phonebook(to_find, phonebook):

    for name in phonebook:  #0(size of phonebook) 0(n)
        if name == to_find:
            return True

    return False 

#                    v
# xxxxxxxxxxxxxxxxxxx|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#     0(log n)

# log is answering this question:
    # 2 is the what power == x 
# 65536 elements to process
# 32768
# 16384
# 8192
# 4096
# 2048
# 1024
# 515
# 256
# 128
# 64
# 32
# 16
# 8
# 4
# 2
# 1


