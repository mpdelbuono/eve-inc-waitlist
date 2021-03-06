import os
import base64
from os import makedirs
from configparser import ConfigParser

if not os.path.isfile(os.path.join(".", "config", "config.cfg")):
    # create a preset file
    config = ConfigParser()
    config.add_section("database")
    config.set("database", "connection_uri", "mysql+mysqldb://user:password@localhost:3306/dbname")
    config.set("database", "sqlalchemy_pool_recycle", "7200")
    
    config.add_section("app")
    config.set("app", "secret_key", base64.b64encode(os.urandom(24)).decode('utf-8', 'strict'))
    config.set("app", "server_port", "81")
    config.set("app", "server_bind", "0.0.0.0")
    config.set("app", "community_name", "IncWaitlist")
    
    config.add_section("logging")
    config.set("logging", "error_file", "/var/log/pywaitlist/error.log")
    config.set("logging", "info_file", "/var/log/pywaitlist/info.log")
    config.set("logging", "access_file", "/var/log/pywaitlist/access.log")
    config.set("logging", "debug_file", "/var/log/pywaitlist/debug.log")
    
    config.add_section("crest")
    config.set("crest", "client_id", "f8934rsdf")
    config.set("crest", "client_secret", "f893ur3")
    config.set("crest", "return_url", "")
    
    config.add_section("motd")
    config.set("motd", "hq", "..")
    config.set("motd", "vg", "..")

    config.add_section("cdn")
    config.set("cdn", "cdn_domain", "")
    config.set("cdn", "cdn_assets", "False")
    config.set("cdn", "cdn_https", "False")
    config.set("cdn", "eve_img_server", "https://imageserver.eveonline.com/{0}.{1}")
    config.set("cdn", "eve_img_server_webp", "False")

    config.add_section("cookies")
    config.set("cookies", "secure_cookies", "False")

    config.add_section("node")
    config.set("node", "node_bin", "")

    config.add_section("debug")
    config.set("debug", "enabled", "False")
    
    config.add_section("security")
    config.set("security", "scramble_names", "False")

    config.add_section("disable")
    config.set("disable", "teamspeak", "False")

    config.add_section("pageinfo")
    config.set("pageinfo", "influence_link", "#")

    config.add_section("fittools")
    config.set("fittools", "stats_enabled", "True")
    config.set("fittools", "stats_uri", "https://quiescens.duckdns.org/wl/ext/wl_external.js")
    config.set("fittools", "stats_sri", "sha384-VonGhMELp1YLVgnJJMq2NqUOpRjhV7nUpiATMsrK5TIMrYQuGUaUPUZlQIInhGc5")

    if not os.path.isdir(os.path.join(".", "config")):
        makedirs(os.path.join(".", "config"))
    with open(os.path.join(".", "config", "config.cfg"), "w") as configfile:
        config.write(configfile)

config = ConfigParser()
config.read(os.path.join("config", "config.cfg"))

title = config.get("app", "community_name")

debug_enabled = config.get("debug", "enabled") == "True"
node_bin = config.get("node", "node_bin")
connection_uri = config.get("database", "connection_uri")
secure_cookies = config.get("cookies", "secure_cookies") == "True"
cdn_https = config.get("cdn", "cdn_https") == "True"
cdn_domain = config.get("cdn", "cdn_domain")
cdn_assets = config.get("cdn", "cdn_assets") == "True"
cdn_eveimg = config.get("cdn", "eve_img_server")
cdn_eveimg_webp = config.get("cdn", "eve_img_server_webp") == "True"

html_min = not debug_enabled
assets_debug = debug_enabled
sqlalchemy_pool_recycle = config.getint("database", "sqlalchemy_pool_recycle")
secret_key = base64.b64decode(config.get("app", "secret_key"))
server_port = config.getint("app", "server_port")
server_bind = config.get("app", "server_bind")
error_log = config.get("logging", "error_file")
info_log = config.get("logging", "info_file")
access_log = config.get("logging", "access_file")
debug_log = config.get("logging", "debug_file")

crest_client_id = config.get("crest", "client_id")
crest_client_secret = config.get("crest", "client_secret")
crest_return_url = config.get("crest", "return_url")

motd_hq = config.get("motd", "hq")
motd_vg = config.get("motd", "vg")

scramble_names = config.get("security", "scramble_names") == "True"

disable_teamspeak = config.get("disable", "teamspeak") == "True"

influence_link = config.get("pageinfo", "influence_link")

cdn_eveimg_js = cdn_eveimg.format("${ path }", "${ suffix }")

stattool_uri = config.get("fittools", "stats_uri")
stattool_sri = config.get("fittools", "stats_sri")
stattool_enabled = config.get("fittools", "stats_enabled") == "True"
