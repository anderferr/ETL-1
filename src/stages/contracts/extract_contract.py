from collections import namedtuple

"""Extraction_date é necessário para o contrato funcionar"""
ExtractContract = namedtuple(
    "ExtractContract",
    '''
        raw_information_content
        extraction_date
    '''
)