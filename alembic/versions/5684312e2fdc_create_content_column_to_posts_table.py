"""create content column to posts table

Revision ID: 5684312e2fdc
Revises: 541ebc3bd228
Create Date: 2022-07-31 13:34:03.700389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5684312e2fdc'
down_revision = '541ebc3bd228'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
