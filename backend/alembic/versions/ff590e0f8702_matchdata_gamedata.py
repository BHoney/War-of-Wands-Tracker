"""matchData -> GameData

Revision ID: ff590e0f8702
Revises: a0cfa84853b9
Create Date: 2024-02-21 22:54:42.666522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff590e0f8702'
down_revision: Union[str, None] = 'a0cfa84853b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('friends_list')
    op.drop_table('posts')
    op.drop_table('characters')
    op.drop_table('user_preference')
    op.drop_table('players')
    op.drop_table('game_data')
    op.drop_table('match_data')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('signup_date', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('rank_points', sa.INTEGER(), nullable=True),
    sa.Column('last_online', sa.DATETIME(), nullable=True),
    sa.Column('username', sa.VARCHAR(length=50), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(), nullable=True),
    sa.Column('avatar', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('match_data',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('winner_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['winner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_data',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('winner_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['winner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('character_id', sa.INTEGER(), nullable=True),
    sa.Column('match_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['match_id'], ['match_data.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_preference',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('value', sa.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('characters',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=40000), nullable=False),
    sa.Column('date_posted', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('kudos', sa.INTEGER(), nullable=True),
    sa.Column('author_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('friends_list',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('owner_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
