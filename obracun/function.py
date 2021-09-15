#functions 

# def country_entity_list():
# 	country_entities = CountryEntity.objects.all()
# 	country_entity_list = [('', '---------')]

# 	for country_entity in country_entities:
# 		one_country_entity = (country_entity.id, country_entity.entity_name)
# 		country_entity_list.append(one_country_entity)
# 	return country_entity_list

# def country_list():
# 	countries = Country.objects.all()
# 	country_list = [('', '---------')]

# 	for country in countries:
# 		one_country = (country.id, country.country_name)
# 		country_list.append(one_country)
# 	return country_list

# def canton_list():
# 	cantones = Canton.objects.all()
# 	canton_list = [(0, '---------')]

# 	for canton in cantones:
# 		one_canton = (canton.id, canton.canton_name)
# 		canton_list.append(one_canton)
# 	return canton_list

# def municipality_list():
# 	municipalities = Municipality.objects.all()
# 	municipality_list = [(0, '---------')]

# 	for municipality in municipalities:
# 		one_municipality = (municipality.id, municipality.municipality_name)
# 		municipality_list.append(one_municipality)
# 	return municipality_list