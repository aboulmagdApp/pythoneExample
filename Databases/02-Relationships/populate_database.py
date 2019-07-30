from models import db,Puppy,Toy,Owner

# Create 2 puppes

rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add Puppes to DB
db.session.add_all([rufus,fido])
db.session.commit()

# Check !
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create Owner Object
jose = Owner('Jose',rufus.id)

# Give Rufus some toys
toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

# GRAB RUFUS After those additation
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()