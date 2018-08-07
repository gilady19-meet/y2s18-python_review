from knowledge_model import Base, Knowledge
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(title, topic, rating):
	article_object = Knowledge(
		title=title,
		topic=topic,
		rating=rating
		)
	session.add(article_object)
	session.commit()

add_article("real" , "sport" , 10 )
add_article("spain" , "contries" , 7 )
add_article("car" , "vheicels" , 6)
add_article("tel aviv" , "cities" , 9)
add_article("turtle" , "animals" , 3)
add_article("harel" , "schools" , 5)
add_article("pizza" , "food" , 4)
add_article("chair" , "sitting" , 2)
add_article("hand" , "bodi" , 8)
add_article("water" , "drinks" , 6)

def query_all_articles():
   	article = session.query(
        Knowledge).all()
   	return article

print(query_all_articles())  

def query_article_by_topic(topic):
   	article = session.query(Knowledge).filter_by(topic=topic).first()
   	return article


print(query_article_by_topic("contries"))

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

#print(delete_article_by_topic("contries"))



def query_article_by_rating(rating):
	article = session.query(Knowledge).filter_by(rating=rating).first()
   	return article

print(query_article_by_rating(10))


def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

#delete_all_articles()




def edit_article_rating(rating, title):
	x = session.query(Knowledge).filter_by(title=title).first()
	x.rating=rating
	session.commit()

edit_article_rating(8 , "spain")
print(query_article_by_rating(8))

def topfive():
	list=session.query(Knowledge).order_by(Knowledge.rating).all()
	return list

print(topfive())