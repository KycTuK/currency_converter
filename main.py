'''
    Python 3.3
    The xml.etree.ElementTree module now imports its C accelerator by default;
    there is no longer a need to explicitly import xml.etree.cElementTree;
'''
import xml.etree.ElementTree as ET
import requests

def get_xml(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("RequestFailed: ", url)
    else:
        print("RequestSuccessed: ", url)
        return response


def get_root(xml):
    root = ET.fromstring(xml.text)
    return root


class ValuteConverter:
    def __init__(self, root):
        self.val_list = list(root)
        self.tag_code_name = 'CharCode'
        self.tag_value_name = 'Value'
        self.tag_descr_name = 'Name'

    def does_code_exists(self, char_code):
        for child in self.val_list:
            if child.find(self.tag_code_name).text == char_code:
                return True
        return False

    def get_value_by_code(self, char_code):
        for child in self.val_list:
            if child.find(self.tag_code_name).text == char_code:
                return child.find(self.tag_value_name).text

    def print_codes(self):
        for child in self.val_list:
            print(child.find(self.tag_code_name).text, "-", child.find(self.tag_descr_name).text)

    def print_codes_with_values(self):
        for child in self.val_list:
            print(child.find(self.tag_code_name).text, "-", child.find(self.tag_value_name).text)

    def input_char_code(self, input_message):
        char_code = input(input_message)
        while not self.does_code_exists(char_code):
            print("Unknown valute char code, use one of the following:")
            self.print_codes()
            char_code = input(input_message)
        return char_code


vc = ValuteConverter(get_root(get_xml('https://cbr.ru/scripts/XML_daily.asp')))
source_code = vc.input_char_code("input source char code: ")
target_code = vc.input_char_code("input target char code: ")
source_value = vc.get_value_by_code(source_code)
target_value = vc.get_value_by_code(target_code)
print("Curs of", source_code, "is", source_value, "RUB")
print("Curs of", target_code, "is", target_value, "RUB")
print("Curs of", target_code, "in", source_code, "is: ", end='')
print(target_code, "/", source_code, " = ", end='')
print(target_value, "/", source_value, " = ", end='')
print(float(target_value.replace(',', '.')) / float(source_value.replace(',', '.')))
