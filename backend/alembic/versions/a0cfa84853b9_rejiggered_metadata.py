"""Rejiggered metadata

Revision ID: a0cfa84853b9
Revises: 1d3e3ab4660b
Create Date: 2024-02-21 22:06:39.485680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0cfa84853b9'
down_revision: Union[str, None] = '1d3e3ab4660b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
