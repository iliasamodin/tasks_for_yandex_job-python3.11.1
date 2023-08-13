# A class whose objects are countries suitable for classmate immigration
class Country:
    def __init__(
        self, 
        country_position,
        min_income, 
        education_requirement, 
        migration_for_children
    ):

        self.position = country_position
        self.income = min_income
        self.education = education_requirement
        self.migration_for_children = migration_for_children


# Class with objects - classmates
class Classmate:
    def __init__(
        self, 
        classmate_income, 
        availability_of_education, 
        parental_citizenship
    ):

        self.income = classmate_income
        self.education = availability_of_education
        # The parental_citizenship attribute of the classmate object 
        #   refers to the country object 
        #   in which the classmate's parents have citizenship
        self.parental_citizenship = parental_citizenship

    # A method that checks the ability of a classmate to immigrate 
    #   to the country passed as an argument
    def in_this_country(self, country):
        return (
            country.migration_for_children and 
            self.parental_citizenship is country
        ) or (
            self.income >= country.income and
            self.education >= country.education
        )


# The function of finding the best country 
#   for immigration of each classmate
def search_where_classmates_migrated(
        list_of_all_countries, 
        countries_without_education,
        list_of_classmates
    ):
    where_classmates_migrated = []
    for classmate in list_of_classmates:
        # Specifying a sample of countries to move 
        #   based on the presence or absence of higher education 
        #   from a classmate
        available_sample_of_countries = \
            list_of_all_countries \
            if classmate.education \
            else countries_without_education

        start_index = 0
        end_index = len(available_sample_of_countries) - 1

        # Until a better country is found 
        #   for the classmate to which he can immigrate, 
        #   the classmate is assigned a default status 
        #   - a status indicating 
        #   that the classmate cannot emigrate from his native country
        best_country_for_classmate = "0"

        # Finding the best country for a classmate using binary search
        # The use of binary search is possible due to the fact 
        #   that countries for immigration are initially sorted 
        #   from the most demanding to the characteristics of migrants 
        #   to the least demanding
        while start_index <= end_index:
            average_position = (start_index + end_index) // 2

            country = available_sample_of_countries[average_position]
            if classmate.in_this_country(country):
                best_country_for_classmate = str(country.position)
                end_index = average_position - 1
            else:
                start_index = average_position + 1

        # Checking three conditions: 
        #   whether the classmate's parents 
        #   have the citizenship of another country, 
        #   whether it is possible to immigrate to this country 
        #   under the family reunification program, 
        #   and whether the country 
        #   in which the classmate's parents have citizenship 
        #   is more attractive 
        #   than the country found for the classmate by binary search
        if classmate.parental_citizenship is not None and \
        classmate.parental_citizenship.migration_for_children and \
        classmate.parental_citizenship.position < \
        int(best_country_for_classmate):
            best_country_for_classmate = \
                str(classmate.parental_citizenship.position)

        where_classmates_migrated.append(best_country_for_classmate)

    return where_classmates_migrated


if __name__ == "__main__":
    with open("input.txt") as input_file:
        _, min_incomes, education_requirements, migrations_for_children, \
        _, classmates_income, availability_of_educations, \
        citizenship_of_parents = \
        [line.strip().split(" ") for line in input_file]

    list_of_all_countries = []
    countries_without_education = []
    for country_position, country_data in enumerate(
        zip(min_incomes, education_requirements, migrations_for_children), 
        start=1
    ):
        min_income, education_requirement, migration_for_children = \
            country_data

        country = Country(
            country_position,
            int(min_income), 
            bool(int(education_requirement)), 
            bool(int(migration_for_children))
        )

        list_of_all_countries.append(country)
        if not int(education_requirement):
            countries_without_education.append(country)

    list_of_classmates = [
        Classmate(
            int(classmate_income), 
            bool(int(availability_of_education)), 
            list_of_all_countries[int(parental_citizenship)-1] if parental_citizenship != "0" else None
        )
        for classmate_income, availability_of_education, parental_citizenship
        in zip(
            classmates_income, 
            availability_of_educations, 
            citizenship_of_parents
        )
    ]

    where_classmates_migrated = search_where_classmates_migrated(
        list_of_all_countries, 
        countries_without_education,
        list_of_classmates
    )
    where_classmates_migrated = " ".join(where_classmates_migrated)

    with open("output.txt", "w") as output_file:
        print(where_classmates_migrated, file=output_file)