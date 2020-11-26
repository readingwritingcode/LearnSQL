from configparser import ConfigParser

def read_db_config(filename='config.ini',section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param finename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # Get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('%s not found in the %d' % (section,filename))

    return db
