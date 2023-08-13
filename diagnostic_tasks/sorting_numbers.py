import requests


# Function for getting a list of numbers from the server 
#   via a get request with two parameters
# To execute the function, on a dedicated terminal, 
#   a server must be running that will respond to get requests. 
#   The test version of such a server 
#   is located in the diagnostic_tasks/tests/ directory 
#   and has the name server_for_test_sorting_numbers.py
def get_integers_from_server(server_url, server_port, a_number, b_number):
    resulting_list_of_numbers = requests.get(
        f"{server_url}:{server_port}?a={a_number}&b={b_number}"
    ).json()
    resulting_list_of_numbers.sort()

    return resulting_list_of_numbers


if __name__ == "__main__":
    with open("input.txt") as input_file:
        server_url = input_file.readline().strip()
        server_port, a_number, b_number = [
            line.strip()
            for line in input_file
        ]

    resulting_list_of_numbers = get_integers_from_server(
        server_url, 
        server_port, 
        a_number, 
        b_number
    )
    resulting_list_of_numbers = [
        str(number) for number in resulting_list_of_numbers
    ]
    resulting_list_of_numbers = "\n".join(resulting_list_of_numbers)

    with open("output.txt", "w") as output_file:
        print(resulting_list_of_numbers, file=output_file)