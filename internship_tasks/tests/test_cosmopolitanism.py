from tasks_for_yandex_job.internship_tasks.cosmopolitanism import (
    Country, Classmate, search_where_classmates_migrated
)
import unittest


class TestSearchWhereClassmatesMigrated(unittest.TestCase):
    def make_country_lists(
        self,
        min_incomes, 
        education_requirements, 
        migrations_for_children
    ):

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

        return list_of_all_countries, countries_without_education

    def make_list_of_classmates(
        self,
        classmates_income, 
        availability_of_educations, 
        citizenship_of_parents,
        list_of_all_countries
    ):

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
        return list_of_classmates

    def test_of_result_1(self):
        list_of_all_countries, countries_without_education = \
            self.make_country_lists(
                [10, 9],
                [1, 0],
                [0, 1]
            )
        list_of_classmates = self.make_list_of_classmates(
            [0, 0, 11, 10, 9],
            [0, 1, 0, 1, 1],
            [2, 1, 0, 0, 0],
            list_of_all_countries
        )

        self.assertEqual(
            search_where_classmates_migrated(
                list_of_all_countries, 
                countries_without_education,
                list_of_classmates
            ),
            ["2", "0", "2", "1", "2"]
        )


if __name__ == "__main__":
    unittest.main()