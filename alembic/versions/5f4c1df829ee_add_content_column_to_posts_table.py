"""add content column to posts table

Revision ID: 5f4c1df829ee
Revises: 49a498e3f5ad
Create Date: 2026-06-11 13:40:09.255995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f4c1df829ee'
down_revision: Union[str, Sequence[str], None] = '49a498e3f5ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
