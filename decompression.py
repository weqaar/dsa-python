class DecompressionProgram:
    def __init__(self):
        self.index = 0
        self.input_string = ""

    def _parse_recursive(self) -> str:
        """
        Recursively parses a segment of the input string.
        A segment can contain letters or k[substring_segment] blocks.
        This function is called to parse the content inside brackets
        or the entire string if it's the outermost call.
        It stops when it encounters a closing bracket ']' (if parsing an inner segment)
        or at the end of the string.
        """
        result_parts = []
        
        while self.index < len(self.input_string):
            current_char = self.input_string[self.index]

            if current_char.isalpha():
                result_parts.append(current_char)
                self.index += 1
            elif current_char.isdigit():
                # Parse the number (k)
                num_start_index = self.index
                while self.index < len(self.input_string) and self.input_string[self.index].isdigit():
                    self.index += 1
                k = int(self.input_string[num_start_index:self.index])

                # Expect and skip '['
                # According to the problem, input is always valid.
                if self.index >= len(self.input_string) or self.input_string[self.index] != '[':
                    # This case should not be reached with valid input.
                    # Handling for robustness or to indicate a misunderstanding of "valid input".
                    raise ValueError(f"Expected '[' after number at index {self.index-1}")
                self.index += 1  # Skip '['

                # Recursively parse the segment to be repeated
                repeated_segment_str = self._parse_recursive()
                
                # Expect and skip ']' for the current repetition block
                if self.index >= len(self.input_string) or self.input_string[self.index] != ']':
                    # This case should not be reached with valid input.
                    raise ValueError(f"Expected ']' to close segment at index {self.index-1}")
                self.index += 1  # Skip ']'

                result_parts.append(repeated_segment_str * k)
            elif current_char == ']':
                # This ']' belongs to an outer scope, so stop parsing for the current segment.
                # The caller that opened the bracket will consume this ']'.
                break 
            else:
                # Should not happen with the defined valid characters (digits, letters, brackets)
                # and valid structure.
                raise ValueError(f"Unexpected character '{current_char}' at index {self.index}")
                
        return "".join(result_parts)

    def decompress(self, s: str) -> str:
        """
        Decompresses a string according to the specified rules.
        Example: "3[abc]4[ab]c" -> "abcabcabcababababc"
        """
        if not s:
            return ""
            
        self.input_string = s
        self.index = 0
        return self._parse_recursive()

if __name__ == '__main__':
    program = DecompressionProgram()

    test_cases = {
        "3[abc]4[ab]c": "abcabcabcababababc",
        "2[3[a]b]": "aaabaaab",
        "10[a]": "aaaaaaaaaa",
        "abc": "abc",
        "": "",
        "1[a]1[b]1[c]": "abc",
        "2[a2[b]]": "abbabb" # a + bb, repeated twice
    }

    for compressed, expected in test_cases.items():
        decompressed = program.decompress(compressed)
        print(f"Input: \"{compressed}\"")
        print(f"Output: \"{decompressed}\"")
        print(f"Expected: \"{expected}\"")
        print(f"Matches expected: {decompressed == expected}")
        print("-" * 20)

