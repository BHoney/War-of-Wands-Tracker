"""added avatars to users

Revision ID: 43cd16a4a5ea
Revises: 6c38731ae141
Create Date: 2024-02-21 20:29:04.420899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43cd16a4a5ea'
down_revision: Union[str, None] = '6c38731ae141'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
