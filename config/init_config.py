import configparser

config_path = "config\main_config.ini"
# Create a ConfigParser object
cfg = configparser.ConfigParser()

# Read the .ini file
cfg.read(config_path)