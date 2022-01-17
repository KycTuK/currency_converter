'''
    Python 3.3
    The xml.etree.ElementTree module now imports its C accelerator by default;
    there is no longer a need to explicitly import xml.etree.cElementTree;
'''
import xml.etree.ElementTree as ET
import requests
#import cXmlProcessing as cXP

def get_xml(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("RequestFailed: ", url)
    else:
        print("RequestSuccessed: ", url)
        #print(response.text)
        return response


def get_root(xml):
    root = ET.fromstring(xml.text)
    return root


class ValuteConverter:
    def __init__(self, root):
        self.val_list = list(root)
        self.tag_code_name = 'CharCode'
        self.tag_value_name = 'Value'

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
            print(child.find(self.tag_code_name).text)

    def print_codes_with_values(self):
        for child in self.val_list:
            print(child.find(self.tag_code_name).text, child.find(self.tag_value_name).text)

    def input_char_code(self, input_message):
        char_code = input(input_message)
        while not self.does_code_exists(char_code):
            #raise ValueError("Unknown valute char code, use one of this:")
            print("Unknown valute char code, use one of the following:")
            self.print_codes()
            char_code = input(input_message)
        return char_code



vc = ValuteConverter(get_root(get_xml('https://cbr.ru/scripts/XML_daily.asp')))
source_code = vc.input_char_code("input source char code: ")
print(vc.get_value_by_code(source_code))
    #print(root.attrib)
    #tree = ET.ElementTree(response.text)
    #getElement(list(root), 'NOK')
    #for child in list(root):
        #print(child.find('CharCode').text, child.find('Value').text)
    #root = tree.getroot()
    #print(root)
    #print(list(root)[5].attrib['ID'])
    #getID = list(root)[0].attrib['Valute']
    #for child in children:
    #    print(child)
    #root = ET.XML(response.text)
    #print(ET.ElementTree(root).parse)
    #for child in root.getchildren():
    #    print(child)
    #print(root.find("./Valute/[CharCode='NOK']").find("Value").text)
    #print(root.findall('./valute/*'))
    #xmldict = cXP.XmlDictConfig(root)
    #print(xmldict.items())
    #print(xmldict.values())
    #print(xmldict.get('Valute'))
    #print(xmldict.items())
    #print(xmldict.get('./valute'))
    #for elem in xmldict.items():
    #    print(elem)
    #print(xmldict.get('CharCode', 'NOK'))


#    print(response.headers['Content-Type'])
#    root = ET.fromstring(response.text)
#    print(root)
#    print(root.find("./Valute/[CharCode='NOK']").find("Value").text)
#    for child in root:
#       print(child.tag, child.attrib)
#    for neighbor in root.iter('CharCode'):
#        print(neighbor.attrib)

