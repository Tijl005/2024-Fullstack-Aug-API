produce = "SELECT name, picture, paragraph FROM sunspire.produce;"
practice = "SELECT name, picture, paragraph FROM sunspire.practice;"
get_tour = "SELECT tourId, firstName, lastName, email FROM sunspire.tour;"
insert_tour = "INSERT INTO sunspire.tour (tourId, firstName, lastName, email) VALUES (%s, %s, %s, %s);"