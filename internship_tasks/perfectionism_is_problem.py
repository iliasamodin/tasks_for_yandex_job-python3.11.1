# The function of searching for sculptures 
#   that can be brought to the desired weight 
#   before the allotted time expires
def sculptures_completion_calculation(
    desired_weight,
    remaining_time_in_minutes,
    list_with_weight_of_sculptures
):

    positions_and_weights_of_sculptures = [
        (str(sculpture_position), int(sculpture_weight))
        for sculpture_position, sculpture_weight in enumerate(
            list_with_weight_of_sculptures,
            start=1
        )
    ]
    positions_and_weights_of_sculptures.sort(
        # A comparator that returns the difference between
        #   the sculpture's desired weight and its actual weight
        key=lambda position_and_weight: 
        abs(desired_weight - position_and_weight[1])
    )

    # Iterate through all the sculptures 
    #   sorted in order of how close their weight 
    #   is to the desired weight of the sculpture 
    #   and check if it is possible to process the sculpture 
    #   obtained in the current iteration in the remaining time
    number_of_completed_sculptures = 0
    positions_of_completed_sculptures = []
    for sculpture_position, sculpture_weight in \
    positions_and_weights_of_sculptures:
        weight_of_modification = abs(desired_weight - sculpture_weight)
        if weight_of_modification <= remaining_time_in_minutes:
            number_of_completed_sculptures += 1
            positions_of_completed_sculptures.append(sculpture_position)
            remaining_time_in_minutes -= weight_of_modification
        else:
            break

    return number_of_completed_sculptures, positions_of_completed_sculptures


if __name__ == "__main__":
    with open("input.txt") as input_file:
        situation_data, list_with_weight_of_sculptures = input_file.readlines()

    _, desired_weight, remaining_time_in_minutes = [
        int(aspect_of_situation)
        for aspect_of_situation in situation_data.strip().split(" ")
    ]
    list_with_weight_of_sculptures = \
        list_with_weight_of_sculptures.strip().split(" ")

    number_of_completed_sculptures, positions_of_completed_sculptures = \
        sculptures_completion_calculation(
            desired_weight,
            remaining_time_in_minutes,
            list_with_weight_of_sculptures
        )
    positions_of_completed_sculptures = \
        " ".join(positions_of_completed_sculptures)

    with open("output.txt", "w") as output_file:
        print(
            number_of_completed_sculptures, 
            positions_of_completed_sculptures,
            sep="\n",
            file=output_file
        )