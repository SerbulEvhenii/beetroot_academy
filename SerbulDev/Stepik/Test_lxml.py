# -*- coding: utf-8 -*-
from urllib import request

from lxml import etree
from lxml.html import fromstring


def parseXML(xmlFile):
    """
    Парсинг XML
    """
    with open(xmlFile) as fobj:
        xml = fobj.read()

    root = etree.fromstring(xml)

    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text

            print(elem.tag + " => " + text)

data = etree.fromstring(bytes(r.text, encoding='utf-8'))


if __name__ == "__main__":
    parseXML("17.1_part.xml")