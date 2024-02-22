"""added avatars to users - second try

Revision ID: 7d8ee0a70149
Revises: 43cd16a4a5ea
Create Date: 2024-02-21 20:29:35.991573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d8ee0a70149'
down_revision: Union[str, None] = '43cd16a4a5ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
