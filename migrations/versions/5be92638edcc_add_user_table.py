"""Add User table

Revision ID: 5be92638edcc
Revises: 
Create Date: 2024-02-04 20:05:27.163733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5be92638edcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('password', sa.Unicode(length=255), nullable=False),
    sa.Column('email', sa.Unicode(length=255), nullable=False),
    sa.Column('username', sa.Unicode(length=255), nullable=False),
    sa.Column('full_name', sa.Unicode(length=255), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
