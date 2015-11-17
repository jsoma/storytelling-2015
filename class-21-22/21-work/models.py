# models.py
# peewee
# Another popular one: SQLAlchemy

from peewee import * 

db = SqliteDatabase('schools.db')

class School(Model):
	# Define every single column
	# from the database that we
	# want to talk about
	dbn = CharField(primary_key=True)
	school_name = CharField()
	boro = CharField()
	total_students = IntegerField()
	phone_number = CharField()
	primary_address_line_1 = CharField()
	city = CharField()
	latitude = DecimalField(max_digits=9,decimal_places=6)
	longitude = DecimalField(max_digits=9,decimal_places=6)

	def full_address(self):
		return "{}, {}, NY".format(self.primary_address_line_1, self.city)

	class Meta:
		database = db
		db_table = "schools"


class Score(Model):
	# You gotta put stuff here
	dbn = CharField(primary_key=True)
	school_name = CharField()
	number_of_test_takers = IntegerField()
	critical_reading_mean = IntegerField()
	mathematics_mean = IntegerField()
	writing_mean = IntegerField()

	class Meta:
		database = db
		db_table = "sat_scores"

