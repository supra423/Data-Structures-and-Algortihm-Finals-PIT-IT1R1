# so one of the things that I thought about is that
# I can still use my sqlite knowledge in this little project
#
# let's say I'm trying to make a student grade report,
# this program basically sorts students using quicksort
# and we are able to use binary search to search through
# list.
#
# One thing I thought about is to also implement sqlite,
# the database is basically going to be a place where
# the students' information are stored
#
# to implement the sorting algorithm part, before adding
# students to the database, I can sort the students accordingly

from databaseTables import database

if __name__ == "__main__":
    database()
