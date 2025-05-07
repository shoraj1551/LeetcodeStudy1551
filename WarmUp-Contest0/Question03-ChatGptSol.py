class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}  # depth -> current total length at that depth

        for line in input.split('\n'):
            depth = line.count('\t')  # level of nesting
            name = line.lstrip('\t')  # actual name of file or directory

            # If it's a file, calculate full path length
            if '.' in name:
                full_len = path_len[depth] + len(name)
                max_len = max(max_len, full_len)
            else:
                # If it's a dir, store path length for the next depth
                # +1 for the '/' that will be added when joined
                path_len[depth + 1] = path_len[depth] + len(name) + 1

        return max_len
