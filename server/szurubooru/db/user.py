import sqlalchemy as sa
from szurubooru.db.base import Base

class User(Base):
    __tablename__ = 'user'

    AVATAR_GRAVATAR = 'gravatar'
    AVATAR_MANUAL = 'manual'

    user_id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String(50), nullable=False, unique=True)
    password_hash = sa.Column('password_hash', sa.String(64), nullable=False)
    password_salt = sa.Column('password_salt', sa.String(32))
    email = sa.Column('email', sa.String(200), nullable=True)
    rank = sa.Column('rank', sa.String(32), nullable=False)
    creation_time = sa.Column('creation_time', sa.DateTime, nullable=False)
    last_login_time = sa.Column('last_login_time', sa.DateTime)
    avatar_style = sa.Column(
        'avatar_style', sa.String(32), nullable=False, default=AVATAR_GRAVATAR)
