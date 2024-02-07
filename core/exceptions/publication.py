from core.exceptions import CustomException


class PublicationTooBigException(CustomException):
    code = 431
    error_code = "PUBLICATION__TEXT_TOO_BIG"
    message = "text_too_big"