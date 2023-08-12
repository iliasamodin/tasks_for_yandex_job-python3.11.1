# Function for calculating the bit depth 
#   (number of transitions between rows) 
#   of the keyboard for typing the specified text
def number_of_transitions_by_rows_calculation(
    key_indices, 
    row_list_for_keys, 
    keystroke_indices
):

    # Formation of a dictionary in which the row of the key location 
    #   corresponds to the index of this key
    row_for_indices = dict(zip(key_indices, row_list_for_keys))

    # Counting the number of transitions between rows 
    #   for typing source text
    number_of_transitions_by_rows = 0
    previous_row = row_for_indices[keystroke_indices[0]]
    for keystroke_index in keystroke_indices:
        row_for_keystroke = row_for_indices[keystroke_index]
        number_of_transitions_by_rows += row_for_keystroke != previous_row 
        previous_row = row_for_keystroke

    return number_of_transitions_by_rows


if __name__ == "__main__":
    with open("input.txt") as input_file:
        _, key_indices, row_list_for_keys, _, keystroke_indices = \
            [line.strip().split(" ") for line in input_file]

        number_of_transitions_by_rows = \
        number_of_transitions_by_rows_calculation(
            key_indices, 
            row_list_for_keys, 
            keystroke_indices
        )

    with open("output.txt", "w") as output_file:
        print(number_of_transitions_by_rows, file=output_file)