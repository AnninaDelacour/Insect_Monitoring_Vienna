import configparser

def read_config(section, key):
    """Read a value from the database.ini file"""
    config = configparser.ConfigParser()
    config.read('database.ini')
    return config[section][key]