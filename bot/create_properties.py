from wikidataintegrator import wdi_core, wdi_login


mediawiki_api_url = "http://185.54.113.31:8181/w/api.php"
sparql_endpoint_url = "http://185.54.113.31:8282/proxy/wdqs/bigdata/namespace/wdq/sparql"
username = "Test"
password = "test2"
login = wdi_login.WDLogin(username, password, mediawiki_api_url=mediawiki_api_url)

def createProperty(login, label, description, property_datatype):
  s = []
  localEntityEngine = wdi_core.WDItemEngine.wikibase_item_engine_factory(mediawiki_api_url,sparql_endpoint_url)
  item = localEntityEngine(data=s)
  item.set_label(label)
  item.set_description(description)
  print(item.write(login, entity_type="property", property_datatype=property_datatype))


## Properties accorind to: https://docs.google.com/spreadsheets/d/1RhxhzRW_Id10uOXiaFeubIG0z6b0I7k9VN6Sg2KqZG8/edit#gid=0
# Session
#createProperty(login, "instance of", "is a", "wikibase-item")
#createProperty(login, "author", "author of the submission (use qualifier author series ordinal (P3)", "wikibase-item")
createProperty(login, "author series ordinal", "author position in series of authors", "string")
createProperty(login, "abstract", "link to abstract of the submission", "url")
createProperty(login, "slides", "link to slides of the submission", "url")
createProperty(login, "streamed at", "link to where the talk will be streamed", "url")
createProperty(login, "video", "url to video", "url")
createProperty(login, "notes", "link to notes", "url")
createProperty(login, "room", "location", "wikibase-item")
createProperty(login, "duration", "duration", "string")
createProperty(login, "date", "date and time", "time")

# Speaker
createProperty(login, "Affiliation", "affiliation of the speaker", "wikibase-item")
createProperty(login, "Contatct", "can be contacted at", "url")

# Room
createProperty(login, "Floor", "Floor", "string")
createProperty(login, "Room type", "type", "string")
createProperty(login, "Seats", "Number of seats", "string")


