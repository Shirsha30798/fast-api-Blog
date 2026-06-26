"""add is_used column to reset token table

Revision ID: 09f13445158f
Revises: 34cea02758fe
Create Date: 2026-06-24 01:35:40.856996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09f13445158f'
down_revision: Union[str, Sequence[str], None] = '34cea02758fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('password_reset_tokens', sa.Column('is_used', sa. Boolean(),    nullable=False, server_default='false'),) 
    pass


def downgrade() -> None:
    op.drop_column('password_reset_tokens', 'is_used')
    pass
