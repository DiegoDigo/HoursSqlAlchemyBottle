from shema.models import User, session

print(linha for linha in session.query(User).all())