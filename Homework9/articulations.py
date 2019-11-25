# ----------------------------------------------------------------------
# Name:     articulations
# Purpose:  Homework 9
#
# Author(s): Ian SooHoo
# ----------------------------------------------------------------------
"""
Generates articulated courses
Generates articulated courses using BeautifulSoup, REGEX, from the SJSU
website seed
"""



# The seed/tip url is declared as a constant.
SEED = 'http://info.sjsu.edu/web-dbgen/artic/all-course-to-course.html'

import urllib.request
import re
import bs4

def make_soup(filename):
    """
    makes a soup object
    :param url: The url link that needs to be parsed
    :return: soup : BeautifulSoup object, containing HTML data
    """
    html_file = urllib.request.urlopen(filename).read()
    soup = bs4.BeautifulSoup(html_file, "html.parser")
    return soup


def get_links(top_url):
    """
    gets all absolute links
    :param top_url: the main URL that contains links to all articulated
    colleges
    :return: list: absolute links
    """
    # Extract list of relevant (absolute) links referenced in top_url
    soup = make_soup(top_url)

    school_table = soup.find_all('table')[2]
    # print(soup.finall('table'))
    # print(soup.finall('table')[1])

    return [urllib.parse.urljoin(top_url, each_anchor.get('href', None)) for
            each_anchor in school_table.find_all('a')]
    # print(some_list)
    # return some_list



def extract_info(url, course_regex):
    """
    gets info for the courses articulated
    :param url: the specific articulated college URL
    :param course_regex: the course we are looking for
    :return: string: that contains the college name with the found course
    """
    # Return college and equivalent course found in the given url if any
    soup = make_soup(url)

    data_table = soup.find_all('table')[2]
    # print("info table" + f'{info_table}')
    college_name = data_table.find_all('h3')[1].get_text() #articulated
    # college name
    # print("college name" + f'{college_name}')
    regex = re.compile(course_regex + r'.*', re.IGNORECASE)
    all_rows = data_table.find_all('td', string=regex)


    for each_row in all_rows:
        next_column = (each_row.find_next_sibling('td')).find_next_sibling(
            'td')
        # print(next_column)
        found_course = next_column.get_text(separator=' ')
        found_course = ' '.join(found_course.split())
        if re.match(found_course, 'No Current Equivalent') is None:
            return f'{college_name}: {found_course}'


def harvest(all_links, course_regex):
    """
    finds the links that match a regex
        :param all_links: all college absolute links
        :param course_regex: the course we are looking for
        :return: string: that contains ALL articulated courses separated by
        new lines
        """

    # Join all the equivalency info into a single string (entries must
    articulated_string = ""


    for each_link in all_links:
        # Invoke extract_url to get the equivalency info for each link in
        # all_links.
        articulated_course = extract_info(each_link, course_regex)
        # Join all the equivalency info into a single string (entries must

        if articulated_course:

            articulated_string = articulated_string + f'{articulated_course}'\
                                 + '\n'  # separated by new line characters.
            # print("found..." + articulated_course)
    return articulated_string


def report(info, course_name):
    """
    generates the output file
        :param info: the string of data to put into file
        :param course_name: the name of course we are looking for
        :return: None, outputs a file
        """
    # Write the info harvested to a text file with the name:
    # course_name.txt where course_name is the name as entered by user.

    output_filename = ''.join([course_name, '.txt'])

    with open(output_filename, 'w+', encoding='utf-8') as output_file:
        output_file.write(info)





def generate_regex(course_name):
    """
    Creates a proper search query from the user input
    :param course_name: the name of the course in whatever the user entered
    :return: course_regex: modified regex to be used
    """
    pattern = r'([A-Za-z]+)[\s]?0*?([1-9]+0?)([A-Za-z]?)'
    course_match = re.finditer(pattern, course_name, re.IGNORECASE)
    if course_match:
        for match in course_match:
            course_regex = match.group(1).upper() + ' 0*' + match.group(2)
            if match.group(3) is None:
                return course_regex
            else:
                return course_regex + match.group(3).upper()
    else:
        print("Please reenter course in the format SUBJECT + COURSE-NUM")
        return None





def main():
    # Get all the relevant links referenced from the seed SEED (top_url)
    links = get_links(SEED)
    # Prompt the user for a course name
    course_name = input('Enter a course name: ')

    # Build a regex corresponding to the course name specified
    course_regex = generate_regex(course_name)
    # print(f'Generated regex: {course_regex}')

    # Harvest information from all the links
    info = harvest(links, course_regex)

    # Write the harvested information to the output file
    report(info, course_name)
    print(f'Your output has been saved in the file:'
          f' {course_name}.txt')


if __name__ == "__main__":
    main()