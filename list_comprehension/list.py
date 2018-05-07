movies = ["Abraham Lincoln", "Blue Steel", "Behind Office Doors", "Bowery at Midnight", "Captain Kidd", "Debbie Does Dallas", "The Emperor Jones", "Rain"]

movies_tuple = [("Abraham Lincoln", 1993), ("Blue Steel", 1938), ("Behind Office Doors", 1999), ("Bowery at Midnight", 2000), ("Captain Kidd",2010), ("Debbie Does Dallas",1908), ("The Emperor Jones", 2016), ("Rain", 2011)]

# selected_movies = []
# for title in movies:
#     if title.startswith("B"):
#         selected_movies.append(title)

#list_comprehension

# [expr for val in collection]
# [expr for val in collection if <test>]
# [expr for val in collection if <test> and <test2>]
# [expr for val1 in collection1 and val2 in collection2]

selected_movies = [title for title in movies if title.startswith("B")]
print(selected_movies)


#this is for tuples
selected_movies2 = [title for (title, year) in movies_tuple if year <2000 ]
print (selected_movies2)