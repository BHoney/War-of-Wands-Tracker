"""create tables

Revision ID: 6c38731ae141
Revises: e722d9d684b5
Create Date: 2024-02-21 20:19:41.633369

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c38731ae141'
down_revision: Union[str, None] = 'e722d9d684b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
