"""rename update_at to updated_at

Revision ID: e8313bf2440f
Revises: 624dfc7de9de
Create Date: 2025-05-17 16:34:36.425366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8313bf2440f'
down_revision: Union[str, None] = '624dfc7de9de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'users',
        'update_at',
        new_column_name='updated_at',
        existing_type=sa.DateTime(timezone=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'users',
        'updated_at',
        new_column_name='update_at',
        existing_type=sa.DateTime(timezone=True),
    )
