def check_storage():
    statvfs = uos.statvfs("/")
    block_size = statvfs[0]       # File system block size
    total_blocks = statvfs[2]     # Total number of blocks
    free_blocks = statvfs[3]      # Free blocks
    total_size = block_size * total_blocks
    free_size = block_size * free_blocks
    used_size = total_size - free_size
    print(f"Total storage: {total_size / 1024 / 1024:.2f} MB")
    print(f"Used storage: {used_size / 1024 / 1024:.2f} MB")
    print(f"Free storage: {free_size / 1024 / 1024:.2f} MB")

check_storage()