class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}  # maps depth to total length at that depth

        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)

            if '.' in name:
                # It's a file
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                # It's a directory
                path_len[depth + 1] = path_len[depth] + len(name) + 1  # add 1 for '/'

        return max_len