"""create posts table

Revision ID: 541ebc3bd228
Revises: 
Create Date: 2022-07-31 12:48:06.398108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '541ebc3bd228'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    


def downgrade() -> None:
    op.drop_table('posts')
    
