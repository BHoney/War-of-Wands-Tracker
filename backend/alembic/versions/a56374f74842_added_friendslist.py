"""added friendslist

Revision ID: a56374f74842
Revises: 7d8ee0a70149
Create Date: 2024-02-21 21:44:14.797129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a56374f74842'
down_revision: Union[str, None] = '7d8ee0a70149'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
