"""add last few columns to the posts table

Revision ID: afe717cfad38
Revises: 9ed9c0b256a3
Create Date: 2026-06-11 14:29:27.430374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afe717cfad38'
down_revision: Union[str, Sequence[str], None] = '9ed9c0b256a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa. Boolean(),    nullable=False, server_default='TRUE'),) 
    op.add_column('posts', sa.Column('created_at', sa. TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
