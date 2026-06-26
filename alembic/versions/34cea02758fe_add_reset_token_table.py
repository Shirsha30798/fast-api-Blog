"""add reset token table

Revision ID: 34cea02758fe
Revises: fedefcedbd5d
Create Date: 2026-06-23 20:43:20.925418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34cea02758fe'
down_revision: Union[str, Sequence[str], None] = 'fedefcedbd5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('password_reset_tokens', 
                sa.Column('id', sa.Integer(), nullable=False),
                sa.Column('user_id', sa.Integer(), nullable=False),
                sa.Column('token', sa.String(), nullable=False),
                sa.Column('expires_at', sa. TIMESTAMP(timezone=True), nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('token'),
                sa.ForeignKeyConstraint(['user_id'], ['users.id']))
    pass


def downgrade() -> None:
    op.drop_table('password_reset_tokens')
    pass
