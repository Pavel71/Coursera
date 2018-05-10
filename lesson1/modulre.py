
import re


def get_List_Found_Text(List_Group_Columns):


    Pattern_re = re.compile('(?:\(|Miss.) *(\w*)')

    List_Found_Name = []

    for element in List_Group_Columns:

        list_found = Pattern_re.findall(element)

        if list_found:

            for element2 in list_found:
                List_Found_Name.append(element2)

    return List_Found_Name



