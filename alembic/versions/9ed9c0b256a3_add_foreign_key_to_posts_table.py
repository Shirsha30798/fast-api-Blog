"""add foreign-key to posts table

Revision ID: 9ed9c0b256a3
Revises: b0ac8c3224aa
Create Date: 2026-06-11 14:08:50.279702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ed9c0b256a3'
down_revision: Union[str, Sequence[str], None] = 'b0ac8c3224aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('pos_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade() -> None:
    op.drop_constraint('pos_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
