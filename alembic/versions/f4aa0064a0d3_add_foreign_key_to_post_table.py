"""add foreign key to post table

Revision ID: f4aa0064a0d3
Revises: 57a84c90853b
Create Date: 2022-07-31 13:57:11.492063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4aa0064a0d3'
down_revision = '57a84c90853b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")

def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
