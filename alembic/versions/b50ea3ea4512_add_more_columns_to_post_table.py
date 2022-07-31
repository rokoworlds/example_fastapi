"""add more columns to post table

Revision ID: b50ea3ea4512
Revises: f4aa0064a0d3
Create Date: 2022-07-31 14:17:39.599306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b50ea3ea4512'
down_revision = 'f4aa0064a0d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)


def downgrade() -> None:
    op.drop_column('posts', "published")
    op.drop_column('posts', 'created_at')
