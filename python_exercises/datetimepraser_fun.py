
def datetime_parser(dct):
    logging.debug("datetime_parser executing...{}".format(dct))
    datetime_format_regex = re.compile("[0-3][0-9]\/[0-1][0-9]\/[0-9]{4} [0-1][0-9]:[0-5][0-9]:[0-5][0-9]")
    for k, v in dct.items():
        if isinstance(v, str) and datetime_format_regex.match(v):
            dct[k] = datetime.datetime.strptime(v, DATE_H_M_S_FORMAT)
    return dct